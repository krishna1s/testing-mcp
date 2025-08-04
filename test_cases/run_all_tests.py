"""
Test Execution Master Script
============================

This script orchestrates the execution of all generated Python Playwright tests.
It provides comprehensive test execution, reporting, and result analysis.

Features:
- Executes all test files in logical order
- Provides detailed reporting and screenshots
- Handles errors gracefully with comprehensive logging
- Generates execution summary reports
"""

import os
import sys
import time
import traceback
from pathlib import Path
from playwright.sync_api import sync_playwright


def get_test_files():
    """
    Get all Python test files in the correct execution order
    """
    test_files = [
        {
            "name": "Main User Journey", 
            "file": "main_user_journey.py",
            "description": "Core user workflow - workspace creation and deletion"
        },
        {
            "name": "Authentication Flows", 
            "file": "auth_flows.py",
            "description": "Login, logout, and authentication validation tests"
        },
        {
            "name": "Form Validations", 
            "file": "form_validations.py",
            "description": "Input validation and form interaction tests"
        },
        {
            "name": "Workspace Management", 
            "file": "workspace_management.py",
            "description": "Workspace CRUD operations and management interface tests"
        },
        {
            "name": "Navigation Comprehensive", 
            "file": "navigation_comprehensive.py",
            "description": "UI navigation, responsive design, and accessibility tests"
        },
        {
            "name": "Error Scenarios", 
            "file": "error_scenarios.py",
            "description": "Edge cases, error conditions, and recovery tests"
        }
    ]
    
    return test_files


def execute_test_file(test_info):
    """
    Execute a single test file and return results
    """
    print(f"\n{'='*80}")
    print(f"🎯 EXECUTING: {test_info['name']}")
    print(f"📁 File: {test_info['file']}")
    print(f"📋 Description: {test_info['description']}")
    print(f"{'='*80}")
    
    start_time = time.time()
    
    try:
        # Import and execute the test module
        test_file_path = Path(__file__).parent / test_info['file']
        
        if not test_file_path.exists():
            print(f"❌ Test file not found: {test_file_path}")
            return {
                "name": test_info['name'],
                "status": "FILE_NOT_FOUND",
                "duration": 0,
                "error": f"File not found: {test_file_path}"
            }
        
        print(f"📂 Executing test file: {test_file_path}")
        
        # Execute the test file
        exec(open(test_file_path).read())
        
        duration = time.time() - start_time
        print(f"✅ {test_info['name']} completed successfully in {duration:.2f}s")
        
        return {
            "name": test_info['name'],
            "status": "PASSED",
            "duration": duration,
            "error": None
        }
        
    except Exception as e:
        duration = time.time() - start_time
        error_msg = str(e)
        traceback_msg = traceback.format_exc()
        
        print(f"❌ {test_info['name']} failed after {duration:.2f}s")
        print(f"Error: {error_msg}")
        print(f"Traceback: {traceback_msg}")
        
        return {
            "name": test_info['name'],
            "status": "FAILED",
            "duration": duration,
            "error": error_msg,
            "traceback": traceback_msg
        }


def generate_summary_report(results):
    """
    Generate a comprehensive summary report of all test executions
    """
    total_tests = len(results)
    passed_tests = len([r for r in results if r['status'] == 'PASSED'])
    failed_tests = len([r for r in results if r['status'] == 'FAILED'])
    not_found_tests = len([r for r in results if r['status'] == 'FILE_NOT_FOUND'])
    total_duration = sum(r['duration'] for r in results)
    
    print(f"\n{'='*80}")
    print(f"📊 COMPREHENSIVE TEST EXECUTION SUMMARY")
    print(f"{'='*80}")
    print(f"📈 Total Tests: {total_tests}")
    print(f"✅ Passed: {passed_tests}")
    print(f"❌ Failed: {failed_tests}")
    print(f"📁 Not Found: {not_found_tests}")
    print(f"⏱️ Total Duration: {total_duration:.2f} seconds")
    print(f"📊 Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    print(f"{'='*80}")
    
    print(f"\n📋 DETAILED RESULTS:")
    for result in results:
        status_emoji = {
            'PASSED': '✅',
            'FAILED': '❌', 
            'FILE_NOT_FOUND': '📁'
        }.get(result['status'], '❓')
        
        print(f"{status_emoji} {result['name']}: {result['status']} ({result['duration']:.2f}s)")
        if result['error']:
            print(f"   💬 Error: {result['error']}")
    
    print(f"\n{'='*80}")
    
    # Generate recommendations
    print(f"🎯 RECOMMENDATIONS:")
    if failed_tests > 0:
        print(f"• {failed_tests} test(s) failed - review error messages and screenshots")
        print(f"• Check browser compatibility and network connectivity")
        print(f"• Verify test credentials and environment setup")
    
    if not_found_tests > 0:
        print(f"• {not_found_tests} test file(s) not found - verify file generation completed")
    
    if passed_tests == total_tests:
        print(f"🎉 All tests passed! Excellent test coverage achieved.")
    
    print(f"{'='*80}")


def main():
    """
    Main execution function - orchestrates all test execution
    """
    print(f"🚀 PLAYWRIGHT PYTHON TEST EXECUTION MASTER")
    print(f"==========================================")
    print(f"🎯 Comprehensive TypeScript to Python test conversion execution")
    print(f"📅 Execution started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Working directory: {os.getcwd()}")
    
    # Get all test files
    test_files = get_test_files()
    print(f"📊 Found {len(test_files)} test files to execute")
    
    # Create screenshots directory
    screenshots_dir = Path("test_screenshots")
    screenshots_dir.mkdir(exist_ok=True)
    print(f"📸 Screenshots will be saved to: {screenshots_dir}")
    
    # Execute all tests
    results = []
    
    for i, test_info in enumerate(test_files, 1):
        print(f"\n🔄 Progress: {i}/{len(test_files)} tests")
        result = execute_test_file(test_info)
        results.append(result)
        
        # Small delay between tests for stability
        time.sleep(2)
    
    # Generate summary report
    generate_summary_report(results)
    
    # Final status
    total_passed = len([r for r in results if r['status'] == 'PASSED'])
    if total_passed == len(results):
        print(f"\n🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
        sys.exit(0)
    else:
        print(f"\n⚠️ SOME TESTS FAILED OR HAD ISSUES - Review results above")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n⚠️ Test execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test execution failed with unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)