#!/usr/bin/env python3
"""
Script to get storage accounts for Azure subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a

This script demonstrates how to use Azure MCP tools to retrieve storage account information.
When run in an authenticated Azure environment, it will call the Azure MCP storage account list function.
"""

import json
import sys
import subprocess
from typing import Dict, Any

# Subscription ID as specified in the issue
SUBSCRIPTION_ID = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"

def check_azure_auth() -> bool:
    """Check if user is authenticated to Azure CLI."""
    try:
        result = subprocess.run(['az', 'account', 'show'], 
                              capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False

def get_storage_accounts_via_azure_cli(subscription_id: str) -> Dict[str, Any]:
    """
    Get storage accounts using Azure CLI as a fallback.
    
    Args:
        subscription_id: Azure subscription ID
        
    Returns:
        Dictionary containing storage account information
    """
    try:
        # Set the subscription
        subprocess.run(['az', 'account', 'set', '--subscription', subscription_id], 
                      check=True, capture_output=True)
        
        # List storage accounts
        result = subprocess.run(['az', 'storage', 'account', 'list', '--output', 'json'], 
                              capture_output=True, text=True, check=True)
        
        storage_accounts = json.loads(result.stdout)
        
        return {
            "status": "success",
            "subscription_id": subscription_id,
            "storage_accounts": storage_accounts,
            "count": len(storage_accounts),
            "method": "azure_cli"
        }
        
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "message": f"Azure CLI error: {e.stderr.decode() if e.stderr else str(e)}",
            "subscription_id": subscription_id
        }
    except Exception as e:
        return {
            "status": "error", 
            "message": f"Unexpected error: {str(e)}",
            "subscription_id": subscription_id
        }

def get_storage_accounts_via_mcp(subscription_id: str) -> Dict[str, Any]:
    """
    Get storage accounts using Azure MCP tools.
    
    This function would typically call the azmcp-storage-account-list tool
    but requires proper Azure authentication to be set up.
    
    Args:
        subscription_id: Azure subscription ID
        
    Returns:
        Dictionary containing storage account information
    """
    # Note: In an environment with Azure MCP tools available and properly configured,
    # this would make a direct call to the MCP tool:
    # result = azmcp_storage_account_list(subscription=subscription_id)
    # return result
    
    # For now, we'll try Azure CLI as an alternative
    if check_azure_auth():
        print("Azure authentication detected. Attempting to list storage accounts via Azure CLI...")
        return get_storage_accounts_via_azure_cli(subscription_id)
    else:
        # Mock response for demonstration purposes when no auth is available
        return {
            "status": "demo_mode", 
            "message": f"Demo mode: This would list storage accounts for subscription {subscription_id}",
            "subscription_id": subscription_id,
            "note": "To run this in a real Azure environment, ensure you are authenticated with 'az login' and have appropriate permissions to the subscription.",
            "azure_mcp_command": f"azmcp-storage-account-list --subscription {subscription_id}"
        }

def main():
    """Main function to retrieve and display storage accounts."""
    print(f"Getting storage accounts for subscription: {SUBSCRIPTION_ID}")
    print("=" * 60)
    
    try:
        result = get_storage_accounts_via_mcp(SUBSCRIPTION_ID)
        print(json.dumps(result, indent=2))
        
        status = result.get("status")
        if status == "success":
            count = result.get("count", 0)
            print(f"\nSuccessfully retrieved {count} storage account(s) for subscription {SUBSCRIPTION_ID}")
            
            # Display storage account names if available
            storage_accounts = result.get("storage_accounts", [])
            if storage_accounts:
                print("\nStorage Accounts found:")
                for account in storage_accounts:
                    name = account.get("name", "Unknown")
                    location = account.get("location", "Unknown")
                    resource_group = account.get("resourceGroup", "Unknown")
                    print(f"  - {name} (Location: {location}, Resource Group: {resource_group})")
                    
        elif status == "demo_mode":
            print(f"\nRunning in demo mode. To get actual storage accounts:")
            print(f"1. Authenticate with Azure CLI: az login")
            print(f"2. Ensure you have access to subscription {SUBSCRIPTION_ID}")
            print(f"3. Re-run this script")
            
        else:
            print(f"\nFailed to retrieve storage accounts: {result.get('message', 'Unknown error')}")
            
    except Exception as e:
        print(f"Error occurred while retrieving storage accounts: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()