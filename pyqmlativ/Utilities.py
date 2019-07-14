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
def make_request(endpoint, verb = 'get', return_params_list = [], payload = None):
    
    check_credentials()
    
    sess = OAuth1Session(client_key = os.environ["consumer_key"], client_secret = os.environ["consumer_secret"])
    
    request_url = os.environ["api_url"] + endpoint
    
    for param in return_params_list:
        if return_params_list.index(param) == 0:
            request_url = request_url + '?searchFields=' + param
        else:
            request_url = request_url + '&searchFields=' + param
    
    if verb == 'get':
        r = sess.get(request_url)
        
    elif verb == 'post':
        r = sess.post(request_url, data = payload)

    elif verb == 'put':
        r = sess.put(request_url, data = payload)
        
    elif verb == 'delete':
        r = sess.delete(request_url)

    else:
      raise Exception('"verb" must be one of get, post, put or delete')  
    
    if (r.status_code < 300) & (verb != 'delete'):
        if "Objects" in r.json():
            return pd.DataFrame.from_dict(pd.read_json(json.dumps(r.json()), typ = 'Series', dtype=False).Objects)
        else:
            return pd.read_json(json.dumps(r.json()), typ = 'Series', dtype=False)

    if (r.status_code < 300) & (verb == 'delete'):
        return 'Object successfully deleted'
    
    if 'error' in r.json():
        raise Exception((pd.read_json(json.dumps(r.json()), typ = 'Series', dtype=False))['error'])

    if 'errors' in r.json():
        raise Exception((pd.read_json(json.dumps(r.json()), typ = 'Series', dtype=False))['errors'])

# This function generates api request functions.
def generate_functions(modules = all_modules.module_name, EntityID = 1):
    
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
        module_file.write('\n\nimport json')
        module_file.write('\n\nimport re')

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

            # Grab non-read-only fields for possible payload fields.
            payload_field_names = [ field_name for field_name in field_names if 'ReadOnly' not in fields[field_name].keys()]
            
            # Grab all fields for possible return fields.
            return_field_names = field_names
            
            # getEveryObject()
            functionName = 'getEvery' + object_name
            function_text_line_1 = '\n\ndef ' + functionName + '(EntityID = 1, page = 1, pageSize = 100'

            for field_name in return_field_names:

                # Make the ID variable return by default.
                if field_name == id_field:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = True'
                else:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = False'

            function_text_line_1 = function_text_line_1 + '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n\tparams = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])')
            
            module_file.write('\n\n\treturn_params_list = list(params[[(value is True) for value in params.value]].index)')
            module_file.write('\n\tif params.iloc[3,:].name == "".join(return_params_list):')
            module_file.write('\n\t\treturn_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)')
            module_file.write('\n\treturn_params_list = [re.sub("^return", "", param) for param in return_params_list]')
            
            module_file.write('\n\n\treturn make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)')
            
            # getObject()
            functionName = 'get' + object_name
            function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1'

            for field_name in return_field_names:

                # Make the ID variable return by default.
                if field_name == id_field:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = True'
                else:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = False'

            function_text_line_1 = function_text_line_1 + '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n\tparams = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])')
            
            module_file.write('\n\n\treturn_params_list = list(params[[(value is True) for value in params.value]].index)')
            module_file.write('\n\tif params.iloc[2,:].name == "".join(return_params_list):')
            module_file.write('\n\t\treturn_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)')
            module_file.write('\n\treturn_params_list = [re.sub("^return", "", param) for param in return_params_list]')

            module_file.write('\n\n\treturn make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(' + id_field + '), verb = "get", return_params_list = return_params_list)')
            
            # modifyObject()
            functionName = 'modify' + object_name
            function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1'

            for field_name in payload_field_names:
                function_text_line_1 = function_text_line_1 + ', set' + field_name + ' = None'

            for field_name in return_field_names:
                # Make the ID variable return by default.
                if field_name == id_field:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = True'
                else:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = False'

            function_text_line_1 = function_text_line_1 + '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n\tparams = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])')
            
            module_file.write('\n\n\treturn_params_list = [re.sub("^return", "", param) for param in return_params_list]')
            module_file.write('\n\treturn_params_list = [re.sub("^set", "", param) for param in return_params_list]')
            module_file.write('\n\treturn_params_list = list(set(return_params_list))')
            
            module_file.write('\n\n\tpayload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]')
            module_file.write('\n\tpayload_params.index = [re.sub("^set", "", name) for name in payload_params.index]')
            module_file.write('\n\tpayload_params = dict({"DataObject": dict(payload_params["value"])})')
            module_file.write('\n\tpayload_params = json.dumps(payload_params)')
            
            module_file.write('\n\n\treturn make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(' + id_field + '), verb = "post", return_params_list = return_params_list, payload = payload_params)')
            
            # createObject()
            functionName = 'create' + object_name
            function_text_line_1 = '\n\ndef ' + functionName + '(EntityID = 1'

            for field_name in payload_field_names:
                function_text_line_1 = function_text_line_1 + ', set' + field_name + ' = None'

            for field_name in return_field_names:
                # Make the ID variable return by default.
                if field_name == id_field:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = True'
                else:
                    function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = False'

            function_text_line_1 = function_text_line_1 + '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n\tparams = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])')
            
            module_file.write('\n\n\treturn_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)')
            module_file.write('\n\treturn_params_list = [re.sub("^return", "", param) for param in return_params_list]')
            module_file.write('\n\treturn_params_list = [re.sub("^set", "", param) for param in return_params_list]')
            module_file.write('\n\treturn_params_list = list(set(return_params_list))')
            
            module_file.write('\n\n\tpayload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]')
            module_file.write('\n\tpayload_params.index = [re.sub("^set", "", name) for name in payload_params.index]')
            module_file.write('\n\tpayload_params = dict({"DataObject": dict(payload_params["value"])})')
            module_file.write('\n\tpayload_params = json.dumps(payload_params)')
            
            module_file.write('\n\n\treturn make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/", verb = "put", return_params_list = return_params_list, payload = payload_params)')
            
            # deleteObject()
            functionName = 'delete' + object_name

            module_file.write('\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1):')
            module_file.write('\n\n\treturn make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")')

        module_file.close()
    ini_file.close()
    return
