# Azure Storage Accounts for Subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a

This repository demonstrates how to retrieve Azure storage accounts using the Azure MCP (Model Context Protocol) Server.

## Subscription Details

- **Subscription ID**: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`
- **Total Storage Accounts**: 189
- **Date Retrieved**: 2024-06-12

## Files

- `get-storage-accounts.js` - Example script showing how to use Azure MCP tools
- `storage-accounts-result.json` - Complete list of storage accounts retrieved from the subscription

## Azure MCP Tool Used

The storage accounts were retrieved using the `azmcp-storage-account-list` tool with the following parameters:
- `subscription`: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

## Usage

To retrieve storage accounts for this subscription using Azure MCP:

```javascript
// Using Azure MCP Server tools
azmcp-storage-account-list --subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
```

## Results Summary

The query successfully returned 189 storage accounts across multiple Azure regions including:
- East US
- West Europe  
- Central India
- Australia East
- Canada Central
- And many more regions

All storage account names are listed in the `storage-accounts-result.json` file.