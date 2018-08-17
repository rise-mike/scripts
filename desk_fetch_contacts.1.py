import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
from config import contactsConfig


def fetchBatchTickets(config, start, limit):    
    config['params']['from'] = start
    config['params']['limit'] = limit

    url = config['domain']
    r = requests.get(url, headers=config['headers'], params=config['params']).json()
    print("Downloading From: ", config['params']['from'], ' To: ', config['params']['from'] + config['params']['limit'], '| Limit: ', config['params']['limit'])
    return r

def writeProjectToJson(jsonObj, dest):
    # Accepts a JSON object, and dumps it into a specified destination file.
    print("Writing to ", dest)
    with open(dest, "w") as outfile:
        json.dump(jsonObj, outfile)

def fetchAllTickets(config):
    allContacts = []
    currentStart = 1
    currentLimit = 99

    while currentLimit > 98 :
        currentPull = fetchBatchTickets(contactsConfig, currentStart, currentLimit)['data']
        allContacts = allContacts + currentPull
        currentLimit = int(len(currentPull))
        currentStart = int(currentStart) + int(currentLimit)
    
    return allContacts

everything = fetchAllTickets(contactsConfig)
writeProjectToJson(everything, 'contacts_all.json')

# For Testing Purposes

# cont1 = fetchBatchTickets(contactsConfig, 1, 1)['data']
# cont2 = fetchBatchTickets(contactsConfig, 2, 1)['data']
# writeProjectToJson(contactsJSON, 'contacts_sample.json')

