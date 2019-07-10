import pandas as pd
import os
import json
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
def check_credentials():

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
def make_request(endpoint, verb = 'get', params_list = [], payload = None):
    
    check_credentials()
    
    sess = OAuth1Session(client_key = os.environ["consumer_key"], client_secret = os.environ["consumer_secret"])
    
    request_url = os.environ["api_url"] + endpoint
    
    for param in params_list:
        if params_list.index(param) == 0:
            request_url = request_url + '?searchFields=' + param
        else:
            request_url = request_url + '&searchFields=' + param
    
    if verb == 'get':
        r = sess.get(request_url)
        df = pd.read_json(json.dumps(r.json()), typ = 'Series')

    elif verb == 'post':
        r = sess.post(request_url, params = params, data = payload)
        df = pd.read_json(json.dumps(r.json()), typ = 'Series')

    elif verb == 'put':
        r = sess.put(request_url, params = params, data = payload)
        df = pd.read_json(json.dumps(r.json()), typ = 'Series')

    elif verb == 'delete':
        r = sess.delete(request_url)
        df = 'Object Deleted Successfully'

    else:
      raise Exception('"verb" must be one of get, post, put or delete')  
    
    if r.status_code < 300:
        return(df)
    else:
        return(r.json())

# This function generates api request functions.
def generateFunctions(modules = all_modules.module_name, EntityID = 1):
    
    if(isinstance(modules, str)):
        modules = [modules]

    # Open ini file to make sure newly created functions are imported.
    ini_file_path = 'pyqmlativ/__init__.py'
    ini_file = open(ini_file_path, "w")
    ini_file.write('from .Utilities import *')

    for module_name in modules:
        
        print('\n\nGenerating ' + module_name + ' functions. ', end = '\n\n')

        ini_file.write('\n\nimport pyqmlativ.' + module_name)
        
        # Create module as a Python module and initiate it.
        module_file_path = 'pyqmlativ/' + module_name + '.py'
        module_file = open(module_file_path, "w")
        module_file.write('# This module contains ' + module_name + ' functions.')
        module_file.write('\n\nfrom .Utilities import make_request')
        module_file.write('\n\nimport pandas as pd')

        # Append functions to module file.
        module_file = open(module_file_path, "a")

        module_endpoint = '/'.join(['', 'Generic', str(EntityID), module_name])
        objects_and_endpoints = make_request(module_endpoint)
        objects = list(objects_and_endpoints.index)
        object_endpoints = [ item['href'] for item in objects_and_endpoints ]

        for i in range(0, len(objects_and_endpoints)):

            print(str(i+1) + '/' + str(len(object_endpoints)), end='\r', flush=True)

            object_name = objects_and_endpoints.index[i]
            object_endpoint = objects_and_endpoints[i]['href']

            fields = make_request(object_endpoint)
            field_names = list(fields.keys())
            id_field_index = [ 'PrimaryKey' in item for item in fields ].index(True)
            id_field = field_names[id_field_index]

            #### Create human-readable function names.
            
            # get_object()
            functionName = 'get' + object_name
            function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1'
            
            field_names.remove(id_field)

            field_names = ['return' + field_name for field_name in field_names]

            for field_name in field_names:

                if field_names.index(field_name) == 0:
                    function_text_line_1 = function_text_line_1 + ', ' + field_name + ' = False'
                else:
                    function_text_line_1 = function_text_line_1 + ', ' + field_name + ' = False'

            function_text_line_1 = function_text_line_1 + '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n\tparams = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])')
            module_file.write('\n\tparams_list = [params.index[0]]')
            module_file.write('\n\tparams_list.extend(list(params[[(value is True) for value in params.value]].index))')
            module_file.write('\n\tparams_list = [ param.replace("return", "") for param in params_list ]')
            module_file.write('\n\n\tresponse = make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(' + id_field + '), verb = "get", params_list = params_list)')
            module_file.write('\n\n\treturn(response)')

            # delete_object()
            functionName = 'delete' + object_name

            module_file.write('\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1):')
            module_file.write('\n\n\tresponse = make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(' + id_field + '), verb = "delete")')
            module_file.write('\n\n\treturn(response)')

            #return

        module_file.close()

        ini_file.close()
        
        return()