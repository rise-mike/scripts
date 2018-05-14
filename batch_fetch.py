import requests
import json


config = {
    "url": "https://projectsapi.zoho.com/restapi/portal/risepeople/projects/?authtoken={lolno}",
}

def apiCall(config, index=0, range=99):
    # Takes in a configuration file, starting index, and ending index relative to the start
    # url = config["url"]
    url = config["url"] + "index=" + str(index) + "&range=" + str(range)
    print(url)
    resp = requests.get(url).json()
    return resp

# def allProjects():
#     all_projects = {}

print(apiCall(config))