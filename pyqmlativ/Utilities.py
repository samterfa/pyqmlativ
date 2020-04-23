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
                                        "OnlineForm", "Reporting", "Scheduling", "Security", "SkySys", "Staff", "StaffPlanning", "Student", "Transportation"],
                            'module_var_name' : ["attendance", "curriculum", "demographics", "discipline", "district",
                                        "enrollment", "family", "graduation_requirements", "gradebook", "grading", "guidance", "health", "message_center",
                                        "online_form", "reporting", "scheduling", "security", "skysys", "staff", "staff_planning", "student", "transportation"]
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

def formatSearchConditionsPayload(searchConditions, conditionGroupType):

	if(type(searchConditions) is str):
		searchConditions = [searchConditions]

	payload_string = 'dict({"SearchCondition":dict({"SearchConditionGroup":dict({"ConditionGroupType":"' + conditionGroupType + '","conditions":['

	for i in range(0, len(searchConditions)):
		search_condition = searchConditions[i]
		
		first_space_index = search_condition.find(' ')
		second_space_index = search_condition.find(' ', first_space_index + 1)

		field_name = search_condition[:first_space_index]
		condition_type = search_condition[(first_space_index + 1): second_space_index]
		value = search_condition[(second_space_index + 1):]

		payload_string +=  'dict({"StringSearchCondition":dict({"FieldName":"' + field_name + '","ConditionType":"' + condition_type + '","Value":"' + value +'"})}), '

    # Remove trailing comma and space.
	payload_string = payload_string[:-2]
	payload_string += ']})})})'

    # Return payload as dict.
	return(eval(payload_string))

# This function performs a QMLATIV API request.
def make_request(endpoint, verb = 'get', return_params_list = [], payload = None):

    """Perform API Request to Endpoint

    This function performs an HTTP request to a Skyward API endpoint. This function 
    is called by all Skyward SDK functions. You will, in general, not need to 
    call this function directly.

    Args:
        endpoint (str): The endpoint URL for the request.
        searchFields (str): A list of parameters primarily used as searchFields.
        verb (str): An HTTP request, either GET, PUT, POST or DELETE. Defaults to GET
        payload (json): A json object used in PUT and POST requests.
        

    Returns:
        A dataframe of information on the requested object(s). 

    """
    
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
            r = sess.post(request_url, json = payload)

    elif verb == 'put':
        r = sess.put(request_url, json = payload)
        
    elif verb == 'delete':
        r = sess.delete(request_url)

    else:
      raise Exception('"verb" must be one of get, post, put or delete')  
    
    if (r.status_code < 300) & (verb != 'delete'):
        if "Objects" in r.json():
            results = r.json()['Objects']
            return pd.read_json(json.dumps(results))
        
        else:
            results = r.json()
            return pd.DataFrame([list(results.values())], columns = results.keys())
          
    if (r.status_code < 300) & (verb == 'delete'):
        return 'Object successfully deleted'
    
 #   if 'error' in r.json():
 #       return(r)
    
    return(r)
# =============================================================================
#         
#         return(r.json())
#         raise Exception((pd.read_json(json.dumps(r.json()), typ = 'Series', dtype=False))['error'])
# 
#     if 'errors' in r.json():
#         raise Exception((pd.read_json(json.dumps(r.json()), typ = 'Series', dtype=False))['errors'])
# =============================================================================

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
        
        module_file.write("\n\n")
        
        module_file.write('from .Utilities import *')
        
        module_file.write("\n\n")
        
        module_file.write('import pandas as pd')
        
        module_file.write('\n\n')
        
        module_file.write('import json')
        
        module_file.write('\n\n')
        
        module_file.write('import re')

        module_endpoint = '/'.join(['', 'Generic', str(EntityID), module_name])
        objects_and_endpoints = make_request(module_endpoint)

        object_names = list(objects_and_endpoints.keys())
        object_endpoints = [ objects_and_endpoints[key][0]['href'] for key in objects_and_endpoints.keys() ]
    
        module_file = open(module_file_path, "a")
        
        for i in range(0, len(object_endpoints)):

            print(str(i+1) + '/' + str(len(object_endpoints)), end='\n', flush=True)
            
            object_name = object_names[i]
            object_endpoint = object_endpoints[i]
           
            fields = make_request(object_endpoint)
            field_names = list(fields.keys())
           
            id_field_index = [ 'PrimaryKey' in fields[key][0] for key in fields.keys() ].index(True)
            
            id_field = field_names[id_field_index]

########### Create human-readable function names.
            
            # Grab non-read-only fields for possible payload fields.
            payload_field_names = [ key for key in fields.keys() if not 'ReadOnly' in fields[key][0] ]
            payload_field_names = [ field_name for field_name in field_names if field_name != 'Relationships']
            
            # Grab all fields for possible return fields.
            return_field_names = [ field_name for field_name in field_names if field_name != 'Relationships']
            
########### getEveryObject()
            functionName = 'getEvery' + object_name
            
            function_text_lines = '\n\n\n'
            
            function_text_lines += 'def ' + functionName + '(searchConditions = [], EntityID = 1'

            for field_name in return_field_names:
                
                function_text_lines += ', return' + field_name + ' = False'

            function_text_lines += ', page = 1, pageSize = 100000, conditionGroupType = "And"):'
            
            # Include documentation
            function_text_lines += '\n\n    """'
            
            function_text_lines += "Get every " + object_name + " in the district."
            
            function_text_lines += "\n\n    "
            
            function_text_lines += "This function returns a dataframe of every " + object_name + " in the district filtered by search conditions."
            
            function_text_lines += '\n\n    """'
            
            function_text_lines += '\n\n    '
            
            # getEvery... code
            function_text_lines += 'params = locals()'
            
            function_text_lines += '\n\n    '
            
            function_text_lines += 'params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])'
            
            function_text_lines += '\n\n    '
            
            function_text_lines += "return_params = params.query('Param.str.startswith(" + '"return"' + ")', engine = 'python')"
            
            function_text_lines += '\n\n    '
            
            function_text_lines += "if not any(return_params.Value):"
            
            function_text_lines += "\n        "
            
            function_text_lines +=  "return_params = list(return_params.assign(Value = True).Param)"
            
            function_text_lines += "\n    "
            
            function_text_lines += "else:"
            
            function_text_lines += "\n        "
            
            function_text_lines +=  "return_params = list(return_params.query('Value == True').Param)"
            
            function_text_lines += "\n\n    "
            
            function_text_lines += "return_params = [re.sub(" + '"^return"' + ", '', param) for param in return_params]"
            
            function_text_lines += "\n\n    "
            
            function_text_lines += "if len(searchConditions) > 0:"
            
            function_text_lines += "\n\n        "
            
            function_text_lines += "searchConditions = params.query('Param == " + '"searchConditions"' + "').Value[0]"
            
            function_text_lines += "\n\n        "
            
            function_text_lines += "payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)"
            
            function_text_lines += "\n\n        "
            
            function_text_lines += 'return make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)'
            
            function_text_lines += "\n\n    "
            
            function_text_lines += "else:"
            
            function_text_lines += "\n        "
            
            function_text_lines += 'return make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)'
            
            module_file.writelines(function_text_lines)

########### getObject()
            functionName = 'get' + object_name
            if id_field == 'EntityID':
                function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field
            else:    
                function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1'
    
            for field_name in return_field_names:
    
                function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = False'
              
            function_text_line_1 = function_text_line_1 + '):'
    
            module_file.write(function_text_line_1)
            
            module_file.write('\n\n    ' + 'params = locals()')

            module_file.write('\n\n    ' + 'params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])')

            module_file.write('\n\n    ' + "return_params = params.query('Param.str.startswith(" + '"return"' + ")', engine = 'python')")
            
            module_file.write('\n\n    ' + "if not any(return_params.Value):")
            
            module_file.write('\n\n        ' + "return_params = list(return_params.assign(Value = True).Param)")
            
            module_file.write('\n    ' + "else:")
            
            module_file.write('\n\n        ' + "return_params = list(return_params.query('Value == True').Param)")
            
            module_file.write('\n\n    ' + "return_params = [re.sub(" + '"^return"' + ", '', param) for param in return_params]")
            
            module_file.write('\n\n    return make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(' + id_field + '), verb = "get", return_params_list = return_params)')
            
########### modifyObject()
            functionName = 'modify' + object_name

            if id_field == 'EntityID':
                function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field
            else:    
                function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1'

            for field_name in payload_field_names:
                function_text_line_1 = function_text_line_1 + ', set' + field_name + ' = None'

            for field_name in return_field_names:
                
                function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = False'

            function_text_line_1 = function_text_line_1 + '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n    ' + 'params = locals()')

            module_file.write('\n\n    ' + 'params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])')

#            module_file.write('\n\n    params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])')
            
            module_file.write('\n\n    ' + "return_params = params.query('Param.str.startswith(" + '"return"' + ")', engine = 'python')")
            
            module_file.write('\n\n    ' + "if not any(return_params.Value):")
            
            module_file.write('\n\n        ' + "return_params = list(return_params.assign(Value = True).Param)")
            
            module_file.write('\n    ' + "else:")
            
            module_file.write('\n\n        ' + "return_params = list(return_params.query('Value == True').Param)")
            
            module_file.write('\n\n    ' + "return_params = [re.sub(" + '"^return"' + ", '', param) for param in return_params]")
            
            module_file.write('\n\n    ' + "payload_params = params.query('Param.str.startswith(" + '"set"' + ") and not Value.isnull()', engine = 'python')")
            
            module_file.write('\n\n    ' + 'payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))')
            
            module_file.write('\n\n    ' + 'payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()')
            
            module_file.write('\n\n    ' + 'payload_params = json.loads(payload_params.to_json(orient = "records"))[0]')
            
            module_file.write('\n\n    ' + 'payload_params = dict({"DataObject": payload_params})')
            
            module_file.write('\n\n    ' + 'payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))')
            
            module_file.write('\n\n    return make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(' + id_field + '), verb = "post", return_params_list = return_params, payload = payload_params)')
            
########### createObject()
            functionName = 'create' + object_name
            function_text_line_1 = '\n\ndef ' + functionName + '(EntityID = 1'

            for field_name in payload_field_names:
                function_text_line_1 = function_text_line_1 + ', set' + field_name + ' = None'

            for field_name in return_field_names:
                
                function_text_line_1 = function_text_line_1 + ', return' + field_name + ' = False'

            function_text_line_1 = function_text_line_1 + '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n    ' + 'params = locals()')

            module_file.write('\n\n    ' + 'params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])')

            module_file.write('\n\n    ' + "return_params = params.query('Param.str.startswith(" + '"return"' + ")', engine = 'python')")
            
            module_file.write('\n\n    ' + "if not any(return_params.Value):")
            
            module_file.write('\n\n        ' + "return_params = list(return_params.assign(Value = True).Param)")
            
            module_file.write('\n    ' + "else:")
            
            module_file.write('\n\n        ' + "return_params = list(return_params.query('Value == True').Param)")
            
            module_file.write('\n\n    ' + "return_params = [re.sub(" + '"^return"' + ", '', param) for param in return_params]")
            
            module_file.write('\n\n    ' + "payload_params = params.query('Param.str.startswith(" + '"set"' + ") and not Value.isnull()', engine = 'python')")
            
            module_file.write('\n\n    ' + 'payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))')
            
            module_file.write('\n\n    ' + 'payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()')
            
            module_file.write('\n\n    ' + 'payload_params = json.loads(payload_params.to_json(orient = "records"))[0]')
            
            module_file.write('\n\n    ' + 'payload_params = dict({"DataObject": payload_params})')
            
            module_file.write('\n\n    ' + 'return make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/", verb = "put", return_params_list = return_params, payload = payload_params)')

########### deleteObject()
            functionName = 'delete' + object_name

            if id_field == 'EntityID':
                function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field
            else:    
                function_text_line_1 = '\n\ndef ' + functionName + '(' + id_field + ', EntityID = 1'

            function_text_line_1 += '):'

            module_file.write(function_text_line_1)

            module_file.write('\n\n    return make_request(endpoint = "' + object_endpoint.replace('/1/', '/" + str(EntityID) + "/') + '/" + str(' + id_field + '), verb = "delete")')

           # module_file.write('\n\n    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")')

        module_file.close()
    ini_file.close()
    return
