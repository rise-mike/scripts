import requests
import json

# Eventually this needs to be dumped to the separate config file - LEAVE FOR TESTING   
config = {
    "domain": "https://projectsapi.zoho.com/restapi/portal/risepeople",
    "endpoints": {
        "project"   : "/projects/1049905000000471105/?authtoken=lolno",
    },
    "params" :{
        "authtoken": "lolno"
    },  
}

# GET THE DATA
def apiCall(config, endpoint):
    # Needs to be reworked - decide on a final config object structure (see ../../desk)
    url = config["domain"]+config["endpoints"][endpoint]
    # returnData = requests.get(url, params=config["params"]).json()
    returnData = requests.get(url).json()
    return returnData

# MODIFY THE DATA

# def isolator():
    # Takes in a project object and isolates blocks to pass to other functions


def linkCleaner(link_dict):
    # Takes in a dict of link dicts and flattens them into a simple dict
    clean_links = {}
    for link in link_dict:
        clean_links[link] = link_dict[link]["url"]
    return clean_links

# WRITE THE DATA
def jsonWriter(file_name, dict):
    # Takes a filename (WITH EXTENSION) and a dict, converts the dict to JSON and writes it to the file    
    with open(file_name, 'w') as f:
        f.write(json.dumps(dict))
        print("Write complete")


project_obj = apiCall(config, "project")["projects"][0]
link_map = linkCleaner(project_obj["link"])


# jsonWriter("projects.json", data_obj)
jsonWriter("link_map.json", link_map)
