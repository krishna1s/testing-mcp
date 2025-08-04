#!/usr/bin/env python3
"""
Simple test script to validate the load testing functionality.
"""

import json
import subprocess
import sys
from pathlib import Path


def test_config_file():
    """Test that the config file is valid and contains expected values."""
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        expected_subscription = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
        expected_tenant = "72f988bf-86f1-41af-91ab-2d7cd011db47"
        
        actual_subscription = config['azure_config']['subscription_id']
        actual_tenant = config['azure_config']['tenant_id']
        
        assert actual_subscription == expected_subscription, f"Expected subscription {expected_subscription}, got {actual_subscription}"
        assert actual_tenant == expected_tenant, f"Expected tenant {expected_tenant}, got {actual_tenant}"
        
        print("✓ Config file test passed")
        return True
        
    except Exception as e:
        print(f"✗ Config file test failed: {e}")
        return False


def test_get_load_tests_script():
    """Test that the get_load_tests.py script runs successfully."""
    try:
        result = subprocess.run([
            sys.executable, 'get_load_tests.py'
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            print(f"✗ Script test failed with return code {result.returncode}")
            print(f"stderr: {result.stderr}")
            return False
        
        # Check that the output contains expected subscription and tenant IDs
        expected_subscription = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
        expected_tenant = "72f988bf-86f1-41af-91ab-2d7cd011db47"
        
        if expected_subscription not in result.stdout or expected_tenant not in result.stdout:
            print("✗ Script test failed: expected subscription/tenant not found in output")
            return False
        
        print("✓ Script test passed")
        return True
        
    except Exception as e:
        print(f"✗ Script test failed: {e}")
        return False


def test_file_existence():
    """Test that all expected files exist."""
    expected_files = ['README.md', 'config.json', 'get_load_tests.py']
    
    for file_name in expected_files:
        if not Path(file_name).exists():
            print(f"✗ File existence test failed: {file_name} not found")
            return False
    
    print("✓ File existence test passed")
    return True


def main():
    """Run all tests."""
    print("Running tests for Azure Load Testing MCP demo...")
    
    tests = [
        test_file_existence,
        test_config_file,
        test_get_load_tests_script
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! ✓")
        return 0
    else:
        print("Some tests failed! ✗")
        return 1


if __name__ == "__main__":
    sys.exit(main())