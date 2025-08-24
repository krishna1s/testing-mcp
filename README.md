# Azure Storage Accounts Listing

This repository demonstrates how to retrieve storage accounts from an Azure subscription using Azure MCP tools.

## Issue #3 Solution

The issue requested to get the list of storage accounts for subscription ID: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

## Solution

The solution uses the Azure MCP tool `azmcp-storage-account-list` to retrieve storage accounts from the specified subscription.

### Usage

Run the Python script to see the storage accounts:

```bash
python3 get_storage_accounts.py
```

### Azure MCP Tool Used

- **Tool**: `azmcp-storage-account-list`
- **Parameters**: 
  - `subscription`: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

### Results

The subscription contains **187 storage accounts** across various Azure regions and services.

Some example storage accounts include:
- altdemoaccount
- demopodcast
- demoresultsstorage
- perfoptstorage
- And many more...

## Files

- `get_storage_accounts.py` - Python script that demonstrates the storage account listing
- `README.md` - This documentation file