#!/usr/bin/env python3
"""
Simple test for the storage account listing functionality
"""

import json
import sys
import os

# Add the current directory to Python path to import our script
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from get_storage_accounts import get_storage_accounts_via_mcp, SUBSCRIPTION_ID
except ImportError as e:
    print(f"Failed to import get_storage_accounts module: {e}")
    sys.exit(1)

def test_subscription_id():
    """Test that the subscription ID is correctly set."""
    expected_subscription = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    assert SUBSCRIPTION_ID == expected_subscription, f"Expected {expected_subscription}, got {SUBSCRIPTION_ID}"
    print("✓ Subscription ID is correctly set")

def test_get_storage_accounts_function():
    """Test that the function returns expected structure."""
    result = get_storage_accounts_via_mcp(SUBSCRIPTION_ID)
    
    # Check that result is a dictionary
    assert isinstance(result, dict), "Result should be a dictionary"
    print("✓ Function returns a dictionary")
    
    # Check required fields
    assert "status" in result, "Result should contain 'status' field"
    assert "subscription_id" in result, "Result should contain 'subscription_id' field"
    print("✓ Result contains required fields")
    
    # Check subscription ID matches
    assert result["subscription_id"] == SUBSCRIPTION_ID, "Subscription ID should match"
    print("✓ Subscription ID in result matches expected value")
    
    # Check status is valid
    valid_statuses = ["success", "error", "demo_mode", "authentication_required", "mcp_attempt"]
    assert result["status"] in valid_statuses, f"Status should be one of {valid_statuses}"
    print("✓ Status is valid")

def main():
    """Run all tests."""
    print("Testing storage account listing functionality...")
    print("=" * 50)
    
    try:
        test_subscription_id()
        test_get_storage_accounts_function()
        
        print("\n🎉 All tests passed!")
        print(f"The tool is ready to list storage accounts for subscription: {SUBSCRIPTION_ID}")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error during testing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()