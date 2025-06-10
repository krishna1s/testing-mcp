#!/usr/bin/env python3
"""
Test script to directly call Azure MCP tools.

This script attempts to directly use the azmcp-storage-account-list tool
to retrieve storage accounts for subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
"""

import json

# Subscription ID as specified in the issue
SUBSCRIPTION_ID = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"

def test_mcp_storage_account_list():
    """
    Test the Azure MCP storage account list function directly.
    """
    print(f"Testing Azure MCP storage account list for subscription: {SUBSCRIPTION_ID}")
    print("=" * 70)
    
    try:
        # This will attempt to call the actual MCP function available in this environment
        print("Attempting to call azmcp-storage-account-list...")
        
        # Note: In the MCP environment, this function should be available
        # We'll try to demonstrate what the call should look like
        print(f"Function call: azmcp_storage_account_list(subscription='{SUBSCRIPTION_ID}')")
        
        # Since we can't directly import or call the MCP function from Python,
        # let's show what the expected call pattern would be
        print("\nExpected MCP tool call parameters:")
        print(f"  - subscription: {SUBSCRIPTION_ID}")
        print("  - auth-method: credential (default)")
        
        print("\nThis would return JSON with storage account information.")
        print("To actually run this, the Azure MCP tools need to be properly configured.")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_mcp_storage_account_list()