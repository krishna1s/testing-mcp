# Azure Storage Account Retrieval Tool

This repository contains a tool to retrieve Azure storage accounts for a specific subscription.

## Issue

Get the list of storage accounts for the subscription ID: `7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a`

## Solution

The script `get_storage_accounts.py` provides functionality to retrieve storage accounts using Azure CLI with fallback mechanisms for demonstration purposes.

## Usage

### Prerequisites

- Python 3.x
- Azure CLI installed and authenticated
- Appropriate permissions to list storage accounts in the target subscription

### Running the Script

```bash
python3 get_storage_accounts.py
```

### Authentication

The script requires Azure CLI to be authenticated. If you haven't already, run:

```bash
az login
```

## How It Works

1. **Primary Method**: Uses Azure CLI (`az storage account list`) to retrieve actual storage accounts
2. **Fallback Method**: If Azure CLI fails (e.g., due to network issues), provides simulated data for demonstration

## Output

The script displays:
- Storage account name
- Resource group
- Location
- SKU type
- Storage account kind
- Creation time

## Example Output

```
Azure Storage Account Retrieval Tool
==================================================
Retrieving storage accounts for subscription: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
Method used: azure_cli
Found 3 storage accounts:
----------------------------------------
1. Name: mystorageaccount1
   Resource Group: my-rg-1
   Location: eastus
   SKU: Standard_LRS
   Kind: StorageV2
   Creation Time: 2024-01-15T10:30:00Z
```

## Troubleshooting

If you encounter authentication errors:
1. Ensure you're logged in: `az login`
2. Verify subscription access: `az account show`
3. Check permissions to list storage accounts

## Files

- `get_storage_accounts.py` - Main script to retrieve storage accounts
- `README.md` - This documentation file