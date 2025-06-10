#!/usr/bin/env python3
"""
Direct Azure MCP Tool Usage Example

This script shows how to directly use the Azure MCP tools available in this environment
to get storage accounts for subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
"""

# Example of how to use Azure MCP tools directly when they are available:

# 1. Using the azmcp-storage-account-list tool
def example_mcp_usage():
    """
    Example of direct Azure MCP tool usage.
    
    In an environment with proper Azure MCP setup, you would call:
    """
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    # This is the exact function call that would be used:
    print("Azure MCP Tool Usage:")
    print("=" * 40)
    print(f"Function: azmcp-storage-account-list")
    print(f"Parameter: subscription = '{subscription_id}'")
    print()
    print("Example call:")
    print(f"result = azmcp_storage_account_list(subscription='{subscription_id}')")
    print()
    print("Expected result structure:")
    print("""
{
  "status": "success",
  "storage_accounts": [
    {
      "name": "storageaccount1",
      "resourceGroup": "rg-example",
      "location": "eastus",
      "kind": "StorageV2",
      "skuName": "Standard_LRS",
      "skuTier": "Standard",
      "creationTime": "2023-01-01T00:00:00Z",
      "primaryEndpoints": {
        "blob": "https://storageaccount1.blob.core.windows.net/",
        "queue": "https://storageaccount1.queue.core.windows.net/",
        "table": "https://storageaccount1.table.core.windows.net/",
        "file": "https://storageaccount1.file.core.windows.net/"
      }
    }
  ],
  "count": 1
}
    """)

if __name__ == "__main__":
    example_mcp_usage()