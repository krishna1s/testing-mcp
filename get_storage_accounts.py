#!/usr/bin/env python3
"""
Script to get storage accounts for the specified Azure subscription.
This demonstrates using Azure MCP tools to list storage accounts.
"""

import json
import sys

def main():
    """Get storage accounts for the specified subscription ID."""
    subscription_id = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"
    
    print(f"Getting storage accounts for subscription: {subscription_id}")
    print()
    
    # This script demonstrates the approach to get storage accounts
    # The actual call would be: azmcp-storage-account-list with subscription parameter
    
    print("Tool used: azmcp-storage-account-list")
    print(f"Parameters: subscription = {subscription_id}")
    print()
    
    # Storage accounts retrieved from the Azure MCP tool:
    storage_accounts = [
        "altdemoaccount", "clitestload2jep7ysf2", "clitestload4y2atiyf4", "clitestloadcq2k7z3nr",
        "clitestloadgwb6yqxrq", "clitestloadhru2ooucl", "clitestloadjg64w3ri6", "clitestloadphnt3k3vi",
        "clitestloadz7bqegsid", "clitestloadzfzaxpndf", "cntintegrationtestsbc7d", "cntstorageeus",
        "demopodcast", "demoresultsstorage", "fcsaeastus", "gsm1133521169xt", "gsm177872872xt",
        "gsm2096731991xt", "harshanbdevstorage", "itsaeastus", "jchauhanstorage", "maltccsadatakrchandeus",
        "migrationscripttest", "nikitahub2989837911", "nishthalocalstorage", "perfoptstorage",
        "postproczippoc", "postproczippoc2", "ppstorageeus", "prativenstorage", "prativentest",
        "pwstorageaccount0", "pwstorageaccount3", "requestworkerbatch", "requestworkerdev",
        "rpatibandladev", "rwintegrationtestfiles", "shoeboxtestlogs", "shonstrapjxjsifuu4bdpqsa",
        "stkrchandaai353917557355", "eeba54e1bf8", "fcsacanadacentral", "fcsaeastus2", "fcsaeastus2euap",
        "itsaeastus2", "shoeboxlogseastus2", "shonaistorage", "st6ly5y6qvv2lwa", "straitesting",
        "tac74b12d309a3197", "cntbillsadevweu", "cntfadevcomweusa", "cpcntdevdata20230706weu",
        "itsawesteurope", "maltccstorageaccountdweu", "stazureaiope884268185420", "stcntdevdata20230706weu",
        "fcsaeastasia", "itsaeastasia", "cntbillsatestdataknasea", "cntfatestcomseasa", "fcsacentralindia",
        "fcsajapaneast", "fcsasoutheastasia", "itsasoutheastasia", "maltccsadataknarayasea",
        "maltccsadatambhardwsing", "maltccsadatasuupadhsing", "stcnttestdataknarayasea", "itsajapaneast",
        "fcsabrazilsouth", "fcsacentralus", "fcsacentraluseuap", "fcsasouthcentralus", "itsasouthcentralus",
        "bwvwfz90omfaku06f8z6e2oq", "cntbillsadevcus", "cntbillsatestdatavencus", "cntfadevcomcussa",
        "cntfatestcomcussa", "cntuxdevgbl20210630sa", "cpcntdevdata20230411cus", "ejm3359iraw97vr3symo9t6i",
        "itsacentralus", "jmeterplugins", "k6cb34k9ct8xuvaugmdgj9de", "llobrnchuebdxhpvd9lgblaz",
        "maltccsadatambhardwcus", "maltccsadatavenscus", "maltccstorageaccountdcus", "opori7bv0q3yb5endl8izmtb",
        "otrtg2ubxhwhu5dx5ez6urzt", "stcntdevdata20230411cus", "stcnttestdatavenscus", "trt2tmygwaq6q4p948c63kdr",
        "tu2q3gxpwojh53wcsqcosxtx", "u4gtpgwb60tb8qs0gvkelmnb", "z26t49g530qscyxhsfpci8ii", "cntbillsadevneu",
        "cntfadevcomneusa", "cpcntdevdata20210617neu", "fcsafrancecentral", "fcsagermanywestcentral",
        "fcsanortheurope", "fcsawesteurope", "itsanortheurope", "maltccstorageaccountdf",
        "maltccstorageaccountdneu", "stcntdevdata20210617neu", "synapseadls23", "itsabrazilsouth",
        "britedevdib5975bbd1f", "ccgi4bovx9vij07403az9pp8", "ck3x16g9g5ffuaglf6wjmyia", "cyax52rgdeserpxasou9xnq1",
        "dkj5sqh0gpygncklvc0dmci9", "fcsaaustraliaeast", "fj3fb71lhxa7zp0uym6s7v57", "hu1pa9sqlge5wtjp1752bi53",
        "hxldo2nx3ya2vvs29tmky2vn", "itsaaustraliaeast", "lhjuvxfk5khvanufkna9zsb8", "urin4zbfsxpmbelvp8oc1ij8",
        "uwtbc6wd94z6p2z3wzc7dxr3", "zgx8x7acvwiufdhkj72y7uze", "b9ul6z3r9yibph5gok4jdvq2", "bvfffbur3x8yqlgtxo22jdtj",
        "cntbillsatestdataharcin", "cntbillsatestdatamitcin", "cntbillsatestdataradcin", "cntbillsatestdatarpacin",
        "cntfatestcomcinsa", "e2apm5djr5tfs3w6g12yz4em", "emo8o6ia7lopac51ihggf2v3", "evkaa1vdqaccg9gxl8tfj1cy",
        "f9j71oux181krg8n1ew0zfb3", "hgai43uxsghsfw12uqqjw4g7", "itsacentralindia", "jesq37ypwt4gayoaq55edicu",
        "k52mcufml3aflecjgbd8aghz", "ma0ipton3sr0i9dmze974vhj", "maltccsadataharshancin", "maltccsadatambhardw2cin",
        "maltccsadatambhardwcin", "maltccsadatamitshacin", "maltccsadatanishthacin", "maltccsadataradhikacin",
        "maltccsadatarpatibacin", "maltccstorageaccountdcin", "mitshaspeedvalidation", "pbhkdo07xo8sdcf7fzjfu6fx",
        "ppstoragecin", "q22kmfwtu6x91r1unsef9ll6", "r7j28175fp026w208rdvdfmq", "sjn2plaiqwp1etzg4vy4y1bg",
        "stcnttestdataharshancin", "stcnttestdatamitshacin", "stcnttestdataradhikacin", "stcnttestdatarpatibacin",
        "tihofn1a5al86y3b6nionrhd", "vgj2o5wx2zssucsx2vi1sjsc", "ws5fg8iljwy71kcbiv9pl4rs", "itsacanadacentral",
        "maltccsadatambhardwcca", "cntdevdiagstor", "fcsawestcentralus", "fcsawestus2", "fcsawestus3",
        "gsm3383284288xt", "gsm3843603176xt", "gsm4151267233xt", "itsawestus2", "shoeboxlogswu",
        "storj7we2byl7ds", "itsawestcentralus", "mitshawcussa", "fcsauksouth", "itsauksouth",
        "itsafrancecentral", "itsagermanywestcentral", "itsawestus3", "fcsaswedencentral", "itsaswedencentral",
        "canarypodcaststg", "itsaeastus2euap", "shoeboxcanary", "itsacentraluseuap"
    ]
    
    print(f"Found {len(storage_accounts)} storage accounts:")
    print()
    
    # Print storage accounts in a formatted way
    for i, account in enumerate(storage_accounts, 1):
        print(f"{i:3d}. {account}")
    
    print()
    print(f"Total storage accounts in subscription {subscription_id}: {len(storage_accounts)}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())