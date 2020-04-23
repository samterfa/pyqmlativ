# This module contains Family functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryChangeRequest(searchConditions = [], EntityID = 1, returnChangeRequestID = False, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ChangeRequest in the district.

    This function returns a dataframe of every ChangeRequest in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getChangeRequest(ChangeRequestID, EntityID = 1, returnChangeRequestID = False, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "get", return_params_list = return_params)

def modifyChangeRequest(ChangeRequestID, EntityID = 1, setChangeRequestID = None, setArea = None, setAreaCode = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setNameID = None, setSchoolYearID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnChangeRequestID = False, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "post", return_params_list = return_params, payload = payload_params)

def createChangeRequest(EntityID = 1, setChangeRequestID = None, setArea = None, setAreaCode = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setNameID = None, setSchoolYearID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnChangeRequestID = False, returnArea = False, returnAreaCode = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteChangeRequest(ChangeRequestID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequest/" + str(ChangeRequestID), verb = "delete")


def getEveryChangeRequestDetail(searchConditions = [], EntityID = 1, returnChangeRequestDetailID = False, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ChangeRequestDetail in the district.

    This function returns a dataframe of every ChangeRequestDetail in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getChangeRequestDetail(ChangeRequestDetailID, EntityID = 1, returnChangeRequestDetailID = False, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "get", return_params_list = return_params)

def modifyChangeRequestDetail(ChangeRequestDetailID, EntityID = 1, setChangeRequestDetailID = None, setChangeRequestID = None, setCreatedTime = None, setFieldName = None, setFieldNameCode = None, setModifiedTime = None, setOriginalValue = None, setRequestedTime = None, setRequestedValue = None, setSourceID = None, setStatus = None, setStatusCode = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRequestedBy = None, returnChangeRequestDetailID = False, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createChangeRequestDetail(EntityID = 1, setChangeRequestDetailID = None, setChangeRequestID = None, setCreatedTime = None, setFieldName = None, setFieldNameCode = None, setModifiedTime = None, setOriginalValue = None, setRequestedTime = None, setRequestedValue = None, setSourceID = None, setStatus = None, setStatusCode = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRequestedBy = None, returnChangeRequestDetailID = False, returnChangeRequestID = False, returnCreatedTime = False, returnFieldName = False, returnFieldNameCode = False, returnModifiedTime = False, returnOriginalValue = False, returnRequestedTime = False, returnRequestedValue = False, returnSourceID = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRequestedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteChangeRequestDetail(ChangeRequestDetailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetail/" + str(ChangeRequestDetailID), verb = "delete")


def getEveryChangeRequestDetailApproval(searchConditions = [], EntityID = 1, returnChangeRequestDetailApprovalID = False, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ChangeRequestDetailApproval in the district.

    This function returns a dataframe of every ChangeRequestDetailApproval in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1, returnChangeRequestDetailApprovalID = False, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "get", return_params_list = return_params)

def modifyChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1, setChangeRequestDetailApprovalID = None, setChangeRequestDetailID = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnChangeRequestDetailApprovalID = False, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "post", return_params_list = return_params, payload = payload_params)

def createChangeRequestDetailApproval(EntityID = 1, setChangeRequestDetailApprovalID = None, setChangeRequestDetailID = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnChangeRequestDetailApprovalID = False, returnChangeRequestDetailID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteChangeRequestDetailApproval(ChangeRequestDetailApprovalID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ChangeRequestDetailApproval/" + str(ChangeRequestDetailApprovalID), verb = "delete")


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayDefaultContact = False, returnDisplayModuleContact = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigDistrictYear in the district.

    This function returns a dataframe of every ConfigDistrictYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayDefaultContact = False, returnDisplayModuleContact = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearID = None, setCreatedTime = None, setDisplayDefaultContact = None, setDisplayModuleContact = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayDefaultContact = False, returnDisplayModuleContact = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearID = None, setCreatedTime = None, setDisplayDefaultContact = None, setDisplayModuleContact = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayDefaultContact = False, returnDisplayModuleContact = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")


def getEveryConfigDistrictYearContact(searchConditions = [], EntityID = 1, returnConfigDistrictYearContactID = False, returnCanDisplayEmail = False, returnCanDisplayPhone = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayEmail = False, returnDisplayPhone = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnModuleDisplay = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigDistrictYearContact in the district.

    This function returns a dataframe of every ConfigDistrictYearContact in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrictYearContact(ConfigDistrictYearContactID, EntityID = 1, returnConfigDistrictYearContactID = False, returnCanDisplayEmail = False, returnCanDisplayPhone = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayEmail = False, returnDisplayPhone = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnModuleDisplay = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/" + str(ConfigDistrictYearContactID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYearContact(ConfigDistrictYearContactID, EntityID = 1, setConfigDistrictYearContactID = None, setCanDisplayEmail = None, setCanDisplayPhone = None, setConfigDistrictYearID = None, setCreatedTime = None, setDisplayEmail = None, setDisplayPhone = None, setModifiedTime = None, setModule = None, setModuleCode = None, setModuleDisplay = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearContactID = False, returnCanDisplayEmail = False, returnCanDisplayPhone = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayEmail = False, returnDisplayPhone = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnModuleDisplay = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/" + str(ConfigDistrictYearContactID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYearContact(EntityID = 1, setConfigDistrictYearContactID = None, setCanDisplayEmail = None, setCanDisplayPhone = None, setConfigDistrictYearID = None, setCreatedTime = None, setDisplayEmail = None, setDisplayPhone = None, setModifiedTime = None, setModule = None, setModuleCode = None, setModuleDisplay = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearContactID = False, returnCanDisplayEmail = False, returnCanDisplayPhone = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDisplayEmail = False, returnDisplayPhone = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnModuleDisplay = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYearContact(ConfigDistrictYearContactID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigDistrictYearContact/" + str(ConfigDistrictYearContactID), verb = "delete")


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayLockerCombination = False, returnFamilyAccessDisplayLockerNumber = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnStaffNameDisplayType = False, returnStaffNameDisplayTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigEntityGroupYear in the district.

    This function returns a dataframe of every ConfigEntityGroupYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = False, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayLockerCombination = False, returnFamilyAccessDisplayLockerNumber = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnStaffNameDisplayType = False, returnStaffNameDisplayTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setConfigEntityGroupYearID = None, setChangeRequestFamilyEmail = None, setChangeRequestFamilyEmailCode = None, setChangeRequestFamilyPhone = None, setChangeRequestFamilyPhoneCode = None, setChangeRequestStudentEmail = None, setChangeRequestStudentEmailCode = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setDefaultFeeManagementOnlinePaymentAccess = None, setDefaultFeeManagementOnlinePaymentAccessCode = None, setDefaultFoodServiceOnlinePaymentAccess = None, setDefaultFoodServiceOnlinePaymentAccessCode = None, setDisplayAssignments = None, setDisplayCalendarEvents = None, setDisplayDistrictActivityEvents = None, setDisplayStudentActivityEvents = None, setEmailTypeIDToDisplayFamilyStudentAccess = None, setEndorsementSignatureOption = None, setEndorsementSignatureOptionCode = None, setEndorsementSignatureStatement = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessAccountInfoEmailBody = None, setFamilyAccessAccountInfoEmailIncludeResetPasswordText = None, setFamilyAccessAccountInfoEmailSubject = None, setFamilyAccessCareerPlanDisplayShowDroppedCourses = None, setFamilyAccessDisplayCommentCodes = None, setFamilyAccessDisplayFreeFormComments = None, setFamilyAccessDisplayGradeBucketsAfterEndDate = None, setFamilyAccessDisplayHonorRoll = None, setFamilyAccessDisplayLockerCombination = None, setFamilyAccessDisplayLockerNumber = None, setFamilyAccessDisplayOnlyCurrentAndCompleteGrades = None, setFamilyAccessDisplayOnlyCurrentMissingAssignments = None, setFamilyAccessDisplayShowActualEarnedCredits = None, setFamilyAccessDisplayShowAttendance = None, setFamilyAccessDisplayShowDroppedCourses = None, setFamilyAccessDisplayShowEndedAttendanceTerms = None, setFamilyAccessDisplayShowPossibleEarnedCredits = None, setFamilyAccessDisplayStudentAddress = None, setFamilyAccessDisplayStudentRank = None, setFamilyAccessDisplayUseReportCardGradeBucketSettings = None, setFamilyAccessLinkStudentSectionsOnReportCard = None, setFamilyStudentAccessDisplayTeacherEmail = None, setFamilyStudentAccessDisplayTeacherPhoneNumber = None, setHideScheduleMessage = None, setHideSchedulePriorToCalendarDays = None, setIsFamilyInformationApprovalWorkflowUpdated = None, setIsStudentInformationApprovalWorkflowUpdated = None, setModifiedTime = None, setPhoneTypeIDToDisplayFamilyStudentAccess = None, setRankMethodIDFamilyAccessReportCardGrading = None, setRankMethodIDFamilyAccessReportCardStudent = None, setReportCardGPADisplay = None, setReportCardGPADisplayCode = None, setReportCardHeaderAddressType = None, setReportCardHeaderAddressTypeCode = None, setReportCardStudentRankDisplay = None, setReportCardStudentRankDisplayCode = None, setSchoolYearID = None, setStaffNameDisplayType = None, setStaffNameDisplayTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayLockerCombination = False, returnFamilyAccessDisplayLockerNumber = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnStaffNameDisplayType = False, returnStaffNameDisplayTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setConfigEntityGroupYearID = None, setChangeRequestFamilyEmail = None, setChangeRequestFamilyEmailCode = None, setChangeRequestFamilyPhone = None, setChangeRequestFamilyPhoneCode = None, setChangeRequestStudentEmail = None, setChangeRequestStudentEmailCode = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setDefaultFeeManagementOnlinePaymentAccess = None, setDefaultFeeManagementOnlinePaymentAccessCode = None, setDefaultFoodServiceOnlinePaymentAccess = None, setDefaultFoodServiceOnlinePaymentAccessCode = None, setDisplayAssignments = None, setDisplayCalendarEvents = None, setDisplayDistrictActivityEvents = None, setDisplayStudentActivityEvents = None, setEmailTypeIDToDisplayFamilyStudentAccess = None, setEndorsementSignatureOption = None, setEndorsementSignatureOptionCode = None, setEndorsementSignatureStatement = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessAccountInfoEmailBody = None, setFamilyAccessAccountInfoEmailIncludeResetPasswordText = None, setFamilyAccessAccountInfoEmailSubject = None, setFamilyAccessCareerPlanDisplayShowDroppedCourses = None, setFamilyAccessDisplayCommentCodes = None, setFamilyAccessDisplayFreeFormComments = None, setFamilyAccessDisplayGradeBucketsAfterEndDate = None, setFamilyAccessDisplayHonorRoll = None, setFamilyAccessDisplayLockerCombination = None, setFamilyAccessDisplayLockerNumber = None, setFamilyAccessDisplayOnlyCurrentAndCompleteGrades = None, setFamilyAccessDisplayOnlyCurrentMissingAssignments = None, setFamilyAccessDisplayShowActualEarnedCredits = None, setFamilyAccessDisplayShowAttendance = None, setFamilyAccessDisplayShowDroppedCourses = None, setFamilyAccessDisplayShowEndedAttendanceTerms = None, setFamilyAccessDisplayShowPossibleEarnedCredits = None, setFamilyAccessDisplayStudentAddress = None, setFamilyAccessDisplayStudentRank = None, setFamilyAccessDisplayUseReportCardGradeBucketSettings = None, setFamilyAccessLinkStudentSectionsOnReportCard = None, setFamilyStudentAccessDisplayTeacherEmail = None, setFamilyStudentAccessDisplayTeacherPhoneNumber = None, setHideScheduleMessage = None, setHideSchedulePriorToCalendarDays = None, setIsFamilyInformationApprovalWorkflowUpdated = None, setIsStudentInformationApprovalWorkflowUpdated = None, setModifiedTime = None, setPhoneTypeIDToDisplayFamilyStudentAccess = None, setRankMethodIDFamilyAccessReportCardGrading = None, setRankMethodIDFamilyAccessReportCardStudent = None, setReportCardGPADisplay = None, setReportCardGPADisplayCode = None, setReportCardHeaderAddressType = None, setReportCardHeaderAddressTypeCode = None, setReportCardStudentRankDisplay = None, setReportCardStudentRankDisplayCode = None, setSchoolYearID = None, setStaffNameDisplayType = None, setStaffNameDisplayTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnChangeRequestFamilyEmail = False, returnChangeRequestFamilyEmailCode = False, returnChangeRequestFamilyPhone = False, returnChangeRequestFamilyPhoneCode = False, returnChangeRequestStudentEmail = False, returnChangeRequestStudentEmailCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultFeeManagementOnlinePaymentAccess = False, returnDefaultFeeManagementOnlinePaymentAccessCode = False, returnDefaultFoodServiceOnlinePaymentAccess = False, returnDefaultFoodServiceOnlinePaymentAccessCode = False, returnDisplayAssignments = False, returnDisplayCalendarEvents = False, returnDisplayDistrictActivityEvents = False, returnDisplayStudentActivityEvents = False, returnEmailTypeIDToDisplayFamilyStudentAccess = False, returnEndorsementSignatureOption = False, returnEndorsementSignatureOptionCode = False, returnEndorsementSignatureStatement = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessAccountInfoEmailBody = False, returnFamilyAccessAccountInfoEmailIncludeResetPasswordText = False, returnFamilyAccessAccountInfoEmailSubject = False, returnFamilyAccessCareerPlanDisplayShowDroppedCourses = False, returnFamilyAccessDisplayCommentCodes = False, returnFamilyAccessDisplayFreeFormComments = False, returnFamilyAccessDisplayGradeBucketsAfterEndDate = False, returnFamilyAccessDisplayHonorRoll = False, returnFamilyAccessDisplayLockerCombination = False, returnFamilyAccessDisplayLockerNumber = False, returnFamilyAccessDisplayOnlyCurrentAndCompleteGrades = False, returnFamilyAccessDisplayOnlyCurrentMissingAssignments = False, returnFamilyAccessDisplayShowActualEarnedCredits = False, returnFamilyAccessDisplayShowAttendance = False, returnFamilyAccessDisplayShowDroppedCourses = False, returnFamilyAccessDisplayShowEndedAttendanceTerms = False, returnFamilyAccessDisplayShowPossibleEarnedCredits = False, returnFamilyAccessDisplayStudentAddress = False, returnFamilyAccessDisplayStudentRank = False, returnFamilyAccessDisplayUseReportCardGradeBucketSettings = False, returnFamilyAccessLinkStudentSectionsOnReportCard = False, returnFamilyStudentAccessDisplayTeacherEmail = False, returnFamilyStudentAccessDisplayTeacherPhoneNumber = False, returnHideScheduleMessage = False, returnHideSchedulePriorToCalendarDays = False, returnIsFamilyInformationApprovalWorkflowUpdated = False, returnIsStudentInformationApprovalWorkflowUpdated = False, returnModifiedTime = False, returnPhoneTypeIDToDisplayFamilyStudentAccess = False, returnRankMethodIDFamilyAccessReportCardGrading = False, returnRankMethodIDFamilyAccessReportCardStudent = False, returnReportCardGPADisplay = False, returnReportCardGPADisplayCode = False, returnReportCardHeaderAddressType = False, returnReportCardHeaderAddressTypeCode = False, returnReportCardStudentRankDisplay = False, returnReportCardStudentRankDisplayCode = False, returnSchoolYearID = False, returnStaffNameDisplayType = False, returnStaffNameDisplayTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setAddressValidationMessage = None, setAllowFamilyAccessDefault = None, setAllowOutOfRangeAddressesToSubmit = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setCreatedTime = None, setEnableAddressValidation = None, setEnableNewStudentEnrollment = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setAddressValidationMessage = None, setAllowFamilyAccessDefault = None, setAllowOutOfRangeAddressesToSubmit = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setCreatedTime = None, setEnableAddressValidation = None, setEnableNewStudentEnrollment = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAddressValidationMessage = False, returnAllowFamilyAccessDefault = False, returnAllowOutOfRangeAddressesToSubmit = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEnableAddressValidation = False, returnEnableNewStudentEnrollment = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryCOPPAConsentObjectMA(searchConditions = [], EntityID = 1, returnCOPPAConsentObjectMAID = False, returnCOPPAConsent = False, returnCreatedTime = False, returnFamilyGuardianID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every COPPAConsentObjectMA in the district.

    This function returns a dataframe of every COPPAConsentObjectMA in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCOPPAConsentObjectMA(COPPAConsentObjectMAID, EntityID = 1, returnCOPPAConsentObjectMAID = False, returnCOPPAConsent = False, returnCreatedTime = False, returnFamilyGuardianID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/" + str(COPPAConsentObjectMAID), verb = "get", return_params_list = return_params)

def modifyCOPPAConsentObjectMA(COPPAConsentObjectMAID, EntityID = 1, setCOPPAConsentObjectMAID = None, setCOPPAConsent = None, setCreatedTime = None, setFamilyGuardianID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCOPPAConsentObjectMAID = False, returnCOPPAConsent = False, returnCreatedTime = False, returnFamilyGuardianID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/" + str(COPPAConsentObjectMAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCOPPAConsentObjectMA(EntityID = 1, setCOPPAConsentObjectMAID = None, setCOPPAConsent = None, setCreatedTime = None, setFamilyGuardianID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCOPPAConsentObjectMAID = False, returnCOPPAConsent = False, returnCreatedTime = False, returnFamilyGuardianID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCOPPAConsentObjectMA(COPPAConsentObjectMAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/COPPAConsentObjectMA/" + str(COPPAConsentObjectMAID), verb = "delete")


def getEveryFamily(searchConditions = [], EntityID = 1, returnFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Family in the district.

    This function returns a dataframe of every Family in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFamily(FamilyID, EntityID = 1, returnFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "get", return_params_list = return_params)

def modifyFamily(FamilyID, EntityID = 1, setFamilyID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setHasStudentInSpecificDistrict = None, setLanguageIDHome = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFamily(EntityID = 1, setFamilyID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setHasStudentInSpecificDistrict = None, setLanguageIDHome = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnHasStudentInSpecificDistrict = False, returnLanguageIDHome = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFamily(FamilyID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/Family/" + str(FamilyID), verb = "delete")


def getEveryFamilyGuardian(searchConditions = [], EntityID = 1, returnFamilyGuardianID = False, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FamilyGuardian in the district.

    This function returns a dataframe of every FamilyGuardian in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFamilyGuardian(FamilyGuardianID, EntityID = 1, returnFamilyGuardianID = False, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "get", return_params_list = return_params)

def modifyFamilyGuardian(FamilyGuardianID, EntityID = 1, setFamilyGuardianID = None, setCreatedTime = None, setFamilyID = None, setHasActiveStudentGuardianRestrictedAccess = None, setModifiedTime = None, setNameID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setAPIOptionFlags = None, returnFamilyGuardianID = False, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFamilyGuardian(EntityID = 1, setFamilyGuardianID = None, setCreatedTime = None, setFamilyID = None, setHasActiveStudentGuardianRestrictedAccess = None, setModifiedTime = None, setNameID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setAPIOptionFlags = None, returnFamilyGuardianID = False, returnCreatedTime = False, returnFamilyID = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnModifiedTime = False, returnNameID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFamilyGuardian(FamilyGuardianID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/FamilyGuardian/" + str(FamilyGuardianID), verb = "delete")


def getEveryStudentFamily(searchConditions = [], EntityID = 1, returnStudentFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentFamily in the district.

    This function returns a dataframe of every StudentFamily in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentFamily(StudentFamilyID, EntityID = 1, returnStudentFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "get", return_params_list = return_params)

def modifyStudentFamily(StudentFamilyID, EntityID = 1, setStudentFamilyID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setFamilyID = None, setHasEmployeeGuardian = None, setIsEmergencyContact = None, setIsPrimaryEmergencyContact = None, setModifiedTime = None, setRank = None, setReceivesForms = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setAPIOptionFlags = None, returnStudentFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentFamily(EntityID = 1, setStudentFamilyID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setFamilyID = None, setHasEmployeeGuardian = None, setIsEmergencyContact = None, setIsPrimaryEmergencyContact = None, setModifiedTime = None, setRank = None, setReceivesForms = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setAPIOptionFlags = None, returnStudentFamilyID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFamilyID = False, returnHasEmployeeGuardian = False, returnIsEmergencyContact = False, returnIsPrimaryEmergencyContact = False, returnModifiedTime = False, returnRank = False, returnReceivesForms = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentFamily(StudentFamilyID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentFamily/" + str(StudentFamilyID), verb = "delete")


def getEveryStudentGuardian(searchConditions = [], EntityID = 1, returnStudentGuardianID = False, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentGuardian in the district.

    This function returns a dataframe of every StudentGuardian in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentGuardian(StudentGuardianID, EntityID = 1, returnStudentGuardianID = False, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "get", return_params_list = return_params)

def modifyStudentGuardian(StudentGuardianID, EntityID = 1, setStudentGuardianID = None, setAllowFamilyAccess = None, setAllowStudentPickup = None, setCreatedTime = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFoodOnlinePaymentOverrideType = None, setFoodOnlinePaymentOverrideTypeCode = None, setGuardianCategory = None, setGuardianNameIDAndFamilyID = None, setHasActiveRestrictedAccess = None, setHasUnrestrictedAccess = None, setIsCustodialGuardian = None, setIsEmergencyContact = None, setModifiedTime = None, setNameIDGuardian = None, setNeedsSecurityGroupAudit = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodOnlinePaymentAccess = None, setRank = None, setRelationshipID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGuardianID = False, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGuardian(EntityID = 1, setStudentGuardianID = None, setAllowFamilyAccess = None, setAllowStudentPickup = None, setCreatedTime = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFoodOnlinePaymentOverrideType = None, setFoodOnlinePaymentOverrideTypeCode = None, setGuardianCategory = None, setGuardianNameIDAndFamilyID = None, setHasActiveRestrictedAccess = None, setHasUnrestrictedAccess = None, setIsCustodialGuardian = None, setIsEmergencyContact = None, setModifiedTime = None, setNameIDGuardian = None, setNeedsSecurityGroupAudit = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodOnlinePaymentAccess = None, setRank = None, setRelationshipID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGuardianID = False, returnAllowFamilyAccess = False, returnAllowStudentPickup = False, returnCreatedTime = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFoodOnlinePaymentOverrideType = False, returnFoodOnlinePaymentOverrideTypeCode = False, returnGuardianCategory = False, returnGuardianNameIDAndFamilyID = False, returnHasActiveRestrictedAccess = False, returnHasUnrestrictedAccess = False, returnIsCustodialGuardian = False, returnIsEmergencyContact = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNeedsSecurityGroupAudit = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodOnlinePaymentAccess = False, returnRank = False, returnRelationshipID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGuardian(StudentGuardianID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardian/" + str(StudentGuardianID), verb = "delete")


def getEveryStudentGuardianRestrictedAccess(searchConditions = [], EntityID = 1, returnStudentGuardianRestrictedAccessID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentGuardianRestrictedAccess in the district.

    This function returns a dataframe of every StudentGuardianRestrictedAccess in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1, returnStudentGuardianRestrictedAccessID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "get", return_params_list = return_params)

def modifyStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1, setStudentGuardianRestrictedAccessID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setEndDate = None, setModifiedTime = None, setReason = None, setStartDate = None, setStudentGuardianID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGuardianRestrictedAccessID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGuardianRestrictedAccess(EntityID = 1, setStudentGuardianRestrictedAccessID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setEndDate = None, setModifiedTime = None, setReason = None, setStartDate = None, setStudentGuardianID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGuardianRestrictedAccessID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnReason = False, returnStartDate = False, returnStudentGuardianID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGuardianRestrictedAccess(StudentGuardianRestrictedAccessID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/StudentGuardianRestrictedAccess/" + str(StudentGuardianRestrictedAccessID), verb = "delete")


def getEveryTempFamilyGuardian(searchConditions = [], EntityID = 1, returnTempFamilyGuardianID = False, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFamilyGuardian in the district.

    This function returns a dataframe of every TempFamilyGuardian in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1, returnTempFamilyGuardianID = False, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "get", return_params_list = return_params)

def modifyTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1, setTempFamilyGuardianID = None, setCreatedTime = None, setGuardianNameID = None, setGuardianNameLFM = None, setIsFamilyAccessUser = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFamilyGuardianID = False, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFamilyGuardian(EntityID = 1, setTempFamilyGuardianID = None, setCreatedTime = None, setGuardianNameID = None, setGuardianNameLFM = None, setIsFamilyAccessUser = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFamilyGuardianID = False, returnCreatedTime = False, returnGuardianNameID = False, returnGuardianNameLFM = False, returnIsFamilyAccessUser = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFamilyGuardian(TempFamilyGuardianID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Family/TempFamilyGuardian/" + str(TempFamilyGuardianID), verb = "delete")