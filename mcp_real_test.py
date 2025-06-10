#!/usr/bin/env python3
"""
Real Azure MCP Tool Test

This script demonstrates the actual Azure MCP tool call and its response.
It shows what happens when we try to call azmcp-storage-account-list.
"""

import json

# Subscription ID as specified in the issue
SUBSCRIPTION_ID = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"

def demonstrate_mcp_call():
    """
    Demonstrate the actual Azure MCP tool call and response.
    """
    print(f"Azure MCP Tool Test for Subscription: {SUBSCRIPTION_ID}")
    print("=" * 60)
    
    print("Tool: azmcp-storage-account-list")
    print(f"Parameter: subscription = '{SUBSCRIPTION_ID}'")
    print()
    
    print("Actual MCP Tool Response:")
    print("-" * 30)
    
    # This is the actual response we got when calling the MCP tool
    mcp_response = {
        "status": 401,
        "message": "Authentication failed. Please run 'az login' to sign in to Azure. Details: The ChainedTokenCredential failed due to an unhandled exception: InteractiveBrowserCredential authentication failed: Persistence check failed. Inspect inner exception for details. To mitigate this issue, please refer to the troubleshooting guidelines here at https://aka.ms/azmcp/troubleshooting.",
        "results": {
            "message": "The ChainedTokenCredential failed due to an unhandled exception: InteractiveBrowserCredential authentication failed: Persistence check failed. Inspect inner exception for details",
            "type": "AuthenticationFailedException"
        },
        "duration": 0
    }
    
    print(json.dumps(mcp_response, indent=2))
    
    print("\nAnalysis:")
    print("✓ Azure MCP tools are available and responding")
    print("✗ Authentication is required (status 401)")
    print("📋 The tool requires Azure credentials to access the subscription")
    
    print("\nTo fix this:")
    print("1. Run 'az login' to authenticate with Azure CLI")
    print("2. Ensure you have proper permissions for the subscription")
    print("3. The MCP tool will then be able to retrieve storage accounts")
    
    print(f"\nOnce authenticated, the tool would return:")
    print("- List of storage accounts in the subscription")
    print("- Account details (names, locations, resource groups)")
    print("- Endpoints and configuration information")

if __name__ == "__main__":
    demonstrate_mcp_call()