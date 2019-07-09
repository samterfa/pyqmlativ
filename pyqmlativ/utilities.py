import pandas as pd
import os
import json

import requests
from requests_oauthlib import OAuth1Session

try:
    import credentials
except:
    pass

all_modules = pd.DataFrame(
                            {'module_name' : ["Attendance", "Curriculum", "Demographics", "Discipline", "District",
                                        "Enrollment", "Family", "GraduationRequirements", "Gradebook", "Grading", "Guidance", "Health", "MessageCenter",
                                        "OnlineForm", "Reporting", "Scheduling", "Security", "Staff", "StaffPlanning", "Student", "Transportation"],
                            'module_var_name' : ["attendance", "curriculum", "demographics", "discipline", "district",
                                        "enrollment", "family", "graduation_requirements", "gradebook", "grading", "guidance", "health", "message_center",
                                        "online_form", "reporting", "scheduling", "security", "staff", "staff_planning", "student", "transportation"]
                            }
                            )

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
def make_request(endpoint, verb = 'get', params = None, payload = None):
    
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
def generateFunctions(entity_id = 1, modules = all_modules.module_name):
    
    # Open ini file to make sure newly created functions are imported.
    ini_file_path = 'pyqmlativ/__init__.py'
    ini_file = open(ini_file_path, "w")
    ini_file.write('from .utilities import *')

    for module_name in modules:
        
        print('\n\nGenerating ' + module_name + ' functions. ', end = '\n\n')

        ini_file.write('\n\nimport pyqmlativ.' + module_name)
        
        # Create module as a Python module.
        module_file_path = 'pyqmlativ/' + module_name + '.py'
        module_file = open(module_file_path, "w")
        module_file.write('# This module contains ' + module_name + ' functions.')
        module_file = open(module_file_path, "a")

        module_endpoint = '/'.join(['', 'Generic', str(entity_id), module_name])

        objects_and_endpoints = make_request(module_endpoint)
        
        objects = list(objects_and_endpoints.index)
        object_endpoints = [ item['href'] for item in objects_and_endpoints ]

        for i in range(0, len(objects_and_endpoints)):

            print(str(i+1) + '/' + str(len(object_endpoints)), end='\r', flush=True)

            object_name = objects_and_endpoints.index[i]
            object_endpoint = objects_and_endpoints[i]['href']

            fields = make_request(object_endpoint)
        
            id_field_index = [ 'PrimaryKey' in item for item in fields ].index(True)
            idField = list(fields.keys())[id_field_index]

            #### Create human-readable function names.
            
            # deleteobject()
            functionName = 'delete' + object_name

            module_file.write('\n\ndef ' + functionName + '(' + idField + ', entity_id = 1):')
            module_file.write('\n\n\tmake_request(endpoint = "' + object_endpoint.replace('/1/', '/" + entity_id + "/') + '/" + ' + idField + ', verb = "delete")')

            #return()
        module_file.close()

    ini_file.close()
        
    return()