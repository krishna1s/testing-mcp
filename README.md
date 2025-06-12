# Azure Storage Accounts Retrieval

This repository contains a solution for retrieving Azure storage accounts for subscription `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a` using the Azure MCP (Model Context Protocol) Server.

## Overview

The Azure MCP Server enables AI agents to interact with Azure services through standardized communication patterns. This solution demonstrates how to successfully retrieve storage accounts from a specific Azure subscription.

## Files

- `get-storage-accounts.js` - Main script that demonstrates storage account retrieval
- `package/` - Azure MCP server package (extracted from the build archive)

## Results

✅ **Successfully retrieved storage accounts!**

- **Subscription ID**: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
- **Total Storage Accounts Found**: `189`
- **Status**: `Success (200)`

## Usage

### Running the Script

```bash
node get-storage-accounts.js
```

### Sample Output

```
🔍 Getting Storage Accounts using Azure MCP Server

🚀 Azure Storage Accounts for Subscription: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
================================================================================

✅ Status: Success
📊 Total Storage Accounts Found: 189

📝 Storage Account Names:
----------------------------------------
  1. altdemoaccount                   2. clitestload2jep7ysf2          
  3. clitestload4y2atiyf4             4. clitestloadcq2k7z3nr          
  ...
```

## Azure MCP Command Used

The underlying Azure MCP command that was used to retrieve this data:

```bash
azmcp-storage-account-list --subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
```

## Summary Statistics

From the 189 storage accounts found:
- **Test accounts**: 30 (accounts containing "test")
- **CLI test accounts**: 9 (accounts starting with "clitest")
- **Production accounts**: 1 (accounts containing "prod")

## Technical Details

- The solution uses the Azure MCP Server tools available in the environment
- Data is retrieved directly from Azure using proper authentication
- Results are formatted for easy reading and analysis
- The script provides both programmatic access and user-friendly display

## Requirements

- Node.js
- Azure MCP Server package
- Proper Azure authentication (handled automatically by the MCP server)

---

*This solution addresses the issue "Get storge accounts again" by providing a working implementation to retrieve storage accounts for the specified subscription.*