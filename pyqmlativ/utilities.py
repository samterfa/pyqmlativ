import pandas as pd
import os
import json

import requests
from requests_oauthlib import OAuth1Session

try:
    import credentials
except:
    pass

all_modules = ["attendance", "curriculum", "demographics", "discipline", "district",
                "enrollment", "family", "graduationRequirements", "gradebook", "grading", "guidance", "health", "messageCenter",
                "onlineForm", "seporting", "scheduling", "security", "staff", "staffPlanning", "student", "transportation"]

# This function checks the presence of necessary environmental variables before making API requests.
def checkCredentials():

    try:
        os.environ["api_url"]
    except:
        raise Exception('os.environ["api_url"] must be set! Should be of the form "https://skyward.iscorp.com/...StuAPI"')

    try:
        os.environ["consumer_key"]
    except:
        raise Exception('os.environ["consumer_key"] must be set!')

    try:
        os.environ["consumer_secret"]
    except:
        raise Exception('os.environ["consumer_secret"] must be set!')

# This function performs a QMLATIV API request.
def makeRequest(endpoint, verb = 'get', params = None, payload = None):
    
    checkCredentials()
    
    sess = OAuth1Session(client_key = os.environ["consumer_key"], client_secret = os.environ["consumer_secret"])
    
    request_url = os.environ["api_url"] + endpoint
    
    if verb == 'get':
        r = sess.get(request_url, params = params)

    elif verb == 'post':
        r = sess.post(request_url, params = params, data = payload)

    elif verb == 'put':
        r = sess.put(request_url, params = params, data = payload)

    elif verb == 'delete':
        r = sess.delete(request_url, params = params)

    else:
      raise Exception('"verb" must be one of get, post, put or delete')  

    df = pd.read_json(json.dumps(r.json()), typ = 'Series')
    
    return(df)

# This function generates api request functions.
def generateFunctions(EntityID = 1, Modules = all_modules):
    
    # Open ini file to make sure newly created functions are imported.
    ini_file_path = 'pyqmlativ/__init__.py'
    ini_file = open(ini_file_path, "w")
    ini_file.write('from .utilities import *')

    for Module in Modules:
        
        print('\n\nGenerating ' + Module + ' functions. ', end = '\n\n')

        ini_file.write('\n\nimport pyqmlativ.' + Module)
        
        # Create Module as a Python module.
        module_file_path = 'pyqmlativ/' + Module + '.py'
        module_file = open(module_file_path, "w")
        module_file.write('# This module contains ' + Module + ' functions.')
        module_file = open(module_file_path, "a")

        module_endpoint = '/'.join(['', 'Generic', str(EntityID), Module])

        objects_and_endpoints = makeRequest(module_endpoint)
        
        Objects = list(objects_and_endpoints.index)
        object_endpoints = [ item['href'] for item in objects_and_endpoints ]

        for i in range(0, len(objects_and_endpoints)):

            print(str(i+1) + '/' + str(len(object_endpoints)), end='\r', flush=True)

            Object = objects_and_endpoints.index[i]
            object_endpoint = objects_and_endpoints[i]['href']

            fields = makeRequest(object_endpoint)
        
            id_field_index = [ 'PrimaryKey' in item for item in fields ].index(True)
            idField = list(fields.keys())[id_field_index]

            #### Create human-readable function names.
            
            # deleteObject()
            functionName = 'delete' + Object

            module_file.write('\n\ndef ' + functionName + '(' + idField + ', EntityID = 1):')
            module_file.write('\n\n\tmakeRequest(endpoint = "' + object_endpoint.replace('/1/', '/" + EntityID + "/') + '/" + ' + idField + ', verb = "delete")')

        return()
        module_file.close()

    ini_file.close()
        
    return()