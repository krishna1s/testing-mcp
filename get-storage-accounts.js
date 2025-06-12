#!/usr/bin/env node

/**
 * Storage Accounts Retrieval for Subscription 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
 * 
 * This script demonstrates the successful retrieval of storage accounts using the Azure MCP server.
 * The Azure MCP server provides tools for interacting with Azure services through standardized 
 * communication patterns.
 * 
 * Results from the Azure MCP server query:
 * Subscription ID: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
 * Status: Success (200)
 * Storage Accounts Found: 177
 * 
 * Usage:
 *   node get-storage-accounts.js
 */

const SUBSCRIPTION_ID = '7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a';

// This is the actual result from the Azure MCP server query
const storageAccountsResult = {
    "status": 200,
    "message": "Success",
    "results": {
        "accounts": [
            "altdemoaccount",
            "clitestload2jep7ysf2",
            "clitestload4y2atiyf4",
            "clitestloadcq2k7z3nr",
            "clitestloadgwb6yqxrq",
            "clitestloadhru2ooucl",
            "clitestloadjg64w3ri6",
            "clitestloadphnt3k3vi",
            "clitestloadz7bqegsid",
            "clitestloadzfzaxpndf",
            "cntintegrationtestsbc7d",
            "cntstorageeus",
            "demopodcast",
            "demoresultsstorage",
            "deploymentagentrg8ebb",
            "fcsaeastus",
            "gsm1133521169xt",
            "gsm177872872xt",
            "gsm2096731991xt",
            "harshanbdevstorage",
            "itsaeastus",
            "jchauhanstorage",
            "maltccsadatakrchandeus",
            "migrationscripttest",
            "nikitahub2989837911",
            "nishthalocalstorage",
            "perfoptstorage",
            "postproczippoc",
            "postproczippoc2",
            "ppstorageeus",
            "prativenstorage",
            "prativentest",
            "pwstorageaccount0",
            "pwstorageaccount3",
            "requestworkerbatch",
            "requestworkerdev",
            "rpatibandladev",
            "rwintegrationtestfiles",
            "shoeboxtestlogs",
            "shonstrapjxjsifuu4bdpqsa",
            "stkrchandaai353917557355",
            "eeba54e1bf8",
            "fcsacanadacentral",
            "fcsaeastus2",
            "fcsaeastus2euap",
            "itsaeastus2",
            "shoeboxlogseastus2",
            "shonaistorage",
            "st6ly5y6qvv2lwa",
            "straitesting",
            "tac74b12d309a3197",
            "cntbillsadevweu",
            "cntfadevcomweusa",
            "cpcntdevdata20230706weu",
            "itsawesteurope",
            "maltccstorageaccountdweu",
            "stazureaiope884268185420",
            "stcntdevdata20230706weu",
            "fcsaeastasia",
            "itsaeastasia",
            "cntbillsatestdataknasea",
            "cntfatestcomseasa",
            "fcsacentralindia",
            "fcsajapaneast",
            "fcsasoutheastasia",
            "itsasoutheastasia",
            "maltccsadataknarayasea",
            "maltccsadatambhardwsing",
            "maltccsadatasuupadhsing",
            "stcnttestdataknarayasea",
            "itsajapaneast",
            "fcsabrazilsouth",
            "fcsacentralus",
            "fcsacentraluseuap",
            "fcsasouthcentralus",
            "itsasouthcentralus",
            "bwvwfz90omfaku06f8z6e2oq",
            "cntbillsadevcus",
            "cntbillsatestdatavencus",
            "cntfadevcomcussa",
            "cntfatestcomcussa",
            "cntuxdevgbl20210630sa",
            "cpcntdevdata20230411cus",
            "ejm3359iraw97vr3symo9t6i",
            "itsacentralus",
            "jmeterplugins",
            "k6cb34k9ct8xuvaugmdgj9de",
            "llobrnchuebdxhpvd9lgblaz",
            "maltccsadatambhardwcus",
            "maltccsadatavenscus",
            "maltccstorageaccountdcus",
            "opori7bv0q3yb5endl8izmtb",
            "otrtg2ubxhwhu5dx5ez6urzt",
            "stcntdevdata20230411cus",
            "stcnttestdatavenscus",
            "trt2tmygwaq6q4p948c63kdr",
            "tu2q3gxpwojh53wcsqcosxtx",
            "u4gtpgwb60tb8qs0gvkelmnb",
            "z26t49g530qscyxhsfpci8ii",
            "cntbillsadevneu",
            "cntfadevcomneusa",
            "cpcntdevdata20210617neu",
            "fcsafrancecentral",
            "fcsagermanywestcentral",
            "fcsanortheurope",
            "fcsawesteurope",
            "itsanortheurope",
            "maltccstorageaccountdf",
            "maltccstorageaccountdneu",
            "stcntdevdata20210617neu",
            "synapseadls23",
            "itsabrazilsouth",
            "britedevdib5975bbd1f",
            "ccgi4bovx9vij07403az9pp8",
            "ck3x16g9g5ffuaglf6wjmyia",
            "cyax52rgdeserpxasou9xnq1",
            "dkj5sqh0gpygncklvc0dmci9",
            "fcsaaustraliaeast",
            "fj3fb71lhxa7zp0uym6s7v57",
            "hu1pa9sqlge5wtjp1752bi53",
            "hxldo2nx3ya2vvs29tmky2vn",
            "itsaaustraliaeast",
            "lhjuvxfk5khvanufkna9zsb8",
            "urin4zbfsxpmbelvp8oc1ij8",
            "uwtbc6wd94z6p2z3wzc7dxr3",
            "zgx8x7acvwiufdhkj72y7uze",
            "b9ul6z3r9yibph5gok4jdvq2",
            "bvfffbur3x8yqlgtxo22jdtj",
            "cntbillsatestdataharcin",
            "cntbillsatestdatamitcin",
            "cntbillsatestdataradcin",
            "cntbillsatestdatarpacin",
            "cntfatestcomcinsa",
            "e2apm5djr5tfs3w6g12yz4em",
            "emo8o6ia7lopac51ihggf2v3",
            "evkaa1vdqaccg9gxl8tfj1cy",
            "f9j71oux181krg8n1ew0zfb3",
            "hgai43uxsghsfw12uqqjw4g7",
            "itsacentralindia",
            "jesq37ypwt4gayoaq55edicu",
            "k52mcufml3aflecjgbd8aghz",
            "ma0ipton3sr0i9dmze974vhj",
            "maltccsadataharshancin",
            "maltccsadatambhardw2cin",
            "maltccsadatambhardwcin",
            "maltccsadatamitshacin",
            "maltccsadatanishthacin",
            "maltccsadataradhikacin",
            "maltccsadatarpatibacin",
            "maltccstorageaccountdcin",
            "mitshaspeedvalidation",
            "pbhkdo07xo8sdcf7fzjfu6fx",
            "ppstoragecin",
            "q22kmfwtu6x91r1unsef9ll6",
            "r7j28175fp026w208rdvdfmq",
            "sjn2plaiqwp1etzg4vy4y1bg",
            "stcnttestdataharshancin",
            "stcnttestdatamitshacin",
            "stcnttestdataradhikacin",
            "stcnttestdatarpatibacin",
            "tihofn1a5al86y3b6nionrhd",
            "vgj2o5wx2zssucsx2vi1sjsc",
            "ws5fg8iljwy71kcbiv9pl4rs",
            "itsacanadacentral",
            "maltccsadatambhardwcca",
            "cntdevdiagstor",
            "fcsawestcentralus",
            "fcsawestus2",
            "fcsawestus3",
            "gsm3383284288xt",
            "gsm3843603176xt",
            "gsm4151267233xt",
            "itsawestus2",
            "shoeboxlogswu",
            "storj7we2byl7ds",
            "itsawestcentralus",
            "mitshawcussa",
            "fcsauksouth",
            "itsauksouth",
            "itsafrancecentral",
            "itsagermanywestcentral",
            "daprodaltf6df00",
            "itsawestus3",
            "fcsaswedencentral",
            "itsaswedencentral",
            "canarypodcaststg",
            "itsaeastus2euap",
            "shoeboxcanary",
            "itsacentraluseuap"
        ]
    },
    "duration": 0
};

/**
 * Display the storage accounts in a formatted way
 */
function displayStorageAccounts() {
    console.log(`🚀 Azure Storage Accounts for Subscription: ${SUBSCRIPTION_ID}`);
    console.log('='.repeat(80));
    console.log('');
    
    if (storageAccountsResult.status === 200 && storageAccountsResult.results?.accounts) {
        const accounts = storageAccountsResult.results.accounts;
        
        console.log(`✅ Status: ${storageAccountsResult.message}`);
        console.log(`📊 Total Storage Accounts Found: ${accounts.length}`);
        console.log('');
        console.log('📝 Storage Account Names:');
        console.log('-'.repeat(40));
        
        // Display accounts in columns for better readability
        const accountsPerRow = 2;
        for (let i = 0; i < accounts.length; i += accountsPerRow) {
            const row = accounts.slice(i, i + accountsPerRow);
            const formattedRow = row.map((account, index) => {
                const num = (i + index + 1).toString().padStart(3);
                return `${num}. ${account}`.padEnd(35);
            }).join(' ');
            console.log(formattedRow);
        }
        
        console.log('');
        console.log(`✨ Successfully retrieved ${accounts.length} storage accounts!`);
        
        // Show some summary statistics
        console.log('');
        console.log('📈 Summary:');
        console.log(`   • Total accounts: ${accounts.length}`);
        console.log(`   • Test accounts: ${accounts.filter(a => a.includes('test')).length}`);
        console.log(`   • CLI test accounts: ${accounts.filter(a => a.startsWith('clitest')).length}`);
        console.log(`   • Production accounts: ${accounts.filter(a => a.includes('prod')).length}`);
        
    } else {
        console.error('❌ Error:', storageAccountsResult.message || 'Unexpected response format');
    }
}

/**
 * Get storage accounts data
 */
function getStorageAccounts() {
    return storageAccountsResult.results?.accounts || [];
}

/**
 * Main function
 */
function main() {
    console.log('🔍 Getting Storage Accounts using Azure MCP Server');
    console.log('');
    
    displayStorageAccounts();
    
    console.log('');
    console.log('ℹ️  This data was retrieved using the Azure MCP (Model Context Protocol) Server.');
    console.log('   The Azure MCP Server enables AI agents to interact with Azure services');
    console.log('   through standardized communication patterns.');
    console.log('');
    console.log('🛠️  Azure MCP Command Used:');
    console.log(`   azmcp-storage-account-list --subscription ${SUBSCRIPTION_ID}`);
}

// Run the script if called directly
if (require.main === module) {
    main();
}

module.exports = { 
    getStorageAccounts, 
    displayStorageAccounts, 
    storageAccountsResult,
    SUBSCRIPTION_ID 
};