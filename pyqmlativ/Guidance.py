# This module contains Guidance functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryNotificationMethod(searchConditions = [], EntityID = 1, returnNotificationMethodID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NotificationMethod in the district.

    This function returns a dataframe of every NotificationMethod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNotificationMethod(NotificationMethodID, EntityID = 1, returnNotificationMethodID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(NotificationMethodID), verb = "get", return_params_list = return_params)

def modifyNotificationMethod(NotificationMethodID, EntityID = 1, setNotificationMethodID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationMethodID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(NotificationMethodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNotificationMethod(EntityID = 1, setNotificationMethodID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNotificationMethodID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNotificationMethod(NotificationMethodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(NotificationMethodID), verb = "delete")


def getEveryOfficeVisitComment(searchConditions = [], EntityID = 1, returnOfficeVisitCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OfficeVisitComment in the district.

    This function returns a dataframe of every OfficeVisitComment in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOfficeVisitComment(OfficeVisitCommentID, EntityID = 1, returnOfficeVisitCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "get", return_params_list = return_params)

def modifyOfficeVisitComment(OfficeVisitCommentID, EntityID = 1, setOfficeVisitCommentID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOfficeVisitCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOfficeVisitComment(EntityID = 1, setOfficeVisitCommentID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOfficeVisitCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOfficeVisitComment(OfficeVisitCommentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "delete")


def getEveryOfficeVisitGuardianResponse(searchConditions = [], EntityID = 1, returnOfficeVisitGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OfficeVisitGuardianResponse in the district.

    This function returns a dataframe of every OfficeVisitGuardianResponse in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1, returnOfficeVisitGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "get", return_params_list = return_params)

def modifyOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1, setOfficeVisitGuardianResponseID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOfficeVisitGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOfficeVisitGuardianResponse(EntityID = 1, setOfficeVisitGuardianResponseID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOfficeVisitGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "delete")


def getEveryOfficeVisitReason(searchConditions = [], EntityID = 1, returnOfficeVisitReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OfficeVisitReason in the district.

    This function returns a dataframe of every OfficeVisitReason in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOfficeVisitReason(OfficeVisitReasonID, EntityID = 1, returnOfficeVisitReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "get", return_params_list = return_params)

def modifyOfficeVisitReason(OfficeVisitReasonID, EntityID = 1, setOfficeVisitReasonID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOfficeVisitReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOfficeVisitReason(EntityID = 1, setOfficeVisitReasonID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOfficeVisitReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOfficeVisitReason(OfficeVisitReasonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "delete")


def getEveryStudentOfficeVisit(searchConditions = [], EntityID = 1, returnStudentOfficeVisitID = False, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentOfficeVisit in the district.

    This function returns a dataframe of every StudentOfficeVisit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1, returnStudentOfficeVisitID = False, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(StudentOfficeVisitID), verb = "get", return_params_list = return_params)

def modifyStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1, setStudentOfficeVisitID = None, setCreatedTime = None, setDisplayStatus = None, setDocumentationIsComplete = None, setEntityID = None, setHasBeenReleased = None, setIsStudentOfficeVisitToday = None, setModifiedTime = None, setOfficeVisitCommentID = None, setSchoolID = None, setSchoolYearID = None, setStudentID = None, setStudentOfficeVisitReasonsListDisplay = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitID = False, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(StudentOfficeVisitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentOfficeVisit(EntityID = 1, setStudentOfficeVisitID = None, setCreatedTime = None, setDisplayStatus = None, setDocumentationIsComplete = None, setEntityID = None, setHasBeenReleased = None, setIsStudentOfficeVisitToday = None, setModifiedTime = None, setOfficeVisitCommentID = None, setSchoolID = None, setSchoolYearID = None, setStudentID = None, setStudentOfficeVisitReasonsListDisplay = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitID = False, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(StudentOfficeVisitID), verb = "delete")


def getEveryStudentOfficeVisitNote(searchConditions = [], EntityID = 1, returnStudentOfficeVisitNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentOfficeVisitNote in the district.

    This function returns a dataframe of every StudentOfficeVisitNote in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1, returnStudentOfficeVisitNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(StudentOfficeVisitNoteID), verb = "get", return_params_list = return_params)

def modifyStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1, setStudentOfficeVisitNoteID = None, setCreatedTime = None, setModifiedTime = None, setNote = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(StudentOfficeVisitNoteID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentOfficeVisitNote(EntityID = 1, setStudentOfficeVisitNoteID = None, setCreatedTime = None, setModifiedTime = None, setNote = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(StudentOfficeVisitNoteID), verb = "delete")


def getEveryStudentOfficeVisitNotification(searchConditions = [], EntityID = 1, returnStudentOfficeVisitNotificationID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentOfficeVisitNotification in the district.

    This function returns a dataframe of every StudentOfficeVisitNotification in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1, returnStudentOfficeVisitNotificationID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(StudentOfficeVisitNotificationID), verb = "get", return_params_list = return_params)

def modifyStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1, setStudentOfficeVisitNotificationID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setNote = None, setNotificationMethodID = None, setNotificationTime = None, setNotificationTimeDate = None, setNotificationTimeTime = None, setOfficeVisitGuardianResponseID = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitNotificationID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(StudentOfficeVisitNotificationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentOfficeVisitNotification(EntityID = 1, setStudentOfficeVisitNotificationID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setNote = None, setNotificationMethodID = None, setNotificationTime = None, setNotificationTimeDate = None, setNotificationTimeTime = None, setOfficeVisitGuardianResponseID = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitNotificationID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(StudentOfficeVisitNotificationID), verb = "delete")


def getEveryStudentOfficeVisitReason(searchConditions = [], EntityID = 1, returnStudentOfficeVisitReasonID = False, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentOfficeVisitReason in the district.

    This function returns a dataframe of every StudentOfficeVisitReason in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1, returnStudentOfficeVisitReasonID = False, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(StudentOfficeVisitReasonID), verb = "get", return_params_list = return_params)

def modifyStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1, setStudentOfficeVisitReasonID = None, setCreatedTime = None, setModifiedTime = None, setOfficeVisitReasonID = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitReasonID = False, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(StudentOfficeVisitReasonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentOfficeVisitReason(EntityID = 1, setStudentOfficeVisitReasonID = None, setCreatedTime = None, setModifiedTime = None, setOfficeVisitReasonID = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitReasonID = False, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(StudentOfficeVisitReasonID), verb = "delete")


def getEveryStudentOfficeVisitTimeTransaction(searchConditions = [], EntityID = 1, returnStudentOfficeVisitTimeTransactionID = False, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentOfficeVisitTimeTransaction in the district.

    This function returns a dataframe of every StudentOfficeVisitTimeTransaction in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1, returnStudentOfficeVisitTimeTransactionID = False, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(StudentOfficeVisitTimeTransactionID), verb = "get", return_params_list = return_params)

def modifyStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1, setStudentOfficeVisitTimeTransactionID = None, setCreatedTime = None, setDisplayDuration = None, setDisplayOrder = None, setDuration = None, setEndTime = None, setEndTimeDate = None, setEndTimeTime = None, setModifiedTime = None, setNote = None, setStartTime = None, setStartTimeDate = None, setStartTimeTime = None, setStatus = None, setStatusCode = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitTimeTransactionID = False, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(StudentOfficeVisitTimeTransactionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentOfficeVisitTimeTransaction(EntityID = 1, setStudentOfficeVisitTimeTransactionID = None, setCreatedTime = None, setDisplayDuration = None, setDisplayOrder = None, setDuration = None, setEndTime = None, setEndTimeDate = None, setEndTimeTime = None, setModifiedTime = None, setNote = None, setStartTime = None, setStartTimeDate = None, setStartTimeTime = None, setStatus = None, setStatusCode = None, setStudentOfficeVisitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentOfficeVisitTimeTransactionID = False, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(StudentOfficeVisitTimeTransactionID), verb = "delete")