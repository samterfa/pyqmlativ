# This module contains Security functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAuthenticationAssertion(searchConditions = [], EntityID = 1, returnAuthenticationAssertionID = False, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AuthenticationAssertion in the district.

    This function returns a dataframe of every AuthenticationAssertion in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAuthenticationAssertion(AuthenticationAssertionID, EntityID = 1, returnAuthenticationAssertionID = False, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(AuthenticationAssertionID), verb = "get", return_params_list = return_params)

def modifyAuthenticationAssertion(AuthenticationAssertionID, EntityID = 1, setAuthenticationAssertionID = None, setAssertionGuid = None, setAuthenticationMethodID = None, setCreatedTime = None, setMobileDevice = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationAssertionID = False, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(AuthenticationAssertionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAuthenticationAssertion(EntityID = 1, setAuthenticationAssertionID = None, setAssertionGuid = None, setAuthenticationMethodID = None, setCreatedTime = None, setMobileDevice = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationAssertionID = False, returnAssertionGuid = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAuthenticationAssertion(AuthenticationAssertionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationAssertion/" + str(AuthenticationAssertionID), verb = "delete")


def getEveryAuthenticationMethod(searchConditions = [], EntityID = 1, returnAuthenticationMethodID = False, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AuthenticationMethod in the district.

    This function returns a dataframe of every AuthenticationMethod in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAuthenticationMethod(AuthenticationMethodID, EntityID = 1, returnAuthenticationMethodID = False, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(AuthenticationMethodID), verb = "get", return_params_list = return_params)

def modifyAuthenticationMethod(AuthenticationMethodID, EntityID = 1, setAuthenticationMethodID = None, setCertificate = None, setCompareNameIDAsNumeric = None, setCreatedTime = None, setIsSkywardMaintained = None, setMetadata = None, setMetadataURL = None, setModifiedTime = None, setName = None, setNameIdentifierSkywardField = None, setNameIdentifierSkywardFieldFriendlyName = None, setNameIdentifierType = None, setSkywardHash = None, setSkywardID = None, setSSOURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationMethodID = False, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(AuthenticationMethodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAuthenticationMethod(EntityID = 1, setAuthenticationMethodID = None, setCertificate = None, setCompareNameIDAsNumeric = None, setCreatedTime = None, setIsSkywardMaintained = None, setMetadata = None, setMetadataURL = None, setModifiedTime = None, setName = None, setNameIdentifierSkywardField = None, setNameIdentifierSkywardFieldFriendlyName = None, setNameIdentifierType = None, setSkywardHash = None, setSkywardID = None, setSSOURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationMethodID = False, returnCertificate = False, returnCompareNameIDAsNumeric = False, returnCreatedTime = False, returnIsSkywardMaintained = False, returnMetadata = False, returnMetadataURL = False, returnModifiedTime = False, returnName = False, returnNameIdentifierSkywardField = False, returnNameIdentifierSkywardFieldFriendlyName = False, returnNameIdentifierType = False, returnSkywardHash = False, returnSkywardID = False, returnSSOURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAuthenticationMethod(AuthenticationMethodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationMethod/" + str(AuthenticationMethodID), verb = "delete")


def getEveryAuthenticationRole(searchConditions = [], EntityID = 1, returnAuthenticationRoleID = False, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AuthenticationRole in the district.

    This function returns a dataframe of every AuthenticationRole in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAuthenticationRole(AuthenticationRoleID, EntityID = 1, returnAuthenticationRoleID = False, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(AuthenticationRoleID), verb = "get", return_params_list = return_params)

def modifyAuthenticationRole(AuthenticationRoleID, EntityID = 1, setAuthenticationRoleID = None, setAllowSkywardCredentials = None, setCreatedTime = None, setDisplayText = None, setHasAuthenticationMethod = None, setHasLDAPProvider = None, setMediaID = None, setModifiedTime = None, setName = None, setPriority = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationRoleID = False, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(AuthenticationRoleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAuthenticationRole(EntityID = 1, setAuthenticationRoleID = None, setAllowSkywardCredentials = None, setCreatedTime = None, setDisplayText = None, setHasAuthenticationMethod = None, setHasLDAPProvider = None, setMediaID = None, setModifiedTime = None, setName = None, setPriority = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationRoleID = False, returnAllowSkywardCredentials = False, returnCreatedTime = False, returnDisplayText = False, returnHasAuthenticationMethod = False, returnHasLDAPProvider = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAuthenticationRole(AuthenticationRoleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRole/" + str(AuthenticationRoleID), verb = "delete")


def getEveryAuthenticationRoleLDAPProvider(searchConditions = [], EntityID = 1, returnAuthenticationRoleLDAPProviderID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AuthenticationRoleLDAPProvider in the district.

    This function returns a dataframe of every AuthenticationRoleLDAPProvider in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAuthenticationRoleLDAPProvider(AuthenticationRoleLDAPProviderID, EntityID = 1, returnAuthenticationRoleLDAPProviderID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(AuthenticationRoleLDAPProviderID), verb = "get", return_params_list = return_params)

def modifyAuthenticationRoleLDAPProvider(AuthenticationRoleLDAPProviderID, EntityID = 1, setAuthenticationRoleLDAPProviderID = None, setAuthenticationRoleID = None, setCreatedTime = None, setLDAPProviderID = None, setModifiedTime = None, setPriority = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationRoleLDAPProviderID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(AuthenticationRoleLDAPProviderID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAuthenticationRoleLDAPProvider(EntityID = 1, setAuthenticationRoleLDAPProviderID = None, setAuthenticationRoleID = None, setCreatedTime = None, setLDAPProviderID = None, setModifiedTime = None, setPriority = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationRoleLDAPProviderID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnLDAPProviderID = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAuthenticationRoleLDAPProvider(AuthenticationRoleLDAPProviderID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleLDAPProvider/" + str(AuthenticationRoleLDAPProviderID), verb = "delete")


def getEveryAuthenticationRoleMethod(searchConditions = [], EntityID = 1, returnAuthenticationRoleMethodID = False, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AuthenticationRoleMethod in the district.

    This function returns a dataframe of every AuthenticationRoleMethod in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAuthenticationRoleMethod(AuthenticationRoleMethodID, EntityID = 1, returnAuthenticationRoleMethodID = False, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(AuthenticationRoleMethodID), verb = "get", return_params_list = return_params)

def modifyAuthenticationRoleMethod(AuthenticationRoleMethodID, EntityID = 1, setAuthenticationRoleMethodID = None, setAuthenticationMethodID = None, setAuthenticationRoleID = None, setCreatedTime = None, setDisplayOrder = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationRoleMethodID = False, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(AuthenticationRoleMethodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAuthenticationRoleMethod(EntityID = 1, setAuthenticationRoleMethodID = None, setAuthenticationMethodID = None, setAuthenticationRoleID = None, setCreatedTime = None, setDisplayOrder = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAuthenticationRoleMethodID = False, returnAuthenticationMethodID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAuthenticationRoleMethod(AuthenticationRoleMethodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/AuthenticationRoleMethod/" + str(AuthenticationRoleMethodID), verb = "delete")


def getEveryBrowseFieldPath(searchConditions = [], EntityID = 1, returnBrowseFieldPathID = False, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BrowseFieldPath in the district.

    This function returns a dataframe of every BrowseFieldPath in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBrowseFieldPath(BrowseFieldPathID, EntityID = 1, returnBrowseFieldPathID = False, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(BrowseFieldPathID), verb = "get", return_params_list = return_params)

def modifyBrowseFieldPath(BrowseFieldPathID, EntityID = 1, setBrowseFieldPathID = None, setBrowseID = None, setCreatedTime = None, setFieldPath = None, setGuidFieldPath = None, setIsSkywardDefined = None, setModifiedTime = None, setRoleID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseFieldPathID = False, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(BrowseFieldPathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBrowseFieldPath(EntityID = 1, setBrowseFieldPathID = None, setBrowseID = None, setCreatedTime = None, setFieldPath = None, setGuidFieldPath = None, setIsSkywardDefined = None, setModifiedTime = None, setRoleID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseFieldPathID = False, returnBrowseID = False, returnCreatedTime = False, returnFieldPath = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnRoleID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBrowseFieldPath(BrowseFieldPathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/BrowseFieldPath/" + str(BrowseFieldPathID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigSystem in the district.

    This function returns a dataframe of every ConfigSystem in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setAccessCodeLength = None, setAdminEmployeeTeacherActivityAllowUsernameChange = None, setAdminMissedSessionPingCountLimit = None, setAdminSessionClientPingSeconds = None, setAdminSessionTimeoutSeconds = None, setAdminSessionWarnSeconds = None, setAuthenticationRoleIDActivity = None, setAuthenticationRoleIDAdministrative = None, setAuthenticationRoleIDEmployee = None, setAuthenticationRoleIDFamilyNewStudentEnrollment = None, setAuthenticationRoleIDStudent = None, setAuthenticationRoleIDTeacher = None, setAutogenerateEmployeeAccessCodes = None, setAutogenerateStaffAccessCodes = None, setAutogenerateStudentAccessCodes = None, setCombineAuthenticationRolesOnSignIn = None, setCreatedTime = None, setDaysUntilPasswordExpires = None, setFailedSignInCountLimit = None, setFamilyAllowUsernameChange = None, setFamilyStudentEmployeeMissedSessionPingCountLimit = None, setFamilyStudentEmployeeSessionClientPingSeconds = None, setFamilyStudentEmployeeSessionTimeoutSeconds = None, setFamilyStudentEmployeeSessionWarnSeconds = None, setForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = None, setLoginLockRetryDelayMinutes = None, setMaximumPasswordLength = None, setMinimumPasswordLength = None, setModifiedTime = None, setMultifactorAuthenticationIDActivity = None, setMultifactorAuthenticationIDAdministrative = None, setMultifactorAuthenticationIDEmployee = None, setMultifactorAuthenticationIDFamilyNewStudentEnrollment = None, setMultifactorAuthenticationIDStudent = None, setMultifactorAuthenticationIDTeacher = None, setRequiredNumericCharacters = None, setRequiredSpecialCharacters = None, setSessionAccessDeniedLimit = None, setStudentAllowUsernameChange = None, setTeacherMissedSessionPingCountLimit = None, setTeacherSessionClientPingSeconds = None, setTeacherSessionTimeoutSeconds = None, setTeacherSessionWarnSeconds = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserImportChangeThreshold = None, setUserImportDeleteThreshold = None, setUserImportFilePath = None, setUserImportFileType = None, setUserImportFileTypeCode = None, setUserImportShouldMaintainExistingUsers = None, returnConfigSystemID = False, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setAccessCodeLength = None, setAdminEmployeeTeacherActivityAllowUsernameChange = None, setAdminMissedSessionPingCountLimit = None, setAdminSessionClientPingSeconds = None, setAdminSessionTimeoutSeconds = None, setAdminSessionWarnSeconds = None, setAuthenticationRoleIDActivity = None, setAuthenticationRoleIDAdministrative = None, setAuthenticationRoleIDEmployee = None, setAuthenticationRoleIDFamilyNewStudentEnrollment = None, setAuthenticationRoleIDStudent = None, setAuthenticationRoleIDTeacher = None, setAutogenerateEmployeeAccessCodes = None, setAutogenerateStaffAccessCodes = None, setAutogenerateStudentAccessCodes = None, setCombineAuthenticationRolesOnSignIn = None, setCreatedTime = None, setDaysUntilPasswordExpires = None, setFailedSignInCountLimit = None, setFamilyAllowUsernameChange = None, setFamilyStudentEmployeeMissedSessionPingCountLimit = None, setFamilyStudentEmployeeSessionClientPingSeconds = None, setFamilyStudentEmployeeSessionTimeoutSeconds = None, setFamilyStudentEmployeeSessionWarnSeconds = None, setForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = None, setLoginLockRetryDelayMinutes = None, setMaximumPasswordLength = None, setMinimumPasswordLength = None, setModifiedTime = None, setMultifactorAuthenticationIDActivity = None, setMultifactorAuthenticationIDAdministrative = None, setMultifactorAuthenticationIDEmployee = None, setMultifactorAuthenticationIDFamilyNewStudentEnrollment = None, setMultifactorAuthenticationIDStudent = None, setMultifactorAuthenticationIDTeacher = None, setRequiredNumericCharacters = None, setRequiredSpecialCharacters = None, setSessionAccessDeniedLimit = None, setStudentAllowUsernameChange = None, setTeacherMissedSessionPingCountLimit = None, setTeacherSessionClientPingSeconds = None, setTeacherSessionTimeoutSeconds = None, setTeacherSessionWarnSeconds = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserImportChangeThreshold = None, setUserImportDeleteThreshold = None, setUserImportFilePath = None, setUserImportFileType = None, setUserImportFileTypeCode = None, setUserImportShouldMaintainExistingUsers = None, returnConfigSystemID = False, returnAccessCodeLength = False, returnAdminEmployeeTeacherActivityAllowUsernameChange = False, returnAdminMissedSessionPingCountLimit = False, returnAdminSessionClientPingSeconds = False, returnAdminSessionTimeoutSeconds = False, returnAdminSessionWarnSeconds = False, returnAuthenticationRoleIDActivity = False, returnAuthenticationRoleIDAdministrative = False, returnAuthenticationRoleIDEmployee = False, returnAuthenticationRoleIDFamilyNewStudentEnrollment = False, returnAuthenticationRoleIDStudent = False, returnAuthenticationRoleIDTeacher = False, returnAutogenerateEmployeeAccessCodes = False, returnAutogenerateStaffAccessCodes = False, returnAutogenerateStudentAccessCodes = False, returnCombineAuthenticationRolesOnSignIn = False, returnCreatedTime = False, returnDaysUntilPasswordExpires = False, returnFailedSignInCountLimit = False, returnFamilyAllowUsernameChange = False, returnFamilyStudentEmployeeMissedSessionPingCountLimit = False, returnFamilyStudentEmployeeSessionClientPingSeconds = False, returnFamilyStudentEmployeeSessionTimeoutSeconds = False, returnFamilyStudentEmployeeSessionWarnSeconds = False, returnForcePasswordExpirationOnSkywardLoginIfPasswordRequirementsNotMet = False, returnLoginLockRetryDelayMinutes = False, returnMaximumPasswordLength = False, returnMinimumPasswordLength = False, returnModifiedTime = False, returnMultifactorAuthenticationIDActivity = False, returnMultifactorAuthenticationIDAdministrative = False, returnMultifactorAuthenticationIDEmployee = False, returnMultifactorAuthenticationIDFamilyNewStudentEnrollment = False, returnMultifactorAuthenticationIDStudent = False, returnMultifactorAuthenticationIDTeacher = False, returnRequiredNumericCharacters = False, returnRequiredSpecialCharacters = False, returnSessionAccessDeniedLimit = False, returnStudentAllowUsernameChange = False, returnTeacherMissedSessionPingCountLimit = False, returnTeacherSessionClientPingSeconds = False, returnTeacherSessionTimeoutSeconds = False, returnTeacherSessionWarnSeconds = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportChangeThreshold = False, returnUserImportDeleteThreshold = False, returnUserImportFilePath = False, returnUserImportFileType = False, returnUserImportFileTypeCode = False, returnUserImportShouldMaintainExistingUsers = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryDataObjectFieldPath(searchConditions = [], EntityID = 1, returnDataObjectFieldPathID = False, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataObjectFieldPath in the district.

    This function returns a dataframe of every DataObjectFieldPath in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataObjectFieldPath(DataObjectFieldPathID, EntityID = 1, returnDataObjectFieldPathID = False, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(DataObjectFieldPathID), verb = "get", return_params_list = return_params)

def modifyDataObjectFieldPath(DataObjectFieldPathID, EntityID = 1, setDataObjectFieldPathID = None, setCreatedTime = None, setDisplayLevel = None, setExactSystemTypeName = None, setField = None, setFieldIDSkySys = None, setFieldPath = None, setFriendlyName = None, setGuidFieldPath = None, setIsSkywardDefined = None, setModifiedTime = None, setNumberOfRelationships = None, setObjectID = None, setObjectSchemaObject = None, setRoleID = None, setSkywardDisplayLevel = None, setSkywardDisplayLevelCode = None, setSkywardFriendlyName = None, setSkywardHash = None, setSkywardID = None, setUserDisplayLevel = None, setUserDisplayLevelCode = None, setUserFriendlyName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataObjectFieldPathID = False, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(DataObjectFieldPathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataObjectFieldPath(EntityID = 1, setDataObjectFieldPathID = None, setCreatedTime = None, setDisplayLevel = None, setExactSystemTypeName = None, setField = None, setFieldIDSkySys = None, setFieldPath = None, setFriendlyName = None, setGuidFieldPath = None, setIsSkywardDefined = None, setModifiedTime = None, setNumberOfRelationships = None, setObjectID = None, setObjectSchemaObject = None, setRoleID = None, setSkywardDisplayLevel = None, setSkywardDisplayLevelCode = None, setSkywardFriendlyName = None, setSkywardHash = None, setSkywardID = None, setUserDisplayLevel = None, setUserDisplayLevelCode = None, setUserFriendlyName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataObjectFieldPathID = False, returnCreatedTime = False, returnDisplayLevel = False, returnExactSystemTypeName = False, returnField = False, returnFieldIDSkySys = False, returnFieldPath = False, returnFriendlyName = False, returnGuidFieldPath = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnNumberOfRelationships = False, returnObjectID = False, returnObjectSchemaObject = False, returnRoleID = False, returnSkywardDisplayLevel = False, returnSkywardDisplayLevelCode = False, returnSkywardFriendlyName = False, returnSkywardHash = False, returnSkywardID = False, returnUserDisplayLevel = False, returnUserDisplayLevelCode = False, returnUserFriendlyName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataObjectFieldPath(DataObjectFieldPathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/DataObjectFieldPath/" + str(DataObjectFieldPathID), verb = "delete")


def getEveryElectronicSignature(searchConditions = [], EntityID = 1, returnElectronicSignatureID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ElectronicSignature in the district.

    This function returns a dataframe of every ElectronicSignature in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getElectronicSignature(ElectronicSignatureID, EntityID = 1, returnElectronicSignatureID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(ElectronicSignatureID), verb = "get", return_params_list = return_params)

def modifyElectronicSignature(ElectronicSignatureID, EntityID = 1, setElectronicSignatureID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEntityID = None, setEntityName = None, setIsForGrading = None, setIsForPurchasing = None, setIsForStateReporting = None, setMediaID = None, setModifiedTime = None, setSignatureLocationKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnElectronicSignatureID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(ElectronicSignatureID), verb = "post", return_params_list = return_params, payload = payload_params)

def createElectronicSignature(EntityID = 1, setElectronicSignatureID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEntityID = None, setEntityName = None, setIsForGrading = None, setIsForPurchasing = None, setIsForStateReporting = None, setMediaID = None, setModifiedTime = None, setSignatureLocationKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnElectronicSignatureID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnEntityName = False, returnIsForGrading = False, returnIsForPurchasing = False, returnIsForStateReporting = False, returnMediaID = False, returnModifiedTime = False, returnSignatureLocationKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteElectronicSignature(ElectronicSignatureID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ElectronicSignature/" + str(ElectronicSignatureID), verb = "delete")


def getEveryFieldRestriction(searchConditions = [], EntityID = 1, returnFieldRestrictionID = False, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FieldRestriction in the district.

    This function returns a dataframe of every FieldRestriction in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFieldRestriction(FieldRestrictionID, EntityID = 1, returnFieldRestrictionID = False, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(FieldRestrictionID), verb = "get", return_params_list = return_params)

def modifyFieldRestriction(FieldRestrictionID, EntityID = 1, setFieldRestrictionID = None, setCreatedTime = None, setFieldID = None, setModifiedTime = None, setName = None, setRestrictionType = None, setRestrictionTypeCode = None, setRoleSetType = None, setRoleSetTypeCode = None, setRoleSetTypeRequiresRoles = None, setScreenSetType = None, setScreenSetTypeCode = None, setScreenSetTypeRequiresScreens = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFieldRestrictionID = False, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(FieldRestrictionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFieldRestriction(EntityID = 1, setFieldRestrictionID = None, setCreatedTime = None, setFieldID = None, setModifiedTime = None, setName = None, setRestrictionType = None, setRestrictionTypeCode = None, setRoleSetType = None, setRoleSetTypeCode = None, setRoleSetTypeRequiresRoles = None, setScreenSetType = None, setScreenSetTypeCode = None, setScreenSetTypeRequiresScreens = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFieldRestrictionID = False, returnCreatedTime = False, returnFieldID = False, returnModifiedTime = False, returnName = False, returnRestrictionType = False, returnRestrictionTypeCode = False, returnRoleSetType = False, returnRoleSetTypeCode = False, returnRoleSetTypeRequiresRoles = False, returnScreenSetType = False, returnScreenSetTypeCode = False, returnScreenSetTypeRequiresScreens = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFieldRestriction(FieldRestrictionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestriction/" + str(FieldRestrictionID), verb = "delete")


def getEveryFieldRestrictionRole(searchConditions = [], EntityID = 1, returnFieldRestrictionRoleID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FieldRestrictionRole in the district.

    This function returns a dataframe of every FieldRestrictionRole in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFieldRestrictionRole(FieldRestrictionRoleID, EntityID = 1, returnFieldRestrictionRoleID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(FieldRestrictionRoleID), verb = "get", return_params_list = return_params)

def modifyFieldRestrictionRole(FieldRestrictionRoleID, EntityID = 1, setFieldRestrictionRoleID = None, setCreatedTime = None, setFieldRestrictionID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFieldRestrictionRoleID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(FieldRestrictionRoleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFieldRestrictionRole(EntityID = 1, setFieldRestrictionRoleID = None, setCreatedTime = None, setFieldRestrictionID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFieldRestrictionRoleID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFieldRestrictionRole(FieldRestrictionRoleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionRole/" + str(FieldRestrictionRoleID), verb = "delete")


def getEveryFieldRestrictionScreen(searchConditions = [], EntityID = 1, returnFieldRestrictionScreenID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FieldRestrictionScreen in the district.

    This function returns a dataframe of every FieldRestrictionScreen in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFieldRestrictionScreen(FieldRestrictionScreenID, EntityID = 1, returnFieldRestrictionScreenID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(FieldRestrictionScreenID), verb = "get", return_params_list = return_params)

def modifyFieldRestrictionScreen(FieldRestrictionScreenID, EntityID = 1, setFieldRestrictionScreenID = None, setCreatedTime = None, setFieldRestrictionID = None, setModifiedTime = None, setSecurityLocationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFieldRestrictionScreenID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(FieldRestrictionScreenID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFieldRestrictionScreen(EntityID = 1, setFieldRestrictionScreenID = None, setCreatedTime = None, setFieldRestrictionID = None, setModifiedTime = None, setSecurityLocationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFieldRestrictionScreenID = False, returnCreatedTime = False, returnFieldRestrictionID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFieldRestrictionScreen(FieldRestrictionScreenID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/FieldRestrictionScreen/" + str(FieldRestrictionScreenID), verb = "delete")


def getEveryGroup(searchConditions = [], EntityID = 1, returnGroupID = False, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Group in the district.

    This function returns a dataframe of every Group in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGroup(GroupID, EntityID = 1, returnGroupID = False, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(GroupID), verb = "get", return_params_list = return_params)

def modifyGroup(GroupID, EntityID = 1, setGroupID = None, setAutoAddToUserType = None, setAutoAddToUserTypeCode = None, setCreatedTime = None, setDescription = None, setEdFiStaffClassificationID = None, setIsActive = None, setModifiedTime = None, setName = None, setNameDescription = None, setPositionTitleOverride = None, setUsedForEmployeeAccess = None, setUsedForFamilyAccess = None, setUsedForNewStudentEnrollment = None, setUsedForStudentAccess = None, setUsedForTeacherAccess = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupID = False, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(GroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGroup(EntityID = 1, setGroupID = None, setAutoAddToUserType = None, setAutoAddToUserTypeCode = None, setCreatedTime = None, setDescription = None, setEdFiStaffClassificationID = None, setIsActive = None, setModifiedTime = None, setName = None, setNameDescription = None, setPositionTitleOverride = None, setUsedForEmployeeAccess = None, setUsedForFamilyAccess = None, setUsedForNewStudentEnrollment = None, setUsedForStudentAccess = None, setUsedForTeacherAccess = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupID = False, returnAutoAddToUserType = False, returnAutoAddToUserTypeCode = False, returnCreatedTime = False, returnDescription = False, returnEdFiStaffClassificationID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnPositionTitleOverride = False, returnUsedForEmployeeAccess = False, returnUsedForFamilyAccess = False, returnUsedForNewStudentEnrollment = False, returnUsedForStudentAccess = False, returnUsedForTeacherAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGroup(GroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Group/" + str(GroupID), verb = "delete")


def getEveryGroupEntityAutoAdd(searchConditions = [], EntityID = 1, returnGroupEntityAutoAddID = False, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every GroupEntityAutoAdd in the district.

    This function returns a dataframe of every GroupEntityAutoAdd in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGroupEntityAutoAdd(GroupEntityAutoAddID, EntityID = 1, returnGroupEntityAutoAddID = False, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(GroupEntityAutoAddID), verb = "get", return_params_list = return_params)

def modifyGroupEntityAutoAdd(GroupEntityAutoAddID, EntityID = 1, setGroupEntityAutoAddID = None, setCreatedTime = None, setEntityID = None, setGroupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupEntityAutoAddID = False, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(GroupEntityAutoAddID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGroupEntityAutoAdd(EntityID = 1, setGroupEntityAutoAddID = None, setCreatedTime = None, setEntityID = None, setGroupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupEntityAutoAddID = False, returnCreatedTime = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGroupEntityAutoAdd(GroupEntityAutoAddID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupEntityAutoAdd/" + str(GroupEntityAutoAddID), verb = "delete")


def getEveryGroupImpersonationRole(searchConditions = [], EntityID = 1, returnGroupImpersonationRoleID = False, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every GroupImpersonationRole in the district.

    This function returns a dataframe of every GroupImpersonationRole in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGroupImpersonationRole(GroupImpersonationRoleID, EntityID = 1, returnGroupImpersonationRoleID = False, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(GroupImpersonationRoleID), verb = "get", return_params_list = return_params)

def modifyGroupImpersonationRole(GroupImpersonationRoleID, EntityID = 1, setGroupImpersonationRoleID = None, setCreatedTime = None, setGroupID = None, setIsReadOnly = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupImpersonationRoleID = False, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(GroupImpersonationRoleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGroupImpersonationRole(EntityID = 1, setGroupImpersonationRoleID = None, setCreatedTime = None, setGroupID = None, setIsReadOnly = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupImpersonationRoleID = False, returnCreatedTime = False, returnGroupID = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGroupImpersonationRole(GroupImpersonationRoleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupImpersonationRole/" + str(GroupImpersonationRoleID), verb = "delete")


def getEveryGroupLDAPSynchronization(searchConditions = [], EntityID = 1, returnGroupLDAPSynchronizationID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every GroupLDAPSynchronization in the district.

    This function returns a dataframe of every GroupLDAPSynchronization in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGroupLDAPSynchronization(GroupLDAPSynchronizationID, EntityID = 1, returnGroupLDAPSynchronizationID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(GroupLDAPSynchronizationID), verb = "get", return_params_list = return_params)

def modifyGroupLDAPSynchronization(GroupLDAPSynchronizationID, EntityID = 1, setGroupLDAPSynchronizationID = None, setCommonName = None, setCreatedTime = None, setDistinguishedName = None, setEntityID = None, setGroupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupLDAPSynchronizationID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(GroupLDAPSynchronizationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGroupLDAPSynchronization(EntityID = 1, setGroupLDAPSynchronizationID = None, setCommonName = None, setCreatedTime = None, setDistinguishedName = None, setEntityID = None, setGroupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupLDAPSynchronizationID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnEntityID = False, returnGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGroupLDAPSynchronization(GroupLDAPSynchronizationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupLDAPSynchronization/" + str(GroupLDAPSynchronizationID), verb = "delete")


def getEveryGroupMembership(searchConditions = [], EntityID = 1, returnGroupMembershipID = False, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every GroupMembership in the district.

    This function returns a dataframe of every GroupMembership in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGroupMembership(GroupMembershipID, EntityID = 1, returnGroupMembershipID = False, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(GroupMembershipID), verb = "get", return_params_list = return_params)

def modifyGroupMembership(GroupMembershipID, EntityID = 1, setGroupMembershipID = None, setCreatedTime = None, setEntityID = None, setExternalUniqueIdentifier = None, setGroupIDParent = None, setMembershipSource = None, setMembershipSourceCode = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDMember = None, setUserIDModifiedBy = None, returnGroupMembershipID = False, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(GroupMembershipID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGroupMembership(EntityID = 1, setGroupMembershipID = None, setCreatedTime = None, setEntityID = None, setExternalUniqueIdentifier = None, setGroupIDParent = None, setMembershipSource = None, setMembershipSourceCode = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDMember = None, setUserIDModifiedBy = None, returnGroupMembershipID = False, returnCreatedTime = False, returnEntityID = False, returnExternalUniqueIdentifier = False, returnGroupIDParent = False, returnMembershipSource = False, returnMembershipSourceCode = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDMember = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGroupMembership(GroupMembershipID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupMembership/" + str(GroupMembershipID), verb = "delete")


def getEveryGroupRole(searchConditions = [], EntityID = 1, returnGroupRoleID = False, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every GroupRole in the district.

    This function returns a dataframe of every GroupRole in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGroupRole(GroupRoleID, EntityID = 1, returnGroupRoleID = False, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(GroupRoleID), verb = "get", return_params_list = return_params)

def modifyGroupRole(GroupRoleID, EntityID = 1, setGroupRoleID = None, setCreatedTime = None, setGroupID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupRoleID = False, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(GroupRoleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGroupRole(EntityID = 1, setGroupRoleID = None, setCreatedTime = None, setGroupID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGroupRoleID = False, returnCreatedTime = False, returnGroupID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGroupRole(GroupRoleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/GroupRole/" + str(GroupRoleID), verb = "delete")


def getEveryImpersonation(searchConditions = [], EntityID = 1, returnImpersonationID = False, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Impersonation in the district.

    This function returns a dataframe of every Impersonation in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getImpersonation(ImpersonationID, EntityID = 1, returnImpersonationID = False, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(ImpersonationID), verb = "get", return_params_list = return_params)

def modifyImpersonation(ImpersonationID, EntityID = 1, setImpersonationID = None, setCreatedTime = None, setImpersonationEnded = None, setImpersonationStarted = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDImpersonated = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnImpersonationID = False, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(ImpersonationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createImpersonation(EntityID = 1, setImpersonationID = None, setCreatedTime = None, setImpersonationEnded = None, setImpersonationStarted = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDImpersonated = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnImpersonationID = False, returnCreatedTime = False, returnImpersonationEnded = False, returnImpersonationStarted = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDImpersonated = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteImpersonation(ImpersonationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Impersonation/" + str(ImpersonationID), verb = "delete")


def getEveryIPRange(searchConditions = [], EntityID = 1, returnIPRangeID = False, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IPRange in the district.

    This function returns a dataframe of every IPRange in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIPRange(IPRangeID, EntityID = 1, returnIPRangeID = False, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(IPRangeID), verb = "get", return_params_list = return_params)

def modifyIPRange(IPRangeID, EntityID = 1, setIPRangeID = None, setCreatedTime = None, setDescription = None, setHigh = None, setIPAddressHigh = None, setIPAddressLow = None, setLow = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIPRangeID = False, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(IPRangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIPRange(EntityID = 1, setIPRangeID = None, setCreatedTime = None, setDescription = None, setHigh = None, setIPAddressHigh = None, setIPAddressLow = None, setLow = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIPRangeID = False, returnCreatedTime = False, returnDescription = False, returnHigh = False, returnIPAddressHigh = False, returnIPAddressLow = False, returnLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIPRange(IPRangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/IPRange/" + str(IPRangeID), verb = "delete")


def getEveryLDAPGroup(searchConditions = [], EntityID = 1, returnLDAPGroupID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LDAPGroup in the district.

    This function returns a dataframe of every LDAPGroup in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLDAPGroup(LDAPGroupID, EntityID = 1, returnLDAPGroupID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(LDAPGroupID), verb = "get", return_params_list = return_params)

def modifyLDAPGroup(LDAPGroupID, EntityID = 1, setLDAPGroupID = None, setCommonName = None, setCreatedTime = None, setDistinguishedName = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLDAPGroupID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(LDAPGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLDAPGroup(EntityID = 1, setLDAPGroupID = None, setCommonName = None, setCreatedTime = None, setDistinguishedName = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLDAPGroupID = False, returnCommonName = False, returnCreatedTime = False, returnDistinguishedName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLDAPGroup(LDAPGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPGroup/" + str(LDAPGroupID), verb = "delete")


def getEveryLDAPProvider(searchConditions = [], EntityID = 1, returnLDAPProviderID = False, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LDAPProvider in the district.

    This function returns a dataframe of every LDAPProvider in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLDAPProvider(LDAPProviderID, EntityID = 1, returnLDAPProviderID = False, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(LDAPProviderID), verb = "get", return_params_list = return_params)

def modifyLDAPProvider(LDAPProviderID, EntityID = 1, setLDAPProviderID = None, setCreatedTime = None, setDisableReferrals = None, setDomainName = None, setGroupBaseDN = None, setGroupFilter = None, setGroupMemberFilter = None, setHost = None, setIgnoreCertificationErrors = None, setModifiedTime = None, setName = None, setPort = None, setProtocol = None, setProtocolCode = None, setSearchBaseDN = None, setSearchFilter = None, setSearchPassword = None, setSearchUserDN = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsernameAttribute = None, returnLDAPProviderID = False, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(LDAPProviderID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLDAPProvider(EntityID = 1, setLDAPProviderID = None, setCreatedTime = None, setDisableReferrals = None, setDomainName = None, setGroupBaseDN = None, setGroupFilter = None, setGroupMemberFilter = None, setHost = None, setIgnoreCertificationErrors = None, setModifiedTime = None, setName = None, setPort = None, setProtocol = None, setProtocolCode = None, setSearchBaseDN = None, setSearchFilter = None, setSearchPassword = None, setSearchUserDN = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsernameAttribute = None, returnLDAPProviderID = False, returnCreatedTime = False, returnDisableReferrals = False, returnDomainName = False, returnGroupBaseDN = False, returnGroupFilter = False, returnGroupMemberFilter = False, returnHost = False, returnIgnoreCertificationErrors = False, returnModifiedTime = False, returnName = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnSearchBaseDN = False, returnSearchFilter = False, returnSearchPassword = False, returnSearchUserDN = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsernameAttribute = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLDAPProvider(LDAPProviderID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/LDAPProvider/" + str(LDAPProviderID), verb = "delete")


def getEveryMenuSecurityItem(searchConditions = [], EntityID = 1, returnMenuSecurityItemID = False, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MenuSecurityItem in the district.

    This function returns a dataframe of every MenuSecurityItem in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMenuSecurityItem(MenuSecurityItemID, EntityID = 1, returnMenuSecurityItemID = False, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(MenuSecurityItemID), verb = "get", return_params_list = return_params)

def modifyMenuSecurityItem(MenuSecurityItemID, EntityID = 1, setMenuSecurityItemID = None, setCreatedTime = None, setMenuScreenID = None, setModifiedTime = None, setProfileScreenID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuSecurityItemID = False, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(MenuSecurityItemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMenuSecurityItem(EntityID = 1, setMenuSecurityItemID = None, setCreatedTime = None, setMenuScreenID = None, setModifiedTime = None, setProfileScreenID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuSecurityItemID = False, returnCreatedTime = False, returnMenuScreenID = False, returnModifiedTime = False, returnProfileScreenID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMenuSecurityItem(MenuSecurityItemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MenuSecurityItem/" + str(MenuSecurityItemID), verb = "delete")


def getEveryMobileSSO(searchConditions = [], EntityID = 1, returnMobileSSOID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MobileSSO in the district.

    This function returns a dataframe of every MobileSSO in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMobileSSO(MobileSSOID, EntityID = 1, returnMobileSSOID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(MobileSSOID), verb = "get", return_params_list = return_params)

def modifyMobileSSO(MobileSSOID, EntityID = 1, setMobileSSOID = None, setCreatedTime = None, setMobileDevice = None, setModifiedTime = None, setSSOToken = None, setSSOTokenExpirationDate = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMobileSSOID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(MobileSSOID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMobileSSO(EntityID = 1, setMobileSSOID = None, setCreatedTime = None, setMobileDevice = None, setModifiedTime = None, setSSOToken = None, setSSOTokenExpirationDate = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMobileSSOID = False, returnCreatedTime = False, returnMobileDevice = False, returnModifiedTime = False, returnSSOToken = False, returnSSOTokenExpirationDate = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMobileSSO(MobileSSOID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MobileSSO/" + str(MobileSSOID), verb = "delete")


def getEveryMultifactorAuthentication(searchConditions = [], EntityID = 1, returnMultifactorAuthenticationID = False, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MultifactorAuthentication in the district.

    This function returns a dataframe of every MultifactorAuthentication in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMultifactorAuthentication(MultifactorAuthenticationID, EntityID = 1, returnMultifactorAuthenticationID = False, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(MultifactorAuthenticationID), verb = "get", return_params_list = return_params)

def modifyMultifactorAuthentication(MultifactorAuthenticationID, EntityID = 1, setMultifactorAuthenticationID = None, setCode = None, setCreatedTime = None, setDaysToExpiration = None, setDescription = None, setIsRequired = None, setModifiedTime = None, setPriority = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsesEmail = None, setUsesSMS = None, returnMultifactorAuthenticationID = False, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(MultifactorAuthenticationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMultifactorAuthentication(EntityID = 1, setMultifactorAuthenticationID = None, setCode = None, setCreatedTime = None, setDaysToExpiration = None, setDescription = None, setIsRequired = None, setModifiedTime = None, setPriority = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsesEmail = None, setUsesSMS = None, returnMultifactorAuthenticationID = False, returnCode = False, returnCreatedTime = False, returnDaysToExpiration = False, returnDescription = False, returnIsRequired = False, returnModifiedTime = False, returnPriority = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesEmail = False, returnUsesSMS = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMultifactorAuthentication(MultifactorAuthenticationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthentication/" + str(MultifactorAuthenticationID), verb = "delete")


def getEveryMultifactorAuthenticationAssertion(searchConditions = [], EntityID = 1, returnMultifactorAuthenticationAssertionID = False, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MultifactorAuthenticationAssertion in the district.

    This function returns a dataframe of every MultifactorAuthenticationAssertion in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMultifactorAuthenticationAssertion(MultifactorAuthenticationAssertionID, EntityID = 1, returnMultifactorAuthenticationAssertionID = False, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(MultifactorAuthenticationAssertionID), verb = "get", return_params_list = return_params)

def modifyMultifactorAuthenticationAssertion(MultifactorAuthenticationAssertionID, EntityID = 1, setMultifactorAuthenticationAssertionID = None, setAssertionCode = None, setAssertionIdentifier = None, setCreatedTime = None, setExpirationTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMultifactorAuthenticationAssertionID = False, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(MultifactorAuthenticationAssertionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMultifactorAuthenticationAssertion(EntityID = 1, setMultifactorAuthenticationAssertionID = None, setAssertionCode = None, setAssertionIdentifier = None, setCreatedTime = None, setExpirationTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMultifactorAuthenticationAssertionID = False, returnAssertionCode = False, returnAssertionIdentifier = False, returnCreatedTime = False, returnExpirationTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMultifactorAuthenticationAssertion(MultifactorAuthenticationAssertionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/MultifactorAuthenticationAssertion/" + str(MultifactorAuthenticationAssertionID), verb = "delete")


def getEveryProduct(searchConditions = [], EntityID = 1, returnProductID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Product in the district.

    This function returns a dataframe of every Product in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getProduct(ProductID, EntityID = 1, returnProductID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(ProductID), verb = "get", return_params_list = return_params)

def modifyProduct(ProductID, EntityID = 1, setProductID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setRMSID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProductID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(ProductID), verb = "post", return_params_list = return_params, payload = payload_params)

def createProduct(EntityID = 1, setProductID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setRMSID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProductID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnRMSID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteProduct(ProductID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Product/" + str(ProductID), verb = "delete")


def getEveryProductModulePath(searchConditions = [], EntityID = 1, returnProductModulePathID = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ProductModulePath in the district.

    This function returns a dataframe of every ProductModulePath in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getProductModulePath(ProductModulePathID, EntityID = 1, returnProductModulePathID = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(ProductModulePathID), verb = "get", return_params_list = return_params)

def modifyProductModulePath(ProductModulePathID, EntityID = 1, setProductModulePathID = None, setController = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setProductID = None, setScreen = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProductModulePathID = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(ProductModulePathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createProductModulePath(EntityID = 1, setProductModulePathID = None, setController = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setProductID = None, setScreen = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProductModulePathID = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnProductID = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteProductModulePath(ProductModulePathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductModulePath/" + str(ProductModulePathID), verb = "delete")


def getEveryProductOwned(searchConditions = [], EntityID = 1, returnProductOwnedID = False, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ProductOwned in the district.

    This function returns a dataframe of every ProductOwned in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getProductOwned(ProductOwnedID, EntityID = 1, returnProductOwnedID = False, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(ProductOwnedID), verb = "get", return_params_list = return_params)

def modifyProductOwned(ProductOwnedID, EntityID = 1, setProductOwnedID = None, setCreatedTime = None, setEndDate = None, setExpirationDate = None, setModifiedTime = None, setProductID = None, setRMSID = None, setStartDate = None, setStatus = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProductOwnedID = False, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(ProductOwnedID), verb = "post", return_params_list = return_params, payload = payload_params)

def createProductOwned(EntityID = 1, setProductOwnedID = None, setCreatedTime = None, setEndDate = None, setExpirationDate = None, setModifiedTime = None, setProductID = None, setRMSID = None, setStartDate = None, setStatus = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProductOwnedID = False, returnCreatedTime = False, returnEndDate = False, returnExpirationDate = False, returnModifiedTime = False, returnProductID = False, returnRMSID = False, returnStartDate = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteProductOwned(ProductOwnedID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/ProductOwned/" + str(ProductOwnedID), verb = "delete")


def getEveryRole(searchConditions = [], EntityID = 1, returnRoleID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Role in the district.

    This function returns a dataframe of every Role in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRole(RoleID, EntityID = 1, returnRoleID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(RoleID), verb = "get", return_params_list = return_params)

def modifyRole(RoleID, EntityID = 1, setRoleID = None, setAuthenticationRoleID = None, setCreatedTime = None, setDescription = None, setDocumentationPersona = None, setDocumentationPersonaCode = None, setIsActive = None, setModifiedTime = None, setMultifactorAuthenticationID = None, setName = None, setReportCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(RoleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRole(EntityID = 1, setRoleID = None, setAuthenticationRoleID = None, setCreatedTime = None, setDescription = None, setDocumentationPersona = None, setDocumentationPersonaCode = None, setIsActive = None, setModifiedTime = None, setMultifactorAuthenticationID = None, setName = None, setReportCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleID = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnDescription = False, returnDocumentationPersona = False, returnDocumentationPersonaCode = False, returnIsActive = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnName = False, returnReportCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRole(RoleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/Role/" + str(RoleID), verb = "delete")


def getEveryRoleAttachmentType(searchConditions = [], EntityID = 1, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowRead = False, returnAllowUpdate = False, returnAttachmentTypeID = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoleAttachmentType in the district.

    This function returns a dataframe of every RoleAttachmentType in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoleAttachmentType(RoleMenuSecurityItemID, EntityID = 1, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowRead = False, returnAllowUpdate = False, returnAttachmentTypeID = False, returnPortal = False, returnPortalCode = False, returnRoleID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/" + str(RoleMenuSecurityItemID), verb = "get", return_params_list = return_params)

def modifyRoleAttachmentType(RoleMenuSecurityItemID, EntityID = 1, setRoleMenuSecurityItemID = None, setAllowCreate = None, setAllowDelete = None, setAllowRead = None, setAllowUpdate = None, setAttachmentTypeID = None, setPortal = None, setPortalCode = None, setRoleID = None, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowRead = False, returnAllowUpdate = False, returnAttachmentTypeID = False, returnPortal = False, returnPortalCode = False, returnRoleID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/" + str(RoleMenuSecurityItemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoleAttachmentType(EntityID = 1, setRoleMenuSecurityItemID = None, setAllowCreate = None, setAllowDelete = None, setAllowRead = None, setAllowUpdate = None, setAttachmentTypeID = None, setPortal = None, setPortalCode = None, setRoleID = None, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowRead = False, returnAllowUpdate = False, returnAttachmentTypeID = False, returnPortal = False, returnPortalCode = False, returnRoleID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoleAttachmentType(RoleMenuSecurityItemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleAttachmentType/" + str(RoleMenuSecurityItemID), verb = "delete")


def getEveryRoleField(searchConditions = [], EntityID = 1, returnRoleFieldID = False, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoleField in the district.

    This function returns a dataframe of every RoleField in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoleField(RoleFieldID, EntityID = 1, returnRoleFieldID = False, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(RoleFieldID), verb = "get", return_params_list = return_params)

def modifyRoleField(RoleFieldID, EntityID = 1, setRoleFieldID = None, setAllowRead = None, setCreatedTime = None, setField = None, setFullField = None, setModifiedTime = None, setModule = None, setObject = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleFieldID = False, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(RoleFieldID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoleField(EntityID = 1, setRoleFieldID = None, setAllowRead = None, setCreatedTime = None, setField = None, setFullField = None, setModifiedTime = None, setModule = None, setObject = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleFieldID = False, returnAllowRead = False, returnCreatedTime = False, returnField = False, returnFullField = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoleField(RoleFieldID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleField/" + str(RoleFieldID), verb = "delete")


def getEveryRoleIPRange(searchConditions = [], EntityID = 1, returnRoleIPRangeID = False, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoleIPRange in the district.

    This function returns a dataframe of every RoleIPRange in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoleIPRange(RoleIPRangeID, EntityID = 1, returnRoleIPRangeID = False, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(RoleIPRangeID), verb = "get", return_params_list = return_params)

def modifyRoleIPRange(RoleIPRangeID, EntityID = 1, setRoleIPRangeID = None, setCreatedTime = None, setIPRangeID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleIPRangeID = False, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(RoleIPRangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoleIPRange(EntityID = 1, setRoleIPRangeID = None, setCreatedTime = None, setIPRangeID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleIPRangeID = False, returnCreatedTime = False, returnIPRangeID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoleIPRange(RoleIPRangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleIPRange/" + str(RoleIPRangeID), verb = "delete")


def getEveryRoleMenuSecurityItem(searchConditions = [], EntityID = 1, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoleMenuSecurityItem in the district.

    This function returns a dataframe of every RoleMenuSecurityItem in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoleMenuSecurityItem(RoleMenuSecurityItemID, EntityID = 1, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(RoleMenuSecurityItemID), verb = "get", return_params_list = return_params)

def modifyRoleMenuSecurityItem(RoleMenuSecurityItemID, EntityID = 1, setRoleMenuSecurityItemID = None, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setCreatedTime = None, setMenuSecurityItemID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(RoleMenuSecurityItemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoleMenuSecurityItem(EntityID = 1, setRoleMenuSecurityItemID = None, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setCreatedTime = None, setMenuSecurityItemID = None, setModifiedTime = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleMenuSecurityItemID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoleMenuSecurityItem(RoleMenuSecurityItemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleMenuSecurityItem/" + str(RoleMenuSecurityItemID), verb = "delete")


def getEveryRoleModulePath(searchConditions = [], EntityID = 1, returnRoleModulePathID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoleModulePath in the district.

    This function returns a dataframe of every RoleModulePath in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoleModulePath(RoleModulePathID, EntityID = 1, returnRoleModulePathID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(RoleModulePathID), verb = "get", return_params_list = return_params)

def modifyRoleModulePath(RoleModulePathID, EntityID = 1, setRoleModulePathID = None, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setCreatedTime = None, setModifiedTime = None, setModulePath = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleModulePathID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(RoleModulePathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoleModulePath(EntityID = 1, setRoleModulePathID = None, setAllowCreate = None, setAllowDelete = None, setAllowMassCreate = None, setAllowMassDelete = None, setAllowMassUpdate = None, setAllowRead = None, setAllowUpdate = None, setCreatedTime = None, setModifiedTime = None, setModulePath = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoleModulePathID = False, returnAllowCreate = False, returnAllowDelete = False, returnAllowMassCreate = False, returnAllowMassDelete = False, returnAllowMassUpdate = False, returnAllowRead = False, returnAllowUpdate = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePath = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoleModulePath(RoleModulePathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RoleModulePath/" + str(RoleModulePathID), verb = "delete")


def getEveryRolePortal(searchConditions = [], EntityID = 1, returnRolePortalID = False, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RolePortal in the district.

    This function returns a dataframe of every RolePortal in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRolePortal(RolePortalID, EntityID = 1, returnRolePortalID = False, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(RolePortalID), verb = "get", return_params_list = return_params)

def modifyRolePortal(RolePortalID, EntityID = 1, setRolePortalID = None, setCreatedTime = None, setModifiedTime = None, setPortal = None, setPortalCode = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRolePortalID = False, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(RolePortalID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRolePortal(EntityID = 1, setRolePortalID = None, setCreatedTime = None, setModifiedTime = None, setPortal = None, setPortalCode = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRolePortalID = False, returnCreatedTime = False, returnModifiedTime = False, returnPortal = False, returnPortalCode = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRolePortal(RolePortalID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/RolePortal/" + str(RolePortalID), verb = "delete")


def getEverySecurityLocation(searchConditions = [], EntityID = 1, returnSecurityLocationID = False, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SecurityLocation in the district.

    This function returns a dataframe of every SecurityLocation in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSecurityLocation(SecurityLocationID, EntityID = 1, returnSecurityLocationID = False, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(SecurityLocationID), verb = "get", return_params_list = return_params)

def modifySecurityLocation(SecurityLocationID, EntityID = 1, setSecurityLocationID = None, setAttachmentTypeGUID = None, setCanAllowCreate = None, setCanAllowDelete = None, setCanAllowMassCreate = None, setCanAllowMassDelete = None, setCanAllowMassUpdate = None, setCanAllowRead = None, setCanAllowUpdate = None, setCreatedTime = None, setMobileCanAllowCreate = None, setMobileCanAllowDelete = None, setMobileCanAllowMassCreate = None, setMobileCanAllowMassDelete = None, setMobileCanAllowMassUpdate = None, setMobileCanAllowRead = None, setMobileCanAllowUpdate = None, setModifiedTime = None, setModulePathID = None, setPath = None, setPortal = None, setPortalCode = None, setReportID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowID = None, returnSecurityLocationID = False, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(SecurityLocationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSecurityLocation(EntityID = 1, setSecurityLocationID = None, setAttachmentTypeGUID = None, setCanAllowCreate = None, setCanAllowDelete = None, setCanAllowMassCreate = None, setCanAllowMassDelete = None, setCanAllowMassUpdate = None, setCanAllowRead = None, setCanAllowUpdate = None, setCreatedTime = None, setMobileCanAllowCreate = None, setMobileCanAllowDelete = None, setMobileCanAllowMassCreate = None, setMobileCanAllowMassDelete = None, setMobileCanAllowMassUpdate = None, setMobileCanAllowRead = None, setMobileCanAllowUpdate = None, setModifiedTime = None, setModulePathID = None, setPath = None, setPortal = None, setPortalCode = None, setReportID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowID = None, returnSecurityLocationID = False, returnAttachmentTypeGUID = False, returnCanAllowCreate = False, returnCanAllowDelete = False, returnCanAllowMassCreate = False, returnCanAllowMassDelete = False, returnCanAllowMassUpdate = False, returnCanAllowRead = False, returnCanAllowUpdate = False, returnCreatedTime = False, returnMobileCanAllowCreate = False, returnMobileCanAllowDelete = False, returnMobileCanAllowMassCreate = False, returnMobileCanAllowMassDelete = False, returnMobileCanAllowMassUpdate = False, returnMobileCanAllowRead = False, returnMobileCanAllowUpdate = False, returnModifiedTime = False, returnModulePathID = False, returnPath = False, returnPortal = False, returnPortalCode = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSecurityLocation(SecurityLocationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocation/" + str(SecurityLocationID), verb = "delete")


def getEverySecurityLocationMenuSecurityItem(searchConditions = [], EntityID = 1, returnSecurityLocationMenuSecurityItemID = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SecurityLocationMenuSecurityItem in the district.

    This function returns a dataframe of every SecurityLocationMenuSecurityItem in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSecurityLocationMenuSecurityItem(SecurityLocationMenuSecurityItemID, EntityID = 1, returnSecurityLocationMenuSecurityItemID = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(SecurityLocationMenuSecurityItemID), verb = "get", return_params_list = return_params)

def modifySecurityLocationMenuSecurityItem(SecurityLocationMenuSecurityItemID, EntityID = 1, setSecurityLocationMenuSecurityItemID = None, setCreatedTime = None, setMenuSecurityItemID = None, setModifiedTime = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSecurityLocationMenuSecurityItemID = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(SecurityLocationMenuSecurityItemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSecurityLocationMenuSecurityItem(EntityID = 1, setSecurityLocationMenuSecurityItemID = None, setCreatedTime = None, setMenuSecurityItemID = None, setModifiedTime = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSecurityLocationMenuSecurityItemID = False, returnCreatedTime = False, returnMenuSecurityItemID = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSecurityLocationMenuSecurityItem(SecurityLocationMenuSecurityItemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SecurityLocationMenuSecurityItem/" + str(SecurityLocationMenuSecurityItemID), verb = "delete")


def getEverySessionFileUpload(searchConditions = [], EntityID = 1, returnSessionFileUploadID = False, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileExtension = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SessionFileUpload in the district.

    This function returns a dataframe of every SessionFileUpload in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSessionFileUpload(SessionFileUploadID, EntityID = 1, returnSessionFileUploadID = False, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileExtension = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(SessionFileUploadID), verb = "get", return_params_list = return_params)

def modifySessionFileUpload(SessionFileUploadID, EntityID = 1, setSessionFileUploadID = None, setBytes = None, setCreatedTime = None, setFileContents = None, setFileExtension = None, setFileName = None, setFilePath = None, setMetaData = None, setMetaDataXml = None, setModifiedTime = None, setSessionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXDimension = None, setYDimension = None, returnSessionFileUploadID = False, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileExtension = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(SessionFileUploadID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSessionFileUpload(EntityID = 1, setSessionFileUploadID = None, setBytes = None, setCreatedTime = None, setFileContents = None, setFileExtension = None, setFileName = None, setFilePath = None, setMetaData = None, setMetaDataXml = None, setModifiedTime = None, setSessionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXDimension = None, setYDimension = None, returnSessionFileUploadID = False, returnBytes = False, returnCreatedTime = False, returnFileContents = False, returnFileExtension = False, returnFileName = False, returnFilePath = False, returnMetaData = False, returnMetaDataXml = False, returnModifiedTime = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSessionFileUpload(SessionFileUploadID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SessionFileUpload/" + str(SessionFileUploadID), verb = "delete")


def getEverySkywardSupportAccess(searchConditions = [], EntityID = 1, returnSkywardSupportAccessID = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SkywardSupportAccess in the district.

    This function returns a dataframe of every SkywardSupportAccess in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSkywardSupportAccess(SkywardSupportAccessID, EntityID = 1, returnSkywardSupportAccessID = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(SkywardSupportAccessID), verb = "get", return_params_list = return_params)

def modifySkywardSupportAccess(SkywardSupportAccessID, EntityID = 1, setSkywardSupportAccessID = None, setCreatedTime = None, setEndDate = None, setIsActive = None, setModifiedTime = None, setNotes = None, setServiceCallNumber = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkywardSupportAccessID = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(SkywardSupportAccessID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSkywardSupportAccess(EntityID = 1, setSkywardSupportAccessID = None, setCreatedTime = None, setEndDate = None, setIsActive = None, setModifiedTime = None, setNotes = None, setServiceCallNumber = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkywardSupportAccessID = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNotes = False, returnServiceCallNumber = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSkywardSupportAccess(SkywardSupportAccessID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccess/" + str(SkywardSupportAccessID), verb = "delete")


def getEverySkywardSupportAccessLoginHistory(searchConditions = [], EntityID = 1, returnSkywardSupportAccessLoginHistoryID = False, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SkywardSupportAccessLoginHistory in the district.

    This function returns a dataframe of every SkywardSupportAccessLoginHistory in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSkywardSupportAccessLoginHistory(SkywardSupportAccessLoginHistoryID, EntityID = 1, returnSkywardSupportAccessLoginHistoryID = False, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(SkywardSupportAccessLoginHistoryID), verb = "get", return_params_list = return_params)

def modifySkywardSupportAccessLoginHistory(SkywardSupportAccessLoginHistoryID, EntityID = 1, setSkywardSupportAccessLoginHistoryID = None, setAccessedTime = None, setCreatedTime = None, setModifiedTime = None, setSessionID = None, setSkywardEmployeeName = None, setSkywardSupportAccessID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkywardSupportAccessLoginHistoryID = False, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(SkywardSupportAccessLoginHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSkywardSupportAccessLoginHistory(EntityID = 1, setSkywardSupportAccessLoginHistoryID = None, setAccessedTime = None, setCreatedTime = None, setModifiedTime = None, setSessionID = None, setSkywardEmployeeName = None, setSkywardSupportAccessID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkywardSupportAccessLoginHistoryID = False, returnAccessedTime = False, returnCreatedTime = False, returnModifiedTime = False, returnSessionID = False, returnSkywardEmployeeName = False, returnSkywardSupportAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSkywardSupportAccessLoginHistory(SkywardSupportAccessLoginHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/SkywardSupportAccessLoginHistory/" + str(SkywardSupportAccessLoginHistoryID), verb = "delete")


def getEveryTempDeletedPortalAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempDeletedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempDeletedPortalAccessSecurityUser in the district.

    This function returns a dataframe of every TempDeletedPortalAccessSecurityUser in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempDeletedPortalAccessSecurityUser(TempDeletedPortalAccessSecurityUserID, EntityID = 1, returnTempDeletedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(TempDeletedPortalAccessSecurityUserID), verb = "get", return_params_list = return_params)

def modifyTempDeletedPortalAccessSecurityUser(TempDeletedPortalAccessSecurityUserID, EntityID = 1, setTempDeletedPortalAccessSecurityUserID = None, setCreatedTime = None, setFullNameLFM = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempDeletedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(TempDeletedPortalAccessSecurityUserID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempDeletedPortalAccessSecurityUser(EntityID = 1, setTempDeletedPortalAccessSecurityUserID = None, setCreatedTime = None, setFullNameLFM = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempDeletedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempDeletedPortalAccessSecurityUser(TempDeletedPortalAccessSecurityUserID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempDeletedPortalAccessSecurityUser/" + str(TempDeletedPortalAccessSecurityUserID), verb = "delete")


def getEveryTempEmployeeAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempEmployeeAccessSecurityUserID = False, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempEmployeeAccessSecurityUser in the district.

    This function returns a dataframe of every TempEmployeeAccessSecurityUser in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempEmployeeAccessSecurityUser(TempEmployeeAccessSecurityUserID, EntityID = 1, returnTempEmployeeAccessSecurityUserID = False, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(TempEmployeeAccessSecurityUserID), verb = "get", return_params_list = return_params)

def modifyTempEmployeeAccessSecurityUser(TempEmployeeAccessSecurityUserID, EntityID = 1, setTempEmployeeAccessSecurityUserID = None, setAddToEmployeeAccess = None, setAllowEmployeeAccess = None, setCreatedTime = None, setEmailAddress = None, setEmployeeID = None, setEmployeeNameLFM = None, setEmployeeNumber = None, setForUserCreation = None, setGroup = None, setIsAuditEmployeeAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setRemoveFromEmployeeAccess = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempEmployeeAccessSecurityUserID = False, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(TempEmployeeAccessSecurityUserID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempEmployeeAccessSecurityUser(EntityID = 1, setTempEmployeeAccessSecurityUserID = None, setAddToEmployeeAccess = None, setAllowEmployeeAccess = None, setCreatedTime = None, setEmailAddress = None, setEmployeeID = None, setEmployeeNameLFM = None, setEmployeeNumber = None, setForUserCreation = None, setGroup = None, setIsAuditEmployeeAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setRemoveFromEmployeeAccess = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempEmployeeAccessSecurityUserID = False, returnAddToEmployeeAccess = False, returnAllowEmployeeAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEmployeeID = False, returnEmployeeNameLFM = False, returnEmployeeNumber = False, returnForUserCreation = False, returnGroup = False, returnIsAuditEmployeeAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromEmployeeAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempEmployeeAccessSecurityUser(TempEmployeeAccessSecurityUserID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEmployeeAccessSecurityUser/" + str(TempEmployeeAccessSecurityUserID), verb = "delete")


def getEveryTempEntityForClone(searchConditions = [], EntityID = 1, returnTempEntityForCloneID = False, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempEntityForClone in the district.

    This function returns a dataframe of every TempEntityForClone in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempEntityForClone(TempEntityForCloneID, EntityID = 1, returnTempEntityForCloneID = False, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(TempEntityForCloneID), verb = "get", return_params_list = return_params)

def modifyTempEntityForClone(TempEntityForCloneID, EntityID = 1, setTempEntityForCloneID = None, setCreatedTime = None, setEntityCode = None, setEntityName = None, setEntityPrimaryKey = None, setModifiedTime = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEntityForCloneID = False, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(TempEntityForCloneID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempEntityForClone(EntityID = 1, setTempEntityForCloneID = None, setCreatedTime = None, setEntityCode = None, setEntityName = None, setEntityPrimaryKey = None, setModifiedTime = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEntityForCloneID = False, returnCreatedTime = False, returnEntityCode = False, returnEntityName = False, returnEntityPrimaryKey = False, returnModifiedTime = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempEntityForClone(TempEntityForCloneID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempEntityForClone/" + str(TempEntityForCloneID), verb = "delete")


def getEveryTempFailedPortalAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempFailedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFailedPortalAccessSecurityUser in the district.

    This function returns a dataframe of every TempFailedPortalAccessSecurityUser in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFailedPortalAccessSecurityUser(TempFailedPortalAccessSecurityUserID, EntityID = 1, returnTempFailedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(TempFailedPortalAccessSecurityUserID), verb = "get", return_params_list = return_params)

def modifyTempFailedPortalAccessSecurityUser(TempFailedPortalAccessSecurityUserID, EntityID = 1, setTempFailedPortalAccessSecurityUserID = None, setCreatedTime = None, setFullNameLFM = None, setModifiedTime = None, setNote = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempFailedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(TempFailedPortalAccessSecurityUserID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFailedPortalAccessSecurityUser(EntityID = 1, setTempFailedPortalAccessSecurityUserID = None, setCreatedTime = None, setFullNameLFM = None, setModifiedTime = None, setNote = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempFailedPortalAccessSecurityUserID = False, returnCreatedTime = False, returnFullNameLFM = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFailedPortalAccessSecurityUser(TempFailedPortalAccessSecurityUserID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFailedPortalAccessSecurityUser/" + str(TempFailedPortalAccessSecurityUserID), verb = "delete")


def getEveryTempFamilyAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempFamilyAccessSecurityUserID = False, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFamilyAccessSecurityUser in the district.

    This function returns a dataframe of every TempFamilyAccessSecurityUser in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFamilyAccessSecurityUser(TempFamilyAccessSecurityUserID, EntityID = 1, returnTempFamilyAccessSecurityUserID = False, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(TempFamilyAccessSecurityUserID), verb = "get", return_params_list = return_params)

def modifyTempFamilyAccessSecurityUser(TempFamilyAccessSecurityUserID, EntityID = 1, setTempFamilyAccessSecurityUserID = None, setAddToFamilyAccess = None, setCreatedTime = None, setEmailAddress = None, setEntityCodeName = None, setForUserCreation = None, setGuardianNameLFM = None, setIsAuditFamilyAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setRemoveFromFamilyAccess = None, setStudentGuardianID = None, setStudentNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempFamilyAccessSecurityUserID = False, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(TempFamilyAccessSecurityUserID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFamilyAccessSecurityUser(EntityID = 1, setTempFamilyAccessSecurityUserID = None, setAddToFamilyAccess = None, setCreatedTime = None, setEmailAddress = None, setEntityCodeName = None, setForUserCreation = None, setGuardianNameLFM = None, setIsAuditFamilyAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setRemoveFromFamilyAccess = None, setStudentGuardianID = None, setStudentNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempFamilyAccessSecurityUserID = False, returnAddToFamilyAccess = False, returnCreatedTime = False, returnEmailAddress = False, returnEntityCodeName = False, returnForUserCreation = False, returnGuardianNameLFM = False, returnIsAuditFamilyAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromFamilyAccess = False, returnStudentGuardianID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFamilyAccessSecurityUser(TempFamilyAccessSecurityUserID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFamilyAccessSecurityUser/" + str(TempFamilyAccessSecurityUserID), verb = "delete")


def getEveryTempFieldRestrictionScreen(searchConditions = [], EntityID = 1, returnTempFieldRestrictionScreenID = False, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFieldRestrictionScreen in the district.

    This function returns a dataframe of every TempFieldRestrictionScreen in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFieldRestrictionScreen(TempFieldRestrictionScreenID, EntityID = 1, returnTempFieldRestrictionScreenID = False, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(TempFieldRestrictionScreenID), verb = "get", return_params_list = return_params)

def modifyTempFieldRestrictionScreen(TempFieldRestrictionScreenID, EntityID = 1, setTempFieldRestrictionScreenID = None, setCreatedTime = None, setDisplayText = None, setModifiedTime = None, setSecurityLocationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFieldRestrictionScreenID = False, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(TempFieldRestrictionScreenID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFieldRestrictionScreen(EntityID = 1, setTempFieldRestrictionScreenID = None, setCreatedTime = None, setDisplayText = None, setModifiedTime = None, setSecurityLocationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFieldRestrictionScreenID = False, returnCreatedTime = False, returnDisplayText = False, returnModifiedTime = False, returnSecurityLocationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFieldRestrictionScreen(TempFieldRestrictionScreenID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempFieldRestrictionScreen/" + str(TempFieldRestrictionScreenID), verb = "delete")


def getEveryTempImpersonationRoleForClone(searchConditions = [], EntityID = 1, returnTempImpersonationRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempImpersonationRoleForClone in the district.

    This function returns a dataframe of every TempImpersonationRoleForClone in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempImpersonationRoleForClone(TempImpersonationRoleForCloneID, EntityID = 1, returnTempImpersonationRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(TempImpersonationRoleForCloneID), verb = "get", return_params_list = return_params)

def modifyTempImpersonationRoleForClone(TempImpersonationRoleForCloneID, EntityID = 1, setTempImpersonationRoleForCloneID = None, setCreatedTime = None, setDescription = None, setIsReadOnly = None, setModifiedTime = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempImpersonationRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(TempImpersonationRoleForCloneID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempImpersonationRoleForClone(EntityID = 1, setTempImpersonationRoleForCloneID = None, setCreatedTime = None, setDescription = None, setIsReadOnly = None, setModifiedTime = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempImpersonationRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnIsReadOnly = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempImpersonationRoleForClone(TempImpersonationRoleForCloneID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempImpersonationRoleForClone/" + str(TempImpersonationRoleForCloneID), verb = "delete")


def getEveryTempRoleForClone(searchConditions = [], EntityID = 1, returnTempRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempRoleForClone in the district.

    This function returns a dataframe of every TempRoleForClone in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempRoleForClone(TempRoleForCloneID, EntityID = 1, returnTempRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(TempRoleForCloneID), verb = "get", return_params_list = return_params)

def modifyTempRoleForClone(TempRoleForCloneID, EntityID = 1, setTempRoleForCloneID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(TempRoleForCloneID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempRoleForClone(EntityID = 1, setTempRoleForCloneID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRoleName = None, setRolePrimaryKey = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempRoleForCloneID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoleName = False, returnRolePrimaryKey = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempRoleForClone(TempRoleForCloneID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempRoleForClone/" + str(TempRoleForCloneID), verb = "delete")


def getEveryTempSecurityImportError(searchConditions = [], EntityID = 1, returnTempSecurityImportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempSecurityImportError in the district.

    This function returns a dataframe of every TempSecurityImportError in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempSecurityImportError(TempSecurityImportErrorID, EntityID = 1, returnTempSecurityImportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(TempSecurityImportErrorID), verb = "get", return_params_list = return_params)

def modifyTempSecurityImportError(TempSecurityImportErrorID, EntityID = 1, setTempSecurityImportErrorID = None, setCreatedTime = None, setErrorMessage = None, setErrorObject = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSecurityImportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(TempSecurityImportErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSecurityImportError(EntityID = 1, setTempSecurityImportErrorID = None, setCreatedTime = None, setErrorMessage = None, setErrorObject = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSecurityImportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnErrorObject = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSecurityImportError(TempSecurityImportErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportError/" + str(TempSecurityImportErrorID), verb = "delete")


def getEveryTempSecurityImportGroupMembership(searchConditions = [], EntityID = 1, returnTempSecurityImportGroupMembershipID = False, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempSecurityImportGroupMembership in the district.

    This function returns a dataframe of every TempSecurityImportGroupMembership in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempSecurityImportGroupMembership(TempSecurityImportGroupMembershipID, EntityID = 1, returnTempSecurityImportGroupMembershipID = False, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(TempSecurityImportGroupMembershipID), verb = "get", return_params_list = return_params)

def modifyTempSecurityImportGroupMembership(TempSecurityImportGroupMembershipID, EntityID = 1, setTempSecurityImportGroupMembershipID = None, setCreatedTime = None, setEntityName = None, setExistingUserID = None, setExternalUniqueIdentifier = None, setGroupName = None, setImportExternalUniqueIdentifier = None, setImportUserNameBirthDate = None, setImportUserNameFullNameLegalLFM = None, setImportUserNameFullNameLFM = None, setImportUserNamePrimaryEmailAddress = None, setMatches = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserNameBirthDate = None, setUserNameFullNameLegalLFM = None, setUserNameFullNameLFM = None, setUserNamePrimaryEmailAddress = None, setUserUsername = None, returnTempSecurityImportGroupMembershipID = False, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(TempSecurityImportGroupMembershipID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSecurityImportGroupMembership(EntityID = 1, setTempSecurityImportGroupMembershipID = None, setCreatedTime = None, setEntityName = None, setExistingUserID = None, setExternalUniqueIdentifier = None, setGroupName = None, setImportExternalUniqueIdentifier = None, setImportUserNameBirthDate = None, setImportUserNameFullNameLegalLFM = None, setImportUserNameFullNameLFM = None, setImportUserNamePrimaryEmailAddress = None, setMatches = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserNameBirthDate = None, setUserNameFullNameLegalLFM = None, setUserNameFullNameLFM = None, setUserNamePrimaryEmailAddress = None, setUserUsername = None, returnTempSecurityImportGroupMembershipID = False, returnCreatedTime = False, returnEntityName = False, returnExistingUserID = False, returnExternalUniqueIdentifier = False, returnGroupName = False, returnImportExternalUniqueIdentifier = False, returnImportUserNameBirthDate = False, returnImportUserNameFullNameLegalLFM = False, returnImportUserNameFullNameLFM = False, returnImportUserNamePrimaryEmailAddress = False, returnMatches = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserNameBirthDate = False, returnUserNameFullNameLegalLFM = False, returnUserNameFullNameLFM = False, returnUserNamePrimaryEmailAddress = False, returnUserUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSecurityImportGroupMembership(TempSecurityImportGroupMembershipID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportGroupMembership/" + str(TempSecurityImportGroupMembershipID), verb = "delete")


def getEveryTempSecurityImportPreview(searchConditions = [], EntityID = 1, returnTempSecurityImportPreviewID = False, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempSecurityImportPreview in the district.

    This function returns a dataframe of every TempSecurityImportPreview in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempSecurityImportPreview(TempSecurityImportPreviewID, EntityID = 1, returnTempSecurityImportPreviewID = False, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(TempSecurityImportPreviewID), verb = "get", return_params_list = return_params)

def modifyTempSecurityImportPreview(TempSecurityImportPreviewID, EntityID = 1, setTempSecurityImportPreviewID = None, setCreatedTime = None, setIdentifier = None, setModifiedTime = None, setObject = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSecurityImportPreviewID = False, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(TempSecurityImportPreviewID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSecurityImportPreview(EntityID = 1, setTempSecurityImportPreviewID = None, setCreatedTime = None, setIdentifier = None, setModifiedTime = None, setObject = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSecurityImportPreviewID = False, returnCreatedTime = False, returnIdentifier = False, returnModifiedTime = False, returnObject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSecurityImportPreview(TempSecurityImportPreviewID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSecurityImportPreview/" + str(TempSecurityImportPreviewID), verb = "delete")


def getEveryTempSpecialtyAccessGroup(searchConditions = [], EntityID = 1, returnTempSpecialtyAccessGroupID = False, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempSpecialtyAccessGroup in the district.

    This function returns a dataframe of every TempSpecialtyAccessGroup in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempSpecialtyAccessGroup(TempSpecialtyAccessGroupID, EntityID = 1, returnTempSpecialtyAccessGroupID = False, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(TempSpecialtyAccessGroupID), verb = "get", return_params_list = return_params)

def modifyTempSpecialtyAccessGroup(TempSpecialtyAccessGroupID, EntityID = 1, setTempSpecialtyAccessGroupID = None, setCreatedTime = None, setGroupName = None, setIdentifier = None, setModifiedTime = None, setSelected = None, setSpecialtyAccessGroupPrimaryKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSpecialtyAccessGroupID = False, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(TempSpecialtyAccessGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSpecialtyAccessGroup(EntityID = 1, setTempSpecialtyAccessGroupID = None, setCreatedTime = None, setGroupName = None, setIdentifier = None, setModifiedTime = None, setSelected = None, setSpecialtyAccessGroupPrimaryKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSpecialtyAccessGroupID = False, returnCreatedTime = False, returnGroupName = False, returnIdentifier = False, returnModifiedTime = False, returnSelected = False, returnSpecialtyAccessGroupPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSpecialtyAccessGroup(TempSpecialtyAccessGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempSpecialtyAccessGroup/" + str(TempSpecialtyAccessGroupID), verb = "delete")


def getEveryTempStudentAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempStudentAccessSecurityUserID = False, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentAccessSecurityUser in the district.

    This function returns a dataframe of every TempStudentAccessSecurityUser in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentAccessSecurityUser(TempStudentAccessSecurityUserID, EntityID = 1, returnTempStudentAccessSecurityUserID = False, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(TempStudentAccessSecurityUserID), verb = "get", return_params_list = return_params)

def modifyTempStudentAccessSecurityUser(TempStudentAccessSecurityUserID, EntityID = 1, setTempStudentAccessSecurityUserID = None, setAddToStudentAccess = None, setCreatedTime = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditStudentAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setRemoveFromStudentAccess = None, setStudentID = None, setStudentNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempStudentAccessSecurityUserID = False, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(TempStudentAccessSecurityUserID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentAccessSecurityUser(EntityID = 1, setTempStudentAccessSecurityUserID = None, setAddToStudentAccess = None, setCreatedTime = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditStudentAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setRemoveFromStudentAccess = None, setStudentID = None, setStudentNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempStudentAccessSecurityUserID = False, returnAddToStudentAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditStudentAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnRemoveFromStudentAccess = False, returnStudentID = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentAccessSecurityUser(TempStudentAccessSecurityUserID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempStudentAccessSecurityUser/" + str(TempStudentAccessSecurityUserID), verb = "delete")


def getEveryTempTeacherAccessSecurityUser(searchConditions = [], EntityID = 1, returnTempTeacherAccessSecurityUserID = False, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempTeacherAccessSecurityUser in the district.

    This function returns a dataframe of every TempTeacherAccessSecurityUser in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempTeacherAccessSecurityUser(TempTeacherAccessSecurityUserID, EntityID = 1, returnTempTeacherAccessSecurityUserID = False, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(TempTeacherAccessSecurityUserID), verb = "get", return_params_list = return_params)

def modifyTempTeacherAccessSecurityUser(TempTeacherAccessSecurityUserID, EntityID = 1, setTempTeacherAccessSecurityUserID = None, setAddToTeacherAccess = None, setAllowTeacherAccess = None, setCreatedTime = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditTeacherAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setNote = None, setRemoveFromTeacherAccess = None, setStaffID = None, setStaffNameLFM = None, setStaffNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempTeacherAccessSecurityUserID = False, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(TempTeacherAccessSecurityUserID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempTeacherAccessSecurityUser(EntityID = 1, setTempTeacherAccessSecurityUserID = None, setAddToTeacherAccess = None, setAllowTeacherAccess = None, setCreatedTime = None, setDeleteUserAfterAudit = None, setEmailAddress = None, setForUserCreation = None, setGroup = None, setIsAuditTeacherAccessSecurity = None, setIsException = None, setIsSelected = None, setModifiedTime = None, setNote = None, setRemoveFromTeacherAccess = None, setStaffID = None, setStaffNameLFM = None, setStaffNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempTeacherAccessSecurityUserID = False, returnAddToTeacherAccess = False, returnAllowTeacherAccess = False, returnCreatedTime = False, returnDeleteUserAfterAudit = False, returnEmailAddress = False, returnForUserCreation = False, returnGroup = False, returnIsAuditTeacherAccessSecurity = False, returnIsException = False, returnIsSelected = False, returnModifiedTime = False, returnNote = False, returnRemoveFromTeacherAccess = False, returnStaffID = False, returnStaffNameLFM = False, returnStaffNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempTeacherAccessSecurityUser(TempTeacherAccessSecurityUserID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TempTeacherAccessSecurityUser/" + str(TempTeacherAccessSecurityUserID), verb = "delete")


def getEveryTrustedDevice(searchConditions = [], EntityID = 1, returnTrustedDeviceID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TrustedDevice in the district.

    This function returns a dataframe of every TrustedDevice in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTrustedDevice(TrustedDeviceID, EntityID = 1, returnTrustedDeviceID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(TrustedDeviceID), verb = "get", return_params_list = return_params)

def modifyTrustedDevice(TrustedDeviceID, EntityID = 1, setTrustedDeviceID = None, setBrowserType = None, setBrowserVersion = None, setCreatedTime = None, setDeviceType = None, setHostAddress = None, setIdentifier = None, setModifiedTime = None, setOperatingSystemType = None, setUserAgent = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTrustedDeviceID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(TrustedDeviceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTrustedDevice(EntityID = 1, setTrustedDeviceID = None, setBrowserType = None, setBrowserVersion = None, setCreatedTime = None, setDeviceType = None, setHostAddress = None, setIdentifier = None, setModifiedTime = None, setOperatingSystemType = None, setUserAgent = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTrustedDeviceID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnHostAddress = False, returnIdentifier = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTrustedDevice(TrustedDeviceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/TrustedDevice/" + str(TrustedDeviceID), verb = "delete")


def getEveryUserAuthenticationMethod(searchConditions = [], EntityID = 1, returnUserAuthenticationMethodID = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserAuthenticationMethod in the district.

    This function returns a dataframe of every UserAuthenticationMethod in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserAuthenticationMethod(UserAuthenticationMethodID, EntityID = 1, returnUserAuthenticationMethodID = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(UserAuthenticationMethodID), verb = "get", return_params_list = return_params)

def modifyUserAuthenticationMethod(UserAuthenticationMethodID, EntityID = 1, setUserAuthenticationMethodID = None, setAuthenticationMethodID = None, setCreatedTime = None, setModifiedTime = None, setProviderUserIdentity = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserAuthenticationMethodID = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(UserAuthenticationMethodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserAuthenticationMethod(EntityID = 1, setUserAuthenticationMethodID = None, setAuthenticationMethodID = None, setCreatedTime = None, setModifiedTime = None, setProviderUserIdentity = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserAuthenticationMethodID = False, returnAuthenticationMethodID = False, returnCreatedTime = False, returnModifiedTime = False, returnProviderUserIdentity = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserAuthenticationMethod(UserAuthenticationMethodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserAuthenticationMethod/" + str(UserAuthenticationMethodID), verb = "delete")


def getEveryUserCalendarPreference(searchConditions = [], EntityID = 1, returnUserCalendarPreferenceID = False, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserCalendarPreference in the district.

    This function returns a dataframe of every UserCalendarPreference in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserCalendarPreference(UserCalendarPreferenceID, EntityID = 1, returnUserCalendarPreferenceID = False, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(UserCalendarPreferenceID), verb = "get", return_params_list = return_params)

def modifyUserCalendarPreference(UserCalendarPreferenceID, EntityID = 1, setUserCalendarPreferenceID = None, setApprovedTimeOffEventBackgroundColor = None, setBirthdayEventBackgroundColor = None, setCalendarEventBackgroundColor = None, setCalendarType = None, setCalendarTypeCode = None, setCreatedTime = None, setDistrictActivityEventBackgroundColor = None, setModifiedTime = None, setPayDayEventBackgroundColor = None, setSelectedView = None, setShowAllMyEmployeesTimeOff = None, setShowAllocatedTimeOff = None, setShowBirthdays = None, setShowCalendarEvents = None, setShowDistrictActivityEvents = None, setShowMyDirectEmployeesTimeOff = None, setShowMyTimeOff = None, setShowTransactionsIHadASubFor = None, setShowTransactionsISubbedFor = None, setShowWeekends = None, setTransactionsIHadASubForEventBackgroundColor = None, setTransactionsISubbedForEventBackgroundColor = None, setUnapprovedTimeOffEventBackgroundColor = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnUserCalendarPreferenceID = False, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(UserCalendarPreferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserCalendarPreference(EntityID = 1, setUserCalendarPreferenceID = None, setApprovedTimeOffEventBackgroundColor = None, setBirthdayEventBackgroundColor = None, setCalendarEventBackgroundColor = None, setCalendarType = None, setCalendarTypeCode = None, setCreatedTime = None, setDistrictActivityEventBackgroundColor = None, setModifiedTime = None, setPayDayEventBackgroundColor = None, setSelectedView = None, setShowAllMyEmployeesTimeOff = None, setShowAllocatedTimeOff = None, setShowBirthdays = None, setShowCalendarEvents = None, setShowDistrictActivityEvents = None, setShowMyDirectEmployeesTimeOff = None, setShowMyTimeOff = None, setShowTransactionsIHadASubFor = None, setShowTransactionsISubbedFor = None, setShowWeekends = None, setTransactionsIHadASubForEventBackgroundColor = None, setTransactionsISubbedForEventBackgroundColor = None, setUnapprovedTimeOffEventBackgroundColor = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnUserCalendarPreferenceID = False, returnApprovedTimeOffEventBackgroundColor = False, returnBirthdayEventBackgroundColor = False, returnCalendarEventBackgroundColor = False, returnCalendarType = False, returnCalendarTypeCode = False, returnCreatedTime = False, returnDistrictActivityEventBackgroundColor = False, returnModifiedTime = False, returnPayDayEventBackgroundColor = False, returnSelectedView = False, returnShowAllMyEmployeesTimeOff = False, returnShowAllocatedTimeOff = False, returnShowBirthdays = False, returnShowCalendarEvents = False, returnShowDistrictActivityEvents = False, returnShowMyDirectEmployeesTimeOff = False, returnShowMyTimeOff = False, returnShowTransactionsIHadASubFor = False, returnShowTransactionsISubbedFor = False, returnShowWeekends = False, returnTransactionsIHadASubForEventBackgroundColor = False, returnTransactionsISubbedForEventBackgroundColor = False, returnUnapprovedTimeOffEventBackgroundColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserCalendarPreference(UserCalendarPreferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserCalendarPreference/" + str(UserCalendarPreferenceID), verb = "delete")


def getEveryUserImport(searchConditions = [], EntityID = 1, returnUserImportID = False, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserImport in the district.

    This function returns a dataframe of every UserImport in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserImport(UserImportID, EntityID = 1, returnUserImportID = False, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(UserImportID), verb = "get", return_params_list = return_params)

def modifyUserImport(UserImportID, EntityID = 1, setUserImportID = None, setAboveChangeThreshold = None, setAboveDeleteThreshold = None, setCreatedTime = None, setDateExecuted = None, setHasErrors = None, setMediaID = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserImportID = False, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(UserImportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserImport(EntityID = 1, setUserImportID = None, setAboveChangeThreshold = None, setAboveDeleteThreshold = None, setCreatedTime = None, setDateExecuted = None, setHasErrors = None, setMediaID = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserImportID = False, returnAboveChangeThreshold = False, returnAboveDeleteThreshold = False, returnCreatedTime = False, returnDateExecuted = False, returnHasErrors = False, returnMediaID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserImport(UserImportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImport/" + str(UserImportID), verb = "delete")


def getEveryUserImportResult(searchConditions = [], EntityID = 1, returnUserImportResultID = False, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserImportResult in the district.

    This function returns a dataframe of every UserImportResult in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserImportResult(UserImportResultID, EntityID = 1, returnUserImportResultID = False, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(UserImportResultID), verb = "get", return_params_list = return_params)

def modifyUserImportResult(UserImportResultID, EntityID = 1, setUserImportResultID = None, setCreatedTime = None, setEntityCode = None, setGroupMembershipChangeType = None, setGroupMembershipChangeTypeCode = None, setGroupName = None, setHasErrors = None, setIsStaff = None, setLineNumber = None, setModifiedTime = None, setNameChangeType = None, setNameChangeTypeCode = None, setSchoolYear = None, setStaffChangeType = None, setStaffChangeTypeCode = None, setUserChangeType = None, setUserChangeTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserImportID = None, setUsername = None, returnUserImportResultID = False, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(UserImportResultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserImportResult(EntityID = 1, setUserImportResultID = None, setCreatedTime = None, setEntityCode = None, setGroupMembershipChangeType = None, setGroupMembershipChangeTypeCode = None, setGroupName = None, setHasErrors = None, setIsStaff = None, setLineNumber = None, setModifiedTime = None, setNameChangeType = None, setNameChangeTypeCode = None, setSchoolYear = None, setStaffChangeType = None, setStaffChangeTypeCode = None, setUserChangeType = None, setUserChangeTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserImportID = None, setUsername = None, returnUserImportResultID = False, returnCreatedTime = False, returnEntityCode = False, returnGroupMembershipChangeType = False, returnGroupMembershipChangeTypeCode = False, returnGroupName = False, returnHasErrors = False, returnIsStaff = False, returnLineNumber = False, returnModifiedTime = False, returnNameChangeType = False, returnNameChangeTypeCode = False, returnSchoolYear = False, returnStaffChangeType = False, returnStaffChangeTypeCode = False, returnUserChangeType = False, returnUserChangeTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportID = False, returnUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserImportResult(UserImportResultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResult/" + str(UserImportResultID), verb = "delete")


def getEveryUserImportResultError(searchConditions = [], EntityID = 1, returnUserImportResultErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserImportResultError in the district.

    This function returns a dataframe of every UserImportResultError in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserImportResultError(UserImportResultErrorID, EntityID = 1, returnUserImportResultErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(UserImportResultErrorID), verb = "get", return_params_list = return_params)

def modifyUserImportResultError(UserImportResultErrorID, EntityID = 1, setUserImportResultErrorID = None, setCreatedTime = None, setErrorMessage = None, setFieldName = None, setFromPreview = None, setModifiedTime = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserImportResultID = None, returnUserImportResultErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(UserImportResultErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserImportResultError(EntityID = 1, setUserImportResultErrorID = None, setCreatedTime = None, setErrorMessage = None, setFieldName = None, setFromPreview = None, setModifiedTime = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserImportResultID = None, returnUserImportResultErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnFieldName = False, returnFromPreview = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserImportResultID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserImportResultError(UserImportResultErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserImportResultError/" + str(UserImportResultErrorID), verb = "delete")


def getEveryUserPasswordReset(searchConditions = [], EntityID = 1, returnUserPasswordResetID = False, returnCreatedTime = False, returnExpirationTime = False, returnHostAddressRequestedFrom = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUsed = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserPasswordReset in the district.

    This function returns a dataframe of every UserPasswordReset in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserPasswordReset(UserPasswordResetID, EntityID = 1, returnUserPasswordResetID = False, returnCreatedTime = False, returnExpirationTime = False, returnHostAddressRequestedFrom = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUsed = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(UserPasswordResetID), verb = "get", return_params_list = return_params)

def modifyUserPasswordReset(UserPasswordResetID, EntityID = 1, setUserPasswordResetID = None, setCreatedTime = None, setExpirationTime = None, setHostAddressRequestedFrom = None, setModifiedTime = None, setResetGuid = None, setResetSalt = None, setUsed = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserPasswordResetID = False, returnCreatedTime = False, returnExpirationTime = False, returnHostAddressRequestedFrom = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUsed = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(UserPasswordResetID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserPasswordReset(EntityID = 1, setUserPasswordResetID = None, setCreatedTime = None, setExpirationTime = None, setHostAddressRequestedFrom = None, setModifiedTime = None, setResetGuid = None, setResetSalt = None, setUsed = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserPasswordResetID = False, returnCreatedTime = False, returnExpirationTime = False, returnHostAddressRequestedFrom = False, returnModifiedTime = False, returnResetGuid = False, returnResetSalt = False, returnUsed = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserPasswordReset(UserPasswordResetID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPasswordReset/" + str(UserPasswordResetID), verb = "delete")


def getEveryUserPreference(searchConditions = [], EntityID = 1, returnUserPreferenceID = False, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserPreference in the district.

    This function returns a dataframe of every UserPreference in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserPreference(UserPreferenceID, EntityID = 1, returnUserPreferenceID = False, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(UserPreferenceID), verb = "get", return_params_list = return_params)

def modifyUserPreference(UserPreferenceID, EntityID = 1, setUserPreferenceID = None, setAccountSelection = None, setAccountSelectionCode = None, setCreatedTime = None, setModifiedTime = None, setThemeID = None, setUseEmailMultifactorAuthentication = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDSecurity = None, returnUserPreferenceID = False, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(UserPreferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserPreference(EntityID = 1, setUserPreferenceID = None, setAccountSelection = None, setAccountSelectionCode = None, setCreatedTime = None, setModifiedTime = None, setThemeID = None, setUseEmailMultifactorAuthentication = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDSecurity = None, returnUserPreferenceID = False, returnAccountSelection = False, returnAccountSelectionCode = False, returnCreatedTime = False, returnModifiedTime = False, returnThemeID = False, returnUseEmailMultifactorAuthentication = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSecurity = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserPreference(UserPreferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserPreference/" + str(UserPreferenceID), verb = "delete")


def getEveryUserProfileData(searchConditions = [], EntityID = 1, returnUserProfileDataID = False, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserProfileData in the district.

    This function returns a dataframe of every UserProfileData in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserProfileData(UserProfileDataID, EntityID = 1, returnUserProfileDataID = False, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(UserProfileDataID), verb = "get", return_params_list = return_params)

def modifyUserProfileData(UserProfileDataID, EntityID = 1, setUserProfileDataID = None, setBrowseObject = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setRelatedRecord = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserProfileDataID = False, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(UserProfileDataID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserProfileData(EntityID = 1, setUserProfileDataID = None, setBrowseObject = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setRelatedRecord = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserProfileDataID = False, returnBrowseObject = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnRelatedRecord = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserProfileData(UserProfileDataID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileData/" + str(UserProfileDataID), verb = "delete")


def getEveryUserProfileTabStatus(searchConditions = [], EntityID = 1, returnUserProfileTabStatusID = False, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserProfileTabStatus in the district.

    This function returns a dataframe of every UserProfileTabStatus in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserProfileTabStatus(UserProfileTabStatusID, EntityID = 1, returnUserProfileTabStatusID = False, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(UserProfileTabStatusID), verb = "get", return_params_list = return_params)

def modifyUserProfileTabStatus(UserProfileTabStatusID, EntityID = 1, setUserProfileTabStatusID = None, setCreatedTime = None, setModifiedTime = None, setOpenTabs = None, setProfileID = None, setProfileScreenIDLastTab = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserProfileTabStatusID = False, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(UserProfileTabStatusID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserProfileTabStatus(EntityID = 1, setUserProfileTabStatusID = None, setCreatedTime = None, setModifiedTime = None, setOpenTabs = None, setProfileID = None, setProfileScreenIDLastTab = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserProfileTabStatusID = False, returnCreatedTime = False, returnModifiedTime = False, returnOpenTabs = False, returnProfileID = False, returnProfileScreenIDLastTab = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserProfileTabStatus(UserProfileTabStatusID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserProfileTabStatus/" + str(UserProfileTabStatusID), verb = "delete")


def getEveryUserSetting(searchConditions = [], EntityID = 1, returnUserSettingID = False, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserSetting in the district.

    This function returns a dataframe of every UserSetting in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserSetting(UserSettingID, EntityID = 1, returnUserSettingID = False, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(UserSettingID), verb = "get", return_params_list = return_params)

def modifyUserSetting(UserSettingID, EntityID = 1, setUserSettingID = None, setAction = None, setArea = None, setCode = None, setController = None, setCreatedTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnUserSettingID = False, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(UserSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserSetting(EntityID = 1, setUserSettingID = None, setAction = None, setArea = None, setCode = None, setController = None, setCreatedTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnUserSettingID = False, returnAction = False, returnArea = False, returnCode = False, returnController = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserSetting(UserSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserSetting/" + str(UserSettingID), verb = "delete")


def getEveryUserStudentCalendarPreference(searchConditions = [], EntityID = 1, returnUserStudentCalendarPreferenceID = False, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserStudentCalendarPreference in the district.

    This function returns a dataframe of every UserStudentCalendarPreference in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserStudentCalendarPreference(UserStudentCalendarPreferenceID, EntityID = 1, returnUserStudentCalendarPreferenceID = False, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(UserStudentCalendarPreferenceID), verb = "get", return_params_list = return_params)

def modifyUserStudentCalendarPreference(UserStudentCalendarPreferenceID, EntityID = 1, setUserStudentCalendarPreferenceID = None, setAssignmentBackgroundColor = None, setCreatedTime = None, setModifiedTime = None, setShowAssignments = None, setShowStudentActivityEvents = None, setStudentActivityEventBackgroundColor = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnUserStudentCalendarPreferenceID = False, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(UserStudentCalendarPreferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserStudentCalendarPreference(EntityID = 1, setUserStudentCalendarPreferenceID = None, setAssignmentBackgroundColor = None, setCreatedTime = None, setModifiedTime = None, setShowAssignments = None, setShowStudentActivityEvents = None, setStudentActivityEventBackgroundColor = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnUserStudentCalendarPreferenceID = False, returnAssignmentBackgroundColor = False, returnCreatedTime = False, returnModifiedTime = False, returnShowAssignments = False, returnShowStudentActivityEvents = False, returnStudentActivityEventBackgroundColor = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserStudentCalendarPreference(UserStudentCalendarPreferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/UserStudentCalendarPreference/" + str(UserStudentCalendarPreferenceID), verb = "delete")


def getEveryUser(searchConditions = [], EntityID = 1, returnUserID = False, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGroupMembershipCount = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every User in the district.

    This function returns a dataframe of every User in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUser(UserID, EntityID = 1, returnUserID = False, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGroupMembershipCount = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(UserID), verb = "get", return_params_list = return_params)

def modifyUser(UserID, EntityID = 1, setUserID = None, setAccessCode = None, setAuthenticationRoleID = None, setCreatedTime = None, setCurrentPortal = None, setCurrentPortalCode = None, setCustomerAccessID = None, setDatabaseUsername = None, setDockDisplayOpen = None, setEffectiveAuthenticationRoleID = None, setEffectiveAuthenticationRoleName = None, setEffectiveCachedAuthenticationRole = None, setEffectiveMultifactorAuthenticationCode = None, setEffectiveMultifactorAuthenticationID = None, setEmulatingMobile = None, setEntityIDCurrent = None, setFailedMultifactorAuthenticationCount = None, setFailedSignInCount = None, setFiscalYearIDCurrent = None, setForcePasswordChange = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setGroupMembershipCount = None, setIsActive = None, setIsDeleted = None, setIsExpired = None, setIsLockedOut = None, setIsSuperUser = None, setLastPasswordChangeTime = None, setLockedOutTime = None, setMessageCount = None, setModifiedTime = None, setMultifactorAuthenticationID = None, setNameID = None, setPasswordExpirationDate = None, setPasswordHash = None, setPasswordSalt = None, setPasswordStrategy = None, setPasswordStrategyCode = None, setRolesAuthenticationRoleID = None, setRolesMultifactorAuthenticationID = None, setUserHasFamilyAccess = None, setUserHasStudentAccess = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsername = None, setUserUncachedID = None, setUsesSkywardAuthentication = None, returnUserID = False, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGroupMembershipCount = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(UserID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUser(EntityID = 1, setUserID = None, setAccessCode = None, setAuthenticationRoleID = None, setCreatedTime = None, setCurrentPortal = None, setCurrentPortalCode = None, setCustomerAccessID = None, setDatabaseUsername = None, setDockDisplayOpen = None, setEffectiveAuthenticationRoleID = None, setEffectiveAuthenticationRoleName = None, setEffectiveCachedAuthenticationRole = None, setEffectiveMultifactorAuthenticationCode = None, setEffectiveMultifactorAuthenticationID = None, setEmulatingMobile = None, setEntityIDCurrent = None, setFailedMultifactorAuthenticationCount = None, setFailedSignInCount = None, setFiscalYearIDCurrent = None, setForcePasswordChange = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setGroupMembershipCount = None, setIsActive = None, setIsDeleted = None, setIsExpired = None, setIsLockedOut = None, setIsSuperUser = None, setLastPasswordChangeTime = None, setLockedOutTime = None, setMessageCount = None, setModifiedTime = None, setMultifactorAuthenticationID = None, setNameID = None, setPasswordExpirationDate = None, setPasswordHash = None, setPasswordSalt = None, setPasswordStrategy = None, setPasswordStrategyCode = None, setRolesAuthenticationRoleID = None, setRolesMultifactorAuthenticationID = None, setUserHasFamilyAccess = None, setUserHasStudentAccess = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsername = None, setUserUncachedID = None, setUsesSkywardAuthentication = None, returnUserID = False, returnAccessCode = False, returnAuthenticationRoleID = False, returnCreatedTime = False, returnCurrentPortal = False, returnCurrentPortalCode = False, returnCustomerAccessID = False, returnDatabaseUsername = False, returnDockDisplayOpen = False, returnEffectiveAuthenticationRoleID = False, returnEffectiveAuthenticationRoleName = False, returnEffectiveCachedAuthenticationRole = False, returnEffectiveMultifactorAuthenticationCode = False, returnEffectiveMultifactorAuthenticationID = False, returnEmulatingMobile = False, returnEntityIDCurrent = False, returnFailedMultifactorAuthenticationCount = False, returnFailedSignInCount = False, returnFiscalYearIDCurrent = False, returnForcePasswordChange = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGroupMembershipCount = False, returnIsActive = False, returnIsDeleted = False, returnIsExpired = False, returnIsLockedOut = False, returnIsSuperUser = False, returnLastPasswordChangeTime = False, returnLockedOutTime = False, returnMessageCount = False, returnModifiedTime = False, returnMultifactorAuthenticationID = False, returnNameID = False, returnPasswordExpirationDate = False, returnPasswordHash = False, returnPasswordSalt = False, returnPasswordStrategy = False, returnPasswordStrategyCode = False, returnRolesAuthenticationRoleID = False, returnRolesMultifactorAuthenticationID = False, returnUserHasFamilyAccess = False, returnUserHasStudentAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, returnUserUncachedID = False, returnUsesSkywardAuthentication = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUser(UserID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Security/User/" + str(UserID), verb = "delete")