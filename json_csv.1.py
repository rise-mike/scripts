import json 
import pandas as pd 
from pandas.io.json import json_normalize 

# v1.0 - This will take a dict of dicts representing Zoho Projects, ask the user for an
# input JSON file, destination CSV file, flatten the JSON and create a CSV.
# This does no additional formatting at this time.

sourceFile = input("Input File (JSON) > ")

destFile = input("Output file (incl '.csv') > ")

with open(sourceFile) as f:
    d = json.load(f)

projDict = json_normalize(d)
print(projDict.head)
projDict.to_csv(destFile)