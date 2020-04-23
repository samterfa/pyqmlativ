# This module contains Staff functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = False, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setConfigEntityGroupYearID = None, setAllowFoodServiceOnlinePaymentsAccessByDefault = None, setCreatedTime = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setConfigEntityGroupYearID = None, setAllowFoodServiceOnlinePaymentsAccessByDefault = None, setCreatedTime = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnAllowFoodServiceOnlinePaymentsAccessByDefault = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setCreatedTime = None, setModifiedTime = None, setNewTeacherAccessUserMessageContent = None, setNewTeacherAccessUserMessageSubject = None, setStaffNumberMask = None, setStaffNumberStartValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setCreatedTime = None, setModifiedTime = None, setNewTeacherAccessUserMessageContent = None, setNewTeacherAccessUserMessageSubject = None, setStaffNumberMask = None, setStaffNumberStartValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnModifiedTime = False, returnNewTeacherAccessUserMessageContent = False, returnNewTeacherAccessUserMessageSubject = False, returnStaffNumberMask = False, returnStaffNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryDepartment(searchConditions = [], EntityID = 1, returnDepartmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Department in the district.

    This function returns a dataframe of every Department in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDepartment(DepartmentID, EntityID = 1, returnDepartmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(DepartmentID), verb = "get", return_params_list = return_params)

def modifyDepartment(DepartmentID, EntityID = 1, setDepartmentID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDepartmentIDClonedFrom = None, setDepartmentIDClonedTo = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setStaffIDDepartmentHead = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDepartmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(DepartmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDepartment(EntityID = 1, setDepartmentID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDepartmentIDClonedFrom = None, setDepartmentIDClonedTo = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setStaffIDDepartmentHead = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDepartmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDepartmentIDClonedFrom = False, returnDepartmentIDClonedTo = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffIDDepartmentHead = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDepartment(DepartmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Department/" + str(DepartmentID), verb = "delete")


def getEveryJobTitleMA(searchConditions = [], EntityID = 1, returnJobTitleMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every JobTitleMA in the district.

    This function returns a dataframe of every JobTitleMA in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getJobTitleMA(JobTitleMAID, EntityID = 1, returnJobTitleMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/" + str(JobTitleMAID), verb = "get", return_params_list = return_params)

def modifyJobTitleMA(JobTitleMAID, EntityID = 1, setJobTitleMAID = None, setCreatedTime = None, setModifiedTime = None, setStaffID = None, setTitle = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnJobTitleMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/" + str(JobTitleMAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createJobTitleMA(EntityID = 1, setJobTitleMAID = None, setCreatedTime = None, setModifiedTime = None, setStaffID = None, setTitle = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnJobTitleMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffID = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteJobTitleMA(JobTitleMAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/JobTitleMA/" + str(JobTitleMAID), verb = "delete")


def getEveryMassPrintStaffScheduleRunHistory(searchConditions = [], EntityID = 1, returnMassPrintStaffScheduleRunHistoryID = False, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MassPrintStaffScheduleRunHistory in the district.

    This function returns a dataframe of every MassPrintStaffScheduleRunHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMassPrintStaffScheduleRunHistory(MassPrintStaffScheduleRunHistoryID, EntityID = 1, returnMassPrintStaffScheduleRunHistoryID = False, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(MassPrintStaffScheduleRunHistoryID), verb = "get", return_params_list = return_params)

def modifyMassPrintStaffScheduleRunHistory(MassPrintStaffScheduleRunHistoryID, EntityID = 1, setMassPrintStaffScheduleRunHistoryID = None, setCreatedTime = None, setEntityID = None, setMediaID = None, setModifiedTime = None, setParameterData = None, setParameterDescription = None, setRequestIdentifier = None, setRunDescription = None, setSchoolYearID = None, setSendMessageOnComplete = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowInstanceID = None, returnMassPrintStaffScheduleRunHistoryID = False, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(MassPrintStaffScheduleRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMassPrintStaffScheduleRunHistory(EntityID = 1, setMassPrintStaffScheduleRunHistoryID = None, setCreatedTime = None, setEntityID = None, setMediaID = None, setModifiedTime = None, setParameterData = None, setParameterDescription = None, setRequestIdentifier = None, setRunDescription = None, setSchoolYearID = None, setSendMessageOnComplete = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowInstanceID = None, returnMassPrintStaffScheduleRunHistoryID = False, returnCreatedTime = False, returnEntityID = False, returnMediaID = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRequestIdentifier = False, returnRunDescription = False, returnSchoolYearID = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMassPrintStaffScheduleRunHistory(MassPrintStaffScheduleRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/MassPrintStaffScheduleRunHistory/" + str(MassPrintStaffScheduleRunHistoryID), verb = "delete")


def getEveryNextStaffNumber(searchConditions = [], EntityID = 1, returnNextStaffNumberID = False, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NextStaffNumber in the district.

    This function returns a dataframe of every NextStaffNumber in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNextStaffNumber(NextStaffNumberID, EntityID = 1, returnNextStaffNumberID = False, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(NextStaffNumberID), verb = "get", return_params_list = return_params)

def modifyNextStaffNumber(NextStaffNumberID, EntityID = 1, setNextStaffNumberID = None, setCreatedTime = None, setMaskPrefix = None, setModifiedTime = None, setSequenceNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNextStaffNumberID = False, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(NextStaffNumberID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNextStaffNumber(EntityID = 1, setNextStaffNumberID = None, setCreatedTime = None, setMaskPrefix = None, setModifiedTime = None, setSequenceNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNextStaffNumberID = False, returnCreatedTime = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNextStaffNumber(NextStaffNumberID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NextStaffNumber/" + str(NextStaffNumberID), verb = "delete")


def getEveryNumberedStaffEntityYearForDistrictAndSchoolYear(searchConditions = [], EntityID = 1, returnStaffEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnSchoolYearID = False, returnStaffDistrictRowNumber = False, returnStaffID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NumberedStaffEntityYearForDistrictAndSchoolYear in the district.

    This function returns a dataframe of every NumberedStaffEntityYearForDistrictAndSchoolYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNumberedStaffEntityYearForDistrictAndSchoolYear(StaffEntityYearID, EntityID = 1, returnStaffEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnSchoolYearID = False, returnStaffDistrictRowNumber = False, returnStaffID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/" + str(StaffEntityYearID), verb = "get", return_params_list = return_params)

def modifyNumberedStaffEntityYearForDistrictAndSchoolYear(StaffEntityYearID, EntityID = 1, setStaffEntityYearID = None, setDistrictID = None, setEntityID = None, setSchoolYearID = None, setStaffDistrictRowNumber = None, setStaffID = None, returnStaffEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnSchoolYearID = False, returnStaffDistrictRowNumber = False, returnStaffID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/" + str(StaffEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNumberedStaffEntityYearForDistrictAndSchoolYear(EntityID = 1, setStaffEntityYearID = None, setDistrictID = None, setEntityID = None, setSchoolYearID = None, setStaffDistrictRowNumber = None, setStaffID = None, returnStaffEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnSchoolYearID = False, returnStaffDistrictRowNumber = False, returnStaffID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNumberedStaffEntityYearForDistrictAndSchoolYear(StaffEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/NumberedStaffEntityYearForDistrictAndSchoolYear/" + str(StaffEntityYearID), verb = "delete")


def getEveryScheduleBlocker(searchConditions = [], EntityID = 1, returnScheduleBlockerID = False, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ScheduleBlocker in the district.

    This function returns a dataframe of every ScheduleBlocker in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getScheduleBlocker(ScheduleBlockerID, EntityID = 1, returnScheduleBlockerID = False, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(ScheduleBlockerID), verb = "get", return_params_list = return_params)

def modifyScheduleBlocker(ScheduleBlockerID, EntityID = 1, setScheduleBlockerID = None, setCreatedTime = None, setEndDate = None, setEntityID = None, setModifiedTime = None, setReason = None, setSchoolYearID = None, setStaffID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScheduleBlockerID = False, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(ScheduleBlockerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScheduleBlocker(EntityID = 1, setScheduleBlockerID = None, setCreatedTime = None, setEndDate = None, setEntityID = None, setModifiedTime = None, setReason = None, setSchoolYearID = None, setStaffID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScheduleBlockerID = False, returnCreatedTime = False, returnEndDate = False, returnEntityID = False, returnModifiedTime = False, returnReason = False, returnSchoolYearID = False, returnStaffID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScheduleBlocker(ScheduleBlockerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlocker/" + str(ScheduleBlockerID), verb = "delete")


def getEveryScheduleBlockerDisplayPeriod(searchConditions = [], EntityID = 1, returnScheduleBlockerDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ScheduleBlockerDisplayPeriod in the district.

    This function returns a dataframe of every ScheduleBlockerDisplayPeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getScheduleBlockerDisplayPeriod(ScheduleBlockerDisplayPeriodID, EntityID = 1, returnScheduleBlockerDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(ScheduleBlockerDisplayPeriodID), verb = "get", return_params_list = return_params)

def modifyScheduleBlockerDisplayPeriod(ScheduleBlockerDisplayPeriodID, EntityID = 1, setScheduleBlockerDisplayPeriodID = None, setCreatedTime = None, setDisplayPeriodID = None, setModifiedTime = None, setScheduleBlockerID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScheduleBlockerDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(ScheduleBlockerDisplayPeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScheduleBlockerDisplayPeriod(EntityID = 1, setScheduleBlockerDisplayPeriodID = None, setCreatedTime = None, setDisplayPeriodID = None, setModifiedTime = None, setScheduleBlockerID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScheduleBlockerDisplayPeriodID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnScheduleBlockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScheduleBlockerDisplayPeriod(ScheduleBlockerDisplayPeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/ScheduleBlockerDisplayPeriod/" + str(ScheduleBlockerDisplayPeriodID), verb = "delete")


def getEveryStaffDepartment(searchConditions = [], EntityID = 1, returnStaffDepartmentID = False, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StaffDepartment in the district.

    This function returns a dataframe of every StaffDepartment in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStaffDepartment(StaffDepartmentID, EntityID = 1, returnStaffDepartmentID = False, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(StaffDepartmentID), verb = "get", return_params_list = return_params)

def modifyStaffDepartment(StaffDepartmentID, EntityID = 1, setStaffDepartmentID = None, setCreatedTime = None, setDepartmentID = None, setIsDefaultDepartment = None, setModifiedTime = None, setStaffDepartmentIDClonedFrom = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffDepartmentID = False, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(StaffDepartmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaffDepartment(EntityID = 1, setStaffDepartmentID = None, setCreatedTime = None, setDepartmentID = None, setIsDefaultDepartment = None, setModifiedTime = None, setStaffDepartmentIDClonedFrom = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffDepartmentID = False, returnCreatedTime = False, returnDepartmentID = False, returnIsDefaultDepartment = False, returnModifiedTime = False, returnStaffDepartmentIDClonedFrom = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaffDepartment(StaffDepartmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffDepartment/" + str(StaffDepartmentID), verb = "delete")


def getEveryStaffEntityYear(searchConditions = [], EntityID = 1, returnStaffEntityYearID = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StaffEntityYear in the district.

    This function returns a dataframe of every StaffEntityYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStaffEntityYear(StaffEntityYearID, EntityID = 1, returnStaffEntityYearID = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(StaffEntityYearID), verb = "get", return_params_list = return_params)

def modifyStaffEntityYear(StaffEntityYearID, EntityID = 1, setStaffEntityYearID = None, setCreatedTime = None, setEntityID = None, setIsActive = None, setIsAdditionalStaffOnNotification = None, setIsCareerCenterCounselor = None, setIsDisciplineOfficer = None, setIsSubstituteTeacher = None, setIsTeacher = None, setModifiedTime = None, setRoomIDDefault = None, setSchoolYearID = None, setStaffDepartmentSummary = None, setStaffEntityYearClonedTo = None, setStaffEntityYearIDClonedFrom = None, setStaffID = None, setTeacherNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffEntityYearID = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(StaffEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaffEntityYear(EntityID = 1, setStaffEntityYearID = None, setCreatedTime = None, setEntityID = None, setIsActive = None, setIsAdditionalStaffOnNotification = None, setIsCareerCenterCounselor = None, setIsDisciplineOfficer = None, setIsSubstituteTeacher = None, setIsTeacher = None, setModifiedTime = None, setRoomIDDefault = None, setSchoolYearID = None, setStaffDepartmentSummary = None, setStaffEntityYearClonedTo = None, setStaffEntityYearIDClonedFrom = None, setStaffID = None, setTeacherNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffEntityYearID = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnIsAdditionalStaffOnNotification = False, returnIsCareerCenterCounselor = False, returnIsDisciplineOfficer = False, returnIsSubstituteTeacher = False, returnIsTeacher = False, returnModifiedTime = False, returnRoomIDDefault = False, returnSchoolYearID = False, returnStaffDepartmentSummary = False, returnStaffEntityYearClonedTo = False, returnStaffEntityYearIDClonedFrom = False, returnStaffID = False, returnTeacherNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaffEntityYear(StaffEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffEntityYear/" + str(StaffEntityYearID), verb = "delete")


def getEveryStaff(searchConditions = [], EntityID = 1, returnStaffID = False, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFamilyStudentAccessStaffNameToUse = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Staff in the district.

    This function returns a dataframe of every Staff in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStaff(StaffID, EntityID = 1, returnStaffID = False, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFamilyStudentAccessStaffNameToUse = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(StaffID), verb = "get", return_params_list = return_params)

def modifyStaff(StaffID, EntityID = 1, setStaffID = None, setActiveStudentCount = None, setAssignmentCount = None, setAssignmentCountForTermCalculated = None, setAssignmentCountYTDCalculated = None, setAssignmentDataString = None, setCreatedTime = None, setDateTimeofLastScoredAssignment = None, setDistrictID = None, setDueDateOfLastAssignmentScored = None, setFamilyStudentAccessStaffNameToUse = None, setFileFolderNumber = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setFutureAssignmentCountForTermCalculated = None, setGradebookLastAccessedTime = None, setGradedAssignmentCountForTermCalculated = None, setGradeLevelLowerBound = None, setGradeLevelUpperBound = None, setIsActiveForDistrict = None, setIsCurrentStaffEntityYear = None, setMissingAssignmentCountForTermCalculated = None, setModifiedTime = None, setNameID = None, setNoCountAssignmentCountForTermCalculated = None, setNonGradedAssignmentCountForTerm = None, setNonGradedAssignmentCountNoStudentAssignmentsForTerm = None, setNonGradedAssignmentCountNoStudentAssignmentsYTD = None, setPercentageOfAssignmentsScoredYTD = None, setScoreClarifierAssignmentCountForTermCalculated = None, setStaffMeetCount = None, setStaffMNID = None, setStaffNumber = None, setStaffWebsite = None, setStudentAssignmentDataString = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffID = False, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFamilyStudentAccessStaffNameToUse = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(StaffID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaff(EntityID = 1, setStaffID = None, setActiveStudentCount = None, setAssignmentCount = None, setAssignmentCountForTermCalculated = None, setAssignmentCountYTDCalculated = None, setAssignmentDataString = None, setCreatedTime = None, setDateTimeofLastScoredAssignment = None, setDistrictID = None, setDueDateOfLastAssignmentScored = None, setFamilyStudentAccessStaffNameToUse = None, setFileFolderNumber = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setFutureAssignmentCountForTermCalculated = None, setGradebookLastAccessedTime = None, setGradedAssignmentCountForTermCalculated = None, setGradeLevelLowerBound = None, setGradeLevelUpperBound = None, setIsActiveForDistrict = None, setIsCurrentStaffEntityYear = None, setMissingAssignmentCountForTermCalculated = None, setModifiedTime = None, setNameID = None, setNoCountAssignmentCountForTermCalculated = None, setNonGradedAssignmentCountForTerm = None, setNonGradedAssignmentCountNoStudentAssignmentsForTerm = None, setNonGradedAssignmentCountNoStudentAssignmentsYTD = None, setPercentageOfAssignmentsScoredYTD = None, setScoreClarifierAssignmentCountForTermCalculated = None, setStaffMeetCount = None, setStaffMNID = None, setStaffNumber = None, setStaffWebsite = None, setStudentAssignmentDataString = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffID = False, returnActiveStudentCount = False, returnAssignmentCount = False, returnAssignmentCountForTermCalculated = False, returnAssignmentCountYTDCalculated = False, returnAssignmentDataString = False, returnCreatedTime = False, returnDateTimeofLastScoredAssignment = False, returnDistrictID = False, returnDueDateOfLastAssignmentScored = False, returnFamilyStudentAccessStaffNameToUse = False, returnFileFolderNumber = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnFutureAssignmentCountForTermCalculated = False, returnGradebookLastAccessedTime = False, returnGradedAssignmentCountForTermCalculated = False, returnGradeLevelLowerBound = False, returnGradeLevelUpperBound = False, returnIsActiveForDistrict = False, returnIsCurrentStaffEntityYear = False, returnMissingAssignmentCountForTermCalculated = False, returnModifiedTime = False, returnNameID = False, returnNoCountAssignmentCountForTermCalculated = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsYTD = False, returnPercentageOfAssignmentsScoredYTD = False, returnScoreClarifierAssignmentCountForTermCalculated = False, returnStaffMeetCount = False, returnStaffMNID = False, returnStaffNumber = False, returnStaffWebsite = False, returnStudentAssignmentDataString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaff(StaffID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/Staff/" + str(StaffID), verb = "delete")


def getEveryStaffStaffType(searchConditions = [], EntityID = 1, returnStaffStaffTypeID = False, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StaffStaffType in the district.

    This function returns a dataframe of every StaffStaffType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStaffStaffType(StaffStaffTypeID, EntityID = 1, returnStaffStaffTypeID = False, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(StaffStaffTypeID), verb = "get", return_params_list = return_params)

def modifyStaffStaffType(StaffStaffTypeID, EntityID = 1, setStaffStaffTypeID = None, setCreatedTime = None, setEndDate = None, setIsPrimary = None, setModifiedTime = None, setStaffID = None, setStaffStaffTypeIDClonedFrom = None, setStaffTypeID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffStaffTypeID = False, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(StaffStaffTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaffStaffType(EntityID = 1, setStaffStaffTypeID = None, setCreatedTime = None, setEndDate = None, setIsPrimary = None, setModifiedTime = None, setStaffID = None, setStaffStaffTypeIDClonedFrom = None, setStaffTypeID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffStaffTypeID = False, returnCreatedTime = False, returnEndDate = False, returnIsPrimary = False, returnModifiedTime = False, returnStaffID = False, returnStaffStaffTypeIDClonedFrom = False, returnStaffTypeID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaffStaffType(StaffStaffTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffStaffType/" + str(StaffStaffTypeID), verb = "delete")


def getEveryStaffType(searchConditions = [], EntityID = 1, returnStaffTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StaffType in the district.

    This function returns a dataframe of every StaffType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStaffType(StaffTypeID, EntityID = 1, returnStaffTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(StaffTypeID), verb = "get", return_params_list = return_params)

def modifyStaffType(StaffTypeID, EntityID = 1, setStaffTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setStaffTypeIDClonedFrom = None, setStaffTypeIDClonedTo = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(StaffTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaffType(EntityID = 1, setStaffTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setStaffTypeIDClonedFrom = None, setStaffTypeIDClonedTo = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStaffTypeIDClonedFrom = False, returnStaffTypeIDClonedTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaffType(StaffTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Staff/StaffType/" + str(StaffTypeID), verb = "delete")