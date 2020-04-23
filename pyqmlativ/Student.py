# This module contains Student functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryActivity(searchConditions = [], EntityID = 1, returnActivityID = False, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnStudentAwardID = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Activity in the district.

    This function returns a dataframe of every Activity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getActivity(ActivityID, EntityID = 1, returnActivityID = False, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnStudentAwardID = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(ActivityID), verb = "get", return_params_list = return_params)

def modifyActivity(ActivityID, EntityID = 1, setActivityID = None, setActivityIDClonedFrom = None, setActivityIDClonedTo = None, setActivityLeaderNames = None, setActivityTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEndDate = None, setEntityID = None, setHideInFamilyAccess = None, setModifiedTime = None, setSchoolYearID = None, setSingleSex = None, setSingleSexCode = None, setStartDate = None, setStudentAwardID = None, setUseForAthleticEligibilityReporting = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActivityID = False, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnStudentAwardID = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(ActivityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createActivity(EntityID = 1, setActivityID = None, setActivityIDClonedFrom = None, setActivityIDClonedTo = None, setActivityLeaderNames = None, setActivityTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEndDate = None, setEntityID = None, setHideInFamilyAccess = None, setModifiedTime = None, setSchoolYearID = None, setSingleSex = None, setSingleSexCode = None, setStartDate = None, setStudentAwardID = None, setUseForAthleticEligibilityReporting = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActivityID = False, returnActivityIDClonedFrom = False, returnActivityIDClonedTo = False, returnActivityLeaderNames = False, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHideInFamilyAccess = False, returnModifiedTime = False, returnSchoolYearID = False, returnSingleSex = False, returnSingleSexCode = False, returnStartDate = False, returnStudentAwardID = False, returnUseForAthleticEligibilityReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteActivity(ActivityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Activity/" + str(ActivityID), verb = "delete")


def getEveryActivityEvent(searchConditions = [], EntityID = 1, returnActivityEventID = False, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDescriptionSummary = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ActivityEvent in the district.

    This function returns a dataframe of every ActivityEvent in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getActivityEvent(ActivityEventID, EntityID = 1, returnActivityEventID = False, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDescriptionSummary = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(ActivityEventID), verb = "get", return_params_list = return_params)

def modifyActivityEvent(ActivityEventID, EntityID = 1, setActivityEventID = None, setActivityID = None, setCodeSummary = None, setContactType = None, setContactTypeCode = None, setCost = None, setCreatedTime = None, setDate = None, setDescription = None, setDescriptionSummary = None, setDisplayOnDistrictCalendar = None, setEndTime = None, setEventTypeID = None, setLocationID = None, setModifiedTime = None, setNameIDContact = None, setStartTime = None, setStatus = None, setStatusCode = None, setSummary = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVisibleTo = None, setVisibleToCode = None, returnActivityEventID = False, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDescriptionSummary = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(ActivityEventID), verb = "post", return_params_list = return_params, payload = payload_params)

def createActivityEvent(EntityID = 1, setActivityEventID = None, setActivityID = None, setCodeSummary = None, setContactType = None, setContactTypeCode = None, setCost = None, setCreatedTime = None, setDate = None, setDescription = None, setDescriptionSummary = None, setDisplayOnDistrictCalendar = None, setEndTime = None, setEventTypeID = None, setLocationID = None, setModifiedTime = None, setNameIDContact = None, setStartTime = None, setStatus = None, setStatusCode = None, setSummary = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVisibleTo = None, setVisibleToCode = None, returnActivityEventID = False, returnActivityID = False, returnCodeSummary = False, returnContactType = False, returnContactTypeCode = False, returnCost = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnDescriptionSummary = False, returnDisplayOnDistrictCalendar = False, returnEndTime = False, returnEventTypeID = False, returnLocationID = False, returnModifiedTime = False, returnNameIDContact = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisibleTo = False, returnVisibleToCode = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteActivityEvent(ActivityEventID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityEvent/" + str(ActivityEventID), verb = "delete")


def getEveryActivityPersonnel(searchConditions = [], EntityID = 1, returnActivityPersonnelID = False, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ActivityPersonnel in the district.

    This function returns a dataframe of every ActivityPersonnel in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getActivityPersonnel(ActivityPersonnelID, EntityID = 1, returnActivityPersonnelID = False, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(ActivityPersonnelID), verb = "get", return_params_list = return_params)

def modifyActivityPersonnel(ActivityPersonnelID, EntityID = 1, setActivityPersonnelID = None, setActivityID = None, setActivityPersonnelIDClonedFrom = None, setCreatedTime = None, setIsLeader = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActivityPersonnelID = False, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(ActivityPersonnelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createActivityPersonnel(EntityID = 1, setActivityPersonnelID = None, setActivityID = None, setActivityPersonnelIDClonedFrom = None, setCreatedTime = None, setIsLeader = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActivityPersonnelID = False, returnActivityID = False, returnActivityPersonnelIDClonedFrom = False, returnCreatedTime = False, returnIsLeader = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteActivityPersonnel(ActivityPersonnelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityPersonnel/" + str(ActivityPersonnelID), verb = "delete")


def getEveryActivityType(searchConditions = [], EntityID = 1, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ActivityType in the district.

    This function returns a dataframe of every ActivityType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getActivityType(ActivityTypeID, EntityID = 1, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(ActivityTypeID), verb = "get", return_params_list = return_params)

def modifyActivityType(ActivityTypeID, EntityID = 1, setActivityTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(ActivityTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createActivityType(EntityID = 1, setActivityTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActivityTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteActivityType(ActivityTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ActivityType/" + str(ActivityTypeID), verb = "delete")


def getEveryAlert(searchConditions = [], EntityID = 1, returnAlertID = False, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Alert in the district.

    This function returns a dataframe of every Alert in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAlert(AlertID, EntityID = 1, returnAlertID = False, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(AlertID), verb = "get", return_params_list = return_params)

def modifyAlert(AlertID, EntityID = 1, setAlertID = None, setCreatedTime = None, setEndDate = None, setInformation = None, setIsActive = None, setIsCritical = None, setModifiedTime = None, setStartDate = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAlertID = False, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(AlertID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAlert(EntityID = 1, setAlertID = None, setCreatedTime = None, setEndDate = None, setInformation = None, setIsActive = None, setIsCritical = None, setModifiedTime = None, setStartDate = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAlertID = False, returnCreatedTime = False, returnEndDate = False, returnInformation = False, returnIsActive = False, returnIsCritical = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAlert(AlertID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Alert/" + str(AlertID), verb = "delete")


def getEveryAwardCategory(searchConditions = [], EntityID = 1, returnAwardCategoryID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AwardCategory in the district.

    This function returns a dataframe of every AwardCategory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAwardCategory(AwardCategoryID, EntityID = 1, returnAwardCategoryID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/" + str(AwardCategoryID), verb = "get", return_params_list = return_params)

def modifyAwardCategory(AwardCategoryID, EntityID = 1, setAwardCategoryID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAwardCategoryID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/" + str(AwardCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAwardCategory(EntityID = 1, setAwardCategoryID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAwardCategoryID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAwardCategory(AwardCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardCategory/" + str(AwardCategoryID), verb = "delete")


def getEveryAwardHardware(searchConditions = [], EntityID = 1, returnAwardHardwareID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AwardHardware in the district.

    This function returns a dataframe of every AwardHardware in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAwardHardware(AwardHardwareID, EntityID = 1, returnAwardHardwareID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/" + str(AwardHardwareID), verb = "get", return_params_list = return_params)

def modifyAwardHardware(AwardHardwareID, EntityID = 1, setAwardHardwareID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAwardHardwareID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/" + str(AwardHardwareID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAwardHardware(EntityID = 1, setAwardHardwareID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAwardHardwareID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAwardHardware(AwardHardwareID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardHardware/" + str(AwardHardwareID), verb = "delete")


def getEveryAwardType(searchConditions = [], EntityID = 1, returnAwardTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AwardType in the district.

    This function returns a dataframe of every AwardType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAwardType(AwardTypeID, EntityID = 1, returnAwardTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/" + str(AwardTypeID), verb = "get", return_params_list = return_params)

def modifyAwardType(AwardTypeID, EntityID = 1, setAwardTypeID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAwardTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/" + str(AwardTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAwardType(EntityID = 1, setAwardTypeID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAwardTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAwardType(AwardTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/AwardType/" + str(AwardTypeID), verb = "delete")


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnableIEPWriterDocumentFunctions = False, returnIEPWriterDocumentSecurityToken = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigDistrict in the district.

    This function returns a dataframe of every ConfigDistrict in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnableIEPWriterDocumentFunctions = False, returnIEPWriterDocumentSecurityToken = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setEnableIEPWriterDocumentFunctions = None, setIEPWriterDocumentSecurityToken = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnableIEPWriterDocumentFunctions = False, returnIEPWriterDocumentSecurityToken = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrict(EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setEnableIEPWriterDocumentFunctions = None, setIEPWriterDocumentSecurityToken = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnableIEPWriterDocumentFunctions = False, returnIEPWriterDocumentSecurityToken = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setConfigEntityGroupYearID = None, setConfigEntityGroupYearIDClonedFrom = None, setCourseSubjectIDFollettDestinyRoomTeacher = None, setCreatedTime = None, setDefaultAllowFeeManagementOnlinePaymentAccess = None, setDefaultAllowFoodServiceOnlinePaymentAccess = None, setEntityGroupKey = None, setEntityID = None, setFollettDestinyCustomEntityCode = None, setFollettDestinyRoomTeacherPeriod = None, setFollettDestinyRoomTeacherType = None, setFollettDestinyRoomTeacherTypeCode = None, setModifiedTime = None, setSchoolYearID = None, setStudentAccessAccountInfoEmailBody = None, setStudentAccessAccountInfoEmailIncludeResetPasswordText = None, setStudentAccessAccountInfoEmailSubject = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setConfigEntityGroupYearID = None, setConfigEntityGroupYearIDClonedFrom = None, setCourseSubjectIDFollettDestinyRoomTeacher = None, setCreatedTime = None, setDefaultAllowFeeManagementOnlinePaymentAccess = None, setDefaultAllowFoodServiceOnlinePaymentAccess = None, setEntityGroupKey = None, setEntityID = None, setFollettDestinyCustomEntityCode = None, setFollettDestinyRoomTeacherPeriod = None, setFollettDestinyRoomTeacherType = None, setFollettDestinyRoomTeacherTypeCode = None, setModifiedTime = None, setSchoolYearID = None, setStudentAccessAccountInfoEmailBody = None, setStudentAccessAccountInfoEmailIncludeResetPasswordText = None, setStudentAccessAccountInfoEmailSubject = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCourseSubjectIDFollettDestinyRoomTeacher = False, returnCreatedTime = False, returnDefaultAllowFeeManagementOnlinePaymentAccess = False, returnDefaultAllowFoodServiceOnlinePaymentAccess = False, returnEntityGroupKey = False, returnEntityID = False, returnFollettDestinyCustomEntityCode = False, returnFollettDestinyRoomTeacherPeriod = False, returnFollettDestinyRoomTeacherType = False, returnFollettDestinyRoomTeacherTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentAccessAccountInfoEmailBody = False, returnStudentAccessAccountInfoEmailIncludeResetPasswordText = False, returnStudentAccessAccountInfoEmailSubject = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setAllowStudentAccessDefault = None, setAutoGenerateEmail = None, setAutoGenerateEmailCode = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setCreatedTime = None, setEasyIEPSection504ImportFilePath = None, setEasyIEPSpecEdImportFilePath = None, setEmailDomain = None, setEmailTypeIDDefault = None, setModifiedTime = None, setStudentAttachmentVisibility = None, setStudentAttachmentVisibilityCode = None, setStudentNumberMask = None, setStudentNumberStartValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setAllowStudentAccessDefault = None, setAutoGenerateEmail = None, setAutoGenerateEmailCode = None, setAutoGenerateSecurityUser = None, setAutoGenerateSecurityUserCode = None, setCreatedTime = None, setEasyIEPSection504ImportFilePath = None, setEasyIEPSpecEdImportFilePath = None, setEmailDomain = None, setEmailTypeIDDefault = None, setModifiedTime = None, setStudentAttachmentVisibility = None, setStudentAttachmentVisibilityCode = None, setStudentNumberMask = None, setStudentNumberStartValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAllowStudentAccessDefault = False, returnAutoGenerateEmail = False, returnAutoGenerateEmailCode = False, returnAutoGenerateSecurityUser = False, returnAutoGenerateSecurityUserCode = False, returnCreatedTime = False, returnEasyIEPSection504ImportFilePath = False, returnEasyIEPSpecEdImportFilePath = False, returnEmailDomain = False, returnEmailTypeIDDefault = False, returnModifiedTime = False, returnStudentAttachmentVisibility = False, returnStudentAttachmentVisibilityCode = False, returnStudentNumberMask = False, returnStudentNumberStartValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryCurrentSportsSelections(searchConditions = [], EntityID = 1, returnCurrentSportsSelectionsID = False, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurrentSportsSelections in the district.

    This function returns a dataframe of every CurrentSportsSelections in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurrentSportsSelections(CurrentSportsSelectionsID, EntityID = 1, returnCurrentSportsSelectionsID = False, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(CurrentSportsSelectionsID), verb = "get", return_params_list = return_params)

def modifyCurrentSportsSelections(CurrentSportsSelectionsID, EntityID = 1, setCurrentSportsSelectionsID = None, setCreatedTime = None, setFallSportID = None, setModifiedTime = None, setSpringSportID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWinterSportID = None, returnCurrentSportsSelectionsID = False, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(CurrentSportsSelectionsID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurrentSportsSelections(EntityID = 1, setCurrentSportsSelectionsID = None, setCreatedTime = None, setFallSportID = None, setModifiedTime = None, setSpringSportID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWinterSportID = None, returnCurrentSportsSelectionsID = False, returnCreatedTime = False, returnFallSportID = False, returnModifiedTime = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurrentSportsSelections(CurrentSportsSelectionsID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CurrentSportsSelections/" + str(CurrentSportsSelectionsID), verb = "delete")


def getEveryCustomCode(searchConditions = [], EntityID = 1, returnCustomCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CustomCode in the district.

    This function returns a dataframe of every CustomCode in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCustomCode(CustomCodeID, EntityID = 1, returnCustomCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(CustomCodeID), verb = "get", return_params_list = return_params)

def modifyCustomCode(CustomCodeID, EntityID = 1, setCustomCodeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCustomCodeTypeID = None, setDescription = None, setDistrictGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(CustomCodeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCustomCode(EntityID = 1, setCustomCodeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCustomCodeTypeID = None, setDescription = None, setDistrictGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCustomCodeTypeID = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCustomCode(CustomCodeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCode/" + str(CustomCodeID), verb = "delete")


def getEveryCustomCodeType(searchConditions = [], EntityID = 1, returnCustomCodeTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CustomCodeType in the district.

    This function returns a dataframe of every CustomCodeType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCustomCodeType(CustomCodeTypeID, EntityID = 1, returnCustomCodeTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(CustomCodeTypeID), verb = "get", return_params_list = return_params)

def modifyCustomCodeType(CustomCodeTypeID, EntityID = 1, setCustomCodeTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomCodeTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(CustomCodeTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCustomCodeType(EntityID = 1, setCustomCodeTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomCodeTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCustomCodeType(CustomCodeTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/CustomCodeType/" + str(CustomCodeTypeID), verb = "delete")


def getEveryEthnicityMA(searchConditions = [], EntityID = 1, returnEthnicityMAID = False, returnCode = False, returnCreatedTime = False, returnEthnicity = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EthnicityMA in the district.

    This function returns a dataframe of every EthnicityMA in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEthnicityMA(EthnicityMAID, EntityID = 1, returnEthnicityMAID = False, returnCode = False, returnCreatedTime = False, returnEthnicity = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/" + str(EthnicityMAID), verb = "get", return_params_list = return_params)

def modifyEthnicityMA(EthnicityMAID, EntityID = 1, setEthnicityMAID = None, setCode = None, setCreatedTime = None, setEthnicity = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEthnicityMAID = False, returnCode = False, returnCreatedTime = False, returnEthnicity = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/" + str(EthnicityMAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEthnicityMA(EntityID = 1, setEthnicityMAID = None, setCode = None, setCreatedTime = None, setEthnicity = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEthnicityMAID = False, returnCode = False, returnCreatedTime = False, returnEthnicity = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEthnicityMA(EthnicityMAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EthnicityMA/" + str(EthnicityMAID), verb = "delete")


def getEveryEventType(searchConditions = [], EntityID = 1, returnEventTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EventType in the district.

    This function returns a dataframe of every EventType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEventType(EventTypeID, EntityID = 1, returnEventTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(EventTypeID), verb = "get", return_params_list = return_params)

def modifyEventType(EventTypeID, EntityID = 1, setEventTypeID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEventTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(EventTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEventType(EntityID = 1, setEventTypeID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEventTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEventType(EventTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/EventType/" + str(EventTypeID), verb = "delete")


def getEveryFallSport(searchConditions = [], EntityID = 1, returnFallSportID = False, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FallSport in the district.

    This function returns a dataframe of every FallSport in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFallSport(FallSportID, EntityID = 1, returnFallSportID = False, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(FallSportID), verb = "get", return_params_list = return_params)

def modifyFallSport(FallSportID, EntityID = 1, setFallSportID = None, setCode = None, setCreatedTime = None, setFallSport = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFallSportID = False, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(FallSportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFallSport(EntityID = 1, setFallSportID = None, setCode = None, setCreatedTime = None, setFallSport = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFallSportID = False, returnCode = False, returnCreatedTime = False, returnFallSport = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFallSport(FallSportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSport/" + str(FallSportID), verb = "delete")


def getEveryFallSportsTeam(searchConditions = [], EntityID = 1, returnFallSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FallSportsTeam in the district.

    This function returns a dataframe of every FallSportsTeam in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFallSportsTeam(FallSportsTeamID, EntityID = 1, returnFallSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(FallSportsTeamID), verb = "get", return_params_list = return_params)

def modifyFallSportsTeam(FallSportsTeamID, EntityID = 1, setFallSportsTeamID = None, setCaptain = None, setCreatedTime = None, setFallSportID = None, setLettered = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFallSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(FallSportsTeamID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFallSportsTeam(EntityID = 1, setFallSportsTeamID = None, setCaptain = None, setCreatedTime = None, setFallSportID = None, setLettered = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFallSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnFallSportID = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFallSportsTeam(FallSportsTeamID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FallSportsTeam/" + str(FallSportsTeamID), verb = "delete")


def getEveryFeederSchool(searchConditions = [], EntityID = 1, returnFeederSchoolID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FeederSchool in the district.

    This function returns a dataframe of every FeederSchool in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFeederSchool(FeederSchoolID, EntityID = 1, returnFeederSchoolID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(FeederSchoolID), verb = "get", return_params_list = return_params)

def modifyFeederSchool(FeederSchoolID, EntityID = 1, setFeederSchoolID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFeederSchoolID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(FeederSchoolID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFeederSchool(EntityID = 1, setFeederSchoolID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFeederSchoolID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFeederSchool(FeederSchoolID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/FeederSchool/" + str(FeederSchoolID), verb = "delete")


def getEveryIndicator(searchConditions = [], EntityID = 1, returnIndicatorID = False, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Indicator in the district.

    This function returns a dataframe of every Indicator in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIndicator(IndicatorID, EntityID = 1, returnIndicatorID = False, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(IndicatorID), verb = "get", return_params_list = return_params)

def modifyIndicator(IndicatorID, EntityID = 1, setIndicatorID = None, setCreatedTime = None, setImage = None, setImageCode = None, setIsActive = None, setModifiedTime = None, setName = None, setRank = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIndicatorID = False, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(IndicatorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIndicator(EntityID = 1, setIndicatorID = None, setCreatedTime = None, setImage = None, setImageCode = None, setIsActive = None, setModifiedTime = None, setName = None, setRank = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIndicatorID = False, returnCreatedTime = False, returnImage = False, returnImageCode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnRank = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIndicator(IndicatorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Indicator/" + str(IndicatorID), verb = "delete")


def getEveryLock(searchConditions = [], EntityID = 1, returnLockID = False, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Lock in the district.

    This function returns a dataframe of every Lock in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLock(LockID, EntityID = 1, returnLockID = False, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(LockID), verb = "get", return_params_list = return_params)

def modifyLock(LockID, EntityID = 1, setLockID = None, setBuildingID = None, setCreatedTime = None, setIsAssigned = None, setIsAttached = None, setIsAvailable = None, setIsBuiltInLock = None, setLockerID = None, setLockMakeID = None, setModifiedTime = None, setOwnedBySchool = None, setRenderRemoveLock = None, setSerialNumber = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockID = False, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(LockID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLock(EntityID = 1, setLockID = None, setBuildingID = None, setCreatedTime = None, setIsAssigned = None, setIsAttached = None, setIsAvailable = None, setIsBuiltInLock = None, setLockerID = None, setLockMakeID = None, setModifiedTime = None, setOwnedBySchool = None, setRenderRemoveLock = None, setSerialNumber = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockID = False, returnBuildingID = False, returnCreatedTime = False, returnIsAssigned = False, returnIsAttached = False, returnIsAvailable = False, returnIsBuiltInLock = False, returnLockerID = False, returnLockMakeID = False, returnModifiedTime = False, returnOwnedBySchool = False, returnRenderRemoveLock = False, returnSerialNumber = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLock(LockID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Lock/" + str(LockID), verb = "delete")


def getEveryLockCombination(searchConditions = [], EntityID = 1, returnLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LockCombination in the district.

    This function returns a dataframe of every LockCombination in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLockCombination(LockCombinationID, EntityID = 1, returnLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(LockCombinationID), verb = "get", return_params_list = return_params)

def modifyLockCombination(LockCombinationID, EntityID = 1, setLockCombinationID = None, setCombination = None, setCombinationNumber = None, setCreatedTime = None, setIsCurrentCombination = None, setLockID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(LockCombinationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLockCombination(EntityID = 1, setLockCombinationID = None, setCombination = None, setCombinationNumber = None, setCreatedTime = None, setIsCurrentCombination = None, setLockID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnIsCurrentCombination = False, returnLockID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLockCombination(LockCombinationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockCombination/" + str(LockCombinationID), verb = "delete")


def getEveryLocker(searchConditions = [], EntityID = 1, returnLockerID = False, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Locker in the district.

    This function returns a dataframe of every Locker in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLocker(LockerID, EntityID = 1, returnLockerID = False, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(LockerID), verb = "get", return_params_list = return_params)

def modifyLocker(LockerID, EntityID = 1, setLockerID = None, setComment = None, setCreatedTime = None, setCurrentCombination = None, setGender = None, setGenderCode = None, setGenderCount = None, setHasBuiltInLock = None, setIsActive = None, setIsAvailable = None, setIsDamaged = None, setLockerAreaID = None, setLockerNumber = None, setModifiedTime = None, setNeedsLock = None, setStudentsPerLocker = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockerID = False, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(LockerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLocker(EntityID = 1, setLockerID = None, setComment = None, setCreatedTime = None, setCurrentCombination = None, setGender = None, setGenderCode = None, setGenderCount = None, setHasBuiltInLock = None, setIsActive = None, setIsAvailable = None, setIsDamaged = None, setLockerAreaID = None, setLockerNumber = None, setModifiedTime = None, setNeedsLock = None, setStudentsPerLocker = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockerID = False, returnComment = False, returnCreatedTime = False, returnCurrentCombination = False, returnGender = False, returnGenderCode = False, returnGenderCount = False, returnHasBuiltInLock = False, returnIsActive = False, returnIsAvailable = False, returnIsDamaged = False, returnLockerAreaID = False, returnLockerNumber = False, returnModifiedTime = False, returnNeedsLock = False, returnStudentsPerLocker = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLocker(LockerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Locker/" + str(LockerID), verb = "delete")


def getEveryLockerArea(searchConditions = [], EntityID = 1, returnLockerAreaID = False, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LockerArea in the district.

    This function returns a dataframe of every LockerArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLockerArea(LockerAreaID, EntityID = 1, returnLockerAreaID = False, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(LockerAreaID), verb = "get", return_params_list = return_params)

def modifyLockerArea(LockerAreaID, EntityID = 1, setLockerAreaID = None, setAllowCoedLocker = None, setBuildingID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setHasBuiltInLockDefault = None, setMaximumStudentsPerLocker = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockerAreaID = False, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(LockerAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLockerArea(EntityID = 1, setLockerAreaID = None, setAllowCoedLocker = None, setBuildingID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setHasBuiltInLockDefault = None, setMaximumStudentsPerLocker = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockerAreaID = False, returnAllowCoedLocker = False, returnBuildingID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnHasBuiltInLockDefault = False, returnMaximumStudentsPerLocker = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLockerArea(LockerAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockerArea/" + str(LockerAreaID), verb = "delete")


def getEveryLockMake(searchConditions = [], EntityID = 1, returnLockMakeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LockMake in the district.

    This function returns a dataframe of every LockMake in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLockMake(LockMakeID, EntityID = 1, returnLockMakeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(LockMakeID), verb = "get", return_params_list = return_params)

def modifyLockMake(LockMakeID, EntityID = 1, setLockMakeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockMakeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(LockMakeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLockMake(EntityID = 1, setLockMakeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLockMakeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLockMake(LockMakeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/LockMake/" + str(LockMakeID), verb = "delete")


def getEveryNextStudentNumber(searchConditions = [], EntityID = 1, returnNextStudentNumberID = False, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NextStudentNumber in the district.

    This function returns a dataframe of every NextStudentNumber in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNextStudentNumber(NextStudentNumberID, EntityID = 1, returnNextStudentNumberID = False, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(NextStudentNumberID), verb = "get", return_params_list = return_params)

def modifyNextStudentNumber(NextStudentNumberID, EntityID = 1, setNextStudentNumberID = None, setCreatedTime = None, setIsForStateID = None, setMaskPrefix = None, setModifiedTime = None, setSequenceNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNextStudentNumberID = False, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(NextStudentNumberID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNextStudentNumber(EntityID = 1, setNextStudentNumberID = None, setCreatedTime = None, setIsForStateID = None, setMaskPrefix = None, setModifiedTime = None, setSequenceNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNextStudentNumberID = False, returnCreatedTime = False, returnIsForStateID = False, returnMaskPrefix = False, returnModifiedTime = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNextStudentNumber(NextStudentNumberID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NextStudentNumber/" + str(NextStudentNumberID), verb = "delete")


def getEveryNoteType(searchConditions = [], EntityID = 1, returnNoteTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NoteType in the district.

    This function returns a dataframe of every NoteType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNoteType(NoteTypeID, EntityID = 1, returnNoteTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(NoteTypeID), verb = "get", return_params_list = return_params)

def modifyNoteType(NoteTypeID, EntityID = 1, setNoteTypeID = None, setCode = None, setCreatedTime = None, setDescription = None, setIndicatorID = None, setIsActive = None, setIsParentalConsent = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNoteTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(NoteTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNoteType(EntityID = 1, setNoteTypeID = None, setCode = None, setCreatedTime = None, setDescription = None, setIndicatorID = None, setIsActive = None, setIsParentalConsent = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNoteTypeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIndicatorID = False, returnIsActive = False, returnIsParentalConsent = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNoteType(NoteTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/NoteType/" + str(NoteTypeID), verb = "delete")


def getEveryReligion(searchConditions = [], EntityID = 1, returnReligionID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Religion in the district.

    This function returns a dataframe of every Religion in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReligion(ReligionID, EntityID = 1, returnReligionID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(ReligionID), verb = "get", return_params_list = return_params)

def modifyReligion(ReligionID, EntityID = 1, setReligionID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReligionID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(ReligionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReligion(EntityID = 1, setReligionID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReligionID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReligion(ReligionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Religion/" + str(ReligionID), verb = "delete")


def getEverySkylertAttendanceExportAttendanceType(searchConditions = [], EntityID = 1, returnSkylertAttendanceExportAttendanceTypeID = False, returnAttendanceTypeCodeOverride = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SkylertAttendanceExportAttendanceType in the district.

    This function returns a dataframe of every SkylertAttendanceExportAttendanceType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSkylertAttendanceExportAttendanceType(SkylertAttendanceExportAttendanceTypeID, EntityID = 1, returnSkylertAttendanceExportAttendanceTypeID = False, returnAttendanceTypeCodeOverride = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(SkylertAttendanceExportAttendanceTypeID), verb = "get", return_params_list = return_params)

def modifySkylertAttendanceExportAttendanceType(SkylertAttendanceExportAttendanceTypeID, EntityID = 1, setSkylertAttendanceExportAttendanceTypeID = None, setAttendanceTypeCodeOverride = None, setAttendanceTypeID = None, setCreatedTime = None, setModifiedTime = None, setSkylertAttendanceExportSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkylertAttendanceExportAttendanceTypeID = False, returnAttendanceTypeCodeOverride = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(SkylertAttendanceExportAttendanceTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSkylertAttendanceExportAttendanceType(EntityID = 1, setSkylertAttendanceExportAttendanceTypeID = None, setAttendanceTypeCodeOverride = None, setAttendanceTypeID = None, setCreatedTime = None, setModifiedTime = None, setSkylertAttendanceExportSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkylertAttendanceExportAttendanceTypeID = False, returnAttendanceTypeCodeOverride = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSkylertAttendanceExportAttendanceType(SkylertAttendanceExportAttendanceTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportAttendanceType/" + str(SkylertAttendanceExportAttendanceTypeID), verb = "delete")


def getEverySkylertAttendanceExportSetting(searchConditions = [], EntityID = 1, returnSkylertAttendanceExportSettingID = False, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SkylertAttendanceExportSetting in the district.

    This function returns a dataframe of every SkylertAttendanceExportSetting in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSkylertAttendanceExportSetting(SkylertAttendanceExportSettingID, EntityID = 1, returnSkylertAttendanceExportSettingID = False, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(SkylertAttendanceExportSettingID), verb = "get", return_params_list = return_params)

def modifySkylertAttendanceExportSetting(SkylertAttendanceExportSettingID, EntityID = 1, setSkylertAttendanceExportSettingID = None, setAttendancePeriodIDHigh = None, setAttendancePeriodIDLow = None, setCreatedTime = None, setEntityID = None, setFileSequence = None, setMinimumPeriodsAbsent = None, setModifiedTime = None, setParentNotifiedOption = None, setParentNotifiedOptionCode = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkylertAttendanceExportSettingID = False, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(SkylertAttendanceExportSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSkylertAttendanceExportSetting(EntityID = 1, setSkylertAttendanceExportSettingID = None, setAttendancePeriodIDHigh = None, setAttendancePeriodIDLow = None, setCreatedTime = None, setEntityID = None, setFileSequence = None, setMinimumPeriodsAbsent = None, setModifiedTime = None, setParentNotifiedOption = None, setParentNotifiedOptionCode = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkylertAttendanceExportSettingID = False, returnAttendancePeriodIDHigh = False, returnAttendancePeriodIDLow = False, returnCreatedTime = False, returnEntityID = False, returnFileSequence = False, returnMinimumPeriodsAbsent = False, returnModifiedTime = False, returnParentNotifiedOption = False, returnParentNotifiedOptionCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSkylertAttendanceExportSetting(SkylertAttendanceExportSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSetting/" + str(SkylertAttendanceExportSettingID), verb = "delete")


def getEverySkylertAttendanceExportSettingScheduledTask(searchConditions = [], EntityID = 1, returnSkylertAttendanceExportSettingScheduledTaskID = False, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SkylertAttendanceExportSettingScheduledTask in the district.

    This function returns a dataframe of every SkylertAttendanceExportSettingScheduledTask in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSkylertAttendanceExportSettingScheduledTask(SkylertAttendanceExportSettingScheduledTaskID, EntityID = 1, returnSkylertAttendanceExportSettingScheduledTaskID = False, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(SkylertAttendanceExportSettingScheduledTaskID), verb = "get", return_params_list = return_params)

def modifySkylertAttendanceExportSettingScheduledTask(SkylertAttendanceExportSettingScheduledTaskID, EntityID = 1, setSkylertAttendanceExportSettingScheduledTaskID = None, setCreatedTime = None, setModifiedTime = None, setScheduledTaskID = None, setSkylertAttendanceExportSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkylertAttendanceExportSettingScheduledTaskID = False, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(SkylertAttendanceExportSettingScheduledTaskID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSkylertAttendanceExportSettingScheduledTask(EntityID = 1, setSkylertAttendanceExportSettingScheduledTaskID = None, setCreatedTime = None, setModifiedTime = None, setScheduledTaskID = None, setSkylertAttendanceExportSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkylertAttendanceExportSettingScheduledTaskID = False, returnCreatedTime = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSkylertAttendanceExportSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSkylertAttendanceExportSettingScheduledTask(SkylertAttendanceExportSettingScheduledTaskID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SkylertAttendanceExportSettingScheduledTask/" + str(SkylertAttendanceExportSettingScheduledTaskID), verb = "delete")


def getEverySpringSport(searchConditions = [], EntityID = 1, returnSpringSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SpringSport in the district.

    This function returns a dataframe of every SpringSport in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSpringSport(SpringSportID, EntityID = 1, returnSpringSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(SpringSportID), verb = "get", return_params_list = return_params)

def modifySpringSport(SpringSportID, EntityID = 1, setSpringSportID = None, setCode = None, setCreatedTime = None, setModifiedTime = None, setSpringSport = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSpringSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(SpringSportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSpringSport(EntityID = 1, setSpringSportID = None, setCode = None, setCreatedTime = None, setModifiedTime = None, setSpringSport = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSpringSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnSpringSport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSpringSport(SpringSportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSport/" + str(SpringSportID), verb = "delete")


def getEverySpringSportsTeam(searchConditions = [], EntityID = 1, returnSpringSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SpringSportsTeam in the district.

    This function returns a dataframe of every SpringSportsTeam in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSpringSportsTeam(SpringSportsTeamID, EntityID = 1, returnSpringSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(SpringSportsTeamID), verb = "get", return_params_list = return_params)

def modifySpringSportsTeam(SpringSportsTeamID, EntityID = 1, setSpringSportsTeamID = None, setCaptain = None, setCreatedTime = None, setLettered = None, setModifiedTime = None, setSchoolYearID = None, setSpringSportID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSpringSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(SpringSportsTeamID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSpringSportsTeam(EntityID = 1, setSpringSportsTeamID = None, setCaptain = None, setCreatedTime = None, setLettered = None, setModifiedTime = None, setSchoolYearID = None, setSpringSportID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSpringSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnSpringSportID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSpringSportsTeam(SpringSportsTeamID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/SpringSportsTeam/" + str(SpringSportsTeamID), verb = "delete")


def getEveryStudentActivity(searchConditions = [], EntityID = 1, returnStudentActivityID = False, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnHasParticipation = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentActivity in the district.

    This function returns a dataframe of every StudentActivity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentActivity(StudentActivityID, EntityID = 1, returnStudentActivityID = False, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnHasParticipation = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(StudentActivityID), verb = "get", return_params_list = return_params)

def modifyStudentActivity(StudentActivityID, EntityID = 1, setStudentActivityID = None, setActivityID = None, setCourseID = None, setCreatedTime = None, setHasParticipation = None, setIsActive = None, setModifiedTime = None, setStudentActivityIDClonedFrom = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentActivityID = False, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnHasParticipation = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(StudentActivityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentActivity(EntityID = 1, setStudentActivityID = None, setActivityID = None, setCourseID = None, setCreatedTime = None, setHasParticipation = None, setIsActive = None, setModifiedTime = None, setStudentActivityIDClonedFrom = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentActivityID = False, returnActivityID = False, returnCourseID = False, returnCreatedTime = False, returnHasParticipation = False, returnIsActive = False, returnModifiedTime = False, returnStudentActivityIDClonedFrom = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentActivity(StudentActivityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivity/" + str(StudentActivityID), verb = "delete")


def getEveryStudentActivityTransaction(searchConditions = [], EntityID = 1, returnStudentActivityTransactionID = False, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentActivityTransaction in the district.

    This function returns a dataframe of every StudentActivityTransaction in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentActivityTransaction(StudentActivityTransactionID, EntityID = 1, returnStudentActivityTransactionID = False, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(StudentActivityTransactionID), verb = "get", return_params_list = return_params)

def modifyStudentActivityTransaction(StudentActivityTransactionID, EntityID = 1, setStudentActivityTransactionID = None, setCreatedTime = None, setModifiedTime = None, setParticipationEndDate = None, setParticipationStartDate = None, setStudentActivityID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentActivityTransactionID = False, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(StudentActivityTransactionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentActivityTransaction(EntityID = 1, setStudentActivityTransactionID = None, setCreatedTime = None, setModifiedTime = None, setParticipationEndDate = None, setParticipationStartDate = None, setStudentActivityID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentActivityTransactionID = False, returnCreatedTime = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentActivityTransaction(StudentActivityTransactionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentActivityTransaction/" + str(StudentActivityTransactionID), verb = "delete")


def getEveryStudentAward(searchConditions = [], EntityID = 1, returnStudentAwardID = False, returnActivityID = False, returnAwardCategoryID = False, returnAwardHardwareID = False, returnAwardTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAward in the district.

    This function returns a dataframe of every StudentAward in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAward(StudentAwardID, EntityID = 1, returnStudentAwardID = False, returnActivityID = False, returnAwardCategoryID = False, returnAwardHardwareID = False, returnAwardTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/" + str(StudentAwardID), verb = "get", return_params_list = return_params)

def modifyStudentAward(StudentAwardID, EntityID = 1, setStudentAwardID = None, setActivityID = None, setAwardCategoryID = None, setAwardHardwareID = None, setAwardTypeID = None, setCreatedTime = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAwardID = False, returnActivityID = False, returnAwardCategoryID = False, returnAwardHardwareID = False, returnAwardTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/" + str(StudentAwardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAward(EntityID = 1, setStudentAwardID = None, setActivityID = None, setAwardCategoryID = None, setAwardHardwareID = None, setAwardTypeID = None, setCreatedTime = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAwardID = False, returnActivityID = False, returnAwardCategoryID = False, returnAwardHardwareID = False, returnAwardTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAward(StudentAwardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentAward/" + str(StudentAwardID), verb = "delete")


def getEveryStudentCustomCode(searchConditions = [], EntityID = 1, returnStudentCustomCodeID = False, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentCustomCode in the district.

    This function returns a dataframe of every StudentCustomCode in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentCustomCode(StudentCustomCodeID, EntityID = 1, returnStudentCustomCodeID = False, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(StudentCustomCodeID), verb = "get", return_params_list = return_params)

def modifyStudentCustomCode(StudentCustomCodeID, EntityID = 1, setStudentCustomCodeID = None, setCreatedTime = None, setCustomCodeID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentCustomCodeID = False, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(StudentCustomCodeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentCustomCode(EntityID = 1, setStudentCustomCodeID = None, setCreatedTime = None, setCustomCodeID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentCustomCodeID = False, returnCreatedTime = False, returnCustomCodeID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentCustomCode(StudentCustomCodeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentCustomCode/" + str(StudentCustomCodeID), verb = "delete")


def getEveryStudentDistrict(searchConditions = [], EntityID = 1, returnStudentDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentDistrict in the district.

    This function returns a dataframe of every StudentDistrict in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentDistrict(StudentDistrictID, EntityID = 1, returnStudentDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(StudentDistrictID), verb = "get", return_params_list = return_params)

def modifyStudentDistrict(StudentDistrictID, EntityID = 1, setStudentDistrictID = None, setCreatedTime = None, setDistrictID = None, setFeederSchoolID = None, setFirstName = None, setGrade = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(StudentDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentDistrict(EntityID = 1, setStudentDistrictID = None, setCreatedTime = None, setDistrictID = None, setFeederSchoolID = None, setFirstName = None, setGrade = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnFeederSchoolID = False, returnFirstName = False, returnGrade = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentDistrict(StudentDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentDistrict/" + str(StudentDistrictID), verb = "delete")


def getEveryStudentEthnicityMA(searchConditions = [], EntityID = 1, returnStudentEthnicityMAID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEthnicityMA in the district.

    This function returns a dataframe of every StudentEthnicityMA in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEthnicityMA(StudentEthnicityMAID, EntityID = 1, returnStudentEthnicityMAID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/" + str(StudentEthnicityMAID), verb = "get", return_params_list = return_params)

def modifyStudentEthnicityMA(StudentEthnicityMAID, EntityID = 1, setStudentEthnicityMAID = None, setCreatedTime = None, setEthnicityMAID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEthnicityMAID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/" + str(StudentEthnicityMAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEthnicityMA(EntityID = 1, setStudentEthnicityMAID = None, setCreatedTime = None, setEthnicityMAID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEthnicityMAID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEthnicityMA(StudentEthnicityMAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentEthnicityMA/" + str(StudentEthnicityMAID), verb = "delete")


def getEveryStudentLocker(searchConditions = [], EntityID = 1, returnStudentLockerID = False, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentLocker in the district.

    This function returns a dataframe of every StudentLocker in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentLocker(StudentLockerID, EntityID = 1, returnStudentLockerID = False, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(StudentLockerID), verb = "get", return_params_list = return_params)

def modifyStudentLocker(StudentLockerID, EntityID = 1, setStudentLockerID = None, setCreatedTime = None, setIsPrimaryLocker = None, setLockerID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentLockerID = False, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(StudentLockerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentLocker(EntityID = 1, setStudentLockerID = None, setCreatedTime = None, setIsPrimaryLocker = None, setLockerID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentLockerID = False, returnCreatedTime = False, returnIsPrimaryLocker = False, returnLockerID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentLocker(StudentLockerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentLocker/" + str(StudentLockerID), verb = "delete")


def getEveryStudentMassUpdate(searchConditions = [], EntityID = 1, returnStudentMassUpdateID = False, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentMassUpdate in the district.

    This function returns a dataframe of every StudentMassUpdate in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentMassUpdate(StudentMassUpdateID, EntityID = 1, returnStudentMassUpdateID = False, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(StudentMassUpdateID), verb = "get", return_params_list = return_params)

def modifyStudentMassUpdate(StudentMassUpdateID, EntityID = 1, setStudentMassUpdateID = None, setAsOfDate = None, setCreatedTime = None, setDistrictID = None, setFilterParameters = None, setModifiedTime = None, setRunReason = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRanBy = None, setValueParameters = None, returnStudentMassUpdateID = False, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(StudentMassUpdateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentMassUpdate(EntityID = 1, setStudentMassUpdateID = None, setAsOfDate = None, setCreatedTime = None, setDistrictID = None, setFilterParameters = None, setModifiedTime = None, setRunReason = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRanBy = None, setValueParameters = None, returnStudentMassUpdateID = False, returnAsOfDate = False, returnCreatedTime = False, returnDistrictID = False, returnFilterParameters = False, returnModifiedTime = False, returnRunReason = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRanBy = False, returnValueParameters = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentMassUpdate(StudentMassUpdateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMassUpdate/" + str(StudentMassUpdateID), verb = "delete")


def getEveryStudentMedia(searchConditions = [], EntityID = 1, returnStudentMediaID = False, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnDisplayOnFamilyAccessPortfolio = False, returnDisplayOnStudentAccessPortfolio = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentMedia in the district.

    This function returns a dataframe of every StudentMedia in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentMedia(StudentMediaID, EntityID = 1, returnStudentMediaID = False, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnDisplayOnFamilyAccessPortfolio = False, returnDisplayOnStudentAccessPortfolio = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(StudentMediaID), verb = "get", return_params_list = return_params)

def modifyStudentMedia(StudentMediaID, EntityID = 1, setStudentMediaID = None, setAttachmentTypeID = None, setCreatedTime = None, setDisplayInTeacherAccess = None, setDisplayName = None, setDisplayNameOrMediaName = None, setDisplayOnFamilyAccessPortfolio = None, setDisplayOnStudentAccessPortfolio = None, setMediaID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentMediaID = False, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnDisplayOnFamilyAccessPortfolio = False, returnDisplayOnStudentAccessPortfolio = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(StudentMediaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentMedia(EntityID = 1, setStudentMediaID = None, setAttachmentTypeID = None, setCreatedTime = None, setDisplayInTeacherAccess = None, setDisplayName = None, setDisplayNameOrMediaName = None, setDisplayOnFamilyAccessPortfolio = None, setDisplayOnStudentAccessPortfolio = None, setMediaID = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentMediaID = False, returnAttachmentTypeID = False, returnCreatedTime = False, returnDisplayInTeacherAccess = False, returnDisplayName = False, returnDisplayNameOrMediaName = False, returnDisplayOnFamilyAccessPortfolio = False, returnDisplayOnStudentAccessPortfolio = False, returnMediaID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentMedia(StudentMediaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentMedia/" + str(StudentMediaID), verb = "delete")


def getEveryStudent(searchConditions = [], EntityID = 1, returnStudentID = False, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEffectiveDateForDirectCertificationImport = False, returnEligibilityCategoryForDirectCertificationImport = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveInterventionPlan = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasInterventionPlanIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnInSpecifiedDirectCertificationImport = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTotalCommunityServiceHours = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Student in the district.

    This function returns a dataframe of every Student in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudent(StudentID, EntityID = 1, returnStudentID = False, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEffectiveDateForDirectCertificationImport = False, returnEligibilityCategoryForDirectCertificationImport = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveInterventionPlan = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasInterventionPlanIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnInSpecifiedDirectCertificationImport = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTotalCommunityServiceHours = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(StudentID), verb = "get", return_params_list = return_params)

def modifyStudent(StudentID, EntityID = 1, setStudentID = None, setAllowCustomerCategoryAdd = None, setAllowDistrictDistribution = None, setAllowHigherEdDistribution = None, setAllowLocalDistribution = None, setAllowMediaDistribution = None, setAllowMilitaryDistribution = None, setAllowPublicDistribution = None, setAllowStudentAccess = None, setAllowTripsDistribution = None, setAllowVendorsDistribution = None, setArrestCount = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCalculatedEntityYearIsActive = None, setCalculatedGrade = None, setCalculatedGradYear = None, setCalculatedLocation = None, setCalculatedPrimaryFormattedPhoneNumber = None, setCalculatedStudentStateID = None, setConversionKey = None, setCorporalPunishmentIncidents = None, setCreatedTime = None, setCurrentDefaultEntityIsActive = None, setCurrentEconomicIndicator = None, setDateOfFirstEntryWithdrawalInEntity = None, setDentalPolicyNumber = None, setDisciplinedBullyingDisability = None, setDisciplinedBullyingRace = None, setDisciplinedBullyingSex = None, setEarliestDistrictEnrollmentDate = None, setEarnedCredits = None, setEarnedCreditsPossible = None, setEdFiCountryIDBirth = None, setEffectiveDateForDirectCertificationImport = None, setEligibilityCategoryForDirectCertificationImport = None, setEntityConfigEarnedCredits = None, setEntityConfigFailedCredits = None, setEntryWithdrawalIDDefaultEntityToday = None, setExpulsionWithoutServicesCount = None, setExpulsionWithServicesCount = None, setFailedCredits = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFirstName = None, setFoodServiceOnlinePaymentOverrideType = None, setFoodServiceOnlinePaymentOverrideTypeCode = None, setFormattedVaccinationDates = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setGrade = None, setGradeNumeric = None, setGraduationDate = None, setGraduationRequirementYear = None, setGradYear = None, setHasActiveAlert = None, setHasActiveCriticalAlert = None, setHasActiveGeneralNote = None, setHasActiveHealthCondition = None, setHasActiveIHP = None, setHasActiveInterventionPlan = None, setHasActiveParentalConsentNote = None, setHasActiveSection504 = None, setHasActiveSpecialEducation = None, setHasActiveStudentGuardianRestrictedAccess = None, setHasAdvancedMathGrade0912 = None, setHasAlertIndicator = None, setHasAlgebraIGrade07 = None, setHasAlgebraIGrade08 = None, setHasAlgebraIGrade0910 = None, setHasAlgebraIGrade1112 = None, setHasAlgebraIIGrade0912 = None, setHasAllowStudentAccessButNoSecurity = None, setHasAPComputerScienceGrade0912 = None, setHasAPCourseGrade0912 = None, setHasAPMathGrade0912 = None, setHasAPOtherGrade0912 = None, setHasAPScienceGrade0912 = None, setHasBiologyGrade0912 = None, setHasCalculusGrade0912 = None, setHasChemistryGrade0912 = None, setHasComputerScienceGrade0912 = None, setHasCreditRecovery = None, setHasCriticalAlertIndicator = None, setHasDuplicateStudentNumber = None, setHasGeneralNoteIndicator = None, setHasGeometryGrade08 = None, setHasGeometryGrade0912 = None, setHasHealthIndicator = None, setHasIHPIndicator = None, setHasInterventionPlanIndicator = None, setHasOneNormalEnrollmentInEntityDuringSchoolYear = None, setHasParentalConsentNoteIndicator = None, setHasPassedAlgebraIGrade07 = None, setHasPassedAlgebraIGrade08 = None, setHasPassedAlgebraIGrade0910 = None, setHasPassedAlgebraIGrade1112 = None, setHasPhysicsGrade0912 = None, setHasSection504Indicator = None, setHasSpecialEducationIndicator = None, setHasStudentEntityYearForCurrentSchoolYear = None, setHasStudentGuardianWithAllowFamilyAccessButNoSecurity = None, setHasTakenACT0912 = None, setHasTakenAPExam0912 = None, setHasTakenSAT0912 = None, setHealthPolicyNumber = None, setHealthProfessionalIDDentist = None, setHealthProfessionalIDPrimaryPhysician = None, setIndicatorsXML = None, setInSchoolSuspensionCount = None, setInSpecifiedDirectCertificationImport = None, setIsActiveAsOfDate = None, setIsChronicallyAbsent = None, setIsCurrentActive = None, setIsCurrentActiveDefaultEnrollment = None, setIsCurrentlyTransported = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsGiftedTalentedSnapshot = None, setIsGraduated = None, setIsHealthProfessionalDentist = None, setIsHealthProfessionalPrimaryPhysician = None, setIsIBDiplomaProgramme = None, setIsIDEA = None, setIsIDEASnapshot = None, setIsLEP = None, setIsLEPSnapshot = None, setIsSection504 = None, setIsSection504Snapshot = None, setIsStateReportingUnknownGender = None, setLanguageIDNative = None, setLanguageIDPrimary = None, setLastName = None, setLawEnforcementReferralCount = None, setLocation = None, setLocationDateToUse = None, setLocationEntityID = None, setLocationSchoolYearID = None, setMaskedStudentNumber = None, setMechanicalRestraintCount = None, setMedicaidNumber = None, setMiddleName = None, setMMRStatus = None, setModifiedTime = None, setNameID = None, setNameIDDentalInsuranceCompany = None, setNameIDDentalPractice = None, setNameIDHealthInsuranceCompany = None, setNameIDHospital = None, setOutOfSchoolSuspensionCount = None, setOutOfSchoolSuspensionMissedDays = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodServiceOnlinePaymentAccess = None, setPhysicalRestraintCount = None, setReportedBulliedDisability = None, setReportedBulliedRace = None, setReportedBulliedSex = None, setSchoolPathExpectedSchoolCode = None, setSchoolPathExpectedSchoolName = None, setSchoolYearIDSpecifiedCohort = None, setSeclusionCount = None, setSingleSexAthleticCount = None, setSpecifiedCohortNumericSchoolYear = None, setSpecifiedEntityYearNoShow = None, setStateEthnicityRaceCodeMNID = None, setStudentIDHash = None, setStudentIndicatorColumn = None, setStudentMNID = None, setStudentNumber = None, setStudentNumberForGradebook = None, setStudentRankSort = None, setStudentStateID = None, setTotalCommunityServiceHours = None, setTransferToAlternativeSchool = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXMLIndicators = None, setZeroToleranceWithoutServicesCount = None, setZeroToleranceWithServicesCount = None, returnStudentID = False, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEffectiveDateForDirectCertificationImport = False, returnEligibilityCategoryForDirectCertificationImport = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveInterventionPlan = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasInterventionPlanIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnInSpecifiedDirectCertificationImport = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTotalCommunityServiceHours = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(StudentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudent(EntityID = 1, setStudentID = None, setAllowCustomerCategoryAdd = None, setAllowDistrictDistribution = None, setAllowHigherEdDistribution = None, setAllowLocalDistribution = None, setAllowMediaDistribution = None, setAllowMilitaryDistribution = None, setAllowPublicDistribution = None, setAllowStudentAccess = None, setAllowTripsDistribution = None, setAllowVendorsDistribution = None, setArrestCount = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCalculatedEntityYearIsActive = None, setCalculatedGrade = None, setCalculatedGradYear = None, setCalculatedLocation = None, setCalculatedPrimaryFormattedPhoneNumber = None, setCalculatedStudentStateID = None, setConversionKey = None, setCorporalPunishmentIncidents = None, setCreatedTime = None, setCurrentDefaultEntityIsActive = None, setCurrentEconomicIndicator = None, setDateOfFirstEntryWithdrawalInEntity = None, setDentalPolicyNumber = None, setDisciplinedBullyingDisability = None, setDisciplinedBullyingRace = None, setDisciplinedBullyingSex = None, setEarliestDistrictEnrollmentDate = None, setEarnedCredits = None, setEarnedCreditsPossible = None, setEdFiCountryIDBirth = None, setEffectiveDateForDirectCertificationImport = None, setEligibilityCategoryForDirectCertificationImport = None, setEntityConfigEarnedCredits = None, setEntityConfigFailedCredits = None, setEntryWithdrawalIDDefaultEntityToday = None, setExpulsionWithoutServicesCount = None, setExpulsionWithServicesCount = None, setFailedCredits = None, setFeeOnlinePaymentOverrideType = None, setFeeOnlinePaymentOverrideTypeCode = None, setFirstName = None, setFoodServiceOnlinePaymentOverrideType = None, setFoodServiceOnlinePaymentOverrideTypeCode = None, setFormattedVaccinationDates = None, setFullNameFL = None, setFullNameFML = None, setFullNameLFM = None, setGrade = None, setGradeNumeric = None, setGraduationDate = None, setGraduationRequirementYear = None, setGradYear = None, setHasActiveAlert = None, setHasActiveCriticalAlert = None, setHasActiveGeneralNote = None, setHasActiveHealthCondition = None, setHasActiveIHP = None, setHasActiveInterventionPlan = None, setHasActiveParentalConsentNote = None, setHasActiveSection504 = None, setHasActiveSpecialEducation = None, setHasActiveStudentGuardianRestrictedAccess = None, setHasAdvancedMathGrade0912 = None, setHasAlertIndicator = None, setHasAlgebraIGrade07 = None, setHasAlgebraIGrade08 = None, setHasAlgebraIGrade0910 = None, setHasAlgebraIGrade1112 = None, setHasAlgebraIIGrade0912 = None, setHasAllowStudentAccessButNoSecurity = None, setHasAPComputerScienceGrade0912 = None, setHasAPCourseGrade0912 = None, setHasAPMathGrade0912 = None, setHasAPOtherGrade0912 = None, setHasAPScienceGrade0912 = None, setHasBiologyGrade0912 = None, setHasCalculusGrade0912 = None, setHasChemistryGrade0912 = None, setHasComputerScienceGrade0912 = None, setHasCreditRecovery = None, setHasCriticalAlertIndicator = None, setHasDuplicateStudentNumber = None, setHasGeneralNoteIndicator = None, setHasGeometryGrade08 = None, setHasGeometryGrade0912 = None, setHasHealthIndicator = None, setHasIHPIndicator = None, setHasInterventionPlanIndicator = None, setHasOneNormalEnrollmentInEntityDuringSchoolYear = None, setHasParentalConsentNoteIndicator = None, setHasPassedAlgebraIGrade07 = None, setHasPassedAlgebraIGrade08 = None, setHasPassedAlgebraIGrade0910 = None, setHasPassedAlgebraIGrade1112 = None, setHasPhysicsGrade0912 = None, setHasSection504Indicator = None, setHasSpecialEducationIndicator = None, setHasStudentEntityYearForCurrentSchoolYear = None, setHasStudentGuardianWithAllowFamilyAccessButNoSecurity = None, setHasTakenACT0912 = None, setHasTakenAPExam0912 = None, setHasTakenSAT0912 = None, setHealthPolicyNumber = None, setHealthProfessionalIDDentist = None, setHealthProfessionalIDPrimaryPhysician = None, setIndicatorsXML = None, setInSchoolSuspensionCount = None, setInSpecifiedDirectCertificationImport = None, setIsActiveAsOfDate = None, setIsChronicallyAbsent = None, setIsCurrentActive = None, setIsCurrentActiveDefaultEnrollment = None, setIsCurrentlyTransported = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsGiftedTalentedSnapshot = None, setIsGraduated = None, setIsHealthProfessionalDentist = None, setIsHealthProfessionalPrimaryPhysician = None, setIsIBDiplomaProgramme = None, setIsIDEA = None, setIsIDEASnapshot = None, setIsLEP = None, setIsLEPSnapshot = None, setIsSection504 = None, setIsSection504Snapshot = None, setIsStateReportingUnknownGender = None, setLanguageIDNative = None, setLanguageIDPrimary = None, setLastName = None, setLawEnforcementReferralCount = None, setLocation = None, setLocationDateToUse = None, setLocationEntityID = None, setLocationSchoolYearID = None, setMaskedStudentNumber = None, setMechanicalRestraintCount = None, setMedicaidNumber = None, setMiddleName = None, setMMRStatus = None, setModifiedTime = None, setNameID = None, setNameIDDentalInsuranceCompany = None, setNameIDDentalPractice = None, setNameIDHealthInsuranceCompany = None, setNameIDHospital = None, setOutOfSchoolSuspensionCount = None, setOutOfSchoolSuspensionMissedDays = None, setOverrideFeeOnlinePaymentAccess = None, setOverrideFoodServiceOnlinePaymentAccess = None, setPhysicalRestraintCount = None, setReportedBulliedDisability = None, setReportedBulliedRace = None, setReportedBulliedSex = None, setSchoolPathExpectedSchoolCode = None, setSchoolPathExpectedSchoolName = None, setSchoolYearIDSpecifiedCohort = None, setSeclusionCount = None, setSingleSexAthleticCount = None, setSpecifiedCohortNumericSchoolYear = None, setSpecifiedEntityYearNoShow = None, setStateEthnicityRaceCodeMNID = None, setStudentIDHash = None, setStudentIndicatorColumn = None, setStudentMNID = None, setStudentNumber = None, setStudentNumberForGradebook = None, setStudentRankSort = None, setStudentStateID = None, setTotalCommunityServiceHours = None, setTransferToAlternativeSchool = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXMLIndicators = None, setZeroToleranceWithoutServicesCount = None, setZeroToleranceWithServicesCount = None, returnStudentID = False, returnAllowCustomerCategoryAdd = False, returnAllowDistrictDistribution = False, returnAllowHigherEdDistribution = False, returnAllowLocalDistribution = False, returnAllowMediaDistribution = False, returnAllowMilitaryDistribution = False, returnAllowPublicDistribution = False, returnAllowStudentAccess = False, returnAllowTripsDistribution = False, returnAllowVendorsDistribution = False, returnArrestCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCalculatedEntityYearIsActive = False, returnCalculatedGrade = False, returnCalculatedGradYear = False, returnCalculatedLocation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnCalculatedStudentStateID = False, returnConversionKey = False, returnCorporalPunishmentIncidents = False, returnCreatedTime = False, returnCurrentDefaultEntityIsActive = False, returnCurrentEconomicIndicator = False, returnDateOfFirstEntryWithdrawalInEntity = False, returnDentalPolicyNumber = False, returnDisciplinedBullyingDisability = False, returnDisciplinedBullyingRace = False, returnDisciplinedBullyingSex = False, returnEarliestDistrictEnrollmentDate = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEdFiCountryIDBirth = False, returnEffectiveDateForDirectCertificationImport = False, returnEligibilityCategoryForDirectCertificationImport = False, returnEntityConfigEarnedCredits = False, returnEntityConfigFailedCredits = False, returnEntryWithdrawalIDDefaultEntityToday = False, returnExpulsionWithoutServicesCount = False, returnExpulsionWithServicesCount = False, returnFailedCredits = False, returnFeeOnlinePaymentOverrideType = False, returnFeeOnlinePaymentOverrideTypeCode = False, returnFirstName = False, returnFoodServiceOnlinePaymentOverrideType = False, returnFoodServiceOnlinePaymentOverrideTypeCode = False, returnFormattedVaccinationDates = False, returnFullNameFL = False, returnFullNameFML = False, returnFullNameLFM = False, returnGrade = False, returnGradeNumeric = False, returnGraduationDate = False, returnGraduationRequirementYear = False, returnGradYear = False, returnHasActiveAlert = False, returnHasActiveCriticalAlert = False, returnHasActiveGeneralNote = False, returnHasActiveHealthCondition = False, returnHasActiveIHP = False, returnHasActiveInterventionPlan = False, returnHasActiveParentalConsentNote = False, returnHasActiveSection504 = False, returnHasActiveSpecialEducation = False, returnHasActiveStudentGuardianRestrictedAccess = False, returnHasAdvancedMathGrade0912 = False, returnHasAlertIndicator = False, returnHasAlgebraIGrade07 = False, returnHasAlgebraIGrade08 = False, returnHasAlgebraIGrade0910 = False, returnHasAlgebraIGrade1112 = False, returnHasAlgebraIIGrade0912 = False, returnHasAllowStudentAccessButNoSecurity = False, returnHasAPComputerScienceGrade0912 = False, returnHasAPCourseGrade0912 = False, returnHasAPMathGrade0912 = False, returnHasAPOtherGrade0912 = False, returnHasAPScienceGrade0912 = False, returnHasBiologyGrade0912 = False, returnHasCalculusGrade0912 = False, returnHasChemistryGrade0912 = False, returnHasComputerScienceGrade0912 = False, returnHasCreditRecovery = False, returnHasCriticalAlertIndicator = False, returnHasDuplicateStudentNumber = False, returnHasGeneralNoteIndicator = False, returnHasGeometryGrade08 = False, returnHasGeometryGrade0912 = False, returnHasHealthIndicator = False, returnHasIHPIndicator = False, returnHasInterventionPlanIndicator = False, returnHasOneNormalEnrollmentInEntityDuringSchoolYear = False, returnHasParentalConsentNoteIndicator = False, returnHasPassedAlgebraIGrade07 = False, returnHasPassedAlgebraIGrade08 = False, returnHasPassedAlgebraIGrade0910 = False, returnHasPassedAlgebraIGrade1112 = False, returnHasPhysicsGrade0912 = False, returnHasSection504Indicator = False, returnHasSpecialEducationIndicator = False, returnHasStudentEntityYearForCurrentSchoolYear = False, returnHasStudentGuardianWithAllowFamilyAccessButNoSecurity = False, returnHasTakenACT0912 = False, returnHasTakenAPExam0912 = False, returnHasTakenSAT0912 = False, returnHealthPolicyNumber = False, returnHealthProfessionalIDDentist = False, returnHealthProfessionalIDPrimaryPhysician = False, returnIndicatorsXML = False, returnInSchoolSuspensionCount = False, returnInSpecifiedDirectCertificationImport = False, returnIsActiveAsOfDate = False, returnIsChronicallyAbsent = False, returnIsCurrentActive = False, returnIsCurrentActiveDefaultEnrollment = False, returnIsCurrentlyTransported = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsGiftedTalentedSnapshot = False, returnIsGraduated = False, returnIsHealthProfessionalDentist = False, returnIsHealthProfessionalPrimaryPhysician = False, returnIsIBDiplomaProgramme = False, returnIsIDEA = False, returnIsIDEASnapshot = False, returnIsLEP = False, returnIsLEPSnapshot = False, returnIsSection504 = False, returnIsSection504Snapshot = False, returnIsStateReportingUnknownGender = False, returnLanguageIDNative = False, returnLanguageIDPrimary = False, returnLastName = False, returnLawEnforcementReferralCount = False, returnLocation = False, returnLocationDateToUse = False, returnLocationEntityID = False, returnLocationSchoolYearID = False, returnMaskedStudentNumber = False, returnMechanicalRestraintCount = False, returnMedicaidNumber = False, returnMiddleName = False, returnMMRStatus = False, returnModifiedTime = False, returnNameID = False, returnNameIDDentalInsuranceCompany = False, returnNameIDDentalPractice = False, returnNameIDHealthInsuranceCompany = False, returnNameIDHospital = False, returnOutOfSchoolSuspensionCount = False, returnOutOfSchoolSuspensionMissedDays = False, returnOverrideFeeOnlinePaymentAccess = False, returnOverrideFoodServiceOnlinePaymentAccess = False, returnPhysicalRestraintCount = False, returnReportedBulliedDisability = False, returnReportedBulliedRace = False, returnReportedBulliedSex = False, returnSchoolPathExpectedSchoolCode = False, returnSchoolPathExpectedSchoolName = False, returnSchoolYearIDSpecifiedCohort = False, returnSeclusionCount = False, returnSingleSexAthleticCount = False, returnSpecifiedCohortNumericSchoolYear = False, returnSpecifiedEntityYearNoShow = False, returnStateEthnicityRaceCodeMNID = False, returnStudentIDHash = False, returnStudentIndicatorColumn = False, returnStudentMNID = False, returnStudentNumber = False, returnStudentNumberForGradebook = False, returnStudentRankSort = False, returnStudentStateID = False, returnTotalCommunityServiceHours = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXMLIndicators = False, returnZeroToleranceWithoutServicesCount = False, returnZeroToleranceWithServicesCount = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudent(StudentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/Student/" + str(StudentID), verb = "delete")


def getEveryStudentNote(searchConditions = [], EntityID = 1, returnStudentNoteID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentNote in the district.

    This function returns a dataframe of every StudentNote in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentNote(StudentNoteID, EntityID = 1, returnStudentNoteID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(StudentNoteID), verb = "get", return_params_list = return_params)

def modifyStudentNote(StudentNoteID, EntityID = 1, setStudentNoteID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setDescription = None, setEndDate = None, setIsActive = None, setModifiedTime = None, setNoteTypeID = None, setStartDate = None, setStudentID = None, setStudentTransportationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentNoteID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(StudentNoteID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentNote(EntityID = 1, setStudentNoteID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setDescription = None, setEndDate = None, setIsActive = None, setModifiedTime = None, setNoteTypeID = None, setStartDate = None, setStudentID = None, setStudentTransportationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentNoteID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnNoteTypeID = False, returnStartDate = False, returnStudentID = False, returnStudentTransportationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentNote(StudentNoteID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/StudentNote/" + str(StudentNoteID), verb = "delete")


def getEveryTempActivityRecord(searchConditions = [], EntityID = 1, returnTempActivityRecordID = False, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempActivityRecord in the district.

    This function returns a dataframe of every TempActivityRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempActivityRecord(TempActivityRecordID, EntityID = 1, returnTempActivityRecordID = False, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(TempActivityRecordID), verb = "get", return_params_list = return_params)

def modifyTempActivityRecord(TempActivityRecordID, EntityID = 1, setTempActivityRecordID = None, setActivityID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setNewEndDate = None, setNewStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempActivityRecordID = False, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(TempActivityRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempActivityRecord(EntityID = 1, setTempActivityRecordID = None, setActivityID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setNewEndDate = None, setNewStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempActivityRecordID = False, returnActivityID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempActivityRecord(TempActivityRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempActivityRecord/" + str(TempActivityRecordID), verb = "delete")


def getEveryTempFitnessGram(searchConditions = [], EntityID = 1, returnTempFitnessGramID = False, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFitnessGram in the district.

    This function returns a dataframe of every TempFitnessGram in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFitnessGram(TempFitnessGramID, EntityID = 1, returnTempFitnessGramID = False, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(TempFitnessGramID), verb = "get", return_params_list = return_params)

def modifyTempFitnessGram(TempFitnessGramID, EntityID = 1, setTempFitnessGramID = None, setClassDescription = None, setClassEndDate = None, setClassID = None, setClassName = None, setClassStartDate = None, setCourseCodeDescription = None, setCreatedTime = None, setHasMissingData = None, setMessage = None, setModifiedTime = None, setParentReportEmail1 = None, setParentReportEmail2 = None, setSchoolID = None, setSectionCode = None, setStudentBirthdate = None, setStudentFirstName = None, setStudentGender = None, setStudentGrade = None, setStudentID = None, setStudentLastName = None, setStudentMiddleInitial = None, setStudentPassword = None, setStudentReportEmail = None, setStudentSSOID = None, setTeacherBirthDate = None, setTeacherEmail = None, setTeacherFirstName = None, setTeacherID = None, setTeacherLastName = None, setTeacherMiddleInitial = None, setTeacherPassword = None, setTeacherSSOID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFitnessGramID = False, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(TempFitnessGramID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFitnessGram(EntityID = 1, setTempFitnessGramID = None, setClassDescription = None, setClassEndDate = None, setClassID = None, setClassName = None, setClassStartDate = None, setCourseCodeDescription = None, setCreatedTime = None, setHasMissingData = None, setMessage = None, setModifiedTime = None, setParentReportEmail1 = None, setParentReportEmail2 = None, setSchoolID = None, setSectionCode = None, setStudentBirthdate = None, setStudentFirstName = None, setStudentGender = None, setStudentGrade = None, setStudentID = None, setStudentLastName = None, setStudentMiddleInitial = None, setStudentPassword = None, setStudentReportEmail = None, setStudentSSOID = None, setTeacherBirthDate = None, setTeacherEmail = None, setTeacherFirstName = None, setTeacherID = None, setTeacherLastName = None, setTeacherMiddleInitial = None, setTeacherPassword = None, setTeacherSSOID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFitnessGramID = False, returnClassDescription = False, returnClassEndDate = False, returnClassID = False, returnClassName = False, returnClassStartDate = False, returnCourseCodeDescription = False, returnCreatedTime = False, returnHasMissingData = False, returnMessage = False, returnModifiedTime = False, returnParentReportEmail1 = False, returnParentReportEmail2 = False, returnSchoolID = False, returnSectionCode = False, returnStudentBirthdate = False, returnStudentFirstName = False, returnStudentGender = False, returnStudentGrade = False, returnStudentID = False, returnStudentLastName = False, returnStudentMiddleInitial = False, returnStudentPassword = False, returnStudentReportEmail = False, returnStudentSSOID = False, returnTeacherBirthDate = False, returnTeacherEmail = False, returnTeacherFirstName = False, returnTeacherID = False, returnTeacherLastName = False, returnTeacherMiddleInitial = False, returnTeacherPassword = False, returnTeacherSSOID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFitnessGram(TempFitnessGramID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempFitnessGram/" + str(TempFitnessGramID), verb = "delete")


def getEveryTempLockCombination(searchConditions = [], EntityID = 1, returnTempLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempLockCombination in the district.

    This function returns a dataframe of every TempLockCombination in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempLockCombination(TempLockCombinationID, EntityID = 1, returnTempLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(TempLockCombinationID), verb = "get", return_params_list = return_params)

def modifyTempLockCombination(TempLockCombinationID, EntityID = 1, setTempLockCombinationID = None, setCombination = None, setCombinationNumber = None, setCreatedTime = None, setFailureReason = None, setModifiedTime = None, setTempLockerID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(TempLockCombinationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempLockCombination(EntityID = 1, setTempLockCombinationID = None, setCombination = None, setCombinationNumber = None, setCreatedTime = None, setFailureReason = None, setModifiedTime = None, setTempLockerID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempLockCombinationID = False, returnCombination = False, returnCombinationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempLockerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempLockCombination(TempLockCombinationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLockCombination/" + str(TempLockCombinationID), verb = "delete")


def getEveryTempLocker(searchConditions = [], EntityID = 1, returnTempLockerID = False, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempLocker in the district.

    This function returns a dataframe of every TempLocker in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempLocker(TempLockerID, EntityID = 1, returnTempLockerID = False, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(TempLockerID), verb = "get", return_params_list = return_params)

def modifyTempLocker(TempLockerID, EntityID = 1, setTempLockerID = None, setBuilding = None, setBuildingID = None, setComment = None, setCreatedTime = None, setFailureReason = None, setLockerArea = None, setLockerAreaID = None, setLockerID = None, setLockerNumber = None, setLockerNumberDigitLength = None, setModifiedTime = None, setNewLockerNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempLockerID = False, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(TempLockerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempLocker(EntityID = 1, setTempLockerID = None, setBuilding = None, setBuildingID = None, setComment = None, setCreatedTime = None, setFailureReason = None, setLockerArea = None, setLockerAreaID = None, setLockerID = None, setLockerNumber = None, setLockerNumberDigitLength = None, setModifiedTime = None, setNewLockerNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempLockerID = False, returnBuilding = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnFailureReason = False, returnLockerArea = False, returnLockerAreaID = False, returnLockerID = False, returnLockerNumber = False, returnLockerNumberDigitLength = False, returnModifiedTime = False, returnNewLockerNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempLocker(TempLockerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempLocker/" + str(TempLockerID), verb = "delete")


def getEveryTempStudentActivity(searchConditions = [], EntityID = 1, returnTempStudentActivityID = False, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentActivity in the district.

    This function returns a dataframe of every TempStudentActivity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentActivity(TempStudentActivityID, EntityID = 1, returnTempStudentActivityID = False, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(TempStudentActivityID), verb = "get", return_params_list = return_params)

def modifyTempStudentActivity(TempStudentActivityID, EntityID = 1, setTempStudentActivityID = None, setActivityID = None, setAge = None, setCode = None, setCreatedTime = None, setDescription = None, setEndDate = None, setEntityCode = None, setErrorNumber = None, setFullNameLFM = None, setGenderCodeAndGender = None, setGradeLevel = None, setGradYear = None, setIsActive = None, setModifiedTime = None, setParticipationEndDate = None, setParticipationStartDate = None, setStartDate = None, setStudentID = None, setStudentName = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentActivityID = False, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(TempStudentActivityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentActivity(EntityID = 1, setTempStudentActivityID = None, setActivityID = None, setAge = None, setCode = None, setCreatedTime = None, setDescription = None, setEndDate = None, setEntityCode = None, setErrorNumber = None, setFullNameLFM = None, setGenderCodeAndGender = None, setGradeLevel = None, setGradYear = None, setIsActive = None, setModifiedTime = None, setParticipationEndDate = None, setParticipationStartDate = None, setStartDate = None, setStudentID = None, setStudentName = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentActivityID = False, returnActivityID = False, returnAge = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityCode = False, returnErrorNumber = False, returnFullNameLFM = False, returnGenderCodeAndGender = False, returnGradeLevel = False, returnGradYear = False, returnIsActive = False, returnModifiedTime = False, returnParticipationEndDate = False, returnParticipationStartDate = False, returnStartDate = False, returnStudentID = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentActivity(TempStudentActivityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivity/" + str(TempStudentActivityID), verb = "delete")


def getEveryTempStudentActivityError(searchConditions = [], EntityID = 1, returnTempStudentActivityErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentActivityError in the district.

    This function returns a dataframe of every TempStudentActivityError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentActivityError(TempStudentActivityErrorID, EntityID = 1, returnTempStudentActivityErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(TempStudentActivityErrorID), verb = "get", return_params_list = return_params)

def modifyTempStudentActivityError(TempStudentActivityErrorID, EntityID = 1, setTempStudentActivityErrorID = None, setCreatedTime = None, setErrorNumber = None, setErrorText = None, setModifiedTime = None, setTempStudentActivityID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentActivityErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(TempStudentActivityErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentActivityError(EntityID = 1, setTempStudentActivityErrorID = None, setCreatedTime = None, setErrorNumber = None, setErrorText = None, setModifiedTime = None, setTempStudentActivityID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentActivityErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempStudentActivityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentActivityError(TempStudentActivityErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityError/" + str(TempStudentActivityErrorID), verb = "delete")


def getEveryTempStudentActivityTransactionRecord(searchConditions = [], EntityID = 1, returnTempStudentActivityTransactionRecordID = False, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentActivityTransactionRecord in the district.

    This function returns a dataframe of every TempStudentActivityTransactionRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentActivityTransactionRecord(TempStudentActivityTransactionRecordID, EntityID = 1, returnTempStudentActivityTransactionRecordID = False, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(TempStudentActivityTransactionRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentActivityTransactionRecord(TempStudentActivityTransactionRecordID, EntityID = 1, setTempStudentActivityTransactionRecordID = None, setActivityID = None, setCreatedTime = None, setIsValidTransaction = None, setModifiedTime = None, setNewEndDate = None, setNewStartDate = None, setStudentActivityTransactionID = None, setStudentFullNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentActivityTransactionRecordID = False, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(TempStudentActivityTransactionRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentActivityTransactionRecord(EntityID = 1, setTempStudentActivityTransactionRecordID = None, setActivityID = None, setCreatedTime = None, setIsValidTransaction = None, setModifiedTime = None, setNewEndDate = None, setNewStartDate = None, setStudentActivityTransactionID = None, setStudentFullNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentActivityTransactionRecordID = False, returnActivityID = False, returnCreatedTime = False, returnIsValidTransaction = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnStudentActivityTransactionID = False, returnStudentFullNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentActivityTransactionRecord(TempStudentActivityTransactionRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentActivityTransactionRecord/" + str(TempStudentActivityTransactionRecordID), verb = "delete")


def getEveryTempStudentAssignedLockCombinationRecord(searchConditions = [], EntityID = 1, returnTempStudentAssignedLockCombinationRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentAssignedLockCombinationRecord in the district.

    This function returns a dataframe of every TempStudentAssignedLockCombinationRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentAssignedLockCombinationRecord(TempStudentAssignedLockCombinationRecordID, EntityID = 1, returnTempStudentAssignedLockCombinationRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(TempStudentAssignedLockCombinationRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentAssignedLockCombinationRecord(TempStudentAssignedLockCombinationRecordID, EntityID = 1, setTempStudentAssignedLockCombinationRecordID = None, setAge = None, setBirthDate = None, setBuilding = None, setCreatedTime = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setLockID = None, setModifiedTime = None, setNewCombination = None, setNewCombinationNumber = None, setNewLockCombinationID = None, setOldCombination = None, setOldCombinationNumber = None, setOldLockCombinationID = None, setStudentID = None, setStudentNumber = None, setUnoccupiedLockersOnly = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentAssignedLockCombinationRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(TempStudentAssignedLockCombinationRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentAssignedLockCombinationRecord(EntityID = 1, setTempStudentAssignedLockCombinationRecordID = None, setAge = None, setBirthDate = None, setBuilding = None, setCreatedTime = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setLockID = None, setModifiedTime = None, setNewCombination = None, setNewCombinationNumber = None, setNewLockCombinationID = None, setOldCombination = None, setOldCombinationNumber = None, setOldLockCombinationID = None, setStudentID = None, setStudentNumber = None, setUnoccupiedLockersOnly = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentAssignedLockCombinationRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnLockID = False, returnModifiedTime = False, returnNewCombination = False, returnNewCombinationNumber = False, returnNewLockCombinationID = False, returnOldCombination = False, returnOldCombinationNumber = False, returnOldLockCombinationID = False, returnStudentID = False, returnStudentNumber = False, returnUnoccupiedLockersOnly = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentAssignedLockCombinationRecord(TempStudentAssignedLockCombinationRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockCombinationRecord/" + str(TempStudentAssignedLockCombinationRecordID), verb = "delete")


def getEveryTempStudentAssignedLockerRecord(searchConditions = [], EntityID = 1, returnTempStudentAssignedLockerRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentAssignedLockerRecord in the district.

    This function returns a dataframe of every TempStudentAssignedLockerRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentAssignedLockerRecord(TempStudentAssignedLockerRecordID, EntityID = 1, returnTempStudentAssignedLockerRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(TempStudentAssignedLockerRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentAssignedLockerRecord(TempStudentAssignedLockerRecordID, EntityID = 1, setTempStudentAssignedLockerRecordID = None, setAge = None, setBirthDate = None, setBuilding = None, setCombination = None, setCreatedTime = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setIsStudentAccessUser = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setModifiedTime = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentAssignedLockerRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(TempStudentAssignedLockerRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentAssignedLockerRecord(EntityID = 1, setTempStudentAssignedLockerRecordID = None, setAge = None, setBirthDate = None, setBuilding = None, setCombination = None, setCreatedTime = None, setFullName = None, setGender = None, setGrade = None, setGradYear = None, setIsStudentAccessUser = None, setLockerArea = None, setLockerID = None, setLockerNumber = None, setModifiedTime = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentAssignedLockerRecordID = False, returnAge = False, returnBirthDate = False, returnBuilding = False, returnCombination = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGrade = False, returnGradYear = False, returnIsStudentAccessUser = False, returnLockerArea = False, returnLockerID = False, returnLockerNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentAssignedLockerRecord(TempStudentAssignedLockerRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentAssignedLockerRecord/" + str(TempStudentAssignedLockerRecordID), verb = "delete")


def getEveryTempStudentError(searchConditions = [], EntityID = 1, returnTempStudentErrorID = False, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentError in the district.

    This function returns a dataframe of every TempStudentError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentError(TempStudentErrorID, EntityID = 1, returnTempStudentErrorID = False, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(TempStudentErrorID), verb = "get", return_params_list = return_params)

def modifyTempStudentError(TempStudentErrorID, EntityID = 1, setTempStudentErrorID = None, setCreatedTime = None, setErrorCount = None, setFullStudentNameLFM = None, setGender = None, setGradeLevelCode = None, setGraduationRequirementYear = None, setGradYear = None, setIsCurrentActive = None, setLockerNumber = None, setModifiedTime = None, setNote = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentErrorID = False, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(TempStudentErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentError(EntityID = 1, setTempStudentErrorID = None, setCreatedTime = None, setErrorCount = None, setFullStudentNameLFM = None, setGender = None, setGradeLevelCode = None, setGraduationRequirementYear = None, setGradYear = None, setIsCurrentActive = None, setLockerNumber = None, setModifiedTime = None, setNote = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentErrorID = False, returnCreatedTime = False, returnErrorCount = False, returnFullStudentNameLFM = False, returnGender = False, returnGradeLevelCode = False, returnGraduationRequirementYear = False, returnGradYear = False, returnIsCurrentActive = False, returnLockerNumber = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentError(TempStudentErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentError/" + str(TempStudentErrorID), verb = "delete")


def getEveryTempStudentErrorMessage(searchConditions = [], EntityID = 1, returnTempStudentErrorMessageID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentErrorMessage in the district.

    This function returns a dataframe of every TempStudentErrorMessage in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentErrorMessage(TempStudentErrorMessageID, EntityID = 1, returnTempStudentErrorMessageID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(TempStudentErrorMessageID), verb = "get", return_params_list = return_params)

def modifyTempStudentErrorMessage(TempStudentErrorMessageID, EntityID = 1, setTempStudentErrorMessageID = None, setCreatedTime = None, setError = None, setErrorDetail = None, setModifiedTime = None, setTempStudentErrorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentErrorMessageID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(TempStudentErrorMessageID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentErrorMessage(EntityID = 1, setTempStudentErrorMessageID = None, setCreatedTime = None, setError = None, setErrorDetail = None, setModifiedTime = None, setTempStudentErrorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentErrorMessageID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentErrorMessage(TempStudentErrorMessageID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentErrorMessage/" + str(TempStudentErrorMessageID), verb = "delete")


def getEveryTempStudentMassUpdateError(searchConditions = [], EntityID = 1, returnTempStudentMassUpdateErrorID = False, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentMassUpdateError in the district.

    This function returns a dataframe of every TempStudentMassUpdateError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentMassUpdateError(TempStudentMassUpdateErrorID, EntityID = 1, returnTempStudentMassUpdateErrorID = False, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(TempStudentMassUpdateErrorID), verb = "get", return_params_list = return_params)

def modifyTempStudentMassUpdateError(TempStudentMassUpdateErrorID, EntityID = 1, setTempStudentMassUpdateErrorID = None, setCreatedTime = None, setFailureReason = None, setFullNameLFM = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentMassUpdateErrorID = False, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(TempStudentMassUpdateErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentMassUpdateError(EntityID = 1, setTempStudentMassUpdateErrorID = None, setCreatedTime = None, setFailureReason = None, setFullNameLFM = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentMassUpdateErrorID = False, returnCreatedTime = False, returnFailureReason = False, returnFullNameLFM = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentMassUpdateError(TempStudentMassUpdateErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateError/" + str(TempStudentMassUpdateErrorID), verb = "delete")


def getEveryTempStudentMassUpdateField(searchConditions = [], EntityID = 1, returnTempStudentMassUpdateFieldID = False, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentMassUpdateField in the district.

    This function returns a dataframe of every TempStudentMassUpdateField in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentMassUpdateField(TempStudentMassUpdateFieldID, EntityID = 1, returnTempStudentMassUpdateFieldID = False, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(TempStudentMassUpdateFieldID), verb = "get", return_params_list = return_params)

def modifyTempStudentMassUpdateField(TempStudentMassUpdateFieldID, EntityID = 1, setTempStudentMassUpdateFieldID = None, setAffectedPrimaryKey = None, setCreatedTime = None, setFieldName = None, setFriendlyOriginalValue = None, setFriendlyUpdatedValue = None, setFullNameLFM = None, setModifiedTime = None, setOriginalValue = None, setRelatedType = None, setRelatedTypeCode = None, setStudentID = None, setUpdatedValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentMassUpdateFieldID = False, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(TempStudentMassUpdateFieldID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentMassUpdateField(EntityID = 1, setTempStudentMassUpdateFieldID = None, setAffectedPrimaryKey = None, setCreatedTime = None, setFieldName = None, setFriendlyOriginalValue = None, setFriendlyUpdatedValue = None, setFullNameLFM = None, setModifiedTime = None, setOriginalValue = None, setRelatedType = None, setRelatedTypeCode = None, setStudentID = None, setUpdatedValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentMassUpdateFieldID = False, returnAffectedPrimaryKey = False, returnCreatedTime = False, returnFieldName = False, returnFriendlyOriginalValue = False, returnFriendlyUpdatedValue = False, returnFullNameLFM = False, returnModifiedTime = False, returnOriginalValue = False, returnRelatedType = False, returnRelatedTypeCode = False, returnStudentID = False, returnUpdatedValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentMassUpdateField(TempStudentMassUpdateFieldID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMassUpdateField/" + str(TempStudentMassUpdateFieldID), verb = "delete")


def getEveryTempStudentMergeObject(searchConditions = [], EntityID = 1, returnTempStudentMergeObjectID = False, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentMergeObject in the district.

    This function returns a dataframe of every TempStudentMergeObject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentMergeObject(TempStudentMergeObjectID, EntityID = 1, returnTempStudentMergeObjectID = False, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(TempStudentMergeObjectID), verb = "get", return_params_list = return_params)

def modifyTempStudentMergeObject(TempStudentMergeObjectID, EntityID = 1, setTempStudentMergeObjectID = None, setCreatedTime = None, setFieldToShow = None, setHandlingType = None, setHandlingTypeCode = None, setModifiedTime = None, setRecordType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentMergeObjectID = False, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(TempStudentMergeObjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentMergeObject(EntityID = 1, setTempStudentMergeObjectID = None, setCreatedTime = None, setFieldToShow = None, setHandlingType = None, setHandlingTypeCode = None, setModifiedTime = None, setRecordType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentMergeObjectID = False, returnCreatedTime = False, returnFieldToShow = False, returnHandlingType = False, returnHandlingTypeCode = False, returnModifiedTime = False, returnRecordType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentMergeObject(TempStudentMergeObjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentMergeObject/" + str(TempStudentMergeObjectID), verb = "delete")


def getEveryTempStudentPermit(searchConditions = [], EntityID = 1, returnTempStudentPermitID = False, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnDistrictID = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentPermit in the district.

    This function returns a dataframe of every TempStudentPermit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentPermit(TempStudentPermitID, EntityID = 1, returnTempStudentPermitID = False, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnDistrictID = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(TempStudentPermitID), verb = "get", return_params_list = return_params)

def modifyTempStudentPermit(TempStudentPermitID, EntityID = 1, setTempStudentPermitID = None, setAddressID = None, setAge = None, setCreatedTime = None, setDistrictID = None, setEntityName = None, setExceptionNote = None, setFullNameLFM = None, setGenderCode = None, setGradYear = None, setHasExceptions = None, setModifiedTime = None, setPermitID = None, setSchoolYearID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentPermitID = False, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnDistrictID = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(TempStudentPermitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentPermit(EntityID = 1, setTempStudentPermitID = None, setAddressID = None, setAge = None, setCreatedTime = None, setDistrictID = None, setEntityName = None, setExceptionNote = None, setFullNameLFM = None, setGenderCode = None, setGradYear = None, setHasExceptions = None, setModifiedTime = None, setPermitID = None, setSchoolYearID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentPermitID = False, returnAddressID = False, returnAge = False, returnCreatedTime = False, returnDistrictID = False, returnEntityName = False, returnExceptionNote = False, returnFullNameLFM = False, returnGenderCode = False, returnGradYear = False, returnHasExceptions = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentPermit(TempStudentPermitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentPermit/" + str(TempStudentPermitID), verb = "delete")


def getEveryTempStudentWithoutLockerRecord(searchConditions = [], EntityID = 1, returnTempStudentWithoutLockerRecordID = False, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentWithoutLockerRecord in the district.

    This function returns a dataframe of every TempStudentWithoutLockerRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentWithoutLockerRecord(TempStudentWithoutLockerRecordID, EntityID = 1, returnTempStudentWithoutLockerRecordID = False, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(TempStudentWithoutLockerRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentWithoutLockerRecord(TempStudentWithoutLockerRecordID, EntityID = 1, setTempStudentWithoutLockerRecordID = None, setAge = None, setCreatedTime = None, setFullName = None, setGender = None, setGradYear = None, setModifiedTime = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentWithoutLockerRecordID = False, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(TempStudentWithoutLockerRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentWithoutLockerRecord(EntityID = 1, setTempStudentWithoutLockerRecordID = None, setAge = None, setCreatedTime = None, setFullName = None, setGender = None, setGradYear = None, setModifiedTime = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentWithoutLockerRecordID = False, returnAge = False, returnCreatedTime = False, returnFullName = False, returnGender = False, returnGradYear = False, returnModifiedTime = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentWithoutLockerRecord(TempStudentWithoutLockerRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/TempStudentWithoutLockerRecord/" + str(TempStudentWithoutLockerRecordID), verb = "delete")


def getEveryWinterSport(searchConditions = [], EntityID = 1, returnWinterSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every WinterSport in the district.

    This function returns a dataframe of every WinterSport in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getWinterSport(WinterSportID, EntityID = 1, returnWinterSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(WinterSportID), verb = "get", return_params_list = return_params)

def modifyWinterSport(WinterSportID, EntityID = 1, setWinterSportID = None, setCode = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWinterSport = None, returnWinterSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(WinterSportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createWinterSport(EntityID = 1, setWinterSportID = None, setCode = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWinterSport = None, returnWinterSportID = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSport = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteWinterSport(WinterSportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSport/" + str(WinterSportID), verb = "delete")


def getEveryWinterSportsTeam(searchConditions = [], EntityID = 1, returnWinterSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every WinterSportsTeam in the district.

    This function returns a dataframe of every WinterSportsTeam in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getWinterSportsTeam(WinterSportsTeamID, EntityID = 1, returnWinterSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(WinterSportsTeamID), verb = "get", return_params_list = return_params)

def modifyWinterSportsTeam(WinterSportsTeamID, EntityID = 1, setWinterSportsTeamID = None, setCaptain = None, setCreatedTime = None, setLettered = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWinterSportID = None, returnWinterSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(WinterSportsTeamID), verb = "post", return_params_list = return_params, payload = payload_params)

def createWinterSportsTeam(EntityID = 1, setWinterSportsTeamID = None, setCaptain = None, setCreatedTime = None, setLettered = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWinterSportID = None, returnWinterSportsTeamID = False, returnCaptain = False, returnCreatedTime = False, returnLettered = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWinterSportID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteWinterSportsTeam(WinterSportsTeamID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Student/WinterSportsTeam/" + str(WinterSportsTeamID), verb = "delete")