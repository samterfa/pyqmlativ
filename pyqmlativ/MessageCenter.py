# This module contains MessageCenter functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setNumberOfDaysAfterWithdrawalToAllowMessages = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setNumberOfDaysAfterWithdrawalToAllowMessages = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnNumberOfDaysAfterWithdrawalToAllowMessages = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")


def getEveryConfigDistrictYearWithdrawalCode(searchConditions = [], EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigDistrictYearWithdrawalCode in the district.

    This function returns a dataframe of every ConfigDistrictYearWithdrawalCode in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, setConfigDistrictYearWithdrawalCodeID = None, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYearWithdrawalCode(EntityID = 1, setConfigDistrictYearWithdrawalCodeID = None, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "delete")


def getEveryMessage(searchConditions = [], EntityID = 1, returnMessageID = False, returnContent = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailsSent = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Message in the district.

    This function returns a dataframe of every Message in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMessage(MessageID, EntityID = 1, returnMessageID = False, returnContent = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailsSent = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(MessageID), verb = "get", return_params_list = return_params)

def modifyMessage(MessageID, EntityID = 1, setMessageID = None, setContent = None, setCreatedTime = None, setEmailRecipientType = None, setEmailsSent = None, setFromInformation = None, setIncludeLinkToObject = None, setIsHidden = None, setIsRead = None, setMessageIDCopiedFrom = None, setMessageMasterID = None, setModifiedTime = None, setNoSourceIDRequired = None, setObjectIDCreatedFor = None, setObjectPrimaryKey = None, setPostDate = None, setPriorityType = None, setPriorityTypeCode = None, setSourceIDCreatedFor = None, setSubject = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRecipient = None, returnMessageID = False, returnContent = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailsSent = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(MessageID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMessage(EntityID = 1, setMessageID = None, setContent = None, setCreatedTime = None, setEmailRecipientType = None, setEmailsSent = None, setFromInformation = None, setIncludeLinkToObject = None, setIsHidden = None, setIsRead = None, setMessageIDCopiedFrom = None, setMessageMasterID = None, setModifiedTime = None, setNoSourceIDRequired = None, setObjectIDCreatedFor = None, setObjectPrimaryKey = None, setPostDate = None, setPriorityType = None, setPriorityTypeCode = None, setSourceIDCreatedFor = None, setSubject = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRecipient = None, returnMessageID = False, returnContent = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailsSent = False, returnFromInformation = False, returnIncludeLinkToObject = False, returnIsHidden = False, returnIsRead = False, returnMessageIDCopiedFrom = False, returnMessageMasterID = False, returnModifiedTime = False, returnNoSourceIDRequired = False, returnObjectIDCreatedFor = False, returnObjectPrimaryKey = False, returnPostDate = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSourceIDCreatedFor = False, returnSubject = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRecipient = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMessage(MessageID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Message/" + str(MessageID), verb = "delete")


def getEveryMessageMaster(searchConditions = [], EntityID = 1, returnMessageMasterID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MessageMaster in the district.

    This function returns a dataframe of every MessageMaster in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMessageMaster(MessageMasterID, EntityID = 1, returnMessageMasterID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(MessageMasterID), verb = "get", return_params_list = return_params)

def modifyMessageMaster(MessageMasterID, EntityID = 1, setMessageMasterID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCarbonCopyStaffIDList = None, setContent = None, setCreatedTime = None, setCustomMessageData = None, setEntityID = None, setIncludeRestrictedGuardians = None, setIsDraft = None, setIsRetracted = None, setLargestMessagePrimaryKey = None, setModifiedTime = None, setObjectIDCreatedFor = None, setPostedTime = None, setPriorityType = None, setPriorityTypeCode = None, setSchoolYearID = None, setSearchConditionFilter = None, setSourceIDCreatedFor = None, setStatus = None, setStatusCode = None, setSubject = None, setSubjectCleaned = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXMLFilter = None, returnMessageMasterID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(MessageMasterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMessageMaster(EntityID = 1, setMessageMasterID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCarbonCopyStaffIDList = None, setContent = None, setCreatedTime = None, setCustomMessageData = None, setEntityID = None, setIncludeRestrictedGuardians = None, setIsDraft = None, setIsRetracted = None, setLargestMessagePrimaryKey = None, setModifiedTime = None, setObjectIDCreatedFor = None, setPostedTime = None, setPriorityType = None, setPriorityTypeCode = None, setSchoolYearID = None, setSearchConditionFilter = None, setSourceIDCreatedFor = None, setStatus = None, setStatusCode = None, setSubject = None, setSubjectCleaned = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXMLFilter = None, returnMessageMasterID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCarbonCopyStaffIDList = False, returnContent = False, returnCreatedTime = False, returnCustomMessageData = False, returnEntityID = False, returnIncludeRestrictedGuardians = False, returnIsDraft = False, returnIsRetracted = False, returnLargestMessagePrimaryKey = False, returnModifiedTime = False, returnObjectIDCreatedFor = False, returnPostedTime = False, returnPriorityType = False, returnPriorityTypeCode = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSourceIDCreatedFor = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMessageMaster(MessageMasterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/MessageMaster/" + str(MessageMasterID), verb = "delete")


def getEveryNotification(searchConditions = [], EntityID = 1, returnNotificationID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Notification in the district.

    This function returns a dataframe of every Notification in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotification(NotificationID, EntityID = 1, returnNotificationID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(NotificationID), verb = "get", return_params_list = return_params)

def modifyNotification(NotificationID, EntityID = 1, setNotificationID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setAttendanceCategoryForCount = None, setAttendanceCategoryForCountCode = None, setAttendanceCountHigh = None, setAttendanceCountLow = None, setAttendanceCountMethod = None, setAttendanceCountMethodCode = None, setConsiderAllStaffMeets = None, setCreatedTime = None, setDayType = None, setDayTypeCode = None, setEntityID = None, setFeeManagementBalanceHigh = None, setFeeManagementBalanceLow = None, setFoodServiceBalanceHigh = None, setFoodServiceBalanceLow = None, setGradingPeriodEndDaysAfter = None, setGradingPeriodEndDaysBefore = None, setIncludeAutoGeneratedMessage = None, setLastEntryType = None, setLastEntryTypeCode = None, setMessage = None, setModifiedTime = None, setNumberOfDays = None, setPriorityType = None, setPriorityTypeCode = None, setScheduledTaskID = None, setScheduleIsAvailableDaysBefore = None, setSchoolYearID = None, setSearchConditionFilter = None, setSendNotificationForDay = None, setSendNotificationForDayCode = None, setSendNotificationForPriorDayCount = None, setSendOnlyIfGuardianNotNotified = None, setSendToDisciplineOfficer = None, setSubject = None, setSubjectCleaned = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setUnrecordedAttendanceMinutes = None, setUnrecordedAttendancePeriodType = None, setUnrecordedAttendancePeriodTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXMLFilter = None, returnNotificationID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(NotificationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotification(EntityID = 1, setNotificationID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setAttendanceCategoryForCount = None, setAttendanceCategoryForCountCode = None, setAttendanceCountHigh = None, setAttendanceCountLow = None, setAttendanceCountMethod = None, setAttendanceCountMethodCode = None, setConsiderAllStaffMeets = None, setCreatedTime = None, setDayType = None, setDayTypeCode = None, setEntityID = None, setFeeManagementBalanceHigh = None, setFeeManagementBalanceLow = None, setFoodServiceBalanceHigh = None, setFoodServiceBalanceLow = None, setGradingPeriodEndDaysAfter = None, setGradingPeriodEndDaysBefore = None, setIncludeAutoGeneratedMessage = None, setLastEntryType = None, setLastEntryTypeCode = None, setMessage = None, setModifiedTime = None, setNumberOfDays = None, setPriorityType = None, setPriorityTypeCode = None, setScheduledTaskID = None, setScheduleIsAvailableDaysBefore = None, setSchoolYearID = None, setSearchConditionFilter = None, setSendNotificationForDay = None, setSendNotificationForDayCode = None, setSendNotificationForPriorDayCount = None, setSendOnlyIfGuardianNotNotified = None, setSendToDisciplineOfficer = None, setSubject = None, setSubjectCleaned = None, setToWhom = None, setToWhomCode = None, setType = None, setTypeCode = None, setUnrecordedAttendanceMinutes = None, setUnrecordedAttendancePeriodType = None, setUnrecordedAttendancePeriodTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXMLFilter = None, returnNotificationID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAttendanceCategoryForCount = False, returnAttendanceCategoryForCountCode = False, returnAttendanceCountHigh = False, returnAttendanceCountLow = False, returnAttendanceCountMethod = False, returnAttendanceCountMethodCode = False, returnConsiderAllStaffMeets = False, returnCreatedTime = False, returnDayType = False, returnDayTypeCode = False, returnEntityID = False, returnFeeManagementBalanceHigh = False, returnFeeManagementBalanceLow = False, returnFoodServiceBalanceHigh = False, returnFoodServiceBalanceLow = False, returnGradingPeriodEndDaysAfter = False, returnGradingPeriodEndDaysBefore = False, returnIncludeAutoGeneratedMessage = False, returnLastEntryType = False, returnLastEntryTypeCode = False, returnMessage = False, returnModifiedTime = False, returnNumberOfDays = False, returnPriorityType = False, returnPriorityTypeCode = False, returnScheduledTaskID = False, returnScheduleIsAvailableDaysBefore = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnSendNotificationForDay = False, returnSendNotificationForDayCode = False, returnSendNotificationForPriorDayCount = False, returnSendOnlyIfGuardianNotNotified = False, returnSendToDisciplineOfficer = False, returnSubject = False, returnSubjectCleaned = False, returnToWhom = False, returnToWhomCode = False, returnType = False, returnTypeCode = False, returnUnrecordedAttendanceMinutes = False, returnUnrecordedAttendancePeriodType = False, returnUnrecordedAttendancePeriodTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLFilter = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotification(NotificationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/Notification/" + str(NotificationID), verb = "delete")


def getEveryNotificationAction(searchConditions = [], EntityID = 1, returnNotificationActionID = False, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationAction in the district.

    This function returns a dataframe of every NotificationAction in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationAction(NotificationActionID, EntityID = 1, returnNotificationActionID = False, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(NotificationActionID), verb = "get", return_params_list = return_params)

def modifyNotificationAction(NotificationActionID, EntityID = 1, setNotificationActionID = None, setActionID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationActionID = False, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(NotificationActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationAction(EntityID = 1, setNotificationActionID = None, setActionID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationActionID = False, returnActionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationAction(NotificationActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAction/" + str(NotificationActionID), verb = "delete")


def getEveryNotificationAttendanceType(searchConditions = [], EntityID = 1, returnNotificationAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationAttendanceType in the district.

    This function returns a dataframe of every NotificationAttendanceType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1, returnNotificationAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(NotificationAttendanceTypeID), verb = "get", return_params_list = return_params)

def modifyNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1, setNotificationAttendanceTypeID = None, setAttendanceTypeID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(NotificationAttendanceTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationAttendanceType(EntityID = 1, setNotificationAttendanceTypeID = None, setAttendanceTypeID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationAttendanceType(NotificationAttendanceTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationAttendanceType/" + str(NotificationAttendanceTypeID), verb = "delete")


def getEveryNotificationCarbonCopyStaff(searchConditions = [], EntityID = 1, returnNotificationCarbonCopyStaffID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationCarbonCopyStaff in the district.

    This function returns a dataframe of every NotificationCarbonCopyStaff in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1, returnNotificationCarbonCopyStaffID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(NotificationCarbonCopyStaffID), verb = "get", return_params_list = return_params)

def modifyNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1, setNotificationCarbonCopyStaffID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationCarbonCopyStaffID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(NotificationCarbonCopyStaffID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationCarbonCopyStaff(EntityID = 1, setNotificationCarbonCopyStaffID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationCarbonCopyStaffID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationCarbonCopyStaff(NotificationCarbonCopyStaffID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationCarbonCopyStaff/" + str(NotificationCarbonCopyStaffID), verb = "delete")


def getEveryNotificationDisciplineThreshold(searchConditions = [], EntityID = 1, returnNotificationDisciplineThresholdID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationDisciplineThreshold in the district.

    This function returns a dataframe of every NotificationDisciplineThreshold in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1, returnNotificationDisciplineThresholdID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(NotificationDisciplineThresholdID), verb = "get", return_params_list = return_params)

def modifyNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1, setNotificationDisciplineThresholdID = None, setCreatedTime = None, setDisciplineThresholdID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationDisciplineThresholdID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(NotificationDisciplineThresholdID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationDisciplineThreshold(EntityID = 1, setNotificationDisciplineThresholdID = None, setCreatedTime = None, setDisciplineThresholdID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationDisciplineThresholdID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationDisciplineThreshold(NotificationDisciplineThresholdID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationDisciplineThreshold/" + str(NotificationDisciplineThresholdID), verb = "delete")


def getEveryNotificationGradeBucket(searchConditions = [], EntityID = 1, returnNotificationGradeBucketID = False, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationGradeBucket in the district.

    This function returns a dataframe of every NotificationGradeBucket in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1, returnNotificationGradeBucketID = False, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(NotificationGradeBucketID), verb = "get", return_params_list = return_params)

def modifyNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1, setNotificationGradeBucketID = None, setCreatedTime = None, setGradeBucketID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationGradeBucketID = False, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(NotificationGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationGradeBucket(EntityID = 1, setNotificationGradeBucketID = None, setCreatedTime = None, setGradeBucketID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationGradeBucketID = False, returnCreatedTime = False, returnGradeBucketID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationGradeBucket(NotificationGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeBucket/" + str(NotificationGradeBucketID), verb = "delete")


def getEveryNotificationGradeMark(searchConditions = [], EntityID = 1, returnNotificationGradeMarkID = False, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationGradeMark in the district.

    This function returns a dataframe of every NotificationGradeMark in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationGradeMark(NotificationGradeMarkID, EntityID = 1, returnNotificationGradeMarkID = False, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(NotificationGradeMarkID), verb = "get", return_params_list = return_params)

def modifyNotificationGradeMark(NotificationGradeMarkID, EntityID = 1, setNotificationGradeMarkID = None, setCreatedTime = None, setGradeMarkID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationGradeMarkID = False, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(NotificationGradeMarkID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationGradeMark(EntityID = 1, setNotificationGradeMarkID = None, setCreatedTime = None, setGradeMarkID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationGradeMarkID = False, returnCreatedTime = False, returnGradeMarkID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationGradeMark(NotificationGradeMarkID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeMark/" + str(NotificationGradeMarkID), verb = "delete")


def getEveryNotificationGradeReference(searchConditions = [], EntityID = 1, returnNotificationGradeReferenceID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationGradeReference in the district.

    This function returns a dataframe of every NotificationGradeReference in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1, returnNotificationGradeReferenceID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(NotificationGradeReferenceID), verb = "get", return_params_list = return_params)

def modifyNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1, setNotificationGradeReferenceID = None, setCreatedTime = None, setGradeReferenceID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationGradeReferenceID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(NotificationGradeReferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationGradeReference(EntityID = 1, setNotificationGradeReferenceID = None, setCreatedTime = None, setGradeReferenceID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationGradeReferenceID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationGradeReference(NotificationGradeReferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationGradeReference/" + str(NotificationGradeReferenceID), verb = "delete")


def getEveryNotificationOffense(searchConditions = [], EntityID = 1, returnNotificationOffenseID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationOffense in the district.

    This function returns a dataframe of every NotificationOffense in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationOffense(NotificationOffenseID, EntityID = 1, returnNotificationOffenseID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(NotificationOffenseID), verb = "get", return_params_list = return_params)

def modifyNotificationOffense(NotificationOffenseID, EntityID = 1, setNotificationOffenseID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationOffenseID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(NotificationOffenseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationOffense(EntityID = 1, setNotificationOffenseID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationOffenseID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationOffense(NotificationOffenseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOffense/" + str(NotificationOffenseID), verb = "delete")


def getEveryNotificationOnlineForm(searchConditions = [], EntityID = 1, returnNotificationOnlineFormID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationOnlineForm in the district.

    This function returns a dataframe of every NotificationOnlineForm in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1, returnNotificationOnlineFormID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(NotificationOnlineFormID), verb = "get", return_params_list = return_params)

def modifyNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1, setNotificationOnlineFormID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationOnlineFormID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(NotificationOnlineFormID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationOnlineForm(EntityID = 1, setNotificationOnlineFormID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationOnlineFormID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationOnlineForm(NotificationOnlineFormID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationOnlineForm/" + str(NotificationOnlineFormID), verb = "delete")


def getEveryNotificationScheduleIsAvailableSectionLength(searchConditions = [], EntityID = 1, returnNotificationScheduleIsAvailableSectionLengthID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationScheduleIsAvailableSectionLength in the district.

    This function returns a dataframe of every NotificationScheduleIsAvailableSectionLength in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1, returnNotificationScheduleIsAvailableSectionLengthID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(NotificationScheduleIsAvailableSectionLengthID), verb = "get", return_params_list = return_params)

def modifyNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1, setNotificationScheduleIsAvailableSectionLengthID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setSectionLengthID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationScheduleIsAvailableSectionLengthID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(NotificationScheduleIsAvailableSectionLengthID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationScheduleIsAvailableSectionLength(EntityID = 1, setNotificationScheduleIsAvailableSectionLengthID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setSectionLengthID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationScheduleIsAvailableSectionLengthID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationScheduleIsAvailableSectionLength(NotificationScheduleIsAvailableSectionLengthID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationScheduleIsAvailableSectionLength/" + str(NotificationScheduleIsAvailableSectionLengthID), verb = "delete")


def getEveryNotificationUnrecordedClassAttendance(searchConditions = [], EntityID = 1, returnNotificationUnrecordedClassAttendanceID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationUnrecordedClassAttendance in the district.

    This function returns a dataframe of every NotificationUnrecordedClassAttendance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1, returnNotificationUnrecordedClassAttendanceID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(NotificationUnrecordedClassAttendanceID), verb = "get", return_params_list = return_params)

def modifyNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1, setNotificationUnrecordedClassAttendanceID = None, setCreatedTime = None, setDisplayPeriodID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationUnrecordedClassAttendanceID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(NotificationUnrecordedClassAttendanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationUnrecordedClassAttendance(EntityID = 1, setNotificationUnrecordedClassAttendanceID = None, setCreatedTime = None, setDisplayPeriodID = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationUnrecordedClassAttendanceID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationUnrecordedClassAttendance(NotificationUnrecordedClassAttendanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationUnrecordedClassAttendance/" + str(NotificationUnrecordedClassAttendanceID), verb = "delete")


def getEveryNotificationWithdrawalCode(searchConditions = [], EntityID = 1, returnNotificationWithdrawalCodeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationWithdrawalCode in the district.

    This function returns a dataframe of every NotificationWithdrawalCode in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1, returnNotificationWithdrawalCodeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(NotificationWithdrawalCodeID), verb = "get", return_params_list = return_params)

def modifyNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1, setNotificationWithdrawalCodeID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, returnNotificationWithdrawalCodeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(NotificationWithdrawalCodeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationWithdrawalCode(EntityID = 1, setNotificationWithdrawalCodeID = None, setCreatedTime = None, setModifiedTime = None, setNotificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, returnNotificationWithdrawalCodeID = False, returnCreatedTime = False, returnModifiedTime = False, returnNotificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationWithdrawalCode(NotificationWithdrawalCodeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/NotificationWithdrawalCode/" + str(NotificationWithdrawalCodeID), verb = "delete")


def getEveryQueuedCompletedCareerPlanChangeNotification(searchConditions = [], EntityID = 1, returnQueuedCompletedCareerPlanChangeNotificationID = False, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every QueuedCompletedCareerPlanChangeNotification in the district.

    This function returns a dataframe of every QueuedCompletedCareerPlanChangeNotification in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1, returnQueuedCompletedCareerPlanChangeNotificationID = False, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(QueuedCompletedCareerPlanChangeNotificationID), verb = "get", return_params_list = return_params)

def modifyQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1, setQueuedCompletedCareerPlanChangeNotificationID = None, setCareerPlanGradeLevelIDCurrent = None, setCareerPlanGradeLevelIDPrevious = None, setCreatedTime = None, setCreditsCurrent = None, setCreditsPrevious = None, setCurriculumID = None, setEntityID = None, setIsDeletedRecord = None, setIsNewRecord = None, setIsSent = None, setIsStudentPermittedToChangeGradeLevelCurrent = None, setIsStudentPermittedToChangeGradeLevelPrevious = None, setIsStudentPermittedToDeleteCurrent = None, setIsStudentPermittedToDeletePrevious = None, setModifiedTime = None, setNotificationID = None, setSchoolYearID = None, setStudentCareerPlanID = None, setStudentCourseRequestIDCurrent = None, setStudentCourseRequestIDPrevious = None, setStudentID = None, setStudentSubAreaIDCurrent = None, setStudentSubAreaIDPrevious = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQueuedCompletedCareerPlanChangeNotificationID = False, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(QueuedCompletedCareerPlanChangeNotificationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQueuedCompletedCareerPlanChangeNotification(EntityID = 1, setQueuedCompletedCareerPlanChangeNotificationID = None, setCareerPlanGradeLevelIDCurrent = None, setCareerPlanGradeLevelIDPrevious = None, setCreatedTime = None, setCreditsCurrent = None, setCreditsPrevious = None, setCurriculumID = None, setEntityID = None, setIsDeletedRecord = None, setIsNewRecord = None, setIsSent = None, setIsStudentPermittedToChangeGradeLevelCurrent = None, setIsStudentPermittedToChangeGradeLevelPrevious = None, setIsStudentPermittedToDeleteCurrent = None, setIsStudentPermittedToDeletePrevious = None, setModifiedTime = None, setNotificationID = None, setSchoolYearID = None, setStudentCareerPlanID = None, setStudentCourseRequestIDCurrent = None, setStudentCourseRequestIDPrevious = None, setStudentID = None, setStudentSubAreaIDCurrent = None, setStudentSubAreaIDPrevious = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQueuedCompletedCareerPlanChangeNotificationID = False, returnCareerPlanGradeLevelIDCurrent = False, returnCareerPlanGradeLevelIDPrevious = False, returnCreatedTime = False, returnCreditsCurrent = False, returnCreditsPrevious = False, returnCurriculumID = False, returnEntityID = False, returnIsDeletedRecord = False, returnIsNewRecord = False, returnIsSent = False, returnIsStudentPermittedToChangeGradeLevelCurrent = False, returnIsStudentPermittedToChangeGradeLevelPrevious = False, returnIsStudentPermittedToDeleteCurrent = False, returnIsStudentPermittedToDeletePrevious = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentCareerPlanID = False, returnStudentCourseRequestIDCurrent = False, returnStudentCourseRequestIDPrevious = False, returnStudentID = False, returnStudentSubAreaIDCurrent = False, returnStudentSubAreaIDPrevious = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQueuedCompletedCareerPlanChangeNotification(QueuedCompletedCareerPlanChangeNotificationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedCareerPlanChangeNotification/" + str(QueuedCompletedCareerPlanChangeNotificationID), verb = "delete")


def getEveryQueuedCompletedGradeChangeNotification(searchConditions = [], EntityID = 1, returnQueuedCompletedGradeChangeNotificationID = False, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every QueuedCompletedGradeChangeNotification in the district.

    This function returns a dataframe of every QueuedCompletedGradeChangeNotification in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1, returnQueuedCompletedGradeChangeNotificationID = False, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(QueuedCompletedGradeChangeNotificationID), verb = "get", return_params_list = return_params)

def modifyQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1, setQueuedCompletedGradeChangeNotificationID = None, setCreatedTime = None, setEntityID = None, setGradeMarkIDCurrent = None, setGradeMarkIDPrevious = None, setIsSent = None, setModifiedTime = None, setNotificationID = None, setSchoolYearID = None, setStudentGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQueuedCompletedGradeChangeNotificationID = False, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(QueuedCompletedGradeChangeNotificationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQueuedCompletedGradeChangeNotification(EntityID = 1, setQueuedCompletedGradeChangeNotificationID = None, setCreatedTime = None, setEntityID = None, setGradeMarkIDCurrent = None, setGradeMarkIDPrevious = None, setIsSent = None, setModifiedTime = None, setNotificationID = None, setSchoolYearID = None, setStudentGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQueuedCompletedGradeChangeNotificationID = False, returnCreatedTime = False, returnEntityID = False, returnGradeMarkIDCurrent = False, returnGradeMarkIDPrevious = False, returnIsSent = False, returnModifiedTime = False, returnNotificationID = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQueuedCompletedGradeChangeNotification(QueuedCompletedGradeChangeNotificationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/QueuedCompletedGradeChangeNotification/" + str(QueuedCompletedGradeChangeNotificationID), verb = "delete")


def getEverySystemEmailTypeConfig(searchConditions = [], EntityID = 1, returnSystemEmailTypeConfigID = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailTypeID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SystemEmailTypeConfig in the district.

    This function returns a dataframe of every SystemEmailTypeConfig in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSystemEmailTypeConfig(SystemEmailTypeConfigID, EntityID = 1, returnSystemEmailTypeConfigID = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailTypeID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/" + str(SystemEmailTypeConfigID), verb = "get", return_params_list = return_params)

def modifySystemEmailTypeConfig(SystemEmailTypeConfigID, EntityID = 1, setSystemEmailTypeConfigID = None, setCreatedTime = None, setEmailRecipientType = None, setEmailTypeID = None, setModifiedTime = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSystemEmailTypeConfigID = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailTypeID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/" + str(SystemEmailTypeConfigID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSystemEmailTypeConfig(EntityID = 1, setSystemEmailTypeConfigID = None, setCreatedTime = None, setEmailRecipientType = None, setEmailTypeID = None, setModifiedTime = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSystemEmailTypeConfigID = False, returnCreatedTime = False, returnEmailRecipientType = False, returnEmailTypeID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSystemEmailTypeConfig(SystemEmailTypeConfigID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/SystemEmailTypeConfig/" + str(SystemEmailTypeConfigID), verb = "delete")


def getEveryTempMessage(searchConditions = [], EntityID = 1, returnTempMessageID = False, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempMessage in the district.

    This function returns a dataframe of every TempMessage in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempMessage(TempMessageID, EntityID = 1, returnTempMessageID = False, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(TempMessageID), verb = "get", return_params_list = return_params)

def modifyTempMessage(TempMessageID, EntityID = 1, setTempMessageID = None, setCreatedTime = None, setModifiedTime = None, setRecipientName = None, setRelationship = None, setSectionInfo = None, setStudentName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMessageID = False, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(TempMessageID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempMessage(EntityID = 1, setTempMessageID = None, setCreatedTime = None, setModifiedTime = None, setRecipientName = None, setRelationship = None, setSectionInfo = None, setStudentName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMessageID = False, returnCreatedTime = False, returnModifiedTime = False, returnRecipientName = False, returnRelationship = False, returnSectionInfo = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempMessage(TempMessageID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/TempMessage/" + str(TempMessageID), verb = "delete")


def getEveryUserMessageSetting(searchConditions = [], EntityID = 1, returnUserMessageSettingID = False, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFamilyAccessMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserMessageSetting in the district.

    This function returns a dataframe of every UserMessageSetting in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserMessageSetting(UserMessageSettingID, EntityID = 1, returnUserMessageSettingID = False, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFamilyAccessMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(UserMessageSettingID), verb = "get", return_params_list = return_params)

def modifyUserMessageSetting(UserMessageSettingID, EntityID = 1, setUserMessageSettingID = None, setAssignmentScoreHighNotification = None, setAssignmentScoreHighNotificationEmail = None, setAssignmentScoreLowNotification = None, setAssignmentScoreLowNotificationEmail = None, setCopyAttendanceMessagesToEmail = None, setCopyDisciplineMessagesToEmail = None, setCopyEnrollmentMessagesToEmail = None, setCopyFamilyAccessMessagesToEmail = None, setCopyFeeManagementMessagesToEmail = None, setCopyFoodServiceMessagesToEmail = None, setCopyGradebookMessagesToEmail = None, setCopyGradingMessagesToEmail = None, setCopyGraduationRequirementsMessagesToEmail = None, setCopyMessagesToEmail = None, setCopyOnlineFormMessagesToEmail = None, setCopySchedulingMessagesToEmail = None, setCreatedTime = None, setCurrentGradeScoreHighNotification = None, setCurrentGradeScoreHighNotificationEmail = None, setCurrentGradeScoreLowNotification = None, setCurrentGradeScoreLowNotificationEmail = None, setEnableCompletedCareerPlanChangeNotification = None, setEnableCompletedCareerPlanChangeNotificationEmail = None, setEnableCompletedGradeChangeNotification = None, setEnableCompletedGradeChangeNotificationEmail = None, setEnableGradebookGradeChangeRequestDeniedEmail = None, setEnableGradebookGradeChangeRequestNotificationEmail = None, setEnableGradebookLastEntryNotificationEmail = None, setEnableOnlineAssignmentAvailableNotificationEmail = None, setEnableOnlineAssingmentScoresAvailableNotificationEmail = None, setEnableStudentScheduleChangeNotification = None, setEnableStudentScheduleChangeNotificationEmail = None, setGradebookHighAssignmentThreshold = None, setGradebookHighThreshold = None, setGradebookLowAssignmentThreshold = None, setGradebookLowThreshold = None, setMissingAssignmentNotification = None, setMissingAssignmentNotificationEmail = None, setModifiedTime = None, setOnlySendAssignmentScoreHighNotificationsOncePerAssignment = None, setOnlySendAssignmentScoreLowNotificationsOncePerAssignment = None, setOnlySendCurrentGradeScoreHighNotificationsOnce = None, setOnlySendCurrentGradeScoreLowNotificationsOnce = None, setOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = None, setOnlySendMissingAssignmentNotificationsOncePerAssignment = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnUserMessageSettingID = False, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFamilyAccessMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(UserMessageSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserMessageSetting(EntityID = 1, setUserMessageSettingID = None, setAssignmentScoreHighNotification = None, setAssignmentScoreHighNotificationEmail = None, setAssignmentScoreLowNotification = None, setAssignmentScoreLowNotificationEmail = None, setCopyAttendanceMessagesToEmail = None, setCopyDisciplineMessagesToEmail = None, setCopyEnrollmentMessagesToEmail = None, setCopyFamilyAccessMessagesToEmail = None, setCopyFeeManagementMessagesToEmail = None, setCopyFoodServiceMessagesToEmail = None, setCopyGradebookMessagesToEmail = None, setCopyGradingMessagesToEmail = None, setCopyGraduationRequirementsMessagesToEmail = None, setCopyMessagesToEmail = None, setCopyOnlineFormMessagesToEmail = None, setCopySchedulingMessagesToEmail = None, setCreatedTime = None, setCurrentGradeScoreHighNotification = None, setCurrentGradeScoreHighNotificationEmail = None, setCurrentGradeScoreLowNotification = None, setCurrentGradeScoreLowNotificationEmail = None, setEnableCompletedCareerPlanChangeNotification = None, setEnableCompletedCareerPlanChangeNotificationEmail = None, setEnableCompletedGradeChangeNotification = None, setEnableCompletedGradeChangeNotificationEmail = None, setEnableGradebookGradeChangeRequestDeniedEmail = None, setEnableGradebookGradeChangeRequestNotificationEmail = None, setEnableGradebookLastEntryNotificationEmail = None, setEnableOnlineAssignmentAvailableNotificationEmail = None, setEnableOnlineAssingmentScoresAvailableNotificationEmail = None, setEnableStudentScheduleChangeNotification = None, setEnableStudentScheduleChangeNotificationEmail = None, setGradebookHighAssignmentThreshold = None, setGradebookHighThreshold = None, setGradebookLowAssignmentThreshold = None, setGradebookLowThreshold = None, setMissingAssignmentNotification = None, setMissingAssignmentNotificationEmail = None, setModifiedTime = None, setOnlySendAssignmentScoreHighNotificationsOncePerAssignment = None, setOnlySendAssignmentScoreLowNotificationsOncePerAssignment = None, setOnlySendCurrentGradeScoreHighNotificationsOnce = None, setOnlySendCurrentGradeScoreLowNotificationsOnce = None, setOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = None, setOnlySendMissingAssignmentNotificationsOncePerAssignment = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnUserMessageSettingID = False, returnAssignmentScoreHighNotification = False, returnAssignmentScoreHighNotificationEmail = False, returnAssignmentScoreLowNotification = False, returnAssignmentScoreLowNotificationEmail = False, returnCopyAttendanceMessagesToEmail = False, returnCopyDisciplineMessagesToEmail = False, returnCopyEnrollmentMessagesToEmail = False, returnCopyFamilyAccessMessagesToEmail = False, returnCopyFeeManagementMessagesToEmail = False, returnCopyFoodServiceMessagesToEmail = False, returnCopyGradebookMessagesToEmail = False, returnCopyGradingMessagesToEmail = False, returnCopyGraduationRequirementsMessagesToEmail = False, returnCopyMessagesToEmail = False, returnCopyOnlineFormMessagesToEmail = False, returnCopySchedulingMessagesToEmail = False, returnCreatedTime = False, returnCurrentGradeScoreHighNotification = False, returnCurrentGradeScoreHighNotificationEmail = False, returnCurrentGradeScoreLowNotification = False, returnCurrentGradeScoreLowNotificationEmail = False, returnEnableCompletedCareerPlanChangeNotification = False, returnEnableCompletedCareerPlanChangeNotificationEmail = False, returnEnableCompletedGradeChangeNotification = False, returnEnableCompletedGradeChangeNotificationEmail = False, returnEnableGradebookGradeChangeRequestDeniedEmail = False, returnEnableGradebookGradeChangeRequestNotificationEmail = False, returnEnableGradebookLastEntryNotificationEmail = False, returnEnableOnlineAssignmentAvailableNotificationEmail = False, returnEnableOnlineAssingmentScoresAvailableNotificationEmail = False, returnEnableStudentScheduleChangeNotification = False, returnEnableStudentScheduleChangeNotificationEmail = False, returnGradebookHighAssignmentThreshold = False, returnGradebookHighThreshold = False, returnGradebookLowAssignmentThreshold = False, returnGradebookLowThreshold = False, returnMissingAssignmentNotification = False, returnMissingAssignmentNotificationEmail = False, returnModifiedTime = False, returnOnlySendAssignmentScoreHighNotificationsOncePerAssignment = False, returnOnlySendAssignmentScoreLowNotificationsOncePerAssignment = False, returnOnlySendCurrentGradeScoreHighNotificationsOnce = False, returnOnlySendCurrentGradeScoreLowNotificationsOnce = False, returnOnlySendMissingAssignmentNotificationForCurrentGradingPeriod = False, returnOnlySendMissingAssignmentNotificationsOncePerAssignment = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserMessageSetting(UserMessageSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/MessageCenter/UserMessageSetting/" + str(UserMessageSettingID), verb = "delete")