#!/usr/bin/env node

/**
 * Simple test to validate storage account retrieval functionality
 */

const fs = require('fs');
const path = require('path');

console.log('Testing storage accounts retrieval...');

// Test 1: Check if result file exists
const resultFile = path.join(__dirname, 'storage-accounts-result.json');
if (!fs.existsSync(resultFile)) {
    console.error('❌ FAIL: storage-accounts-result.json not found');
    process.exit(1);
}
console.log('✅ PASS: Result file exists');

// Test 2: Validate result file content
try {
    const data = JSON.parse(fs.readFileSync(resultFile, 'utf8'));
    
    // Check subscription ID
    if (data.subscription_id !== '7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a') {
        console.error('❌ FAIL: Incorrect subscription ID');
        process.exit(1);
    }
    console.log('✅ PASS: Correct subscription ID');
    
    // Check if storage accounts array exists and has content
    if (!Array.isArray(data.storage_accounts) || data.storage_accounts.length === 0) {
        console.error('❌ FAIL: No storage accounts found');
        process.exit(1);
    }
    console.log(`✅ PASS: Found ${data.storage_accounts.length} storage accounts`);
    
    // Check if total count matches array length
    if (data.total_storage_accounts !== data.storage_accounts.length) {
        console.error('❌ FAIL: Total count mismatch');
        process.exit(1);
    }
    console.log('✅ PASS: Total count matches array length');
    
    // Check status
    if (data.status !== 'success') {
        console.error('❌ FAIL: Status is not success');
        process.exit(1);
    }
    console.log('✅ PASS: Status is success');
    
} catch (error) {
    console.error('❌ FAIL: Invalid JSON in result file:', error.message);
    process.exit(1);
}

console.log('\n🎉 All tests passed! Storage account retrieval functionality is working correctly.');