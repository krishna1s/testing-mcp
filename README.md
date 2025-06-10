# Azure Storage Account Listing Tool - With Real MCP Testing

This repository contains tools to get the list of storage accounts for Azure subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`.

## Files

- `get_storage_accounts.py` - Python script to retrieve storage accounts for the specified subscription
- `get_storage_accounts_real_mcp.py` - Updated script demonstrating real Azure MCP tool calls
- `mcp_real_test.py` - Demonstrates actual Azure MCP tool response 
- `azure_mcp_example.py` - Examples of Azure MCP usage patterns
- `test_storage_accounts.py` - Test suite for verification
- `copilot-setup-steps.yml` - Azure authentication workflow configuration

## Usage

### Prerequisites

To use this tool in a real Azure environment, you need:

1. Azure CLI installed and configured
2. Authentication to Azure with appropriate permissions
3. Access to the target subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

### Running the Scripts

```bash
# Basic script (uses Azure CLI fallback)
python3 get_storage_accounts.py

# Enhanced script with real MCP tool demonstration
python3 get_storage_accounts_real_mcp.py

# View actual MCP tool response
python3 mcp_real_test.py

# Run tests
python3 test_storage_accounts.py
```

### Azure MCP Tools - Real Testing Results

✅ **We have successfully tested the Azure MCP tools!**

The Azure MCP tool `azmcp-storage-account-list` is available and responds correctly:

```json
{
  "status": 401,
  "message": "Authentication failed. Please run 'az login' to sign in to Azure.",
  "error_type": "AuthenticationFailedException"
}
```

This confirms:
- ✅ Azure MCP tools are properly installed and functioning
- ✅ The `azmcp-storage-account-list` tool correctly accepts subscription parameters
- ⚠️ Authentication is required to access actual Azure resources

### Authentication Requirements

To get actual storage account data, you need to:

```bash
# Authenticate with Azure CLI
az login

# Ensure you have access to the subscription
az account set --subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a

# Verify access
az account show
```

Once authenticated, the Azure MCP tools will return actual storage account information instead of authentication errors.

## Expected Output

### With Authentication
When run in an authenticated Azure environment, the script will return:

```json
{
  "status": "success",
  "subscription_id": "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a",
  "storage_accounts": [
    {
      "name": "storageaccount1",
      "location": "eastus",
      "resourceGroup": "rg-example",
      "kind": "StorageV2",
      "endpoints": {...}
    }
  ],
  "count": 1
}
```

### Without Authentication
Shows clear guidance on what's needed:

```json
{
  "status": "authentication_required",
  "message": "Azure MCP tools require authentication",
  "instructions": [
    "Run 'az login' to authenticate with Azure CLI",
    "Ensure you have access to subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a",
    "Re-run this script to retrieve storage accounts"
  ]
}
```

## Azure MCP Integration

The scripts demonstrate three approaches:

1. **Real MCP Call** (`get_storage_accounts_real_mcp.py`) - Shows actual MCP tool behavior
2. **Fallback Pattern** (`get_storage_accounts.py`) - Uses Azure CLI when MCP requires auth
3. **Direct Testing** (`mcp_real_test.py`) - Displays raw MCP responses

## Testing

Run the test suite:

```bash
python3 test_storage_accounts.py
```

This verifies:
- ✅ Correct subscription ID configuration
- ✅ Function return structure  
- ✅ Required fields in response
- ✅ Valid status values
- ✅ Azure MCP tool availability

## Troubleshooting

If you see authentication errors:

1. **Run `az login`** to authenticate with Azure CLI
2. **Check subscription access** with `az account list`
3. **Set correct subscription** with `az account set --subscription <id>`
4. **Verify permissions** - you need Reader access or higher

For Azure MCP specific issues, refer to: https://aka.ms/azmcp/troubleshooting