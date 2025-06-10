# Azure Storage Account Listing Tool

This repository contains tools to get the list of storage accounts for Azure subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`.

## Files

- `get_storage_accounts.py` - Python script to retrieve storage accounts for the specified subscription
- `copilot-setup-steps.yml` - Azure authentication workflow configuration

## Usage

### Prerequisites

To use this tool in a real Azure environment, you need:

1. Azure CLI installed and configured
2. Authentication to Azure with appropriate permissions
3. Access to the target subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

### Running the Script

```bash
# Make sure you're authenticated to Azure
az login

# Run the storage account listing script
python3 get_storage_accounts.py
```

### Using Azure MCP Tools Directly

This repository is designed to work with Azure MCP (Model Context Protocol) tools. In an environment where Azure MCP tools are available, you can directly call:

```python
from azure_mcp_tools import azmcp_storage_account_list

result = azmcp_storage_account_list(subscription="7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a")
print(result)
```

## Expected Output

When run in an authenticated Azure environment, the script will return a JSON response containing:

- List of storage accounts in the subscription
- Account names, locations, resource groups
- Storage account properties and status information

## Authentication

The script requires Azure authentication. Ensure you have:

1. Valid Azure credentials
2. Appropriate RBAC permissions on the target subscription
3. Reader or Contributor access to view storage accounts

## Error Handling

The script includes error handling for common scenarios:

- Authentication failures
- Permission issues
- Network connectivity problems
- Invalid subscription IDs

## Testing

To verify the functionality, run the included test:

```bash
python3 test_storage_accounts.py
```

This test verifies:
- Correct subscription ID configuration
- Function return structure
- Required fields in response
- Valid status values

In environments without Azure authentication, the script will run in demo mode showing the expected structure and functionality.