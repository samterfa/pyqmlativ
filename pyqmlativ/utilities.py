import pandas as pd
import os
import json

import requests
from requests_oauthlib import OAuth1Session

try:
    import credentials
except:
    pass

allModules = ["Attendance", "Curriculum", "Demographics", "Discipline", "District",
                "Enrollment", "Family", "GraduationRequirements", "Gradebook", "Grading", "Guidance", "Health", "MessageCenter",
                "OnlineForm", "Reporting", "Scheduling", "Security", "Staff", "StaffPlanning", "Student", "Transportation"]

# This function checks the presence of necessary environmental variables before making API requests.
def checkCredentials():

    try:
        os.environ["apiUrl"]
    except:
        raise Exception('os.environ["apiUrl"] must be set! Should be of the form "https://skyward.iscorp.com/...StuAPI"')

    try:
        os.environ["consumerKey"]
    except:
        raise Exception('os.environ["consumerKey"] must be set!')

    try:
        os.environ["consumerSecret"]
    except:
        raise Exception('os.environ["consumerSecret"] must be set!')

# This function performs a QMLATIV API request.
def makeRequest(endpoint, verb = 'get', params = None, payload = None):
    
    checkCredentials()
    
    sess = OAuth1Session(client_key = os.environ["consumerKey"], client_secret = os.environ["consumerSecret"])
    
    requestUrl = os.environ["apiUrl"] + endpoint
    print(requestUrl)
    if verb == 'get':
        r = sess.get(requestUrl, params = params)

    elif verb == 'post':
        r = sess.post(requestUrl, params = params, data = payload)

    elif verb == 'put':
        r = sess.put(requestUrl, params = params, data = payload)

    elif verb == 'delete':
        r = sess.delete(requestUrl, params = params)

    else:
      raise Exception('"verb" must be one of get, post, put or delete')  

    df = pd.read_json(json.dumps(r.json()), typ = 'Series')
    
    return(df)

# This function generates api request functions.
def generateFunctions(EntityID = 1, Modules = allModules):
    
    for Module in Modules:
        
        ModuleEndpoint = '/'.join(['', 'Generic', str(EntityID), Module])

        ObjectsAndEndpoints = makeRequest(ModuleEndpoint)
        
        Objects = list(ObjectsAndEndpoints.index)
        ObjectEndpoints = [ item['href'] for item in ObjectsAndEndpoints ]

        for i in range(0, len(ObjectsAndEndpoints)):

            Object = ObjectsAndEndpoints.index[i]
            ObjectEndpoint = ObjectsAndEndpoints[i]['href']

            fields = makeRequest(ObjectEndpoint)

            return(fields)