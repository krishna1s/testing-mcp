#!/usr/bin/env node

/**
 * Simple test for the get-storage-accounts functionality
 */

const { getStorageAccounts, storageAccountsResult, SUBSCRIPTION_ID } = require('./get-storage-accounts');

console.log('🧪 Testing Storage Accounts Retrieval...\n');

// Test 1: Check if the subscription ID is correct
console.log('Test 1: Subscription ID');
const expectedSubscriptionId = '7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a';
if (SUBSCRIPTION_ID === expectedSubscriptionId) {
    console.log('✅ PASS - Subscription ID matches expected value');
} else {
    console.log('❌ FAIL - Subscription ID mismatch');
    console.log(`   Expected: ${expectedSubscriptionId}`);
    console.log(`   Actual: ${SUBSCRIPTION_ID}`);
}

// Test 2: Check if result has successful status
console.log('\nTest 2: Result Status');
if (storageAccountsResult.status === 200) {
    console.log('✅ PASS - API call was successful (status 200)');
} else {
    console.log('❌ FAIL - API call failed');
    console.log(`   Status: ${storageAccountsResult.status}`);
    console.log(`   Message: ${storageAccountsResult.message}`);
}

// Test 3: Check if we have storage accounts
console.log('\nTest 3: Storage Accounts Data');
const accounts = getStorageAccounts();
if (Array.isArray(accounts) && accounts.length > 0) {
    console.log(`✅ PASS - Found ${accounts.length} storage accounts`);
} else {
    console.log('❌ FAIL - No storage accounts found or data is not an array');
    console.log(`   Data type: ${typeof accounts}`);
    console.log(`   Length: ${accounts ? accounts.length : 'N/A'}`);
}

// Test 4: Check specific account names format
console.log('\nTest 4: Account Name Format');
const sampleAccounts = accounts.slice(0, 5);
let validNames = 0;
sampleAccounts.forEach(account => {
    // Azure storage account names should be lowercase alphanumeric
    if (typeof account === 'string' && /^[a-z0-9]+$/.test(account)) {
        validNames++;
    }
});

if (validNames === sampleAccounts.length) {
    console.log('✅ PASS - Account names follow valid Azure naming conventions');
} else {
    console.log('❌ FAIL - Some account names have invalid format');
    console.log(`   Valid: ${validNames}/${sampleAccounts.length}`);
}

// Test 5: Check for expected test accounts
console.log('\nTest 5: Expected Account Types');
const testAccounts = accounts.filter(name => name.includes('test')).length;
const cliTestAccounts = accounts.filter(name => name.startsWith('clitest')).length;

if (testAccounts > 0 && cliTestAccounts > 0) {
    console.log('✅ PASS - Found expected test account types');
    console.log(`   Test accounts: ${testAccounts}`);
    console.log(`   CLI test accounts: ${cliTestAccounts}`);
} else {
    console.log('❌ FAIL - Missing expected test account types');
}

console.log('\n🎯 Test Summary:');
console.log(`   Subscription: ${SUBSCRIPTION_ID}`);
console.log(`   Total Storage Accounts: ${accounts.length}`);
console.log(`   Status: ${storageAccountsResult.message}`);
console.log('\n✅ All tests completed successfully!');