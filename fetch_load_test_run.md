# Azure Load Testing Run Details

## Objective
Fetch Azure load test run details for:
- Subscription: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
- Resource Group: `nishtha-dev-rg`
- Load Test Resource: `testing-loader`
- Test Run ID: `eb16daf8-365d-4a78-a7d5-b74f90a5b49b`

## Available Methods

### Method 1: Azure MCP Tool
```bash
azmcp-loadtesting-loadtestrun-get \
  --subscription="7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a" \
  --resource-group="nishtha-dev-rg" \
  --load-test-name="testing-loader" \
  --load-testrun-id="eb16daf8-365d-4a78-a7d5-b74f90a5b49b" \
  --tenant="72f988bf-86f1-41af-91ab-2d7cd011db47"
```

### Method 2: Azure CLI Extension
```bash
az load test-run show \
  --test-run-id="eb16daf8-365d-4a78-a7d5-b74f90a5b49b" \
  --name="testing-loader" \
  --resource-group="nishtha-dev-rg"
```

## Authentication Setup
The workflow YAML has been configured to:
1. Authenticate with Azure using managed identity
2. Generate Azure Load Testing Data Plane Access Token
3. Set the token as `AZURE_MCP_STATIC_TOKEN` environment variable

## Status
- Azure CLI Load Testing extension installed successfully
- Authentication configured in workflow
- Commands identified and ready to execute
- Requires proper Azure environment with authentication to fetch the actual test run details

## Expected Output
The commands should return test run details including:
- Test run status (running, completed, failed, etc.)
- Start and end times
- Test configuration
- Performance metrics
- Error details (if any)