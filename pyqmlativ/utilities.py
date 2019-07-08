import pandas as pd
import os
import json

import requests
from requests_oauthlib import OAuth1Session

import config

# This function performs a QMLATIV API request.
def makeRequest(endpoint, verb = 'get', params = None, payload = None):
    
    sess = OAuth1Session(client_key = config.consumerKey, client_secret = config.consumerSecret)
    
    if verb == 'get':
        r = sess.get(config.apiUrl + endpoint, params = params)

    elif verb == 'post':
        r = sess.post(config.apiUrl + endpoint, params = params, data = payload)

    elif verb == 'put':
        r = sess.put(config.apiUrl + endpoint, params = params, data = payload)

    elif verb == 'delete':
        r = sess.delete(config.apiUrl + endpoint, params = params)

    else:
      raise Exception('"verb" must be one of get, post, put or delete')  

    df = pd.read_json(json.dumps(r.json()), typ = 'Series')
    
    return(df)


# This function generates api request functions.