# Azure Load Testing MCP Demo

This repository demonstrates how to retrieve Azure Load Testing resources for a specific subscription and tenant.

## Subscription and Tenant Details

- **Subscription ID**: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
- **Tenant ID**: `72f988bf-86f1-41af-91ab-2d7cd011db47`

## Usage

### Using the Python Script

Run the Python script to demonstrate load test retrieval:

```bash
python3 get_load_tests.py
```

### Using Azure MCP Tools

If you have access to Azure MCP tools, you can use the following command structure:

```bash
# List load tests for the subscription
azmcp-loadtesting-loadtest-list --subscription "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a" --tenant "72f988bf-86f1-41af-91ab-2d7cd011db47"
```

## Prerequisites

- Azure authentication (if using real Azure APIs)
- Python 3.x (for the demo script)
- Appropriate Azure permissions for the subscription and tenant

## Files

- `get_load_tests.py`: Python script that demonstrates load test retrieval
- `README.md`: This documentation file
- `.github/workflows/copilot-setup-steps.yml`: GitHub workflow for Azure authentication

## Authentication

The GitHub workflow includes Azure login configuration using:
- Azure Client ID (from secrets)
- Azure Tenant ID (from secrets)

## Notes

The Python script serves as a demonstration and template. In a real implementation, it would:
1. Authenticate with Azure using proper credentials
2. Use Azure SDK or MCP tools to query actual load testing resources
3. Handle errors and edge cases appropriately
4. Return actual load test data from the specified subscription