#!/bin/bash

# Azure Load Test Resources Lister - Shell Script
# This script demonstrates the direct MCP function call needed

SUBSCRIPTION_ID="7c71b563-0dc0-4bc0-4bc0-bcf6-06f8f0516c7a"

echo "Azure Load Test Resources Lister (Shell Script)"
echo "================================================"
echo "Subscription ID: $SUBSCRIPTION_ID"
echo ""

echo "MCP Function Call Required:"
echo "Function: azmcp-loadtesting-loadtest-list"
echo "Parameters:"
echo "  subscription: $SUBSCRIPTION_ID"
echo ""

echo "Note: This requires proper Azure authentication and MCP environment."
echo "To authenticate: az login"
echo ""

echo "Expected JSON structure for MCP call:"
cat << EOF
{
  "function": "azmcp-loadtesting-loadtest-list",
  "parameters": {
    "subscription": "$SUBSCRIPTION_ID"
  }
}
EOF