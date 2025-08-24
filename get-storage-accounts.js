#!/usr/bin/env node

/**
 * Example script to get storage accounts for a specific Azure subscription
 * 
 * This demonstrates how to use the Azure MCP tools to list storage accounts
 * for subscription ID: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
 */

const subscriptionId = '7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a';

console.log(`Getting storage accounts for subscription: ${subscriptionId}`);
console.log('Using Azure MCP Server storage account list functionality...');

// Note: This script demonstrates the concept. In practice, you would use:
// - The Azure MCP Server via Model Context Protocol
// - Tools like azmcp-storage-account-list with the subscription parameter
// - Integration with LLM agents that can call the Azure MCP tools

console.log('\nExample Azure MCP tool call:');
console.log(`azmcp-storage-account-list --subscription ${subscriptionId}`);

console.log('\nFor actual results, see: storage-accounts-result.json');