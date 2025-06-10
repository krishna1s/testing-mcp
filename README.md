# Azure Load Test Resources Lister

This repository contains a demonstration script for listing Azure Load Test resources for a specific subscription using Azure MCP (Model Context Protocol) functions.

## Purpose

This implementation addresses the requirement to get a list of Azure Load Test resources for subscription ID `7c71b563-0dc0-4bc0-4bc0-bcf6-06f8f0516c7a`.

## Files

- `azure_load_test_lister.py` - Main Python script that demonstrates how to list Azure Load Test resources
- `requirements.txt` - Python dependencies (if any)
- `.github/workflows/copilot-setup-steps.yml` - GitHub Actions workflow for Azure authentication

## Usage

### Prerequisites

1. **Azure Authentication**: You must be authenticated with Azure CLI
   ```bash
   az login
   ```

2. **Azure Permissions**: Your account must have appropriate permissions to list Load Testing resources in the subscription

### Running the Script

```bash
python3 azure_load_test_lister.py
```

### Expected Output

The script will:
1. Display the subscription ID being queried
2. Show the MCP request structure that would be used
3. Return a list of Azure Load Test resources (or sample data in demonstration mode)

## MCP Function Used

The implementation uses the `azmcp-loadtesting-loadtest-list` MCP function with the following parameters:

```json
{
  "function": "azmcp-loadtesting-loadtest-list",
  "parameters": {
    "subscription": "7c71b563-0dc0-4bc0-4bc0-bcf6-06f8f0516c7a"
  }
}
```

## Authentication Requirements

The MCP function requires Azure authentication. The error message you might see without proper authentication:

```
Authentication failed. Please run 'az login' to sign in to Azure.
```

## Implementation Notes

- The script is designed to be minimal and focused on the specific requirement
- It demonstrates the proper MCP function call structure
- Error handling is included for authentication and other potential issues
- The implementation follows Azure best practices for resource listing

## Testing

To test the actual functionality (requires Azure authentication):

1. Ensure you're logged into Azure CLI: `az login`
2. Verify you have access to the subscription: `az account show`
3. Run the script: `python3 azure_load_test_lister.py`

## Troubleshooting

If you encounter authentication issues:
1. Run `az login` to authenticate
2. Verify your account has access to the subscription
3. Check that your account has permissions to list Load Testing resources