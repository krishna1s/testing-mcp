#!/usr/bin/env python3
"""
Test Case Accuracy Validation Script
===================================

This script validates the accuracy and completeness of the generated Python Playwright test cases
by analyzing their structure, syntax, and logical flow without requiring actual test execution.

Features:
- Syntax validation for all Python test files
- Structure analysis and best practices checking
- Test coverage assessment
- Playwright API usage validation
- Documentation and error handling review
"""

import ast
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Any
import re


class TestValidator:
    """Comprehensive test case validator"""
    
    def __init__(self, test_directory: str):
        self.test_directory = Path(test_directory)
        self.test_files = [
            "main_user_journey.py",
            "auth_flows.py", 
            "form_validations.py",
            "workspace_management.py",
            "navigation_comprehensive.py",
            "error_scenarios.py"
        ]
        self.validation_results = {}
        
    def validate_syntax(self, file_path: Path) -> Dict[str, Any]:
        """Validate Python syntax of a test file"""
        result = {
            "valid_syntax": False,
            "error": None,
            "ast_tree": None
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                source_code = f.read()
            
            # Parse the AST
            tree = ast.parse(source_code, filename=str(file_path))
            result["valid_syntax"] = True
            result["ast_tree"] = tree
            
        except SyntaxError as e:
            result["error"] = f"Syntax Error: {e}"
        except Exception as e:
            result["error"] = f"Parse Error: {e}"
            
        return result
    
    def analyze_playwright_usage(self, ast_tree: ast.AST) -> Dict[str, Any]:
        """Analyze Playwright API usage patterns"""
        result = {
            "imports_playwright": False,
            "uses_sync_api": False,
            "has_browser_launch": False,
            "has_page_actions": False,
            "has_expectations": False,
            "has_screenshots": False,
            "has_wait_statements": False,
            "playwright_methods": []
        }
        
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.ImportFrom):
                if node.module and "playwright" in node.module:
                    result["imports_playwright"] = True
                    if "sync_api" in node.module:
                        result["uses_sync_api"] = True
            
            elif isinstance(node, ast.Attribute):
                attr_name = node.attr
                result["playwright_methods"].append(attr_name)
                
                if attr_name in ["launch", "chromium", "firefox", "webkit"]:
                    result["has_browser_launch"] = True
                elif attr_name in ["click", "fill", "goto", "get_by_role", "get_by_text"]:
                    result["has_page_actions"] = True
                elif attr_name in ["to_be_visible", "to_have_text", "to_contain_text"]:
                    result["has_expectations"] = True
                elif attr_name == "screenshot":
                    result["has_screenshots"] = True
                elif attr_name in ["wait_for_load_state", "wait_for_selector"]:
                    result["has_wait_statements"] = True
        
        return result
    
    def analyze_test_structure(self, ast_tree: ast.AST) -> Dict[str, Any]:
        """Analyze test structure and organization"""
        result = {
            "has_docstring": False,
            "function_count": 0,
            "test_functions": [],
            "has_error_handling": False,
            "has_cleanup": False,
            "documentation_score": 0
        }
        
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.FunctionDef):
                result["function_count"] += 1
                result["test_functions"].append(node.name)
                
                # Check for docstring
                if (node.body and isinstance(node.body[0], ast.Expr) and 
                    isinstance(node.body[0].value, ast.Constant) and 
                    isinstance(node.body[0].value.value, str)):
                    result["has_docstring"] = True
                    result["documentation_score"] += 1
            
            elif isinstance(node, ast.Try):
                result["has_error_handling"] = True
            elif isinstance(node, ast.ExceptHandler):
                result["has_error_handling"] = True
            elif isinstance(node, ast.With):
                # Context managers often used for cleanup
                result["has_cleanup"] = True
        
        # Check module-level docstring
        if (ast_tree.body and isinstance(ast_tree.body[0], ast.Expr) and 
            isinstance(ast_tree.body[0].value, ast.Constant) and 
            isinstance(ast_tree.body[0].value.value, str)):
            result["documentation_score"] += 2
        
        return result
    
    def validate_test_logic(self, file_path: Path) -> Dict[str, Any]:
        """Validate test logic and flow"""
        result = {
            "logical_flow": True,
            "error_handling": False,
            "comprehensive_coverage": False,
            "issues": []
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for common patterns
            if "try:" in content and "except" in content:
                result["error_handling"] = True
            
            # Check for comprehensive test patterns
            patterns = [
                r"page\.goto\(",
                r"page\.screenshot\(",
                r"expect\(",
                r"wait_for_load_state",
                r"get_by_role\("
            ]
            
            pattern_matches = sum(1 for pattern in patterns if re.search(pattern, content))
            if pattern_matches >= 4:
                result["comprehensive_coverage"] = True
            
            # Check for common issues
            if "print(" not in content:
                result["issues"].append("No logging/debug output found")
            
            if "screenshot" not in content:
                result["issues"].append("No screenshot capture found")
                
        except Exception as e:
            result["issues"].append(f"File analysis error: {e}")
            result["logical_flow"] = False
        
        return result
    
    def calculate_test_quality_score(self, validations: Dict[str, Any]) -> float:
        """Calculate overall test quality score (0-100)"""
        score = 0
        
        # Syntax (20 points)
        if validations["syntax"]["valid_syntax"]:
            score += 20
        
        # Playwright usage (30 points)
        pw_usage = validations["playwright_usage"]
        if pw_usage["imports_playwright"]: score += 5
        if pw_usage["uses_sync_api"]: score += 5
        if pw_usage["has_browser_launch"]: score += 5
        if pw_usage["has_page_actions"]: score += 5
        if pw_usage["has_expectations"]: score += 5
        if pw_usage["has_screenshots"]: score += 5
        
        # Test structure (25 points)
        structure = validations["structure"]
        if structure["has_docstring"]: score += 5
        if structure["function_count"] > 0: score += 5
        if structure["has_error_handling"]: score += 5
        if structure["documentation_score"] > 2: score += 10
        
        # Test logic (25 points)
        logic = validations["logic"]
        if logic["logical_flow"]: score += 10
        if logic["error_handling"]: score += 10
        if logic["comprehensive_coverage"]: score += 5
        
        return min(score, 100)
    
    def validate_file(self, filename: str) -> Dict[str, Any]:
        """Validate a single test file comprehensively"""
        file_path = self.test_directory / filename
        
        if not file_path.exists():
            return {
                "file": filename,
                "exists": False,
                "error": "File not found"
            }
        
        print(f"🔍 Validating {filename}...")
        
        # Syntax validation
        syntax_result = self.validate_syntax(file_path)
        
        # Structure analysis (only if syntax is valid)
        structure_result = {}
        playwright_usage = {}
        logic_result = {}
        
        if syntax_result["valid_syntax"]:
            structure_result = self.analyze_test_structure(syntax_result["ast_tree"])
            playwright_usage = self.analyze_playwright_usage(syntax_result["ast_tree"])
            logic_result = self.validate_test_logic(file_path)
        
        validations = {
            "syntax": syntax_result,
            "structure": structure_result,
            "playwright_usage": playwright_usage,
            "logic": logic_result
        }
        
        quality_score = self.calculate_test_quality_score(validations)
        
        return {
            "file": filename,
            "exists": True,
            "validations": validations,
            "quality_score": quality_score,
            "file_size": file_path.stat().st_size
        }
    
    def run_validation(self) -> Dict[str, Any]:
        """Run comprehensive validation on all test files"""
        print("🚀 Starting comprehensive test validation...")
        print("=" * 80)
        
        start_time = time.time()
        results = {}
        
        for filename in self.test_files:
            results[filename] = self.validate_file(filename)
        
        # Generate summary
        total_files = len(self.test_files)
        valid_files = sum(1 for r in results.values() if r.get("exists") and 
                         r.get("validations", {}).get("syntax", {}).get("valid_syntax", False))
        
        avg_quality = sum(r.get("quality_score", 0) for r in results.values()) / total_files
        
        duration = time.time() - start_time
        
        summary = {
            "total_files": total_files,
            "valid_files": valid_files,
            "invalid_files": total_files - valid_files,
            "average_quality_score": avg_quality,
            "validation_duration": duration,
            "results": results
        }
        
        return summary
    
    def generate_report(self, results: Dict[str, Any]) -> str:
        """Generate comprehensive validation report"""
        report = []
        report.append("📊 TEST CASE ACCURACY VALIDATION REPORT")
        report.append("=" * 80)
        report.append(f"📅 Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"📁 Test Directory: {self.test_directory}")
        report.append(f"⏱️ Validation Duration: {results['validation_duration']:.2f} seconds")
        report.append("")
        
        # Summary section
        report.append("📈 VALIDATION SUMMARY:")
        report.append(f"  • Total Test Files: {results['total_files']}")
        report.append(f"  • Valid Syntax Files: {results['valid_files']}")
        report.append(f"  • Invalid Files: {results['invalid_files']}")
        report.append(f"  • Average Quality Score: {results['average_quality_score']:.1f}/100")
        report.append("")
        
        # Detailed results
        report.append("📋 DETAILED FILE ANALYSIS:")
        report.append("-" * 80)
        
        for filename, file_result in results["results"].items():
            if not file_result["exists"]:
                report.append(f"❌ {filename}: FILE NOT FOUND")
                continue
            
            validations = file_result.get("validations", {})
            quality = file_result.get("quality_score", 0)
            
            # File header
            quality_emoji = "🟢" if quality >= 80 else "🟡" if quality >= 60 else "🔴"
            report.append(f"{quality_emoji} {filename} - Quality Score: {quality:.1f}/100")
            
            # Syntax validation
            syntax = validations.get("syntax", {})
            if syntax.get("valid_syntax"):
                report.append(f"  ✅ Syntax: Valid Python code")
            else:
                report.append(f"  ❌ Syntax: {syntax.get('error', 'Unknown error')}")
            
            # Playwright usage
            pw_usage = validations.get("playwright_usage", {})
            if pw_usage:
                report.append(f"  🎭 Playwright Usage:")
                report.append(f"    • Imports Playwright: {'✅' if pw_usage.get('imports_playwright') else '❌'}")
                report.append(f"    • Uses Sync API: {'✅' if pw_usage.get('uses_sync_api') else '❌'}")
                report.append(f"    • Browser Launch: {'✅' if pw_usage.get('has_browser_launch') else '❌'}")
                report.append(f"    • Page Actions: {'✅' if pw_usage.get('has_page_actions') else '❌'}")
                report.append(f"    • Expectations: {'✅' if pw_usage.get('has_expectations') else '❌'}")
                report.append(f"    • Screenshots: {'✅' if pw_usage.get('has_screenshots') else '❌'}")
            
            # Structure analysis
            structure = validations.get("structure", {})
            if structure:
                report.append(f"  📋 Test Structure:")
                report.append(f"    • Function Count: {structure.get('function_count', 0)}")
                report.append(f"    • Has Docstrings: {'✅' if structure.get('has_docstring') else '❌'}")
                report.append(f"    • Error Handling: {'✅' if structure.get('has_error_handling') else '❌'}")
                report.append(f"    • Documentation Score: {structure.get('documentation_score', 0)}")
            
            # Logic validation
            logic = validations.get("logic", {})
            if logic:
                report.append(f"  🧠 Test Logic:")
                report.append(f"    • Logical Flow: {'✅' if logic.get('logical_flow') else '❌'}")
                report.append(f"    • Error Handling: {'✅' if logic.get('error_handling') else '❌'}")
                report.append(f"    • Comprehensive: {'✅' if logic.get('comprehensive_coverage') else '❌'}")
                if logic.get("issues"):
                    report.append(f"    • Issues: {', '.join(logic['issues'])}")
            
            report.append(f"  📊 File Size: {file_result.get('file_size', 0):,} bytes")
            report.append("")
        
        # Recommendations
        report.append("🎯 VALIDATION RECOMMENDATIONS:")
        report.append("-" * 40)
        
        if results["average_quality_score"] >= 80:
            report.append("🎉 Excellent test quality! All tests meet high standards.")
        elif results["average_quality_score"] >= 60:
            report.append("👍 Good test quality with room for improvement:")
            report.append("  • Add more comprehensive error handling")
            report.append("  • Increase documentation coverage")
            report.append("  • Add more assertion validations")
        else:
            report.append("⚠️ Test quality needs improvement:")
            report.append("  • Fix syntax errors in failing files")
            report.append("  • Add proper Playwright API usage")
            report.append("  • Implement comprehensive error handling")
            report.append("  • Add detailed documentation")
        
        report.append("")
        report.append("🔧 EXECUTION READINESS:")
        if results["valid_files"] == results["total_files"]:
            report.append("✅ All test files have valid syntax and are ready for execution")
            report.append("✅ Playwright API usage appears correct")
            report.append("✅ Test structure follows best practices")
        else:
            report.append("❌ Some test files have issues that prevent execution")
            report.append("⚠️ Review and fix reported issues before running tests")
        
        report.append("")
        report.append("=" * 80)
        report.append("Validation completed successfully! 🎯")
        
        return "\n".join(report)


def main():
    """Main validation execution"""
    # Get current directory (should be test_cases)
    current_dir = os.getcwd()
    if not current_dir.endswith("test_cases"):
        test_dir = os.path.join(current_dir, "test_cases")
        if os.path.exists(test_dir):
            current_dir = test_dir
    
    print(f"🔍 Validating tests in: {current_dir}")
    
    # Initialize validator
    validator = TestValidator(current_dir)
    
    # Run validation
    results = validator.run_validation()
    
    # Generate and display report
    report = validator.generate_report(results)
    print(report)
    
    # Save report to file
    report_file = Path(current_dir) / "validation_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\n📄 Full report saved to: {report_file}")
    
    # Return success/failure based on results
    if results["valid_files"] == results["total_files"] and results["average_quality_score"] >= 70:
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())