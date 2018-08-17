import json
import requests
from config import accountsConfig
import sys

def apiCallRepeater(repeatList):
    """Accepts a list of Zoho IDs, warns user of number of API calls to be made, gives an option to end the script
    or proceed and returns a list of Zoho Account dicts."""
    confirm = input("We're about to make " + str(len(repeatList)) + " API calls, is this OK? (Y/N) > ")
    if confirm == "Y" or confirm == 'y':
        print("OK")
        accts = fetchById(repeatList)
        return accts
    else:
        print('K, byeeee')
        sys.exit()
    
def fetchById(accountIdList):
    """Takes in a list of Zoho Desk Account IDs, and makes an API call to the /accounts endpoint for rach ID.
    Returns a list of all responses"""
    accounts= []
    url = accountsConfig['domain']
    for accId in accountIdList:
        r = requests.get(url +'/'+ str(accId), headers=accountsConfig['headers']).json()
        accounts.append(r)
    return accounts

def fetchAllAccounts(config):
    """Takes in a config dict, and makes API calls in chunks of 99 records, until the number of records
    in the response is < 99, returns an array of all responses"""
    allAccounts = []
    currentStart = 1
    currentLimit = 99
    while currentLimit > 98 :
        currentPull = fetchBatchAccounts(accountsConfig, currentStart, currentLimit)['data']
        allAccounts = allAccounts + currentPull
        currentLimit = int(len(currentPull))
        currentStart = int(currentStart) + int(currentLimit)
    return allAccounts

def fetchBatchAccounts(config, start, limit):
    """Accepts a config dict, start int and limit int, and makes an API call, returning the data as JSON"""    
    config['params']['from'] = start
    config['params']['limit'] = limit
    url = config['domain']
    r = requests.get(url, headers=config['headers'], params=config['params']).json()
    print("Downloading From: ", config['params']['from'], ' To: ', config['params']['from'] + config['params']['limit'], '| Limit: ', config['params']['limit'])
    return r

def idParser(json):
    """Take in a JSON array of Zoho Desk Account objects. For each account,the id is pulled out and a separate API call for ALL account details is made. 
    The result is added to an array of dicts, flattened, and written to a CSV."""
    acctIds = []
    for account in json:
        acctIds.append(account['id'])
    return acctIds

def writeProjectToJson(jsonObj, dest):
    """Accepts a JSON object, and dumps it into a specified destination file"""
    print("Writing to ", dest)
    with open(dest, "w") as outfile:
        json.dump(jsonObj, outfile)

dest = input("Name the file to output to (JSON)> ")
allAcctIds = apiCallRepeater(idParser(fetchAllAccounts(accountsConfig)))
writeProjectToJson(allAcctIds, dest)
