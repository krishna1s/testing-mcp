#!/usr/bin/env python3
"""
Azure Load Test Resources Lister

This script demonstrates how to list Azure Load Test resources for a specific subscription
using the Azure MCP (Model Context Protocol) functions.

Requirements:
- Azure CLI authentication (run 'az login' first)
- Appropriate Azure permissions to list Load Testing resources
"""

import json
import sys
from typing import Dict, Any, List

def get_load_test_resources(subscription_id: str) -> Dict[str, Any]:
    """
    Get Azure Load Test resources for the specified subscription ID.
    
    This function would use the MCP function azmcp-loadtesting-loadtest-list
    to retrieve the load test resources.
    
    Args:
        subscription_id (str): The Azure subscription ID to query
        
    Returns:
        Dict[str, Any]: Response containing the list of load test resources
        
    Note:
        In a real implementation, this would call the MCP function:
        azmcp-loadtesting-loadtest-list with the subscription parameter
    """
    # This is a demonstration of what the MCP call would look like
    mcp_request = {
        "function": "azmcp-loadtesting-loadtest-list",
        "parameters": {
            "subscription": subscription_id
        }
    }
    
    print(f"MCP Request that would be made:")
    print(json.dumps(mcp_request, indent=2))
    
    # In a real scenario, this would return actual Azure Load Test resources
    # For demonstration purposes, return a sample response structure
    sample_response = {
        "status": "success",
        "subscription_id": subscription_id,
        "load_test_resources": [
            {
                "name": "example-load-test-1",
                "resource_group": "example-rg",
                "location": "East US",
                "status": "Active"
            },
            {
                "name": "example-load-test-2", 
                "resource_group": "example-rg-2",
                "location": "West US 2",
                "status": "Active"
            }
        ],
        "note": "This is sample data. Real implementation requires Azure authentication."
    }
    
    return sample_response

def main():
    """Main function to demonstrate Azure Load Test resource listing."""
    
    # The subscription ID from the issue
    subscription_id = "7c71b563-0dc0-4bc0-4bc0-bcf6-06f8f0516c7a"
    
    print("Azure Load Test Resources Lister")
    print("=" * 40)
    print(f"Subscription ID: {subscription_id}")
    print()
    
    try:
        # Get the load test resources
        result = get_load_test_resources(subscription_id)
        
        print("Result:")
        print(json.dumps(result, indent=2))
        
        if "load_test_resources" in result:
            resources = result["load_test_resources"]
            print(f"\nFound {len(resources)} Load Test resource(s):")
            for i, resource in enumerate(resources, 1):
                print(f"{i}. {resource.get('name', 'Unknown')} "
                      f"(RG: {resource.get('resource_group', 'Unknown')}, "
                      f"Location: {resource.get('location', 'Unknown')})")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()