# This module contains Enrollment functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAMTransportation(searchConditions = [], EntityID = 1, returnAMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AMTransportation in the district.

    This function returns a dataframe of every AMTransportation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAMTransportation(AMTransportationID, EntityID = 1, returnAMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/" + str(AMTransportationID), verb = "get", return_params_list = return_params)

def modifyAMTransportation(AMTransportationID, EntityID = 1, setAMTransportationID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/" + str(AMTransportationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAMTransportation(EntityID = 1, setAMTransportationID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAMTransportation(AMTransportationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AMTransportation/" + str(AMTransportationID), verb = "delete")


def getEveryCommonEducationDataStandardsGradeLevel(searchConditions = [], EntityID = 1, returnCommonEducationDataStandardsGradeLevelID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CommonEducationDataStandardsGradeLevel in the district.

    This function returns a dataframe of every CommonEducationDataStandardsGradeLevel in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCommonEducationDataStandardsGradeLevel(CommonEducationDataStandardsGradeLevelID, EntityID = 1, returnCommonEducationDataStandardsGradeLevelID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/" + str(CommonEducationDataStandardsGradeLevelID), verb = "get", return_params_list = return_params)

def modifyCommonEducationDataStandardsGradeLevel(CommonEducationDataStandardsGradeLevelID, EntityID = 1, setCommonEducationDataStandardsGradeLevelID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setOrderNumber = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCommonEducationDataStandardsGradeLevelID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/" + str(CommonEducationDataStandardsGradeLevelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCommonEducationDataStandardsGradeLevel(EntityID = 1, setCommonEducationDataStandardsGradeLevelID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setOrderNumber = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCommonEducationDataStandardsGradeLevelID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCommonEducationDataStandardsGradeLevel(CommonEducationDataStandardsGradeLevelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/CommonEducationDataStandardsGradeLevel/" + str(CommonEducationDataStandardsGradeLevelID), verb = "delete")


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = False, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setConfigDistrictID = None, setAllowDualEnrollment = None, setCreatedTime = None, setDistrictID = None, setEntryDaysBeforeCalendarStart = None, setModifiedTime = None, setNumberDaysBackdateEntry = None, setNumberDaysBackdateWithdrawal = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalDaysAfterCalendarEnd = None, returnConfigDistrictID = False, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrict(EntityID = 1, setConfigDistrictID = None, setAllowDualEnrollment = None, setCreatedTime = None, setDistrictID = None, setEntryDaysBeforeCalendarStart = None, setModifiedTime = None, setNumberDaysBackdateEntry = None, setNumberDaysBackdateWithdrawal = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalDaysAfterCalendarEnd = None, returnConfigDistrictID = False, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnAutoAddSchoolPathOverride = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPermitIDAutoAdd = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = False, returnAutoAddSchoolPathOverride = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPermitIDAutoAdd = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearID = None, setAutoAddSchoolPathOverride = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDistrictID = None, setEnableNoShow = None, setEnrolledDifferentEntityNoShowActionType = None, setEnrolledDifferentEntityNoShowActionTypeCode = None, setEnrolledDifferentEntityNoShowEntryDate = None, setEnrolledDifferentEntityNoShowWithdrawalDate = None, setModifiedTime = None, setNoDistrictEnrollmentNoShowActionType = None, setNoDistrictEnrollmentNoShowActionTypeCode = None, setNoDistrictEnrollmentNoShowEntryDate = None, setNoDistrictEnrollmentNoShowWithdrawalDate = None, setPermitIDAutoAdd = None, setPreviouslyEnrolledSameEntityNoShowActionType = None, setPreviouslyEnrolledSameEntityNoShowActionTypeCode = None, setPreviouslyEnrolledSameEntityNoShowEntryDate = None, setPreviouslyEnrolledSameEntityNoShowWithdrawalDate = None, setPriorNoShowRecord = None, setPriorNoShowRecordCode = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnAutoAddSchoolPathOverride = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPermitIDAutoAdd = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearID = None, setAutoAddSchoolPathOverride = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDistrictID = None, setEnableNoShow = None, setEnrolledDifferentEntityNoShowActionType = None, setEnrolledDifferentEntityNoShowActionTypeCode = None, setEnrolledDifferentEntityNoShowEntryDate = None, setEnrolledDifferentEntityNoShowWithdrawalDate = None, setModifiedTime = None, setNoDistrictEnrollmentNoShowActionType = None, setNoDistrictEnrollmentNoShowActionTypeCode = None, setNoDistrictEnrollmentNoShowEntryDate = None, setNoDistrictEnrollmentNoShowWithdrawalDate = None, setPermitIDAutoAdd = None, setPreviouslyEnrolledSameEntityNoShowActionType = None, setPreviouslyEnrolledSameEntityNoShowActionTypeCode = None, setPreviouslyEnrolledSameEntityNoShowEntryDate = None, setPreviouslyEnrolledSameEntityNoShowWithdrawalDate = None, setPriorNoShowRecord = None, setPriorNoShowRecordCode = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnAutoAddSchoolPathOverride = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPermitIDAutoAdd = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")


def getEveryConfigDistrictYearWithdrawalCode(searchConditions = [], EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, setConfigDistrictYearWithdrawalCodeID = None, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setCreatedTime = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYearWithdrawalCode(EntityID = 1, setConfigDistrictYearWithdrawalCodeID = None, setConfigDistrictYearID = None, setConfigDistrictYearWithdrawalCodeIDClonedFrom = None, setCreatedTime = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, returnConfigDistrictYearWithdrawalCodeID = False, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "delete")


def getEveryEntitySchool(searchConditions = [], EntityID = 1, returnEntitySchoolID = False, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntitySchool in the district.

    This function returns a dataframe of every EntitySchool in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntitySchool(EntitySchoolID, EntityID = 1, returnEntitySchoolID = False, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "get", return_params_list = return_params)

def modifyEntitySchool(EntitySchoolID, EntityID = 1, setEntitySchoolID = None, setCreatedTime = None, setEntityID = None, setEntitySchoolIDClonedFrom = None, setEntitySchoolIDClonedTo = None, setIsDefaultEntityForSchool = None, setIsDefaultSchoolForEntity = None, setIsOnlySchoolInEntity = None, setModifiedTime = None, setSchoolID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntitySchoolID = False, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntitySchool(EntityID = 1, setEntitySchoolID = None, setCreatedTime = None, setEntityID = None, setEntitySchoolIDClonedFrom = None, setEntitySchoolIDClonedTo = None, setIsDefaultEntityForSchool = None, setIsDefaultSchoolForEntity = None, setIsOnlySchoolInEntity = None, setModifiedTime = None, setSchoolID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntitySchoolID = False, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntitySchool(EntitySchoolID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "delete")


def getEveryEntitySchoolBuilding(searchConditions = [], EntityID = 1, returnEntitySchoolBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntitySchoolBuilding in the district.

    This function returns a dataframe of every EntitySchoolBuilding in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1, returnEntitySchoolBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "get", return_params_list = return_params)

def modifyEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1, setEntitySchoolBuildingID = None, setBuildingID = None, setCreatedTime = None, setEntitySchoolBuildingIDClonedFrom = None, setEntitySchoolID = None, setIsPrimary = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntitySchoolBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntitySchoolBuilding(EntityID = 1, setEntitySchoolBuildingID = None, setBuildingID = None, setCreatedTime = None, setEntitySchoolBuildingIDClonedFrom = None, setEntitySchoolID = None, setIsPrimary = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntitySchoolBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "delete")


def getEveryEntryCode(searchConditions = [], EntityID = 1, returnEntryCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntryCode in the district.

    This function returns a dataframe of every EntryCode in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntryCode(EntryCodeID, EntityID = 1, returnEntryCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "get", return_params_list = return_params)

def modifyEntryCode(EntryCodeID, EntityID = 1, setEntryCodeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEntryCodeIDClonedFrom = None, setIsCrossEntityCourseEnrollment = None, setModifiedTime = None, setSchoolYearID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntryCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntryCode(EntityID = 1, setEntryCodeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEntryCodeIDClonedFrom = None, setIsCrossEntityCourseEnrollment = None, setModifiedTime = None, setSchoolYearID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntryCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntryCode(EntryCodeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "delete")


def getEveryEntryWithdrawal(searchConditions = [], EntityID = 1, returnEntryWithdrawalID = False, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntryWithdrawal in the district.

    This function returns a dataframe of every EntryWithdrawal in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntryWithdrawal(EntryWithdrawalID, EntityID = 1, returnEntryWithdrawalID = False, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "get", return_params_list = return_params)

def modifyEntryWithdrawal(EntryWithdrawalID, EntityID = 1, setEntryWithdrawalID = None, setAttendanceDays = None, setCalendarID = None, setCreatedTime = None, setEndDate = None, setEnrolledAtLeastOneDay = None, setEntityID = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalIDStatusChangePrevious = None, setEntryWithdrawalMNID = None, setGradeReferenceID = None, setHasMessageCenterAllowedWithdrawalCodeOverride = None, setIsCombinedEnrollmentFullTime = None, setIsCrossEntityCourseEnrollment = None, setIsCurrentOrFutureEnrollment = None, setIsDefaultEntity = None, setIsHistoricalEnrollment = None, setIsIndependentStudy = None, setIsNoShow = None, setIsPostSecondaryOption = None, setIsPSEOConcurrentEnrollment = None, setIsStartDateOnOrAfterFirstDayOfSchool = None, setMembershipDays = None, setModifiedTime = None, setPercentEnrolled = None, setPromotionStatus = None, setPromotionStatusCode = None, setPSEOHours = None, setRenderDeleteOption = None, setRenderNoShowOption = None, setRenderPrintWithdrawalFormOption = None, setRenderUndoStatusChangeOption = None, setRenderWithdrawalAndStatusChangeOptions = None, setSchoolID = None, setSchoolYearID = None, setSpecialEdServiceHours = None, setStartDate = None, setStateAidCategoryCodeMNID = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStatusChangeEntry = None, setStatusChangeWithdrawal = None, setStudentID = None, setStudentTypeID = None, setTotalMembershipDays = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, setWithdrawalComment = None, setWithdrawalDate = None, returnEntryWithdrawalID = False, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntryWithdrawal(EntityID = 1, setEntryWithdrawalID = None, setAttendanceDays = None, setCalendarID = None, setCreatedTime = None, setEndDate = None, setEnrolledAtLeastOneDay = None, setEntityID = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalIDStatusChangePrevious = None, setEntryWithdrawalMNID = None, setGradeReferenceID = None, setHasMessageCenterAllowedWithdrawalCodeOverride = None, setIsCombinedEnrollmentFullTime = None, setIsCrossEntityCourseEnrollment = None, setIsCurrentOrFutureEnrollment = None, setIsDefaultEntity = None, setIsHistoricalEnrollment = None, setIsIndependentStudy = None, setIsNoShow = None, setIsPostSecondaryOption = None, setIsPSEOConcurrentEnrollment = None, setIsStartDateOnOrAfterFirstDayOfSchool = None, setMembershipDays = None, setModifiedTime = None, setPercentEnrolled = None, setPromotionStatus = None, setPromotionStatusCode = None, setPSEOHours = None, setRenderDeleteOption = None, setRenderNoShowOption = None, setRenderPrintWithdrawalFormOption = None, setRenderUndoStatusChangeOption = None, setRenderWithdrawalAndStatusChangeOptions = None, setSchoolID = None, setSchoolYearID = None, setSpecialEdServiceHours = None, setStartDate = None, setStateAidCategoryCodeMNID = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStatusChangeEntry = None, setStatusChangeWithdrawal = None, setStudentID = None, setStudentTypeID = None, setTotalMembershipDays = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeID = None, setWithdrawalComment = None, setWithdrawalDate = None, returnEntryWithdrawalID = False, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntryWithdrawal(EntryWithdrawalID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "delete")


def getEveryGradeLevel(searchConditions = [], EntityID = 1, returnGradeLevelID = False, returnCode = False, returnCodeDescription = False, returnCommonEducationDataStandardsGradeLevelID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnIlluminate = False, returnIlluminateCalculated = False, returnIlluminateOverride = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every GradeLevel in the district.

    This function returns a dataframe of every GradeLevel in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGradeLevel(GradeLevelID, EntityID = 1, returnGradeLevelID = False, returnCode = False, returnCodeDescription = False, returnCommonEducationDataStandardsGradeLevelID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnIlluminate = False, returnIlluminateCalculated = False, returnIlluminateOverride = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "get", return_params_list = return_params)

def modifyGradeLevel(GradeLevelID, EntityID = 1, setGradeLevelID = None, setCode = None, setCodeDescription = None, setCommonEducationDataStandardsGradeLevelID = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setFederalGradeLevel = None, setFederalGradeLevelCode = None, setIlluminate = None, setIlluminateCalculated = None, setIlluminateOverride = None, setModifiedTime = None, setNumericValue = None, setStateGradeLevel = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradeLevelID = False, returnCode = False, returnCodeDescription = False, returnCommonEducationDataStandardsGradeLevelID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnIlluminate = False, returnIlluminateCalculated = False, returnIlluminateOverride = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGradeLevel(EntityID = 1, setGradeLevelID = None, setCode = None, setCodeDescription = None, setCommonEducationDataStandardsGradeLevelID = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setFederalGradeLevel = None, setFederalGradeLevelCode = None, setIlluminate = None, setIlluminateCalculated = None, setIlluminateOverride = None, setModifiedTime = None, setNumericValue = None, setStateGradeLevel = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradeLevelID = False, returnCode = False, returnCodeDescription = False, returnCommonEducationDataStandardsGradeLevelID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnIlluminate = False, returnIlluminateCalculated = False, returnIlluminateOverride = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGradeLevel(GradeLevelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "delete")


def getEveryGradeReference(searchConditions = [], EntityID = 1, returnGradeReferenceID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every GradeReference in the district.

    This function returns a dataframe of every GradeReference in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getGradeReference(GradeReferenceID, EntityID = 1, returnGradeReferenceID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "get", return_params_list = return_params)

def modifyGradeReference(GradeReferenceID, EntityID = 1, setGradeReferenceID = None, setCreatedTime = None, setDistrictGroupKey = None, setGradeLevelID = None, setGradeReferenceIDClonedFrom = None, setGradeReferenceIDClonedTo = None, setGradeReferenceMNID = None, setGradYear = None, setMinutesPresentFullDay = None, setMinutesPresentHalfDay = None, setModifiedTime = None, setSchoolYearID = None, setStateGradeLevel = None, setStateSTARGradeLevelMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradeReferenceID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGradeReference(EntityID = 1, setGradeReferenceID = None, setCreatedTime = None, setDistrictGroupKey = None, setGradeLevelID = None, setGradeReferenceIDClonedFrom = None, setGradeReferenceIDClonedTo = None, setGradeReferenceMNID = None, setGradYear = None, setMinutesPresentFullDay = None, setMinutesPresentHalfDay = None, setModifiedTime = None, setSchoolYearID = None, setStateGradeLevel = None, setStateSTARGradeLevelMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradeReferenceID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGradeReference(GradeReferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "delete")


def getEveryHomeroom(searchConditions = [], EntityID = 1, returnHomeroomID = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Homeroom in the district.

    This function returns a dataframe of every Homeroom in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getHomeroom(HomeroomID, EntityID = 1, returnHomeroomID = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "get", return_params_list = return_params)

def modifyHomeroom(HomeroomID, EntityID = 1, setHomeroomID = None, setCode = None, setCreatedTime = None, setEntityID = None, setHomeroomDetails = None, setHomeroomIDClonedFrom = None, setHomeroomIDClonedTo = None, setModifiedTime = None, setRoomID = None, setSchoolYearID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnHomeroomID = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "post", return_params_list = return_params, payload = payload_params)

def createHomeroom(EntityID = 1, setHomeroomID = None, setCode = None, setCreatedTime = None, setEntityID = None, setHomeroomDetails = None, setHomeroomIDClonedFrom = None, setHomeroomIDClonedTo = None, setModifiedTime = None, setRoomID = None, setSchoolYearID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnHomeroomID = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteHomeroom(HomeroomID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "delete")


def getEveryNumberedStudentEntityYearForDistrictAndSchoolYear(searchConditions = [], EntityID = 1, returnStudentEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnIsDefaultEntity = False, returnSchoolYearID = False, returnStudentDistrictRowNumber = False, returnStudentID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NumberedStudentEntityYearForDistrictAndSchoolYear in the district.

    This function returns a dataframe of every NumberedStudentEntityYearForDistrictAndSchoolYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNumberedStudentEntityYearForDistrictAndSchoolYear(StudentEntityYearID, EntityID = 1, returnStudentEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnIsDefaultEntity = False, returnSchoolYearID = False, returnStudentDistrictRowNumber = False, returnStudentID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/" + str(StudentEntityYearID), verb = "get", return_params_list = return_params)

def modifyNumberedStudentEntityYearForDistrictAndSchoolYear(StudentEntityYearID, EntityID = 1, setStudentEntityYearID = None, setDistrictID = None, setEntityID = None, setIsDefaultEntity = None, setSchoolYearID = None, setStudentDistrictRowNumber = None, setStudentID = None, returnStudentEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnIsDefaultEntity = False, returnSchoolYearID = False, returnStudentDistrictRowNumber = False, returnStudentID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/" + str(StudentEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNumberedStudentEntityYearForDistrictAndSchoolYear(EntityID = 1, setStudentEntityYearID = None, setDistrictID = None, setEntityID = None, setIsDefaultEntity = None, setSchoolYearID = None, setStudentDistrictRowNumber = None, setStudentID = None, returnStudentEntityYearID = False, returnDistrictID = False, returnEntityID = False, returnIsDefaultEntity = False, returnSchoolYearID = False, returnStudentDistrictRowNumber = False, returnStudentID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNumberedStudentEntityYearForDistrictAndSchoolYear(StudentEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/NumberedStudentEntityYearForDistrictAndSchoolYear/" + str(StudentEntityYearID), verb = "delete")


def getEveryPaymentPlanMA(searchConditions = [], EntityID = 1, returnPaymentPlanMAID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PaymentPlanMA in the district.

    This function returns a dataframe of every PaymentPlanMA in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPaymentPlanMA(PaymentPlanMAID, EntityID = 1, returnPaymentPlanMAID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "get", return_params_list = return_params)

def modifyPaymentPlanMA(PaymentPlanMAID, EntityID = 1, setPaymentPlanMAID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPaymentPlanMAID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPaymentPlanMA(EntityID = 1, setPaymentPlanMAID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPaymentPlanMAID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePaymentPlanMA(PaymentPlanMAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "delete")


def getEveryPermit(searchConditions = [], EntityID = 1, returnPermitID = False, returnAllowSchoolPathAssignment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPermitIDClonedFrom = False, returnPermitIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Permit in the district.

    This function returns a dataframe of every Permit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPermit(PermitID, EntityID = 1, returnPermitID = False, returnAllowSchoolPathAssignment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPermitIDClonedFrom = False, returnPermitIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "get", return_params_list = return_params)

def modifyPermit(PermitID, EntityID = 1, setPermitID = None, setAllowSchoolPathAssignment = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setPermitIDClonedFrom = None, setPermitIDClonedTo = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPermitID = False, returnAllowSchoolPathAssignment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPermitIDClonedFrom = False, returnPermitIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPermit(EntityID = 1, setPermitID = None, setAllowSchoolPathAssignment = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setPermitIDClonedFrom = None, setPermitIDClonedTo = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPermitID = False, returnAllowSchoolPathAssignment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPermitIDClonedFrom = False, returnPermitIDClonedTo = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePermit(PermitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "delete")


def getEveryPMTransportation(searchConditions = [], EntityID = 1, returnPMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PMTransportation in the district.

    This function returns a dataframe of every PMTransportation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPMTransportation(PMTransportationID, EntityID = 1, returnPMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/" + str(PMTransportationID), verb = "get", return_params_list = return_params)

def modifyPMTransportation(PMTransportationID, EntityID = 1, setPMTransportationID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/" + str(PMTransportationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPMTransportation(EntityID = 1, setPMTransportationID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPMTransportationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePMTransportation(PMTransportationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PMTransportation/" + str(PMTransportationID), verb = "delete")


def getEverySchoolDistrict(searchConditions = [], EntityID = 1, returnSchoolDistrictID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchoolDistrict in the district.

    This function returns a dataframe of every SchoolDistrict in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchoolDistrict(SchoolDistrictID, EntityID = 1, returnSchoolDistrictID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/" + str(SchoolDistrictID), verb = "get", return_params_list = return_params)

def modifySchoolDistrict(SchoolDistrictID, EntityID = 1, setSchoolDistrictID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolDistrictID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/" + str(SchoolDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchoolDistrict(EntityID = 1, setSchoolDistrictID = None, setCode = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolDistrictID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchoolDistrict(SchoolDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolDistrict/" + str(SchoolDistrictID), verb = "delete")


def getEverySchool(searchConditions = [], EntityID = 1, returnSchoolID = False, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnIsTitleISchoolwide = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateAssignedID = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every School in the district.

    This function returns a dataframe of every School in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchool(SchoolID, EntityID = 1, returnSchoolID = False, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnIsTitleISchoolwide = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateAssignedID = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "get", return_params_list = return_params)

def modifySchool(SchoolID, EntityID = 1, setSchoolID = None, setAllowsSchoolDevices = None, setAllowsStudentDevices = None, setBuildingID = None, setCampusAccountabilityRatingID = None, setCEEBCode = None, setCode = None, setCodeName = None, setCreatedTime = None, setDaysInRegularSchoolYear = None, setDaysPriorForAlgebraICounts = None, setDistrictID = None, setEdFiSchoolCategoryID = None, setEdFiSchoolID = None, setEducationalProgramHoursPerWeek = None, setExcludeFromCRDC = None, setFaxNumber = None, setFaxNumberIsInternational = None, setFederalAlternativeSchoolDetailID = None, setFederalJusticeFacilityTypeID = None, setFederalNCESSchoolID = None, setFormattedFaxNumber = None, setFormattedPhoneNumber = None, setGradeLevelIDHigh = None, setGradeLevelIDLow = None, setHasAlcoholDrugEducation = None, setHasAntiBullying = None, setHasAntiViolence = None, setHasAPCourses = None, setHasAPSelfSelection = None, setHasCorporalPunishment = None, setHasCreditRecovery = None, setHasCrisisPlan = None, setHasDualEnrollment = None, setHasFiberOptic = None, setHasGifted = None, setHasHomicideOccurred = None, setHasIBDiplomaProgramme = None, setHasPreschoolNonIDEAAge3 = None, setHasPreschoolNonIDEAAge4 = None, setHasPreschoolNonIDEAAge5 = None, setHasSafetyPlan = None, setHasShootingOccurred = None, setHasSingleSexAthletics = None, setHasSingleSexClasses = None, setHasUngraded = None, setHasUngradedMainlyElementary = None, setHasUngradedMainlyHighSchool = None, setHasUngradedMainlyMiddleSchool = None, setHasWiFi = None, setHasZeroTolerance = None, setIsALCSchool = None, setIsAlternative = None, setIsCEP = None, setIsCharter = None, setIsCRDCCollectedForSchoolYear = None, setIsEntireSchoolMagnet = None, setIsMagnet = None, setIsNonLEA = None, setIsSpecialEducation = None, setIsTitleIII = None, setIsTitleISchoolwide = None, setModifiedTime = None, setName = None, setNameIDSafetySpecialist = None, setNumberWiFiDevices = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setSchoolIDClonedFrom = None, setSchoolIDClonedTo = None, setSchoolMNID = None, setSchoolNumber = None, setSchoolYearID = None, setStaffIDPrincipal = None, setStateAssignedID = None, setStateKindergartenScheduleIndicatorCodeMNID = None, setStateSchoolMNID = None, setStateTitleISchoolIndicatorCodeMNID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolID = False, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnIsTitleISchoolwide = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateAssignedID = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchool(EntityID = 1, setSchoolID = None, setAllowsSchoolDevices = None, setAllowsStudentDevices = None, setBuildingID = None, setCampusAccountabilityRatingID = None, setCEEBCode = None, setCode = None, setCodeName = None, setCreatedTime = None, setDaysInRegularSchoolYear = None, setDaysPriorForAlgebraICounts = None, setDistrictID = None, setEdFiSchoolCategoryID = None, setEdFiSchoolID = None, setEducationalProgramHoursPerWeek = None, setExcludeFromCRDC = None, setFaxNumber = None, setFaxNumberIsInternational = None, setFederalAlternativeSchoolDetailID = None, setFederalJusticeFacilityTypeID = None, setFederalNCESSchoolID = None, setFormattedFaxNumber = None, setFormattedPhoneNumber = None, setGradeLevelIDHigh = None, setGradeLevelIDLow = None, setHasAlcoholDrugEducation = None, setHasAntiBullying = None, setHasAntiViolence = None, setHasAPCourses = None, setHasAPSelfSelection = None, setHasCorporalPunishment = None, setHasCreditRecovery = None, setHasCrisisPlan = None, setHasDualEnrollment = None, setHasFiberOptic = None, setHasGifted = None, setHasHomicideOccurred = None, setHasIBDiplomaProgramme = None, setHasPreschoolNonIDEAAge3 = None, setHasPreschoolNonIDEAAge4 = None, setHasPreschoolNonIDEAAge5 = None, setHasSafetyPlan = None, setHasShootingOccurred = None, setHasSingleSexAthletics = None, setHasSingleSexClasses = None, setHasUngraded = None, setHasUngradedMainlyElementary = None, setHasUngradedMainlyHighSchool = None, setHasUngradedMainlyMiddleSchool = None, setHasWiFi = None, setHasZeroTolerance = None, setIsALCSchool = None, setIsAlternative = None, setIsCEP = None, setIsCharter = None, setIsCRDCCollectedForSchoolYear = None, setIsEntireSchoolMagnet = None, setIsMagnet = None, setIsNonLEA = None, setIsSpecialEducation = None, setIsTitleIII = None, setIsTitleISchoolwide = None, setModifiedTime = None, setName = None, setNameIDSafetySpecialist = None, setNumberWiFiDevices = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setSchoolIDClonedFrom = None, setSchoolIDClonedTo = None, setSchoolMNID = None, setSchoolNumber = None, setSchoolYearID = None, setStaffIDPrincipal = None, setStateAssignedID = None, setStateKindergartenScheduleIndicatorCodeMNID = None, setStateSchoolMNID = None, setStateTitleISchoolIndicatorCodeMNID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolID = False, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnIsTitleISchoolwide = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateAssignedID = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchool(SchoolID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "delete")


def getEverySchoolPath(searchConditions = [], EntityID = 1, returnSchoolPathID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnSchoolPathIDClonedFrom = False, returnSchoolPathIDClonedTo = False, returnSchoolPathTypeID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchoolPath in the district.

    This function returns a dataframe of every SchoolPath in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchoolPath(SchoolPathID, EntityID = 1, returnSchoolPathID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnSchoolPathIDClonedFrom = False, returnSchoolPathIDClonedTo = False, returnSchoolPathTypeID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/" + str(SchoolPathID), verb = "get", return_params_list = return_params)

def modifySchoolPath(SchoolPathID, EntityID = 1, setSchoolPathID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setName = None, setSchoolPathIDClonedFrom = None, setSchoolPathIDClonedTo = None, setSchoolPathTypeID = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnSchoolPathIDClonedFrom = False, returnSchoolPathIDClonedTo = False, returnSchoolPathTypeID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/" + str(SchoolPathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchoolPath(EntityID = 1, setSchoolPathID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setName = None, setSchoolPathIDClonedFrom = None, setSchoolPathIDClonedTo = None, setSchoolPathTypeID = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnSchoolPathIDClonedFrom = False, returnSchoolPathIDClonedTo = False, returnSchoolPathTypeID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchoolPath(SchoolPathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPath/" + str(SchoolPathID), verb = "delete")


def getEverySchoolPathSchool(searchConditions = [], EntityID = 1, returnSchoolPathSchoolID = False, returnCodeDescription = False, returnCreatedTime = False, returnDistrictID = False, returnIsOverriddenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnSchoolPathID = False, returnSchoolPathSchoolIDClonedFrom = False, returnSchoolPathSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchoolPathSchool in the district.

    This function returns a dataframe of every SchoolPathSchool in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchoolPathSchool(SchoolPathSchoolID, EntityID = 1, returnSchoolPathSchoolID = False, returnCodeDescription = False, returnCreatedTime = False, returnDistrictID = False, returnIsOverriddenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnSchoolPathID = False, returnSchoolPathSchoolIDClonedFrom = False, returnSchoolPathSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/" + str(SchoolPathSchoolID), verb = "get", return_params_list = return_params)

def modifySchoolPathSchool(SchoolPathSchoolID, EntityID = 1, setSchoolPathSchoolID = None, setCodeDescription = None, setCreatedTime = None, setDistrictID = None, setIsOverriddenForStudent = None, setModifiedTime = None, setOrder = None, setOverriddenSchoolName = None, setSchoolID = None, setSchoolPathID = None, setSchoolPathSchoolIDClonedFrom = None, setSchoolPathSchoolIDClonedTo = None, setSchoolYearID = None, setStudentHasPermit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathSchoolID = False, returnCodeDescription = False, returnCreatedTime = False, returnDistrictID = False, returnIsOverriddenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnSchoolPathID = False, returnSchoolPathSchoolIDClonedFrom = False, returnSchoolPathSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/" + str(SchoolPathSchoolID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchoolPathSchool(EntityID = 1, setSchoolPathSchoolID = None, setCodeDescription = None, setCreatedTime = None, setDistrictID = None, setIsOverriddenForStudent = None, setModifiedTime = None, setOrder = None, setOverriddenSchoolName = None, setSchoolID = None, setSchoolPathID = None, setSchoolPathSchoolIDClonedFrom = None, setSchoolPathSchoolIDClonedTo = None, setSchoolYearID = None, setStudentHasPermit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathSchoolID = False, returnCodeDescription = False, returnCreatedTime = False, returnDistrictID = False, returnIsOverriddenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnSchoolPathID = False, returnSchoolPathSchoolIDClonedFrom = False, returnSchoolPathSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchoolPathSchool(SchoolPathSchoolID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchool/" + str(SchoolPathSchoolID), verb = "delete")


def getEverySchoolPathSchoolOverride(searchConditions = [], EntityID = 1, returnSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchoolPathSchoolOverride in the district.

    This function returns a dataframe of every SchoolPathSchoolOverride in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchoolPathSchoolOverride(SchoolPathSchoolOverrideID, EntityID = 1, returnSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/" + str(SchoolPathSchoolOverrideID), verb = "get", return_params_list = return_params)

def modifySchoolPathSchoolOverride(SchoolPathSchoolOverrideID, EntityID = 1, setSchoolPathSchoolOverrideID = None, setCreatedTime = None, setModifiedTime = None, setOrder = None, setSchoolID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/" + str(SchoolPathSchoolOverrideID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchoolPathSchoolOverride(EntityID = 1, setSchoolPathSchoolOverrideID = None, setCreatedTime = None, setModifiedTime = None, setOrder = None, setSchoolID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchoolPathSchoolOverride(SchoolPathSchoolOverrideID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathSchoolOverride/" + str(SchoolPathSchoolOverrideID), verb = "delete")


def getEverySchoolPathStudent(searchConditions = [], EntityID = 1, returnSchoolPathStudentID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchoolPathStudent in the district.

    This function returns a dataframe of every SchoolPathStudent in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchoolPathStudent(SchoolPathStudentID, EntityID = 1, returnSchoolPathStudentID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/" + str(SchoolPathStudentID), verb = "get", return_params_list = return_params)

def modifySchoolPathStudent(SchoolPathStudentID, EntityID = 1, setSchoolPathStudentID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setSchoolPathID = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathStudentID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/" + str(SchoolPathStudentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchoolPathStudent(EntityID = 1, setSchoolPathStudentID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setSchoolPathID = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathStudentID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchoolPathStudent(SchoolPathStudentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathStudent/" + str(SchoolPathStudentID), verb = "delete")


def getEverySchoolPathType(searchConditions = [], EntityID = 1, returnSchoolPathTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchoolPathType in the district.

    This function returns a dataframe of every SchoolPathType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchoolPathType(SchoolPathTypeID, EntityID = 1, returnSchoolPathTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/" + str(SchoolPathTypeID), verb = "get", return_params_list = return_params)

def modifySchoolPathType(SchoolPathTypeID, EntityID = 1, setSchoolPathTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/" + str(SchoolPathTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchoolPathType(EntityID = 1, setSchoolPathTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolPathTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchoolPathType(SchoolPathTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/SchoolPathType/" + str(SchoolPathTypeID), verb = "delete")


def getEveryStudentAccountsMA(searchConditions = [], EntityID = 1, returnStudentAccountsMAID = False, returnAMTransportationID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnFacultyStaffChild = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnNYDepositPaid = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnPMTransportationID = False, returnReligionID = False, returnSchoolDistrictID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAccountsMA in the district.

    This function returns a dataframe of every StudentAccountsMA in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAccountsMA(StudentAccountsMAID, EntityID = 1, returnStudentAccountsMAID = False, returnAMTransportationID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnFacultyStaffChild = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnNYDepositPaid = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnPMTransportationID = False, returnReligionID = False, returnSchoolDistrictID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "get", return_params_list = return_params)

def modifyStudentAccountsMA(StudentAccountsMAID, EntityID = 1, setStudentAccountsMAID = None, setAMTransportationID = None, setCreatedTime = None, setEthnicityMAID = None, setFacultyStaffChild = None, setFinancialAid = None, setiPadLease = None, setModifiedTime = None, setNYDepositPaid = None, setPaymentPlanMAID = None, setPlaceofWorship = None, setPMTransportationID = None, setReligionID = None, setSchoolDistrictID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAccountsMAID = False, returnAMTransportationID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnFacultyStaffChild = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnNYDepositPaid = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnPMTransportationID = False, returnReligionID = False, returnSchoolDistrictID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAccountsMA(EntityID = 1, setStudentAccountsMAID = None, setAMTransportationID = None, setCreatedTime = None, setEthnicityMAID = None, setFacultyStaffChild = None, setFinancialAid = None, setiPadLease = None, setModifiedTime = None, setNYDepositPaid = None, setPaymentPlanMAID = None, setPlaceofWorship = None, setPMTransportationID = None, setReligionID = None, setSchoolDistrictID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAccountsMAID = False, returnAMTransportationID = False, returnCreatedTime = False, returnEthnicityMAID = False, returnFacultyStaffChild = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnNYDepositPaid = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnPMTransportationID = False, returnReligionID = False, returnSchoolDistrictID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAccountsMA(StudentAccountsMAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "delete")


def getEveryStudentEntityYear(searchConditions = [], EntityID = 1, returnStudentEntityYearID = False, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnCurrentPercentEnrolled = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasNonCrossEntityCourseSchedulingEntryWithdrawal = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolIDPathExpectedSchool = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEntityYear in the district.

    This function returns a dataframe of every StudentEntityYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEntityYear(StudentEntityYearID, EntityID = 1, returnStudentEntityYearID = False, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnCurrentPercentEnrolled = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasNonCrossEntityCourseSchedulingEntryWithdrawal = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolIDPathExpectedSchool = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "get", return_params_list = return_params)

def modifyStudentEntityYear(StudentEntityYearID, EntityID = 1, setStudentEntityYearID = None, setChromebookDocumentsReturned = None, setCreatedTime = None, setCurrentPercentEnrolled = None, setDaysAbsentYTD = None, setDaysEnrolledYTD = None, setDaysExcusedYTD = None, setDaysOtherYTD = None, setDaysUnexcusedYTD = None, setEntityID = None, setEntryWithdrawalIDLatest = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setExistsConflictedStudentCourseRequests = None, setExistsUnscheduleableStudentSections = None, setFeeAmountDue = None, setFeeChargeAmount = None, setFeePaidAmount = None, setFeePaidAndWaivedAmount = None, setFeeUnappliedAmount = None, setFeeWaivedAmount = None, setFirstName = None, setFlaggedMissingAssignmentsCount = None, setGrade = None, setHandbookSigned = None, setHasActiveCareerPlanDeclarationTimePeriod = None, setHasActiveEndorsementDeclarationTimePeriod = None, setHasConflictedStudentCourseRequest = None, setHasFlaggedMissingAssignments = None, setHasMissingAssignments = None, setHasNoAttendanceToday = None, setHasNonCrossEntityCourseSchedulingEntryWithdrawal = None, setHasOpenDisplayPeriodsInRegularSchoolDay = None, setHasOverscheduledPeriod = None, setHasValidStudentPlan = None, setHomeroomCodeFollettDestiny = None, setHomeroomID = None, setHomeroomPeriodFollettDestiny = None, setHomeroomStaffNameFollettDestiny = None, setIncludeAsProspectiveRank = None, setIsActive = None, setIsCrossEntityCourseEnrollment = None, setIsDefaultEntity = None, setIsTransportationRequested = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setNumberOfStudentCourseRequests = None, setNumberOfStudentSections = None, setOptOutOfMedia = None, setSchedulingCategories = None, setSchedulingTeamID = None, setSchoolIDPathExpectedSchool = None, setSchoolYearID = None, setSectionLengthAbsent = None, setSectionLengthEnrolled = None, setSemester2Absent = None, setSemester2Enrolled = None, setSignedAcceptableUsePolicy = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setTardyCountYTD = None, setTardyKioskTotals = None, setTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = None, setTotalMissedAssignmentCount = None, setUILFeeReceived = None, setUnscheduleableStudentSectionCount = None, setUnscheduledStudentCourseRequestCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalDate = None, returnStudentEntityYearID = False, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnCurrentPercentEnrolled = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasNonCrossEntityCourseSchedulingEntryWithdrawal = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolIDPathExpectedSchool = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEntityYear(EntityID = 1, setStudentEntityYearID = None, setChromebookDocumentsReturned = None, setCreatedTime = None, setCurrentPercentEnrolled = None, setDaysAbsentYTD = None, setDaysEnrolledYTD = None, setDaysExcusedYTD = None, setDaysOtherYTD = None, setDaysUnexcusedYTD = None, setEntityID = None, setEntryWithdrawalIDLatest = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setExistsConflictedStudentCourseRequests = None, setExistsUnscheduleableStudentSections = None, setFeeAmountDue = None, setFeeChargeAmount = None, setFeePaidAmount = None, setFeePaidAndWaivedAmount = None, setFeeUnappliedAmount = None, setFeeWaivedAmount = None, setFirstName = None, setFlaggedMissingAssignmentsCount = None, setGrade = None, setHandbookSigned = None, setHasActiveCareerPlanDeclarationTimePeriod = None, setHasActiveEndorsementDeclarationTimePeriod = None, setHasConflictedStudentCourseRequest = None, setHasFlaggedMissingAssignments = None, setHasMissingAssignments = None, setHasNoAttendanceToday = None, setHasNonCrossEntityCourseSchedulingEntryWithdrawal = None, setHasOpenDisplayPeriodsInRegularSchoolDay = None, setHasOverscheduledPeriod = None, setHasValidStudentPlan = None, setHomeroomCodeFollettDestiny = None, setHomeroomID = None, setHomeroomPeriodFollettDestiny = None, setHomeroomStaffNameFollettDestiny = None, setIncludeAsProspectiveRank = None, setIsActive = None, setIsCrossEntityCourseEnrollment = None, setIsDefaultEntity = None, setIsTransportationRequested = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setNumberOfStudentCourseRequests = None, setNumberOfStudentSections = None, setOptOutOfMedia = None, setSchedulingCategories = None, setSchedulingTeamID = None, setSchoolIDPathExpectedSchool = None, setSchoolYearID = None, setSectionLengthAbsent = None, setSectionLengthEnrolled = None, setSemester2Absent = None, setSemester2Enrolled = None, setSignedAcceptableUsePolicy = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setTardyCountYTD = None, setTardyKioskTotals = None, setTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = None, setTotalMissedAssignmentCount = None, setUILFeeReceived = None, setUnscheduleableStudentSectionCount = None, setUnscheduledStudentCourseRequestCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalDate = None, returnStudentEntityYearID = False, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnCurrentPercentEnrolled = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasNonCrossEntityCourseSchedulingEntryWithdrawal = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolIDPathExpectedSchool = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEntityYear(StudentEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "delete")


def getEveryStudentPermit(searchConditions = [], EntityID = 1, returnStudentPermitID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentPermit in the district.

    This function returns a dataframe of every StudentPermit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentPermit(StudentPermitID, EntityID = 1, returnStudentPermitID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/" + str(StudentPermitID), verb = "get", return_params_list = return_params)

def modifyStudentPermit(StudentPermitID, EntityID = 1, setStudentPermitID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setPermitID = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentPermitID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/" + str(StudentPermitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentPermit(EntityID = 1, setStudentPermitID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setPermitID = None, setSchoolYearID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentPermitID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnPermitID = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentPermit(StudentPermitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentPermit/" + str(StudentPermitID), verb = "delete")


def getEveryStudentType(searchConditions = [], EntityID = 1, returnStudentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentType in the district.

    This function returns a dataframe of every StudentType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentType(StudentTypeID, EntityID = 1, returnStudentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "get", return_params_list = return_params)

def modifyStudentType(StudentTypeID, EntityID = 1, setStudentTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentType(EntityID = 1, setStudentTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentType(StudentTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "delete")


def getEveryTempAffectedWithdrawalRecord(searchConditions = [], EntityID = 1, returnTempAffectedWithdrawalRecordID = False, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnHasTransactionPreventingStudentSectionDelete = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnParentPrimaryKey = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAffectedWithdrawalRecord in the district.

    This function returns a dataframe of every TempAffectedWithdrawalRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1, returnTempAffectedWithdrawalRecordID = False, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnHasTransactionPreventingStudentSectionDelete = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnParentPrimaryKey = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "get", return_params_list = return_params)

def modifyTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1, setTempAffectedWithdrawalRecordID = None, setAction = None, setActionCode = None, setActionMessage = None, setAffectedPrimaryKey = None, setCourseID = None, setCreatedTime = None, setDescription = None, setEndDate = None, setEntityID = None, setHasAttendance = None, setHasFutureAttendance = None, setHasFutureGrades = None, setHasGrades = None, setHasPartiallyPaidFees = None, setHasTransactionPreventingStudentSectionDelete = None, setIsFutureEntryWithdrawal = None, setModifiedTime = None, setMostFutureGradeStartDate = None, setNameIDRequestedBy = None, setNewEndDate = None, setParentPrimaryKey = None, setRecordType = None, setRecordTypeCode = None, setSchoolYearID = None, setSection = None, setSectionID = None, setStartDate = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedWithdrawalRecordID = False, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnHasTransactionPreventingStudentSectionDelete = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnParentPrimaryKey = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAffectedWithdrawalRecord(EntityID = 1, setTempAffectedWithdrawalRecordID = None, setAction = None, setActionCode = None, setActionMessage = None, setAffectedPrimaryKey = None, setCourseID = None, setCreatedTime = None, setDescription = None, setEndDate = None, setEntityID = None, setHasAttendance = None, setHasFutureAttendance = None, setHasFutureGrades = None, setHasGrades = None, setHasPartiallyPaidFees = None, setHasTransactionPreventingStudentSectionDelete = None, setIsFutureEntryWithdrawal = None, setModifiedTime = None, setMostFutureGradeStartDate = None, setNameIDRequestedBy = None, setNewEndDate = None, setParentPrimaryKey = None, setRecordType = None, setRecordTypeCode = None, setSchoolYearID = None, setSection = None, setSectionID = None, setStartDate = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedWithdrawalRecordID = False, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnHasTransactionPreventingStudentSectionDelete = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnParentPrimaryKey = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "delete")


def getEveryTempHomeroomError(searchConditions = [], EntityID = 1, returnTempHomeroomErrorID = False, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempHomeroomError in the district.

    This function returns a dataframe of every TempHomeroomError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempHomeroomError(TempHomeroomErrorID, EntityID = 1, returnTempHomeroomErrorID = False, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "get", return_params_list = return_params)

def modifyTempHomeroomError(TempHomeroomErrorID, EntityID = 1, setTempHomeroomErrorID = None, setCode = None, setCreatedTime = None, setFailureReason = None, setModifiedTime = None, setTempHomeroomRecordID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempHomeroomErrorID = False, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempHomeroomError(EntityID = 1, setTempHomeroomErrorID = None, setCode = None, setCreatedTime = None, setFailureReason = None, setModifiedTime = None, setTempHomeroomRecordID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempHomeroomErrorID = False, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempHomeroomError(TempHomeroomErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "delete")


def getEveryTempHomeroomRecord(searchConditions = [], EntityID = 1, returnTempHomeroomRecordID = False, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempHomeroomRecord in the district.

    This function returns a dataframe of every TempHomeroomRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1, returnTempHomeroomRecordID = False, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "get", return_params_list = return_params)

def modifyTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1, setTempHomeroomRecordID = None, setBuilding = None, setBuildingID = None, setCode = None, setColumnIndex = None, setCreatedTime = None, setHasSaveError = None, setHomeroomID = None, setIsOverwrite = None, setModifiedTime = None, setRoom = None, setRoomID = None, setSchoolYear = None, setSchoolYearID = None, setStaff = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempHomeroomRecordID = False, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempHomeroomRecord(EntityID = 1, setTempHomeroomRecordID = None, setBuilding = None, setBuildingID = None, setCode = None, setColumnIndex = None, setCreatedTime = None, setHasSaveError = None, setHomeroomID = None, setIsOverwrite = None, setModifiedTime = None, setRoom = None, setRoomID = None, setSchoolYear = None, setSchoolYearID = None, setStaff = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempHomeroomRecordID = False, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "delete")


def getEveryTempNameAddressMoveSchoolPathSchoolOverride(searchConditions = [], EntityID = 1, returnTempNameAddressMoveSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnPermitID = False, returnPermitSchoolYearID = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolPathSchoolOverrideID = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempNameAddressMoveSchoolPathSchoolOverride in the district.

    This function returns a dataframe of every TempNameAddressMoveSchoolPathSchoolOverride in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempNameAddressMoveSchoolPathSchoolOverride(TempNameAddressMoveSchoolPathSchoolOverrideID, EntityID = 1, returnTempNameAddressMoveSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnPermitID = False, returnPermitSchoolYearID = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolPathSchoolOverrideID = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/" + str(TempNameAddressMoveSchoolPathSchoolOverrideID), verb = "get", return_params_list = return_params)

def modifyTempNameAddressMoveSchoolPathSchoolOverride(TempNameAddressMoveSchoolPathSchoolOverrideID, EntityID = 1, setTempNameAddressMoveSchoolPathSchoolOverrideID = None, setCreatedTime = None, setIsCreateOverride = None, setIsOverrideExists = None, setIsRemoveOverride = None, setIsRemovePermit = None, setIsUpdateOverride = None, setModifiedTime = None, setOrder = None, setPermitID = None, setPermitSchoolYearID = None, setSchoolID = None, setSchoolNameOverriddingTo = None, setSchoolNameToOverride = None, setSchoolPathSchoolOverrideID = None, setSchoolYearDescription = None, setStudentFullNameLFM = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameAddressMoveSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnPermitID = False, returnPermitSchoolYearID = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolPathSchoolOverrideID = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/" + str(TempNameAddressMoveSchoolPathSchoolOverrideID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNameAddressMoveSchoolPathSchoolOverride(EntityID = 1, setTempNameAddressMoveSchoolPathSchoolOverrideID = None, setCreatedTime = None, setIsCreateOverride = None, setIsOverrideExists = None, setIsRemoveOverride = None, setIsRemovePermit = None, setIsUpdateOverride = None, setModifiedTime = None, setOrder = None, setPermitID = None, setPermitSchoolYearID = None, setSchoolID = None, setSchoolNameOverriddingTo = None, setSchoolNameToOverride = None, setSchoolPathSchoolOverrideID = None, setSchoolYearDescription = None, setStudentFullNameLFM = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameAddressMoveSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnPermitID = False, returnPermitSchoolYearID = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolPathSchoolOverrideID = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNameAddressMoveSchoolPathSchoolOverride(TempNameAddressMoveSchoolPathSchoolOverrideID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNameAddressMoveSchoolPathSchoolOverride/" + str(TempNameAddressMoveSchoolPathSchoolOverrideID), verb = "delete")


def getEveryTempNoShowEntryWithdrawal(searchConditions = [], EntityID = 1, returnTempNoShowEntryWithdrawalID = False, returnAttemptToUpdateWithdrawalCode = False, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempNoShowEntryWithdrawal in the district.

    This function returns a dataframe of every TempNoShowEntryWithdrawal in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1, returnTempNoShowEntryWithdrawalID = False, returnAttemptToUpdateWithdrawalCode = False, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "get", return_params_list = return_params)

def modifyTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1, setTempNoShowEntryWithdrawalID = None, setAttemptToUpdateWithdrawalCode = None, setCreatedTime = None, setDisplayAction = None, setDisplayActionCode = None, setEndDate = None, setEntity = None, setEntryCode = None, setEntryWithdrawalID = None, setFailureReason = None, setGradeLevel = None, setModifiedTime = None, setNoShowAction = None, setNoShowActionCode = None, setNoShowEntryWithdrawalType = None, setNoShowEntryWithdrawalTypeCode = None, setNoShowTypeOfNoShow = None, setNoShowTypeOfNoShowCode = None, setSchoolYear = None, setSchoolYearID = None, setStartDate = None, setStudent = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCode = None, setWithdrawalCodeID = None, returnTempNoShowEntryWithdrawalID = False, returnAttemptToUpdateWithdrawalCode = False, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNoShowEntryWithdrawal(EntityID = 1, setTempNoShowEntryWithdrawalID = None, setAttemptToUpdateWithdrawalCode = None, setCreatedTime = None, setDisplayAction = None, setDisplayActionCode = None, setEndDate = None, setEntity = None, setEntryCode = None, setEntryWithdrawalID = None, setFailureReason = None, setGradeLevel = None, setModifiedTime = None, setNoShowAction = None, setNoShowActionCode = None, setNoShowEntryWithdrawalType = None, setNoShowEntryWithdrawalTypeCode = None, setNoShowTypeOfNoShow = None, setNoShowTypeOfNoShowCode = None, setSchoolYear = None, setSchoolYearID = None, setStartDate = None, setStudent = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCode = None, setWithdrawalCodeID = None, returnTempNoShowEntryWithdrawalID = False, returnAttemptToUpdateWithdrawalCode = False, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "delete")


def getEveryTempSchoolPathSchoolOverride(searchConditions = [], EntityID = 1, returnTempSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnDistrictID = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnPermitCodeDescription = False, returnPermitID = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempSchoolPathSchoolOverride in the district.

    This function returns a dataframe of every TempSchoolPathSchoolOverride in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempSchoolPathSchoolOverride(TempSchoolPathSchoolOverrideID, EntityID = 1, returnTempSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnDistrictID = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnPermitCodeDescription = False, returnPermitID = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/" + str(TempSchoolPathSchoolOverrideID), verb = "get", return_params_list = return_params)

def modifyTempSchoolPathSchoolOverride(TempSchoolPathSchoolOverrideID, EntityID = 1, setTempSchoolPathSchoolOverrideID = None, setCreatedTime = None, setDistrictID = None, setExceptionNote = None, setHasExceptions = None, setModifiedTime = None, setOrder = None, setPermitCodeDescription = None, setPermitID = None, setSchoolCodeName = None, setSchoolID = None, setSchoolIDClonedTo = None, setSchoolYearID = None, setStudentID = None, setStudentName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnDistrictID = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnPermitCodeDescription = False, returnPermitID = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/" + str(TempSchoolPathSchoolOverrideID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSchoolPathSchoolOverride(EntityID = 1, setTempSchoolPathSchoolOverrideID = None, setCreatedTime = None, setDistrictID = None, setExceptionNote = None, setHasExceptions = None, setModifiedTime = None, setOrder = None, setPermitCodeDescription = None, setPermitID = None, setSchoolCodeName = None, setSchoolID = None, setSchoolIDClonedTo = None, setSchoolYearID = None, setStudentID = None, setStudentName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSchoolPathSchoolOverrideID = False, returnCreatedTime = False, returnDistrictID = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnPermitCodeDescription = False, returnPermitID = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnSchoolYearID = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSchoolPathSchoolOverride(TempSchoolPathSchoolOverrideID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempSchoolPathSchoolOverride/" + str(TempSchoolPathSchoolOverrideID), verb = "delete")


def getEveryTempStudentEnrollmentError(searchConditions = [], EntityID = 1, returnTempStudentEnrollmentErrorID = False, returnCreatedTime = False, returnError = False, returnErrorCount = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentEnrollmentRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentEnrollmentError in the district.

    This function returns a dataframe of every TempStudentEnrollmentError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentEnrollmentError(TempStudentEnrollmentErrorID, EntityID = 1, returnTempStudentEnrollmentErrorID = False, returnCreatedTime = False, returnError = False, returnErrorCount = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentEnrollmentRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/" + str(TempStudentEnrollmentErrorID), verb = "get", return_params_list = return_params)

def modifyTempStudentEnrollmentError(TempStudentEnrollmentErrorID, EntityID = 1, setTempStudentEnrollmentErrorID = None, setCreatedTime = None, setError = None, setErrorCount = None, setErrorDetail = None, setModifiedTime = None, setTempStudentEnrollmentRecordID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentEnrollmentErrorID = False, returnCreatedTime = False, returnError = False, returnErrorCount = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentEnrollmentRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/" + str(TempStudentEnrollmentErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentEnrollmentError(EntityID = 1, setTempStudentEnrollmentErrorID = None, setCreatedTime = None, setError = None, setErrorCount = None, setErrorDetail = None, setModifiedTime = None, setTempStudentEnrollmentRecordID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentEnrollmentErrorID = False, returnCreatedTime = False, returnError = False, returnErrorCount = False, returnErrorDetail = False, returnModifiedTime = False, returnTempStudentEnrollmentRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentEnrollmentError(TempStudentEnrollmentErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentError/" + str(TempStudentEnrollmentErrorID), verb = "delete")


def getEveryTempStudentEnrollmentRecord(searchConditions = [], EntityID = 1, returnTempStudentEnrollmentRecordID = False, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnError = False, returnErrorCount = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnProcessEntryWithdrawal = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentEnrollmentRecord in the district.

    This function returns a dataframe of every TempStudentEnrollmentRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1, returnTempStudentEnrollmentRecordID = False, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnError = False, returnErrorCount = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnProcessEntryWithdrawal = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1, setTempStudentEnrollmentRecordID = None, setAdvisorFullName = None, setCalendarCode = None, setCalendarID = None, setCompletedSchoolYearOverride = None, setCreatedTime = None, setCreateFeeManagementCustomer = None, setCreateFeeManagementCustomerEntityYear = None, setDisciplineOfficerFullName = None, setEdFiDistrictIDResidence = None, setEdFiDistrictIDTransfer = None, setEdFiDistrictResidenceCodeDescription = None, setEdFiSchoolIDTransfer = None, setEndDate = None, setEnrollIntoEntityCode = None, setEnrollmentMoveable = None, setEntityCode = None, setEntityID = None, setEntryCode = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalID = None, setError = None, setErrorCount = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setExcludeFromThirdFridaySeptemberCount = None, setFailureReason = None, setFeeManagementCustomerID = None, setGradeLevelCode = None, setGradeReferenceID = None, setGradYear = None, setGSAADAClaimableOverrideCode = None, setGSAADAClaimableOverrideCodeDisplayName = None, setHomeroomCode = None, setHomeroomID = None, setIncludeAsProspectiveRank = None, setIsCurrentActive = None, setIsDefaultEntityForEntryWithdrawal = None, setIsDefaultEntityForStudentEntityYear = None, setIsPermanentExit = None, setIsPrivateSchoolChoiceStudent = None, setIsTuitionPaidOutOfDistrict = None, setModifiedTime = None, setNumericYear = None, setOutgoingStudent = None, setPercentEnrolled = None, setProcessEntryWithdrawal = None, setPromotionStatus = None, setPromotionStatusCode = None, setScheduledSectionCount = None, setSchoolCode = None, setSchoolID = None, setSchoolYearID = None, setServingRCDTSOverrideCode = None, setServingRCDTSOverrideCodeDisplayName = None, setServingRCDTSOverrideID = None, setSourceEntryWithdrawalID = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStartDate = None, setStateAidCategoryMNID = None, setStateDistrictMNCodeName = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStudentCourseRequestNotMoveableCount = None, setStudentCourseRequestToDeleteCount = None, setStudentFullName = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeID = None, setTestingSchoolCode = None, setTestingSchoolCodeDisplayName = None, setTestingSchoolRCDTSOverrideCode = None, setTestingSchoolRCDTSOverrideCodeDisplayName = None, setTestingSchoolRCDTSOverrideID = None, setTotalStudentCourseRequestCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCode = None, setWithdrawalCodeID = None, setWithdrawalComment = None, returnTempStudentEnrollmentRecordID = False, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnError = False, returnErrorCount = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnProcessEntryWithdrawal = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentEnrollmentRecord(EntityID = 1, setTempStudentEnrollmentRecordID = None, setAdvisorFullName = None, setCalendarCode = None, setCalendarID = None, setCompletedSchoolYearOverride = None, setCreatedTime = None, setCreateFeeManagementCustomer = None, setCreateFeeManagementCustomerEntityYear = None, setDisciplineOfficerFullName = None, setEdFiDistrictIDResidence = None, setEdFiDistrictIDTransfer = None, setEdFiDistrictResidenceCodeDescription = None, setEdFiSchoolIDTransfer = None, setEndDate = None, setEnrollIntoEntityCode = None, setEnrollmentMoveable = None, setEntityCode = None, setEntityID = None, setEntryCode = None, setEntryCodeID = None, setEntryComment = None, setEntryWithdrawalID = None, setError = None, setErrorCount = None, setExcludeFromHonorRoll = None, setExcludeFromRank = None, setExcludeFromThirdFridaySeptemberCount = None, setFailureReason = None, setFeeManagementCustomerID = None, setGradeLevelCode = None, setGradeReferenceID = None, setGradYear = None, setGSAADAClaimableOverrideCode = None, setGSAADAClaimableOverrideCodeDisplayName = None, setHomeroomCode = None, setHomeroomID = None, setIncludeAsProspectiveRank = None, setIsCurrentActive = None, setIsDefaultEntityForEntryWithdrawal = None, setIsDefaultEntityForStudentEntityYear = None, setIsPermanentExit = None, setIsPrivateSchoolChoiceStudent = None, setIsTuitionPaidOutOfDistrict = None, setModifiedTime = None, setNumericYear = None, setOutgoingStudent = None, setPercentEnrolled = None, setProcessEntryWithdrawal = None, setPromotionStatus = None, setPromotionStatusCode = None, setScheduledSectionCount = None, setSchoolCode = None, setSchoolID = None, setSchoolYearID = None, setServingRCDTSOverrideCode = None, setServingRCDTSOverrideCodeDisplayName = None, setServingRCDTSOverrideID = None, setSourceEntryWithdrawalID = None, setStaffIDAdvisor = None, setStaffIDDisciplineOfficer = None, setStartDate = None, setStateAidCategoryMNID = None, setStateDistrictMNCodeName = None, setStateDistrictMNID = None, setStateLastAttendanceLocationCodeMNID = None, setStudentCourseRequestNotMoveableCount = None, setStudentCourseRequestToDeleteCount = None, setStudentFullName = None, setStudentID = None, setStudentNumber = None, setStudentTypeCode = None, setStudentTypeID = None, setTestingSchoolCode = None, setTestingSchoolCodeDisplayName = None, setTestingSchoolRCDTSOverrideCode = None, setTestingSchoolRCDTSOverrideCodeDisplayName = None, setTestingSchoolRCDTSOverrideID = None, setTotalStudentCourseRequestCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCode = None, setWithdrawalCodeID = None, setWithdrawalComment = None, returnTempStudentEnrollmentRecordID = False, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnError = False, returnErrorCount = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnProcessEntryWithdrawal = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "delete")


def getEveryTempStudentEntityYear(searchConditions = [], EntityID = 1, returnTempStudentEntityYearID = False, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentEntityYear in the district.

    This function returns a dataframe of every TempStudentEntityYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1, returnTempStudentEntityYearID = False, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "get", return_params_list = return_params)

def modifyTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1, setTempStudentEntityYearID = None, setAdvisorDetails = None, setCreatedTime = None, setCurrentAdvisorDetails = None, setCurrentHomeroomDetails = None, setGenderCode = None, setGradeLevelCodeDescription = None, setHomeroomDetails = None, setHomeroomID = None, setIsActive = None, setMessage = None, setModifiedTime = None, setStaffIDAdvisor = None, setStudentEntityYearID = None, setStudentFullName = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentEntityYearID = False, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentEntityYear(EntityID = 1, setTempStudentEntityYearID = None, setAdvisorDetails = None, setCreatedTime = None, setCurrentAdvisorDetails = None, setCurrentHomeroomDetails = None, setGenderCode = None, setGradeLevelCodeDescription = None, setHomeroomDetails = None, setHomeroomID = None, setIsActive = None, setMessage = None, setModifiedTime = None, setStaffIDAdvisor = None, setStudentEntityYearID = None, setStudentFullName = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentEntityYearID = False, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "delete")


def getEveryWithdrawalCode(searchConditions = [], EntityID = 1, returnWithdrawalCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every WithdrawalCode in the district.

    This function returns a dataframe of every WithdrawalCode in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getWithdrawalCode(WithdrawalCodeID, EntityID = 1, returnWithdrawalCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "get", return_params_list = return_params)

def modifyWithdrawalCode(WithdrawalCodeID, EntityID = 1, setWithdrawalCodeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEdFiExitWithdrawID = None, setIsCrossEntityCourseEnrollment = None, setModifiedTime = None, setSchoolYearID = None, setStateStatusEndCodeMNID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeIDClonedFrom = None, setWithdrawalCodeMNID = None, returnWithdrawalCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createWithdrawalCode(EntityID = 1, setWithdrawalCodeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEdFiExitWithdrawID = None, setIsCrossEntityCourseEnrollment = None, setModifiedTime = None, setSchoolYearID = None, setStateStatusEndCodeMNID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithdrawalCodeIDClonedFrom = None, setWithdrawalCodeMNID = None, returnWithdrawalCodeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteWithdrawalCode(WithdrawalCodeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "delete")