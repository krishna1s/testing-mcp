# Azure MCP Storage Account Testing

## Objective
Test the Azure MCP tool to retrieve storage accounts for subscription ID: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

## Environment Setup
The following Azure environment variables are available:
- `AZURE_TENANT_ID`: 72f988bf-86f1-41af-91ab-2d7cd011db47
- `AZURE_CLIENT_ID`: 12fa8445-f1ce-4697-9ae3-c8d9260770ad
- `AZURE_SUBSCRIPTION_ID`: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
- `AZURE_FEDERATED_TOKEN_FILE`: /tmp/github_oidc_token

## Azure CLI Verification
Azure CLI is authenticated and working:
```json
{
  "environmentName": "AzureCloud",
  "homeTenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
  "id": "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a",
  "isDefault": true,
  "managedByTenants": [],
  "name": "Cloud-Native-Testing-IDC-Test",
  "state": "Enabled",
  "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
  "user": {
    "name": "12fa8445-f1ce-4697-9ae3-c8d9260770ad",
    "type": "servicePrincipal"
  }
}
```

## Azure MCP Tool Testing Results
Attempted to use various Azure MCP functions with different authentication parameters:

### Storage Account Tests

#### Test 1: Basic call
```
azmcp-storage-account-list(subscription="7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a")
```
Result: Authentication failed (401)

#### Test 2: With tenant parameter
```
azmcp-storage-account-list(
    subscription="7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a",
    tenant="72f988bf-86f1-41af-91ab-2d7cd011db47"
)
```
Result: Authentication failed (401)

#### Test 3: With credential auth method
```
azmcp-storage-account-list(
    auth-method=0,
    subscription="7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a",
    tenant="72f988bf-86f1-41af-91ab-2d7cd011db47"
)
```
Result: Authentication failed (401)

### Subscription List Tests

#### Test 4: Basic subscription list
```
azmcp-subscription-list()
```
Result: Authentication failed (401)

#### Test 5: Subscription list with tenant
```
azmcp-subscription-list(tenant="72f988bf-86f1-41af-91ab-2d7cd011db47")
```
Result: Authentication failed (401)

## Error Details
All attempts resulted in the same authentication error:
```
ChainedTokenCredential failed due to an unhandled exception: 
InteractiveBrowserCredential authentication failed: 
Persistence check failed.
```

## Analysis
The Azure MCP tool appears to be using ChainedTokenCredential which includes InteractiveBrowserCredential, but this fails in the GitHub Actions environment where no interactive browser is available. The tool should be configured to use the available service principal authentication via the environment variables or OIDC token.

## Recommendation
The Azure MCP tool needs to be updated to properly handle service principal authentication in non-interactive environments like GitHub Actions, using the available Azure environment variables:
- AZURE_CLIENT_ID
- AZURE_TENANT_ID  
- AZURE_FEDERATED_TOKEN_FILE

This would allow the tool to authenticate using the OIDC token provided by GitHub Actions.

## Conclusion
**The Azure MCP tool validation for listing storage accounts has identified an authentication issue.**

✅ **What works:**
- Azure CLI authentication is properly configured and working
- Subscription ID `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a` is accessible
- All required environment variables are available

❌ **What doesn't work:**
- Azure MCP tools fail to authenticate in GitHub Actions environment
- ChainedTokenCredential attempts to use InteractiveBrowserCredential which fails in non-interactive environments
- None of the available auth-method parameters resolve the authentication issue

**Recommendation for Azure MCP Tool:**
The tool needs to be enhanced to support federated token authentication using `AZURE_FEDERATED_TOKEN_FILE` in GitHub Actions environments, similar to how Azure CLI successfully authenticates in the same environment.