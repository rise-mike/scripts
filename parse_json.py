import pandas as pd
import os
import glob

# Set path to directory of json files to import, glob all filenames ending in "".json" to a list.
# Iterate through the list, writing to an excel file where "sheet_name = filename" and the contents of the sheet
# are a dataframe of the JSON content of the file

path = '../one-offs/french/'

json_glob = glob.glob(path + '*.json')
print("We're reading from " + str(len(json_glob)) + " files")
outfile = 'json_french.xlsx'

writer = pd.ExcelWriter(outfile)

for file in json_glob:
    head, tail = os.path.split(file)
    sheet = tail
    open_json = pd.read_json(file)
    open_json.to_excel(writer,sheet)

writer.save()
print("Files written to: " + outfile)