import pandas as pd
import os
import json

import requests
from requests_oauthlib import OAuth1Session

import config

allModules = ["Attendance", "Curriculum", "Demographics", "Discipline", "District",
                "Enrollment", "Family", "GraduationRequirements", "Gradebook", "Grading", "Guidance", "Health", "MessageCenter",
                "OnlineForm", "Reporting", "Scheduling", "Security", "Staff", "StaffPlanning", "Student", "Transportation"]

# This function performs a QMLATIV API request.
def makeRequest(endpoint, verb = 'get', params = None, payload = None):
    
    sess = OAuth1Session(client_key = config.consumerKey, client_secret = config.consumerSecret)
    
    requestUrl = config.apiUrl + endpoint

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

def getObjectNamesForModule(ModuleEndpoint):

    ModuleEndpoint = '/'.join(['Generic', str(EntityID), Module])

    ObjectNames = list(makeRequest(ModuleEndpoint).index)

    return(ObjectNames)


def testing():

    for Module in allModules:

        print(Module)



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