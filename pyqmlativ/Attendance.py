# This module contains Attendance functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAttendancePeriod(searchConditions = [], EntityID = 1, returnAttendancePeriodID = False, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForSchoolTrakPositiveAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttendancePeriod in the district.

    This function returns a dataframe of every AttendancePeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttendancePeriod(AttendancePeriodID, EntityID = 1, returnAttendancePeriodID = False, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForSchoolTrakPositiveAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "get", return_params_list = return_params)

def modifyAttendancePeriod(AttendancePeriodID, EntityID = 1, setAttendancePeriodID = None, setAttendancePeriodIDClonedFrom = None, setAttendancePeriodIDClonedTo = None, setCode = None, setCreatedTime = None, setDisplayOrder = None, setDynamicRelationshipID = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUseForSchoolTrakPositiveAttendance = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseTeacherEntryCutOffTime = None, returnAttendancePeriodID = False, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForSchoolTrakPositiveAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttendancePeriod(EntityID = 1, setAttendancePeriodID = None, setAttendancePeriodIDClonedFrom = None, setAttendancePeriodIDClonedTo = None, setCode = None, setCreatedTime = None, setDisplayOrder = None, setDynamicRelationshipID = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUseForSchoolTrakPositiveAttendance = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseTeacherEntryCutOffTime = None, returnAttendancePeriodID = False, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForSchoolTrakPositiveAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttendancePeriod(AttendancePeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")


def getEveryAttendancePeriodConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnAttendancePeriodConfigEntityGroupYearID = False, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttendancePeriodConfigEntityGroupYear in the district.

    This function returns a dataframe of every AttendancePeriodConfigEntityGroupYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1, returnAttendancePeriodConfigEntityGroupYearID = False, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "get", return_params_list = return_params)

def modifyAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1, setAttendancePeriodConfigEntityGroupYearID = None, setAttendancePeriodConfigEntityGroupYearIDClonedFrom = None, setAttendancePeriodID = None, setConfigEntityGroupYearID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutoffNumberOfMinutesAfter = None, setTeacherEntryCutoffTime = None, setTeacherEntryCutoffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutoffTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendancePeriodConfigEntityGroupYearID = False, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttendancePeriodConfigEntityGroupYear(EntityID = 1, setAttendancePeriodConfigEntityGroupYearID = None, setAttendancePeriodConfigEntityGroupYearIDClonedFrom = None, setAttendancePeriodID = None, setConfigEntityGroupYearID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutoffNumberOfMinutesAfter = None, setTeacherEntryCutoffTime = None, setTeacherEntryCutoffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutoffTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendancePeriodConfigEntityGroupYearID = False, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "delete")


def getEveryAttendanceReason(searchConditions = [], EntityID = 1, returnAttendanceReasonID = False, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttendanceReason in the district.

    This function returns a dataframe of every AttendanceReason in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttendanceReason(AttendanceReasonID, EntityID = 1, returnAttendanceReasonID = False, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "get", return_params_list = return_params)

def modifyAttendanceReason(AttendanceReasonID, EntityID = 1, setAttendanceReasonID = None, setAttendanceReasonIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setTeacherEntryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceReasonID = False, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttendanceReason(EntityID = 1, setAttendanceReasonID = None, setAttendanceReasonIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setTeacherEntryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceReasonID = False, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttendanceReason(AttendanceReasonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "delete")


def getEveryAttendanceReportRunHistory(searchConditions = [], EntityID = 1, returnAttendanceReportRunHistoryID = False, returnAttachmentDisplayName = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnPostToFASA = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttendanceReportRunHistory in the district.

    This function returns a dataframe of every AttendanceReportRunHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1, returnAttendanceReportRunHistoryID = False, returnAttachmentDisplayName = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnPostToFASA = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "get", return_params_list = return_params)

def modifyAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1, setAttendanceReportRunHistoryID = None, setAttachmentDisplayName = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCountType = None, setCreatedTime = None, setDate = None, setEntityID = None, setEntityIDList = None, setFilterType = None, setFilterTypeCode = None, setFiscalYearID = None, setGracePeriod = None, setIsActive = None, setModifiedTime = None, setParameterData = None, setParameterDescription = None, setPostToFASA = None, setPrintAttendanceLetterForWindowedEnvelope = None, setReportRunInfoID = None, setRunDescription = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceReportRunHistoryID = False, returnAttachmentDisplayName = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnPostToFASA = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttendanceReportRunHistory(EntityID = 1, setAttendanceReportRunHistoryID = None, setAttachmentDisplayName = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCountType = None, setCreatedTime = None, setDate = None, setEntityID = None, setEntityIDList = None, setFilterType = None, setFilterTypeCode = None, setFiscalYearID = None, setGracePeriod = None, setIsActive = None, setModifiedTime = None, setParameterData = None, setParameterDescription = None, setPostToFASA = None, setPrintAttendanceLetterForWindowedEnvelope = None, setReportRunInfoID = None, setRunDescription = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceReportRunHistoryID = False, returnAttachmentDisplayName = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnPostToFASA = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "delete")


def getEveryAttendanceReportRunHistoryThresholdResetRange(searchConditions = [], EntityID = 1, returnAttendanceReportRunHistoryThresholdResetRangeID = False, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttendanceReportRunHistoryThresholdResetRange in the district.

    This function returns a dataframe of every AttendanceReportRunHistoryThresholdResetRange in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1, returnAttendanceReportRunHistoryThresholdResetRangeID = False, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "get", return_params_list = return_params)

def modifyAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1, setAttendanceReportRunHistoryThresholdResetRangeID = None, setAttendanceReportRunHistoryID = None, setCreatedTime = None, setModifiedTime = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceReportRunHistoryThresholdResetRangeID = False, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttendanceReportRunHistoryThresholdResetRange(EntityID = 1, setAttendanceReportRunHistoryThresholdResetRangeID = None, setAttendanceReportRunHistoryID = None, setCreatedTime = None, setModifiedTime = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceReportRunHistoryThresholdResetRangeID = False, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "delete")


def getEveryAttendanceTerm(searchConditions = [], EntityID = 1, returnAttendanceTermID = False, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttendanceTerm in the district.

    This function returns a dataframe of every AttendanceTerm in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttendanceTerm(AttendanceTermID, EntityID = 1, returnAttendanceTermID = False, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "get", return_params_list = return_params)

def modifyAttendanceTerm(AttendanceTermID, EntityID = 1, setAttendanceTermID = None, setAttendanceTermIDClonedFrom = None, setCalendarID = None, setCode = None, setCreatedTime = None, setDaysInTerm = None, setEndDate = None, setModifiedTime = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceTermID = False, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttendanceTerm(EntityID = 1, setAttendanceTermID = None, setAttendanceTermIDClonedFrom = None, setCalendarID = None, setCode = None, setCreatedTime = None, setDaysInTerm = None, setEndDate = None, setModifiedTime = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceTermID = False, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttendanceTerm(AttendanceTermID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "delete")


def getEveryAttendanceType(searchConditions = [], EntityID = 1, returnAttendanceTypeID = False, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttendanceType in the district.

    This function returns a dataframe of every AttendanceType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttendanceType(AttendanceTypeID, EntityID = 1, returnAttendanceTypeID = False, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "get", return_params_list = return_params)

def modifyAttendanceType(AttendanceTypeID, EntityID = 1, setAttendanceTypeID = None, setAttendanceTypeIDClonedFrom = None, setAttendanceTypeMNID = None, setCategory = None, setCategoryCode = None, setCategoryDescription = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIncludeInClassCounts = None, setIncludeInSpecialClassCounts = None, setIncludeInTotals = None, setIsTruant = None, setModifiedTime = None, setSchoolYearID = None, setShowOnGradesheetAssignments = None, setTeacherEntryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceTypeID = False, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttendanceType(EntityID = 1, setAttendanceTypeID = None, setAttendanceTypeIDClonedFrom = None, setAttendanceTypeMNID = None, setCategory = None, setCategoryCode = None, setCategoryDescription = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIncludeInClassCounts = None, setIncludeInSpecialClassCounts = None, setIncludeInTotals = None, setIsTruant = None, setModifiedTime = None, setSchoolYearID = None, setShowOnGradesheetAssignments = None, setTeacherEntryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttendanceTypeID = False, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttendanceType(AttendanceTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "delete")


def getEveryBellSchedule(searchConditions = [], EntityID = 1, returnBellScheduleID = False, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BellSchedule in the district.

    This function returns a dataframe of every BellSchedule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBellSchedule(BellScheduleID, EntityID = 1, returnBellScheduleID = False, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "get", return_params_list = return_params)

def modifyBellSchedule(BellScheduleID, EntityID = 1, setBellScheduleID = None, setBellScheduleIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityID = None, setIsDefault = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellScheduleID = False, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBellSchedule(EntityID = 1, setBellScheduleID = None, setBellScheduleIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityID = None, setIsDefault = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellScheduleID = False, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBellSchedule(BellScheduleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "delete")


def getEveryBellScheduleGroup(searchConditions = [], EntityID = 1, returnBellScheduleGroupID = False, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BellScheduleGroup in the district.

    This function returns a dataframe of every BellScheduleGroup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBellScheduleGroup(BellScheduleGroupID, EntityID = 1, returnBellScheduleGroupID = False, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "get", return_params_list = return_params)

def modifyBellScheduleGroup(BellScheduleGroupID, EntityID = 1, setBellScheduleGroupID = None, setAttendancePeriodIDAsOfDate = None, setBellScheduleGroupIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityID = None, setIsDefault = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellScheduleGroupID = False, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBellScheduleGroup(EntityID = 1, setBellScheduleGroupID = None, setAttendancePeriodIDAsOfDate = None, setBellScheduleGroupIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityID = None, setIsDefault = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellScheduleGroupID = False, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBellScheduleGroup(BellScheduleGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "delete")


def getEveryBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BellScheduleGroupBellSchedule in the district.

    This function returns a dataframe of every BellScheduleGroupBellSchedule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "get", return_params_list = return_params)

def modifyBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupID = None, setBellScheduleID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBellScheduleGroupBellSchedule(EntityID = 1, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupID = None, setBellScheduleID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "delete")


def getEveryBellSchedulingPeriod(searchConditions = [], EntityID = 1, returnBellSchedulingPeriodID = False, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BellSchedulingPeriod in the district.

    This function returns a dataframe of every BellSchedulingPeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1, returnBellSchedulingPeriodID = False, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "get", return_params_list = return_params)

def modifyBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1, setBellSchedulingPeriodID = None, setBellScheduleID = None, setBellSchedulingPeriodIDClonedFrom = None, setCreatedTime = None, setEndTime = None, setEndTimeWithOverride = None, setLengthInMinutes = None, setModifiedTime = None, setSchedulingPeriodID = None, setStartTime = None, setStartTimeWithOverride = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellSchedulingPeriodID = False, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBellSchedulingPeriod(EntityID = 1, setBellSchedulingPeriodID = None, setBellScheduleID = None, setBellSchedulingPeriodIDClonedFrom = None, setCreatedTime = None, setEndTime = None, setEndTimeWithOverride = None, setLengthInMinutes = None, setModifiedTime = None, setSchedulingPeriodID = None, setStartTime = None, setStartTimeWithOverride = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBellSchedulingPeriodID = False, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "delete")


def getEveryCalendarDay(searchConditions = [], EntityID = 1, returnCalendarDayID = False, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnDynamicRelationshipID = False, returnFoodServicePurchaseExists = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarDay in the district.

    This function returns a dataframe of every CalendarDay in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarDay(CalendarDayID, EntityID = 1, returnCalendarDayID = False, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnDynamicRelationshipID = False, returnFoodServicePurchaseExists = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "get", return_params_list = return_params)

def modifyCalendarDay(CalendarDayID, EntityID = 1, setCalendarDayID = None, setAttendanceTerm = None, setBellScheduleGroupSummary = None, setBellScheduleID = None, setCalendarID = None, setComment = None, setCountAs = None, setCreatedTime = None, setDate = None, setDateWithDayOfWeekAbbreviated = None, setDayOfTheWeek = None, setDayOfTheWeekNumber = None, setDayRotationID = None, setDynamicRelationshipID = None, setFoodServicePurchaseExists = None, setModifiedTime = None, setNumberOfCalendarDayEvents = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayID = False, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnDynamicRelationshipID = False, returnFoodServicePurchaseExists = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarDay(EntityID = 1, setCalendarDayID = None, setAttendanceTerm = None, setBellScheduleGroupSummary = None, setBellScheduleID = None, setCalendarID = None, setComment = None, setCountAs = None, setCreatedTime = None, setDate = None, setDateWithDayOfWeekAbbreviated = None, setDayOfTheWeek = None, setDayOfTheWeekNumber = None, setDayRotationID = None, setDynamicRelationshipID = None, setFoodServicePurchaseExists = None, setModifiedTime = None, setNumberOfCalendarDayEvents = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayID = False, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnDynamicRelationshipID = False, returnFoodServicePurchaseExists = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarDay(CalendarDayID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "delete")


def getEveryCalendarDayBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarDayBellScheduleGroupBellSchedule in the district.

    This function returns a dataframe of every CalendarDayBellScheduleGroupBellSchedule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1, returnCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "get", return_params_list = return_params)

def modifyCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1, setCalendarDayBellScheduleGroupBellScheduleID = None, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupID = None, setCalendarDayID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarDayBellScheduleGroupBellSchedule(EntityID = 1, setCalendarDayBellScheduleGroupBellScheduleID = None, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupID = None, setCalendarDayID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "delete")


def getEveryCalendarDayCalendarEvent(searchConditions = [], EntityID = 1, returnCalendarDayCalendarEventID = False, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarDayCalendarEvent in the district.

    This function returns a dataframe of every CalendarDayCalendarEvent in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1, returnCalendarDayCalendarEventID = False, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "get", return_params_list = return_params)

def modifyCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1, setCalendarDayCalendarEventID = None, setCalendarDayID = None, setCalendarEventID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayCalendarEventID = False, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarDayCalendarEvent(EntityID = 1, setCalendarDayCalendarEventID = None, setCalendarDayID = None, setCalendarEventID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayCalendarEventID = False, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "delete")


def getEveryCalendarDayDisplayPeriodOverride(searchConditions = [], EntityID = 1, returnCalendarDayDisplayPeriodOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarDayDisplayPeriodOverride in the district.

    This function returns a dataframe of every CalendarDayDisplayPeriodOverride in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1, returnCalendarDayDisplayPeriodOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "get", return_params_list = return_params)

def modifyCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1, setCalendarDayDisplayPeriodOverrideID = None, setCalendarDayID = None, setCreatedTime = None, setDisplayPeriodID = None, setLengthMinutes = None, setModifiedTime = None, setRemovePeriod = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayDisplayPeriodOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarDayDisplayPeriodOverride(EntityID = 1, setCalendarDayDisplayPeriodOverrideID = None, setCalendarDayID = None, setCreatedTime = None, setDisplayPeriodID = None, setLengthMinutes = None, setModifiedTime = None, setRemovePeriod = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDayDisplayPeriodOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "delete")


def getEveryCalendarDaySchedulingPeriodTimesOverride(searchConditions = [], EntityID = 1, returnCalendarDaySchedulingPeriodTimesOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarDaySchedulingPeriodTimesOverride in the district.

    This function returns a dataframe of every CalendarDaySchedulingPeriodTimesOverride in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1, returnCalendarDaySchedulingPeriodTimesOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "get", return_params_list = return_params)

def modifyCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1, setCalendarDaySchedulingPeriodTimesOverrideID = None, setCalendarDayID = None, setCreatedTime = None, setDurationInMinutes = None, setEndTime = None, setModifiedTime = None, setSchedulingPeriodID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDaySchedulingPeriodTimesOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarDaySchedulingPeriodTimesOverride(EntityID = 1, setCalendarDaySchedulingPeriodTimesOverrideID = None, setCalendarDayID = None, setCreatedTime = None, setDurationInMinutes = None, setEndTime = None, setModifiedTime = None, setSchedulingPeriodID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDaySchedulingPeriodTimesOverrideID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "delete")


def getEveryCalendarDisplayPeriod(searchConditions = [], EntityID = 1, returnCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarDisplayPeriodIDClonedTo = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarDisplayPeriod in the district.

    This function returns a dataframe of every CalendarDisplayPeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1, returnCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarDisplayPeriodIDClonedTo = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "get", return_params_list = return_params)

def modifyCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1, setCalendarDisplayPeriodID = None, setCalendarDisplayPeriodIDClonedFrom = None, setCalendarDisplayPeriodIDClonedTo = None, setCalendarID = None, setCreatedTime = None, setDisplayPeriodID = None, setIncludeInClassCounts = None, setIncludeInTotalCounts = None, setModifiedTime = None, setTakeAttendance = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarDisplayPeriodIDClonedTo = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarDisplayPeriod(EntityID = 1, setCalendarDisplayPeriodID = None, setCalendarDisplayPeriodIDClonedFrom = None, setCalendarDisplayPeriodIDClonedTo = None, setCalendarID = None, setCreatedTime = None, setDisplayPeriodID = None, setIncludeInClassCounts = None, setIncludeInTotalCounts = None, setModifiedTime = None, setTakeAttendance = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarDisplayPeriodIDClonedTo = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "delete")


def getEveryCalendarEvent(searchConditions = [], EntityID = 1, returnCalendarEventID = False, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarEvent in the district.

    This function returns a dataframe of every CalendarEvent in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarEvent(CalendarEventID, EntityID = 1, returnCalendarEventID = False, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "get", return_params_list = return_params)

def modifyCalendarEvent(CalendarEventID, EntityID = 1, setCalendarEventID = None, setCalendarEventIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEdFiCalendarEventID = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarEventID = False, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarEvent(EntityID = 1, setCalendarEventID = None, setCalendarEventIDClonedFrom = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEdFiCalendarEventID = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarEventID = False, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarEvent(CalendarEventID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "delete")


def getEveryCalendar(searchConditions = [], EntityID = 1, returnCalendarID = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Calendar in the district.

    This function returns a dataframe of every Calendar in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendar(CalendarID, EntityID = 1, returnCalendarID = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "get", return_params_list = return_params)

def modifyCalendar(CalendarID, EntityID = 1, setCalendarID = None, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCalendarIDClonedFrom = None, setCalendarIDClonedTo = None, setCalendarMNID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setMCCCAcademicYearImportID = None, setMCCCCalendarImportID = None, setModifiedTime = None, setNorthEastSemesterReportData = None, setSchoolYearID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZeroDayHighPeriodCount = None, returnCalendarID = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendar(EntityID = 1, setCalendarID = None, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCalendarIDClonedFrom = None, setCalendarIDClonedTo = None, setCalendarMNID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setMCCCAcademicYearImportID = None, setMCCCCalendarImportID = None, setModifiedTime = None, setNorthEastSemesterReportData = None, setSchoolYearID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZeroDayHighPeriodCount = None, returnCalendarID = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendar(CalendarID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "delete")


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = False, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setConfigEntityGroupYearID = None, setAttendanceReasonIDTardyDefault = None, setAttendanceTypeIDTardyDefault = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setEnableInOutTime = None, setEntityGroupKey = None, setEntityID = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setIncludeTardyCountOnLetter = None, setModifiedTime = None, setMultiPeriodClassCountMethod = None, setMultiPeriodClassCountMethodCode = None, setPresentBackgroundColor = None, setPresentBackgroundColorHex = None, setPresentBackgroundColorRgba = None, setPrintAttendanceLetterForWindowedEnvelope = None, setRestrictTeacherAttendanceUpdates = None, setSchoolYearID = None, setSpecialClassCountsLabel = None, setTardyDefaultComment = None, setTardyKioskTardySlipTitle = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutOffNumberOfMinutesAfter = None, setTeacherEntryCutOffTime = None, setTeacherEntryCutOffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutOffTime = None, setUseInOutTimeForCalculations = None, setUseMarkAllStudentsPresentOnTile = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseSpecialClassCounts = None, setUseTardyCalculator = None, setUseTardyKiosk = None, setUseTeacherPerfectAttendanceConfirmation = None, returnConfigEntityGroupYearID = False, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setConfigEntityGroupYearID = None, setAttendanceReasonIDTardyDefault = None, setAttendanceTypeIDTardyDefault = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setEnableInOutTime = None, setEntityGroupKey = None, setEntityID = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setIncludeTardyCountOnLetter = None, setModifiedTime = None, setMultiPeriodClassCountMethod = None, setMultiPeriodClassCountMethodCode = None, setPresentBackgroundColor = None, setPresentBackgroundColorHex = None, setPresentBackgroundColorRgba = None, setPrintAttendanceLetterForWindowedEnvelope = None, setRestrictTeacherAttendanceUpdates = None, setSchoolYearID = None, setSpecialClassCountsLabel = None, setTardyDefaultComment = None, setTardyKioskTardySlipTitle = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutOffNumberOfMinutesAfter = None, setTeacherEntryCutOffTime = None, setTeacherEntryCutOffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutOffTime = None, setUseInOutTimeForCalculations = None, setUseMarkAllStudentsPresentOnTile = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseSpecialClassCounts = None, setUseTardyCalculator = None, setUseTardyKiosk = None, setUseTeacherPerfectAttendanceConfirmation = None, returnConfigEntityGroupYearID = False, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnPrintAttendanceLetterForWindowedEnvelope = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")


def getEveryCrossEntityAttendanceReason(searchConditions = [], EntityID = 1, returnCrossEntityAttendanceReasonID = False, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CrossEntityAttendanceReason in the district.

    This function returns a dataframe of every CrossEntityAttendanceReason in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1, returnCrossEntityAttendanceReasonID = False, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "get", return_params_list = return_params)

def modifyCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1, setCrossEntityAttendanceReasonID = None, setAttendanceReasonIDFrom = None, setAttendanceReasonIDTo = None, setCreatedTime = None, setEntityIDTo = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCrossEntityAttendanceReasonID = False, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCrossEntityAttendanceReason(EntityID = 1, setCrossEntityAttendanceReasonID = None, setAttendanceReasonIDFrom = None, setAttendanceReasonIDTo = None, setCreatedTime = None, setEntityIDTo = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCrossEntityAttendanceReasonID = False, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "delete")


def getEveryCrossEntityAttendanceType(searchConditions = [], EntityID = 1, returnCrossEntityAttendanceTypeID = False, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CrossEntityAttendanceType in the district.

    This function returns a dataframe of every CrossEntityAttendanceType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1, returnCrossEntityAttendanceTypeID = False, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "get", return_params_list = return_params)

def modifyCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1, setCrossEntityAttendanceTypeID = None, setAttendanceTypeIDFrom = None, setAttendanceTypeIDTo = None, setCreatedTime = None, setEntityIDTo = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCrossEntityAttendanceTypeID = False, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCrossEntityAttendanceType(EntityID = 1, setCrossEntityAttendanceTypeID = None, setAttendanceTypeIDFrom = None, setAttendanceTypeIDTo = None, setCreatedTime = None, setEntityIDTo = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCrossEntityAttendanceTypeID = False, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "delete")


def getEveryCrossEntityCalendarDisplayPeriod(searchConditions = [], EntityID = 1, returnCrossEntityCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnCrossEntityCalendarDisplayPeriodIDClonedFrom = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CrossEntityCalendarDisplayPeriod in the district.

    This function returns a dataframe of every CrossEntityCalendarDisplayPeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1, returnCrossEntityCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnCrossEntityCalendarDisplayPeriodIDClonedFrom = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "get", return_params_list = return_params)

def modifyCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1, setCrossEntityCalendarDisplayPeriodID = None, setCalendarDisplayPeriodIDFrom = None, setCalendarDisplayPeriodIDTo = None, setCreatedTime = None, setCrossEntityCalendarDisplayPeriodIDClonedFrom = None, setIsAutoCreated = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCrossEntityCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnCrossEntityCalendarDisplayPeriodIDClonedFrom = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCrossEntityCalendarDisplayPeriod(EntityID = 1, setCrossEntityCalendarDisplayPeriodID = None, setCalendarDisplayPeriodIDFrom = None, setCalendarDisplayPeriodIDTo = None, setCreatedTime = None, setCrossEntityCalendarDisplayPeriodIDClonedFrom = None, setIsAutoCreated = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCrossEntityCalendarDisplayPeriodID = False, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnCrossEntityCalendarDisplayPeriodIDClonedFrom = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "delete")


def getEveryDailySectionAttendance(searchConditions = [], EntityID = 1, returnDailySectionAttendanceID = False, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DailySectionAttendance in the district.

    This function returns a dataframe of every DailySectionAttendance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDailySectionAttendance(DailySectionAttendanceID, EntityID = 1, returnDailySectionAttendanceID = False, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "get", return_params_list = return_params)

def modifyDailySectionAttendance(DailySectionAttendanceID, EntityID = 1, setDailySectionAttendanceID = None, setAttendancePeriodID = None, setCalendarDayID = None, setCreatedTime = None, setMeetID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDailySectionAttendanceID = False, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDailySectionAttendance(EntityID = 1, setDailySectionAttendanceID = None, setAttendancePeriodID = None, setCalendarDayID = None, setCreatedTime = None, setMeetID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDailySectionAttendanceID = False, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDailySectionAttendance(DailySectionAttendanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "delete")


def getEveryDayRotationPattern(searchConditions = [], EntityID = 1, returnDayRotationPatternID = False, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DayRotationPattern in the district.

    This function returns a dataframe of every DayRotationPattern in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDayRotationPattern(DayRotationPatternID, EntityID = 1, returnDayRotationPatternID = False, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "get", return_params_list = return_params)

def modifyDayRotationPattern(DayRotationPatternID, EntityID = 1, setDayRotationPatternID = None, setCreatedTime = None, setDayNumber = None, setDayRotationID = None, setDayRotationPatternIDClonedFrom = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDayRotationPatternID = False, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDayRotationPattern(EntityID = 1, setDayRotationPatternID = None, setCreatedTime = None, setDayNumber = None, setDayRotationID = None, setDayRotationPatternIDClonedFrom = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDayRotationPatternID = False, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDayRotationPattern(DayRotationPatternID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "delete")


def getEveryDisciplineThreshold(searchConditions = [], EntityID = 1, returnDisciplineThresholdID = False, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineThreshold in the district.

    This function returns a dataframe of every DisciplineThreshold in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineThreshold(DisciplineThresholdID, EntityID = 1, returnDisciplineThresholdID = False, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "get", return_params_list = return_params)

def modifyDisciplineThreshold(DisciplineThresholdID, EntityID = 1, setDisciplineThresholdID = None, setActionID = None, setAllowDisciplineOnCurrentDay = None, setAttendanceLettersRan = None, setAttendanceSlipComment = None, setBuildingIDServing = None, setCreateDisciplineRecord = None, setCreatedTime = None, setDisciplineSlipComment = None, setDurationToServe = None, setDurationToServePerDay = None, setFooterComment = None, setGenerateActionDetail = None, setGreeting = None, setIncidentDefaultComment = None, setIncidentDescription = None, setIsRepeatable = None, setLocationIDServing = None, setModifiedTime = None, setOffenseID = None, setRangeDisplay = None, setRoomIDServing = None, setServeOnFriday = None, setServeOnMonday = None, setServeOnSaturday = None, setServeOnSunday = None, setServeOnThursday = None, setServeOnTuesday = None, setServeOnWednesday = None, setServingTime = None, setStaffIDAuthorizedBy = None, setThresholdRangeHigh = None, setThresholdRangeLow = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineThresholdID = False, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineThreshold(EntityID = 1, setDisciplineThresholdID = None, setActionID = None, setAllowDisciplineOnCurrentDay = None, setAttendanceLettersRan = None, setAttendanceSlipComment = None, setBuildingIDServing = None, setCreateDisciplineRecord = None, setCreatedTime = None, setDisciplineSlipComment = None, setDurationToServe = None, setDurationToServePerDay = None, setFooterComment = None, setGenerateActionDetail = None, setGreeting = None, setIncidentDefaultComment = None, setIncidentDescription = None, setIsRepeatable = None, setLocationIDServing = None, setModifiedTime = None, setOffenseID = None, setRangeDisplay = None, setRoomIDServing = None, setServeOnFriday = None, setServeOnMonday = None, setServeOnSaturday = None, setServeOnSunday = None, setServeOnThursday = None, setServeOnTuesday = None, setServeOnWednesday = None, setServingTime = None, setStaffIDAuthorizedBy = None, setThresholdRangeHigh = None, setThresholdRangeLow = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineThresholdID = False, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineThreshold(DisciplineThresholdID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "delete")


def getEveryDroppedStudentAttendancePeriod(searchConditions = [], EntityID = 1, returnDroppedStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DroppedStudentAttendancePeriod in the district.

    This function returns a dataframe of every DroppedStudentAttendancePeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1, returnDroppedStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "get", return_params_list = return_params)

def modifyDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1, setDroppedStudentAttendancePeriodID = None, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setCalendarDayID = None, setComment = None, setCreatedTime = None, setIncidentOffenseNameActionDetailID = None, setIsGuardianNotified = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDroppedStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDroppedStudentAttendancePeriod(EntityID = 1, setDroppedStudentAttendancePeriodID = None, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setCalendarDayID = None, setComment = None, setCreatedTime = None, setIncidentOffenseNameActionDetailID = None, setIsGuardianNotified = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDroppedStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "delete")


def getEveryMassCreateAttendanceByClassActivityRangeRun(searchConditions = [], EntityID = 1, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnAffectedStudentAttendanceCount = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnModifiedTime = False, returnRunTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRunBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MassCreateAttendanceByClassActivityRangeRun in the district.

    This function returns a dataframe of every MassCreateAttendanceByClassActivityRangeRun in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMassCreateAttendanceByClassActivityRangeRun(MassCreateAttendanceByClassActivityRangeRunID, EntityID = 1, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnAffectedStudentAttendanceCount = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnModifiedTime = False, returnRunTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRunBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/" + str(MassCreateAttendanceByClassActivityRangeRunID), verb = "get", return_params_list = return_params)

def modifyMassCreateAttendanceByClassActivityRangeRun(MassCreateAttendanceByClassActivityRangeRunID, EntityID = 1, setMassCreateAttendanceByClassActivityRangeRunID = None, setAffectedStudentAttendanceCount = None, setCreatedTime = None, setEntityID = None, setIsActive = None, setModifiedTime = None, setRunTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRunBy = None, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnAffectedStudentAttendanceCount = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnModifiedTime = False, returnRunTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRunBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/" + str(MassCreateAttendanceByClassActivityRangeRunID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMassCreateAttendanceByClassActivityRangeRun(EntityID = 1, setMassCreateAttendanceByClassActivityRangeRunID = None, setAffectedStudentAttendanceCount = None, setCreatedTime = None, setEntityID = None, setIsActive = None, setModifiedTime = None, setRunTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDRunBy = None, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnAffectedStudentAttendanceCount = False, returnCreatedTime = False, returnEntityID = False, returnIsActive = False, returnModifiedTime = False, returnRunTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDRunBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMassCreateAttendanceByClassActivityRangeRun(MassCreateAttendanceByClassActivityRangeRunID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/MassCreateAttendanceByClassActivityRangeRun/" + str(MassCreateAttendanceByClassActivityRangeRunID), verb = "delete")


def getEveryRecordedUnrecordedAttendance(searchConditions = [], EntityID = 1, returnMeetDisplayPeriodID = False, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RecordedUnrecordedAttendance in the district.

    This function returns a dataframe of every RecordedUnrecordedAttendance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1, returnMeetDisplayPeriodID = False, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "get", return_params_list = return_params)

def modifyRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1, setMeetDisplayPeriodID = None, setAttendanceTaken = None, setCountAs = None, setCreatedTime = None, setDailySectionAttendanceID = None, setDate = None, setDayOfTheWeek = None, setDisplayPeriodCode = None, setMeetID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMeetDisplayPeriodID = False, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRecordedUnrecordedAttendance(EntityID = 1, setMeetDisplayPeriodID = None, setAttendanceTaken = None, setCountAs = None, setCreatedTime = None, setDailySectionAttendanceID = None, setDate = None, setDayOfTheWeek = None, setDisplayPeriodCode = None, setMeetID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMeetDisplayPeriodID = False, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "delete")


def getEveryRoomLayout(searchConditions = [], EntityID = 1, returnRoomLayoutID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoomLayout in the district.

    This function returns a dataframe of every RoomLayout in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoomLayout(RoomLayoutID, EntityID = 1, returnRoomLayoutID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "get", return_params_list = return_params)

def modifyRoomLayout(RoomLayoutID, EntityID = 1, setRoomLayoutID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRoomID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomLayoutID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoomLayout(EntityID = 1, setRoomLayoutID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRoomID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomLayoutID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoomLayout(RoomLayoutID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "delete")


def getEveryRoomLayoutObject(searchConditions = [], EntityID = 1, returnRoomLayoutObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoomLayoutObject in the district.

    This function returns a dataframe of every RoomLayoutObject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoomLayoutObject(RoomLayoutObjectID, EntityID = 1, returnRoomLayoutObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "get", return_params_list = return_params)

def modifyRoomLayoutObject(RoomLayoutObjectID, EntityID = 1, setRoomLayoutObjectID = None, setCreatedTime = None, setModifiedTime = None, setRoomLayoutID = None, setRoomObjectID = None, setRotation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXLocation = None, setYLocation = None, returnRoomLayoutObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoomLayoutObject(EntityID = 1, setRoomLayoutObjectID = None, setCreatedTime = None, setModifiedTime = None, setRoomLayoutID = None, setRoomObjectID = None, setRotation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXLocation = None, setYLocation = None, returnRoomLayoutObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoomLayoutObject(RoomLayoutObjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "delete")


def getEveryRoomObject(searchConditions = [], EntityID = 1, returnRoomObjectID = False, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoomObject in the district.

    This function returns a dataframe of every RoomObject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoomObject(RoomObjectID, EntityID = 1, returnRoomObjectID = False, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "get", return_params_list = return_params)

def modifyRoomObject(RoomObjectID, EntityID = 1, setRoomObjectID = None, setCreatedTime = None, setIsStudentSeat = None, setLabel = None, setModifiedTime = None, setParameters = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomObjectID = False, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoomObject(EntityID = 1, setRoomObjectID = None, setCreatedTime = None, setIsStudentSeat = None, setLabel = None, setModifiedTime = None, setParameters = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomObjectID = False, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoomObject(RoomObjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "delete")


def getEverySeatingChart(searchConditions = [], EntityID = 1, returnSeatingChartID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SeatingChart in the district.

    This function returns a dataframe of every SeatingChart in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSeatingChart(SeatingChartID, EntityID = 1, returnSeatingChartID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "get", return_params_list = return_params)

def modifySeatingChart(SeatingChartID, EntityID = 1, setSeatingChartID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRoomLayoutID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSeatingChart(EntityID = 1, setSeatingChartID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRoomLayoutID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSeatingChart(SeatingChartID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "delete")


def getEverySeatingChartMeet(searchConditions = [], EntityID = 1, returnSeatingChartMeetID = False, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SeatingChartMeet in the district.

    This function returns a dataframe of every SeatingChartMeet in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSeatingChartMeet(SeatingChartMeetID, EntityID = 1, returnSeatingChartMeetID = False, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "get", return_params_list = return_params)

def modifySeatingChartMeet(SeatingChartMeetID, EntityID = 1, setSeatingChartMeetID = None, setCreatedTime = None, setIsCurrent = None, setMeetID = None, setModifiedTime = None, setSeatingChartID = None, setSectionList = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartMeetID = False, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSeatingChartMeet(EntityID = 1, setSeatingChartMeetID = None, setCreatedTime = None, setIsCurrent = None, setMeetID = None, setModifiedTime = None, setSeatingChartID = None, setSectionList = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartMeetID = False, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSeatingChartMeet(SeatingChartMeetID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "delete")


def getEverySeatingChartSeat(searchConditions = [], EntityID = 1, returnSeatingChartSeatID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SeatingChartSeat in the district.

    This function returns a dataframe of every SeatingChartSeat in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSeatingChartSeat(SeatingChartSeatID, EntityID = 1, returnSeatingChartSeatID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "get", return_params_list = return_params)

def modifySeatingChartSeat(SeatingChartSeatID, EntityID = 1, setSeatingChartSeatID = None, setCreatedTime = None, setModifiedTime = None, setRoomLayoutObjectID = None, setSeatingChartID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartSeatID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSeatingChartSeat(EntityID = 1, setSeatingChartSeatID = None, setCreatedTime = None, setModifiedTime = None, setRoomLayoutObjectID = None, setSeatingChartID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartSeatID = False, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSeatingChartSeat(SeatingChartSeatID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "delete")


def getEverySeatingChartUsedLast(searchConditions = [], EntityID = 1, returnSeatingChartUsedLastID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SeatingChartUsedLast in the district.

    This function returns a dataframe of every SeatingChartUsedLast in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1, returnSeatingChartUsedLastID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "get", return_params_list = return_params)

def modifySeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1, setSeatingChartUsedLastID = None, setCreatedTime = None, setDisplayPeriodID = None, setModifiedTime = None, setRoomID = None, setSeatingChartID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartUsedLastID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSeatingChartUsedLast(EntityID = 1, setSeatingChartUsedLastID = None, setCreatedTime = None, setDisplayPeriodID = None, setModifiedTime = None, setRoomID = None, setSeatingChartID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSeatingChartUsedLastID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "delete")


def getEveryStaffMeetSetting(searchConditions = [], EntityID = 1, returnStaffMeetSettingID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayCourseDescription = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentNumber = False, returnHideLockedColumns = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StaffMeetSetting in the district.

    This function returns a dataframe of every StaffMeetSetting in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStaffMeetSetting(StaffMeetSettingID, EntityID = 1, returnStaffMeetSettingID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayCourseDescription = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentNumber = False, returnHideLockedColumns = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "get", return_params_list = return_params)

def modifyStaffMeetSetting(StaffMeetSettingID, EntityID = 1, setStaffMeetSettingID = None, setBrowseViewID = None, setCreatedTime = None, setDisplayAttendanceTotalsOnDesktop = None, setDisplayAttendanceTotalsOnMobile = None, setDisplayCourseDescription = None, setDisplayHistoricalAttendanceOnDesktop = None, setDisplayHistoricalAttendanceOnMobile = None, setDisplayStudentGradeLevel = None, setDisplayStudentNumber = None, setHideLockedColumns = None, setModifiedTime = None, setStaffMeetID = None, setStudentNameDisplayType = None, setStudentNameDisplayTypeCode = None, setUseCustomClassRosterSort = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffMeetSettingID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayCourseDescription = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentNumber = False, returnHideLockedColumns = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaffMeetSetting(EntityID = 1, setStaffMeetSettingID = None, setBrowseViewID = None, setCreatedTime = None, setDisplayAttendanceTotalsOnDesktop = None, setDisplayAttendanceTotalsOnMobile = None, setDisplayCourseDescription = None, setDisplayHistoricalAttendanceOnDesktop = None, setDisplayHistoricalAttendanceOnMobile = None, setDisplayStudentGradeLevel = None, setDisplayStudentNumber = None, setHideLockedColumns = None, setModifiedTime = None, setStaffMeetID = None, setStudentNameDisplayType = None, setStudentNameDisplayTypeCode = None, setUseCustomClassRosterSort = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffMeetSettingID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayCourseDescription = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentNumber = False, returnHideLockedColumns = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaffMeetSetting(StaffMeetSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "delete")


def getEveryStudentAttendance(searchConditions = [], EntityID = 1, returnStudentAttendanceID = False, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnHideRecordMA = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAttendance in the district.

    This function returns a dataframe of every StudentAttendance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAttendance(StudentAttendanceID, EntityID = 1, returnStudentAttendanceID = False, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnHideRecordMA = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "get", return_params_list = return_params)

def modifyStudentAttendance(StudentAttendanceID, EntityID = 1, setStudentAttendanceID = None, setCalendarDayID = None, setComment = None, setCommentsExistForStudentAttendance = None, setCreatedTime = None, setDaysAbsent = None, setDaysExcused = None, setDaysOther = None, setDaysUnexcused = None, setEntityID = None, setHideRecordMA = None, setIsGuardianNotified = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setTardyCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAttendanceID = False, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnHideRecordMA = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAttendance(EntityID = 1, setStudentAttendanceID = None, setCalendarDayID = None, setComment = None, setCommentsExistForStudentAttendance = None, setCreatedTime = None, setDaysAbsent = None, setDaysExcused = None, setDaysOther = None, setDaysUnexcused = None, setEntityID = None, setHideRecordMA = None, setIsGuardianNotified = None, setModifiedTime = None, setSchoolYearID = None, setStudentID = None, setTardyCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAttendanceID = False, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnHideRecordMA = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAttendance(StudentAttendanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "delete")


def getEveryStudentAttendanceEntity(searchConditions = [], EntityID = 1, returnStudentAttendanceID = False, returnEntityID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAttendanceEntity in the district.

    This function returns a dataframe of every StudentAttendanceEntity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAttendanceEntity(StudentAttendanceID, EntityID = 1, returnStudentAttendanceID = False, returnEntityID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/" + str(StudentAttendanceID), verb = "get", return_params_list = return_params)

def modifyStudentAttendanceEntity(StudentAttendanceID, EntityID = 1, setStudentAttendanceID = None, setEntityID = None, returnStudentAttendanceID = False, returnEntityID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/" + str(StudentAttendanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAttendanceEntity(EntityID = 1, setStudentAttendanceID = None, setEntityID = None, returnStudentAttendanceID = False, returnEntityID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAttendanceEntity(StudentAttendanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceEntity/" + str(StudentAttendanceID), verb = "delete")


def getEveryStudentAttendancePeriod(searchConditions = [], EntityID = 1, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAttendancePeriod in the district.

    This function returns a dataframe of every StudentAttendancePeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "get", return_params_list = return_params)

def modifyStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1, setStudentAttendancePeriodID = None, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setAttendanceTypeWithReason = None, setComment = None, setCreatedTime = None, setCrossWalkedAttendanceTypeWithReason = None, setEntityIDAttendancePeriod = None, setEntityIDCourse = None, setIncidentOffenseNameActionDetailID = None, setModifiedTime = None, setStudentAttendanceID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setViewingFromAttendanceEntity = None, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAttendancePeriod(EntityID = 1, setStudentAttendancePeriodID = None, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setAttendanceTypeWithReason = None, setComment = None, setCreatedTime = None, setCrossWalkedAttendanceTypeWithReason = None, setEntityIDAttendancePeriod = None, setEntityIDCourse = None, setIncidentOffenseNameActionDetailID = None, setModifiedTime = None, setStudentAttendanceID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setViewingFromAttendanceEntity = None, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "delete")


def getEveryStudentAttendancePeriodGroup(searchConditions = [], EntityID = 1, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAttendancePeriodGroup in the district.

    This function returns a dataframe of every StudentAttendancePeriodGroup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "get", return_params_list = return_params)

def modifyStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1, setStudentAttendancePeriodID = None, setAttendancePeriodID = None, setEntityID = None, setSchoolYearID = None, setStudentAttendanceID = None, setStudentID = None, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAttendancePeriodGroup(EntityID = 1, setStudentAttendancePeriodID = None, setAttendancePeriodID = None, setEntityID = None, setSchoolYearID = None, setStudentAttendanceID = None, setStudentID = None, returnStudentAttendancePeriodID = False, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "delete")


def getEveryStudentAttendancePeriodRunHistory(searchConditions = [], EntityID = 1, returnStudentAttendancePeriodRunHistoryID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnModifiedTime = False, returnNewAttendanceReasonID = False, returnNewAttendanceTypeID = False, returnNewComment = False, returnOriginalAttendanceReasonID = False, returnOriginalAttendanceTypeID = False, returnOriginalComment = False, returnProcedure = False, returnStatus = False, returnStudentAttendancePeriodID = False, returnStudentAttendanceRunHistoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAttendancePeriodRunHistory in the district.

    This function returns a dataframe of every StudentAttendancePeriodRunHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAttendancePeriodRunHistory(StudentAttendancePeriodRunHistoryID, EntityID = 1, returnStudentAttendancePeriodRunHistoryID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnModifiedTime = False, returnNewAttendanceReasonID = False, returnNewAttendanceTypeID = False, returnNewComment = False, returnOriginalAttendanceReasonID = False, returnOriginalAttendanceTypeID = False, returnOriginalComment = False, returnProcedure = False, returnStatus = False, returnStudentAttendancePeriodID = False, returnStudentAttendanceRunHistoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/" + str(StudentAttendancePeriodRunHistoryID), verb = "get", return_params_list = return_params)

def modifyStudentAttendancePeriodRunHistory(StudentAttendancePeriodRunHistoryID, EntityID = 1, setStudentAttendancePeriodRunHistoryID = None, setAttendancePeriodID = None, setCreatedTime = None, setIsActive = None, setIsInsert = None, setModifiedTime = None, setNewAttendanceReasonID = None, setNewAttendanceTypeID = None, setNewComment = None, setOriginalAttendanceReasonID = None, setOriginalAttendanceTypeID = None, setOriginalComment = None, setProcedure = None, setStatus = None, setStudentAttendancePeriodID = None, setStudentAttendanceRunHistoryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAttendancePeriodRunHistoryID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnModifiedTime = False, returnNewAttendanceReasonID = False, returnNewAttendanceTypeID = False, returnNewComment = False, returnOriginalAttendanceReasonID = False, returnOriginalAttendanceTypeID = False, returnOriginalComment = False, returnProcedure = False, returnStatus = False, returnStudentAttendancePeriodID = False, returnStudentAttendanceRunHistoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/" + str(StudentAttendancePeriodRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAttendancePeriodRunHistory(EntityID = 1, setStudentAttendancePeriodRunHistoryID = None, setAttendancePeriodID = None, setCreatedTime = None, setIsActive = None, setIsInsert = None, setModifiedTime = None, setNewAttendanceReasonID = None, setNewAttendanceTypeID = None, setNewComment = None, setOriginalAttendanceReasonID = None, setOriginalAttendanceTypeID = None, setOriginalComment = None, setProcedure = None, setStatus = None, setStudentAttendancePeriodID = None, setStudentAttendanceRunHistoryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAttendancePeriodRunHistoryID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnModifiedTime = False, returnNewAttendanceReasonID = False, returnNewAttendanceTypeID = False, returnNewComment = False, returnOriginalAttendanceReasonID = False, returnOriginalAttendanceTypeID = False, returnOriginalComment = False, returnProcedure = False, returnStatus = False, returnStudentAttendancePeriodID = False, returnStudentAttendanceRunHistoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAttendancePeriodRunHistory(StudentAttendancePeriodRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodRunHistory/" + str(StudentAttendancePeriodRunHistoryID), verb = "delete")


def getEveryStudentAttendanceRunHistory(searchConditions = [], EntityID = 1, returnStudentAttendanceRunHistoryID = False, returnCalendarDayID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnModifiedTime = False, returnNewComment = False, returnNewIsGuardianNotified = False, returnOriginalComment = False, returnOriginalIsGuardianNotified = False, returnProcedure = False, returnStatus = False, returnStudentAttendanceID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAttendanceRunHistory in the district.

    This function returns a dataframe of every StudentAttendanceRunHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAttendanceRunHistory(StudentAttendanceRunHistoryID, EntityID = 1, returnStudentAttendanceRunHistoryID = False, returnCalendarDayID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnModifiedTime = False, returnNewComment = False, returnNewIsGuardianNotified = False, returnOriginalComment = False, returnOriginalIsGuardianNotified = False, returnProcedure = False, returnStatus = False, returnStudentAttendanceID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/" + str(StudentAttendanceRunHistoryID), verb = "get", return_params_list = return_params)

def modifyStudentAttendanceRunHistory(StudentAttendanceRunHistoryID, EntityID = 1, setStudentAttendanceRunHistoryID = None, setCalendarDayID = None, setCreatedTime = None, setIsActive = None, setIsInsert = None, setMassCreateAttendanceByClassActivityRangeRunID = None, setModifiedTime = None, setNewComment = None, setNewIsGuardianNotified = None, setOriginalComment = None, setOriginalIsGuardianNotified = None, setProcedure = None, setStatus = None, setStudentAttendanceID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAttendanceRunHistoryID = False, returnCalendarDayID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnModifiedTime = False, returnNewComment = False, returnNewIsGuardianNotified = False, returnOriginalComment = False, returnOriginalIsGuardianNotified = False, returnProcedure = False, returnStatus = False, returnStudentAttendanceID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/" + str(StudentAttendanceRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAttendanceRunHistory(EntityID = 1, setStudentAttendanceRunHistoryID = None, setCalendarDayID = None, setCreatedTime = None, setIsActive = None, setIsInsert = None, setMassCreateAttendanceByClassActivityRangeRunID = None, setModifiedTime = None, setNewComment = None, setNewIsGuardianNotified = None, setOriginalComment = None, setOriginalIsGuardianNotified = None, setProcedure = None, setStatus = None, setStudentAttendanceID = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAttendanceRunHistoryID = False, returnCalendarDayID = False, returnCreatedTime = False, returnIsActive = False, returnIsInsert = False, returnMassCreateAttendanceByClassActivityRangeRunID = False, returnModifiedTime = False, returnNewComment = False, returnNewIsGuardianNotified = False, returnOriginalComment = False, returnOriginalIsGuardianNotified = False, returnProcedure = False, returnStatus = False, returnStudentAttendanceID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAttendanceRunHistory(StudentAttendanceRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceRunHistory/" + str(StudentAttendanceRunHistoryID), verb = "delete")


def getEveryStudentAttendanceTerm(searchConditions = [], EntityID = 1, returnStudentID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysPossible = False, returnTotalDaysPresent = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentAttendanceTerm in the district.

    This function returns a dataframe of every StudentAttendanceTerm in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentAttendanceTerm(StudentID, EntityID = 1, returnStudentID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysPossible = False, returnTotalDaysPresent = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "get", return_params_list = return_params)

def modifyStudentAttendanceTerm(StudentID, EntityID = 1, setStudentID = None, setAttendanceTermCode = None, setAttendanceTermID = None, setEndDate = None, setEntityID = None, setIsDefault = None, setSchoolYearID = None, setStartDate = None, setTotalDaysAbsent = None, setTotalDaysExcused = None, setTotalDaysOther = None, setTotalDaysPossible = None, setTotalDaysPresent = None, setTotalDaysUnexcused = None, setTotalTardyCount = None, returnStudentID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysPossible = False, returnTotalDaysPresent = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAttendanceTerm(EntityID = 1, setStudentID = None, setAttendanceTermCode = None, setAttendanceTermID = None, setEndDate = None, setEntityID = None, setIsDefault = None, setSchoolYearID = None, setStartDate = None, setTotalDaysAbsent = None, setTotalDaysExcused = None, setTotalDaysOther = None, setTotalDaysPossible = None, setTotalDaysPresent = None, setTotalDaysUnexcused = None, setTotalTardyCount = None, returnStudentID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysPossible = False, returnTotalDaysPresent = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAttendanceTerm(StudentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "delete")


def getEveryStudentDisciplineThresholdAttendanceReportRunHistory(searchConditions = [], EntityID = 1, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnAttachmentID = False, returnAttendanceReportRunHistoryID = False, returnBody = False, returnBodyForReport = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFooter = False, returnFooterForReport = False, returnHeader = False, returnHeaderForReport = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentDisciplineThresholdAttendanceReportRunHistory in the district.

    This function returns a dataframe of every StudentDisciplineThresholdAttendanceReportRunHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnAttachmentID = False, returnAttendanceReportRunHistoryID = False, returnBody = False, returnBodyForReport = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFooter = False, returnFooterForReport = False, returnHeader = False, returnHeaderForReport = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "get", return_params_list = return_params)

def modifyStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1, setStudentDisciplineThresholdAttendanceReportRunHistoryID = None, setAttachmentID = None, setAttendanceReportRunHistoryID = None, setBody = None, setBodyForReport = None, setCreatedTime = None, setDisciplineThresholdID = None, setFooter = None, setFooterForReport = None, setHeader = None, setHeaderForReport = None, setIsActive = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnAttachmentID = False, returnAttendanceReportRunHistoryID = False, returnBody = False, returnBodyForReport = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFooter = False, returnFooterForReport = False, returnHeader = False, returnHeaderForReport = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentDisciplineThresholdAttendanceReportRunHistory(EntityID = 1, setStudentDisciplineThresholdAttendanceReportRunHistoryID = None, setAttachmentID = None, setAttendanceReportRunHistoryID = None, setBody = None, setBodyForReport = None, setCreatedTime = None, setDisciplineThresholdID = None, setFooter = None, setFooterForReport = None, setHeader = None, setHeaderForReport = None, setIsActive = None, setModifiedTime = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnAttachmentID = False, returnAttendanceReportRunHistoryID = False, returnBody = False, returnBodyForReport = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFooter = False, returnFooterForReport = False, returnHeader = False, returnHeaderForReport = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "delete")


def getEveryStudentInOutTime(searchConditions = [], EntityID = 1, returnStudentInOutTimeID = False, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentInOutTime in the district.

    This function returns a dataframe of every StudentInOutTime in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentInOutTime(StudentInOutTimeID, EntityID = 1, returnStudentInOutTimeID = False, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "get", return_params_list = return_params)

def modifyStudentInOutTime(StudentInOutTimeID, EntityID = 1, setStudentInOutTimeID = None, setCreatedTime = None, setMinutesPresent = None, setModifiedTime = None, setPeriodTimes = None, setStudentAttendanceID = None, setTimeIn = None, setTimeOut = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentInOutTimeID = False, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentInOutTime(EntityID = 1, setStudentInOutTimeID = None, setCreatedTime = None, setMinutesPresent = None, setModifiedTime = None, setPeriodTimes = None, setStudentAttendanceID = None, setTimeIn = None, setTimeOut = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentInOutTimeID = False, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentInOutTime(StudentInOutTimeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "delete")


def getEveryStudentThresholdPeriod(searchConditions = [], EntityID = 1, returnStudentThresholdPeriodID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentThresholdPeriod in the district.

    This function returns a dataframe of every StudentThresholdPeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1, returnStudentThresholdPeriodID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "get", return_params_list = return_params)

def modifyStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1, setStudentThresholdPeriodID = None, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setCountsTowardsThreshold = None, setCreatedTime = None, setDate = None, setModifiedTime = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentDisciplineThresholdAttendanceReportRunHistoryID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentThresholdPeriodID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentThresholdPeriod(EntityID = 1, setStudentThresholdPeriodID = None, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setCountsTowardsThreshold = None, setCreatedTime = None, setDate = None, setModifiedTime = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentDisciplineThresholdAttendanceReportRunHistoryID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentThresholdPeriodID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "delete")


def getEveryTeacherEntry(searchConditions = [], EntityID = 1, returnTeacherEntryID = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TeacherEntry in the district.

    This function returns a dataframe of every TeacherEntry in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTeacherEntry(TeacherEntryID, EntityID = 1, returnTeacherEntryID = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "get", return_params_list = return_params)

def modifyTeacherEntry(TeacherEntryID, EntityID = 1, setTeacherEntryID = None, setBackgroundColor = None, setBackgroundColorHex = None, setBackgroundColorRgba = None, setCreatedTime = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setLabel = None, setModifiedTime = None, setSchoolYearID = None, setTeacherEntryIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherEntryID = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherEntry(EntityID = 1, setTeacherEntryID = None, setBackgroundColor = None, setBackgroundColorHex = None, setBackgroundColorRgba = None, setCreatedTime = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setLabel = None, setModifiedTime = None, setSchoolYearID = None, setTeacherEntryIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherEntryID = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherEntry(TeacherEntryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "delete")


def getEveryTempAffectedCalendarDayRecord(searchConditions = [], EntityID = 1, returnTempAffectedCalendarDayRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAffectedCalendarDayRecord in the district.

    This function returns a dataframe of every TempAffectedCalendarDayRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1, returnTempAffectedCalendarDayRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "get", return_params_list = return_params)

def modifyTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1, setTempAffectedCalendarDayRecordID = None, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setCalendar = None, setCalendarID = None, setComment = None, setCountAs = None, setCreatedTime = None, setDate = None, setDayOfTheWeek = None, setEntity = None, setFailureReason = None, setModifiedTime = None, setNewBellSchedule = None, setNewCountAs = None, setNewDayRotation = None, setNewDayRotationID = None, setNewFundingPeriod = None, setNewFundingPeriodID = None, setNewInstructionalMinutesOverride = None, setNewOperationalMinutesOverride = None, setNewStateCalendarWaiverEventTypeCodeTX = None, setNewStateCalendarWaiverEventTypeCodeTXID = None, setNewStateSchoolDayEventCodeTX = None, setNewStateSchoolDayEventCodeTXID = None, setNewUseInstructionalMinutesOverride = None, setNewUseOperationalMinutesOverride = None, setNewWaiverMinutes = None, setOldBellSchedule = None, setOldDayRotation = None, setOldDayRotationID = None, setOldFundingPeriod = None, setOldFundingPeriodID = None, setOldInstructionalMinutesOverride = None, setOldOperationalMinutesOverride = None, setOldStateCalendarWaiverEventTypeCodeTX = None, setOldStateCalendarWaiverEventTypeCodeTXID = None, setOldStateSchoolDayEventCodeTX = None, setOldStateSchoolDayEventCodeTXID = None, setOldUseInstructionalMinutesOverride = None, setOldUseOperationalMinutesOverride = None, setOldWaiverMinutes = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedCalendarDayRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAffectedCalendarDayRecord(EntityID = 1, setTempAffectedCalendarDayRecordID = None, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setCalendar = None, setCalendarID = None, setComment = None, setCountAs = None, setCreatedTime = None, setDate = None, setDayOfTheWeek = None, setEntity = None, setFailureReason = None, setModifiedTime = None, setNewBellSchedule = None, setNewCountAs = None, setNewDayRotation = None, setNewDayRotationID = None, setNewFundingPeriod = None, setNewFundingPeriodID = None, setNewInstructionalMinutesOverride = None, setNewOperationalMinutesOverride = None, setNewStateCalendarWaiverEventTypeCodeTX = None, setNewStateCalendarWaiverEventTypeCodeTXID = None, setNewStateSchoolDayEventCodeTX = None, setNewStateSchoolDayEventCodeTXID = None, setNewUseInstructionalMinutesOverride = None, setNewUseOperationalMinutesOverride = None, setNewWaiverMinutes = None, setOldBellSchedule = None, setOldDayRotation = None, setOldDayRotationID = None, setOldFundingPeriod = None, setOldFundingPeriodID = None, setOldInstructionalMinutesOverride = None, setOldOperationalMinutesOverride = None, setOldStateCalendarWaiverEventTypeCodeTX = None, setOldStateCalendarWaiverEventTypeCodeTXID = None, setOldStateSchoolDayEventCodeTX = None, setOldStateSchoolDayEventCodeTXID = None, setOldUseInstructionalMinutesOverride = None, setOldUseOperationalMinutesOverride = None, setOldWaiverMinutes = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedCalendarDayRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "delete")


def getEveryTempAffectedStudentAttendancePeriodRecord(searchConditions = [], EntityID = 1, returnTempAffectedStudentAttendancePeriodRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAffectedStudentAttendancePeriodRecord in the district.

    This function returns a dataframe of every TempAffectedStudentAttendancePeriodRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1, returnTempAffectedStudentAttendancePeriodRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "get", return_params_list = return_params)

def modifyTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1, setTempAffectedStudentAttendancePeriodRecordID = None, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setAttendanceCategory = None, setAttendancePeriodID = None, setAttendanceReasonCodeDescription = None, setAttendanceReasonID = None, setAttendanceTypeCodeDescription = None, setAttendanceTypeID = None, setCalendarDayID = None, setCECEAttendancePeriodID = None, setCECEAttendanceReasonID = None, setCECEAttendanceTypeID = None, setComment = None, setCreatedTime = None, setDate = None, setDayRotationCode = None, setEntity = None, setFailureReason = None, setFullName = None, setIsForCECEAttendancePeriod = None, setIsGuardianNotified = None, setModifiedTime = None, setNewStudentSectionCode = None, setNewStudentSectionID = None, setOldStudentSectionCode = None, setOldStudentSectionID = None, setPeriodCode = None, setProcessFromCECEEntity = None, setStudentAttendanceID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedStudentAttendancePeriodRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAffectedStudentAttendancePeriodRecord(EntityID = 1, setTempAffectedStudentAttendancePeriodRecordID = None, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setAttendanceCategory = None, setAttendancePeriodID = None, setAttendanceReasonCodeDescription = None, setAttendanceReasonID = None, setAttendanceTypeCodeDescription = None, setAttendanceTypeID = None, setCalendarDayID = None, setCECEAttendancePeriodID = None, setCECEAttendanceReasonID = None, setCECEAttendanceTypeID = None, setComment = None, setCreatedTime = None, setDate = None, setDayRotationCode = None, setEntity = None, setFailureReason = None, setFullName = None, setIsForCECEAttendancePeriod = None, setIsGuardianNotified = None, setModifiedTime = None, setNewStudentSectionCode = None, setNewStudentSectionID = None, setOldStudentSectionCode = None, setOldStudentSectionID = None, setPeriodCode = None, setProcessFromCECEEntity = None, setStudentAttendanceID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedStudentAttendancePeriodRecordID = False, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "delete")


def getEveryTempAffectedStudentAttendanceRecord(searchConditions = [], EntityID = 1, returnTempAffectedStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAffectedStudentAttendanceRecord in the district.

    This function returns a dataframe of every TempAffectedStudentAttendanceRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1, returnTempAffectedStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "get", return_params_list = return_params)

def modifyTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1, setTempAffectedStudentAttendanceRecordID = None, setAffectedPrimaryKey = None, setCalendarDayID = None, setComment = None, setCreatedTime = None, setDate = None, setDayRotationCode = None, setFailedStudentAttendancePeriods = None, setFailureReason = None, setFullName = None, setIsGuardianNotified = None, setModifiedTime = None, setNewDaysAbsent = None, setNewDaysExcused = None, setNewDaysOther = None, setNewDaysUnexcused = None, setNewGuardianNotified = None, setNewStudentAttendancePeriods = None, setNewTardyCount = None, setOldDaysAbsent = None, setOldDaysExcused = None, setOldDaysOther = None, setOldDaysUnexcused = None, setOldStudentAttendancePeriods = None, setOldTardyCount = None, setPreviousGuardianNotified = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAffectedStudentAttendanceRecord(EntityID = 1, setTempAffectedStudentAttendanceRecordID = None, setAffectedPrimaryKey = None, setCalendarDayID = None, setComment = None, setCreatedTime = None, setDate = None, setDayRotationCode = None, setFailedStudentAttendancePeriods = None, setFailureReason = None, setFullName = None, setIsGuardianNotified = None, setModifiedTime = None, setNewDaysAbsent = None, setNewDaysExcused = None, setNewDaysOther = None, setNewDaysUnexcused = None, setNewGuardianNotified = None, setNewStudentAttendancePeriods = None, setNewTardyCount = None, setOldDaysAbsent = None, setOldDaysExcused = None, setOldDaysOther = None, setOldDaysUnexcused = None, setOldStudentAttendancePeriods = None, setOldTardyCount = None, setPreviousGuardianNotified = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAffectedStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "delete")


def getEveryTempAttendanceTerm(searchConditions = [], EntityID = 1, returnTempAttendanceTermID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarEndDate = False, returnCalendarID = False, returnCalendarStartDate = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAttendanceTerm in the district.

    This function returns a dataframe of every TempAttendanceTerm in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAttendanceTerm(TempAttendanceTermID, EntityID = 1, returnTempAttendanceTermID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarEndDate = False, returnCalendarID = False, returnCalendarStartDate = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "get", return_params_list = return_params)

def modifyTempAttendanceTerm(TempAttendanceTermID, EntityID = 1, setTempAttendanceTermID = None, setAttendanceTermCode = None, setAttendanceTermID = None, setCalendarCode = None, setCalendarEndDate = None, setCalendarID = None, setCalendarStartDate = None, setCreatedTime = None, setEndDate = None, setIsUpdated = None, setModifiedTime = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAttendanceTermID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarEndDate = False, returnCalendarID = False, returnCalendarStartDate = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAttendanceTerm(EntityID = 1, setTempAttendanceTermID = None, setAttendanceTermCode = None, setAttendanceTermID = None, setCalendarCode = None, setCalendarEndDate = None, setCalendarID = None, setCalendarStartDate = None, setCreatedTime = None, setEndDate = None, setIsUpdated = None, setModifiedTime = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAttendanceTermID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarEndDate = False, returnCalendarID = False, returnCalendarStartDate = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAttendanceTerm(TempAttendanceTermID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "delete")


def getEveryTempBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnTempBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnShouldUpdate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempBellScheduleGroupBellSchedule in the district.

    This function returns a dataframe of every TempBellScheduleGroupBellSchedule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempBellScheduleGroupBellSchedule(TempBellScheduleGroupBellScheduleID, EntityID = 1, returnTempBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnShouldUpdate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/" + str(TempBellScheduleGroupBellScheduleID), verb = "get", return_params_list = return_params)

def modifyTempBellScheduleGroupBellSchedule(TempBellScheduleGroupBellScheduleID, EntityID = 1, setTempBellScheduleGroupBellScheduleID = None, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupCodeDescription = None, setBellScheduleGroupID = None, setBellScheduleID = None, setCreatedTime = None, setIsDefault = None, setModifiedTime = None, setShouldUpdate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnShouldUpdate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/" + str(TempBellScheduleGroupBellScheduleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempBellScheduleGroupBellSchedule(EntityID = 1, setTempBellScheduleGroupBellScheduleID = None, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupCodeDescription = None, setBellScheduleGroupID = None, setBellScheduleID = None, setCreatedTime = None, setIsDefault = None, setModifiedTime = None, setShouldUpdate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnShouldUpdate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempBellScheduleGroupBellSchedule(TempBellScheduleGroupBellScheduleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempBellScheduleGroupBellSchedule/" + str(TempBellScheduleGroupBellScheduleID), verb = "delete")


def getEveryTempCalendar(searchConditions = [], EntityID = 1, returnTempCalendarID = False, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnIsDefault = False, returnIsUpdated = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCalendar in the district.

    This function returns a dataframe of every TempCalendar in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCalendar(TempCalendarID, EntityID = 1, returnTempCalendarID = False, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnIsDefault = False, returnIsUpdated = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "get", return_params_list = return_params)

def modifyTempCalendar(TempCalendarID, EntityID = 1, setTempCalendarID = None, setAffectedPrimaryKey = None, setCalendarID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setEndDate = None, setIsDefault = None, setIsUpdated = None, setModifiedTime = None, setNewEndDate = None, setNewStartDate = None, setOldEndDate = None, setOldStartDate = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarID = False, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnIsDefault = False, returnIsUpdated = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalendar(EntityID = 1, setTempCalendarID = None, setAffectedPrimaryKey = None, setCalendarID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setEndDate = None, setIsDefault = None, setIsUpdated = None, setModifiedTime = None, setNewEndDate = None, setNewStartDate = None, setOldEndDate = None, setOldStartDate = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarID = False, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnIsDefault = False, returnIsUpdated = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalendar(TempCalendarID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "delete")


def getEveryTempCalendarAttendanceTerm(searchConditions = [], EntityID = 1, returnTempCalendarAttendanceTermID = False, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCalendarAttendanceTerm in the district.

    This function returns a dataframe of every TempCalendarAttendanceTerm in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1, returnTempCalendarAttendanceTermID = False, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "get", return_params_list = return_params)

def modifyTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1, setTempCalendarAttendanceTermID = None, setAttendanceTermID = None, setCalendarID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setEndDate = None, setModifiedTime = None, setOriginalEndDate = None, setOriginalStartDate = None, setStartDate = None, setTableType = None, setTableTypeCode = None, setTableTypeString = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarAttendanceTermID = False, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalendarAttendanceTerm(EntityID = 1, setTempCalendarAttendanceTermID = None, setAttendanceTermID = None, setCalendarID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setEndDate = None, setModifiedTime = None, setOriginalEndDate = None, setOriginalStartDate = None, setStartDate = None, setTableType = None, setTableTypeCode = None, setTableTypeString = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarAttendanceTermID = False, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "delete")


def getEveryTempCalendarDayBellScheduleGroupBellSchedule(searchConditions = [], EntityID = 1, returnTempCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleDescription = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCalendar = False, returnCalendarDayID = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnExistingBellScheduleCode = False, returnExistingBellScheduleGroupBellScheduleID = False, returnExistingCalendarDayBellScheduleGroupBellScheduleID = False, returnIsDefault = False, returnModifiedTime = False, returnUpdateBellSchedule = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCalendarDayBellScheduleGroupBellSchedule in the district.

    This function returns a dataframe of every TempCalendarDayBellScheduleGroupBellSchedule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCalendarDayBellScheduleGroupBellSchedule(TempCalendarDayBellScheduleGroupBellScheduleID, EntityID = 1, returnTempCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleDescription = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCalendar = False, returnCalendarDayID = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnExistingBellScheduleCode = False, returnExistingBellScheduleGroupBellScheduleID = False, returnExistingCalendarDayBellScheduleGroupBellScheduleID = False, returnIsDefault = False, returnModifiedTime = False, returnUpdateBellSchedule = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/" + str(TempCalendarDayBellScheduleGroupBellScheduleID), verb = "get", return_params_list = return_params)

def modifyTempCalendarDayBellScheduleGroupBellSchedule(TempCalendarDayBellScheduleGroupBellScheduleID, EntityID = 1, setTempCalendarDayBellScheduleGroupBellScheduleID = None, setBellScheduleDescription = None, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupCodeDescription = None, setBellScheduleGroupID = None, setBellScheduleID = None, setCalendar = None, setCalendarDayID = None, setCountAs = None, setCreatedTime = None, setDate = None, setDayRotationCode = None, setExistingBellScheduleCode = None, setExistingBellScheduleGroupBellScheduleID = None, setExistingCalendarDayBellScheduleGroupBellScheduleID = None, setIsDefault = None, setModifiedTime = None, setUpdateBellSchedule = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleDescription = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCalendar = False, returnCalendarDayID = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnExistingBellScheduleCode = False, returnExistingBellScheduleGroupBellScheduleID = False, returnExistingCalendarDayBellScheduleGroupBellScheduleID = False, returnIsDefault = False, returnModifiedTime = False, returnUpdateBellSchedule = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/" + str(TempCalendarDayBellScheduleGroupBellScheduleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalendarDayBellScheduleGroupBellSchedule(EntityID = 1, setTempCalendarDayBellScheduleGroupBellScheduleID = None, setBellScheduleDescription = None, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupCodeDescription = None, setBellScheduleGroupID = None, setBellScheduleID = None, setCalendar = None, setCalendarDayID = None, setCountAs = None, setCreatedTime = None, setDate = None, setDayRotationCode = None, setExistingBellScheduleCode = None, setExistingBellScheduleGroupBellScheduleID = None, setExistingCalendarDayBellScheduleGroupBellScheduleID = None, setIsDefault = None, setModifiedTime = None, setUpdateBellSchedule = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarDayBellScheduleGroupBellScheduleID = False, returnBellScheduleDescription = False, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupCodeDescription = False, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCalendar = False, returnCalendarDayID = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnExistingBellScheduleCode = False, returnExistingBellScheduleGroupBellScheduleID = False, returnExistingCalendarDayBellScheduleGroupBellScheduleID = False, returnIsDefault = False, returnModifiedTime = False, returnUpdateBellSchedule = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalendarDayBellScheduleGroupBellSchedule(TempCalendarDayBellScheduleGroupBellScheduleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayBellScheduleGroupBellSchedule/" + str(TempCalendarDayBellScheduleGroupBellScheduleID), verb = "delete")


def getEveryTempCalendarDayCalendarEventRecord(searchConditions = [], EntityID = 1, returnTempCalendarDayCalendarEventRecordID = False, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCalendarDayCalendarEventRecord in the district.

    This function returns a dataframe of every TempCalendarDayCalendarEventRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1, returnTempCalendarDayCalendarEventRecordID = False, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "get", return_params_list = return_params)

def modifyTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1, setTempCalendarDayCalendarEventRecordID = None, setCalendar = None, setCalendarDayID = None, setCalendarEvent = None, setCalendarEventID = None, setCreatedTime = None, setDate = None, setFailureReason = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarDayCalendarEventRecordID = False, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalendarDayCalendarEventRecord(EntityID = 1, setTempCalendarDayCalendarEventRecordID = None, setCalendar = None, setCalendarDayID = None, setCalendarEvent = None, setCalendarEventID = None, setCreatedTime = None, setDate = None, setFailureReason = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalendarDayCalendarEventRecordID = False, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "delete")


def getEveryTempCloneCalendarError(searchConditions = [], EntityID = 1, returnTempCloneCalendarErrorID = False, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCloneCalendarError in the district.

    This function returns a dataframe of every TempCloneCalendarError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1, returnTempCloneCalendarErrorID = False, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "get", return_params_list = return_params)

def modifyTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1, setTempCloneCalendarErrorID = None, setCreatedTime = None, setDescription = None, setEntityName = None, setFailureReason = None, setModifiedTime = None, setRecordType = None, setRecordTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCloneCalendarErrorID = False, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCloneCalendarError(EntityID = 1, setTempCloneCalendarErrorID = None, setCreatedTime = None, setDescription = None, setEntityName = None, setFailureReason = None, setModifiedTime = None, setRecordType = None, setRecordTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCloneCalendarErrorID = False, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "delete")


def getEveryTempCloneCalendarRecord(searchConditions = [], EntityID = 1, returnTempCloneCalendarRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCloneCalendarRecord in the district.

    This function returns a dataframe of every TempCloneCalendarRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1, returnTempCloneCalendarRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "get", return_params_list = return_params)

def modifyTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1, setTempCloneCalendarRecordID = None, setAffectedPrimaryKey = None, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCode = None, setCreatedTime = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntity = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setModifiedTime = None, setSchoolYearID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZeroDayHighPeriodCount = None, returnTempCloneCalendarRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCloneCalendarRecord(EntityID = 1, setTempCloneCalendarRecordID = None, setAffectedPrimaryKey = None, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCode = None, setCreatedTime = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntity = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setModifiedTime = None, setSchoolYearID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZeroDayHighPeriodCount = None, returnTempCloneCalendarRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "delete")


def getEveryTempStudentAttendanceRecord(searchConditions = [], EntityID = 1, returnTempStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentAttendanceRecord in the district.

    This function returns a dataframe of every TempStudentAttendanceRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1, returnTempStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1, setTempStudentAttendanceRecordID = None, setAffectedPrimaryKey = None, setAttendanceTakenByPeriod = None, setCreatedTime = None, setDate = None, setDayOfTheWeek = None, setDayRotation = None, setDayRotationID = None, setGuardianNotified = None, setModifiedTime = None, setStudentName = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentAttendanceRecord(EntityID = 1, setTempStudentAttendanceRecordID = None, setAffectedPrimaryKey = None, setAttendanceTakenByPeriod = None, setCreatedTime = None, setDate = None, setDayOfTheWeek = None, setDayRotation = None, setDayRotationID = None, setGuardianNotified = None, setModifiedTime = None, setStudentName = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentAttendanceRecordID = False, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "delete")


def getEveryTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(searchConditions = [], EntityID = 1, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNumberOfDays = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord in the district.

    This function returns a dataframe of every TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNumberOfDays = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1, setTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = None, setCountType = None, setCountTypeCode = None, setCreatedTime = None, setDateHigh = None, setDateLow = None, setDateType = None, setDateTypeCode = None, setDayCountType = None, setDayCountTypeCode = None, setDisciplineThresholdID = None, setModifiedTime = None, setNumberOfDays = None, setResetRangeAttendanceTypes = None, setStudentID = None, setStudentName = None, setThresholdValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNumberOfDays = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(EntityID = 1, setTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = None, setCountType = None, setCountTypeCode = None, setCreatedTime = None, setDateHigh = None, setDateLow = None, setDateType = None, setDateTypeCode = None, setDayCountType = None, setDayCountTypeCode = None, setDisciplineThresholdID = None, setModifiedTime = None, setNumberOfDays = None, setResetRangeAttendanceTypes = None, setStudentID = None, setStudentName = None, setThresholdValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnNumberOfDays = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "delete")


def getEveryTempStudentThresholdPeriodRecord(searchConditions = [], EntityID = 1, returnTempStudentThresholdPeriodRecordID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentThresholdPeriodRecord in the district.

    This function returns a dataframe of every TempStudentThresholdPeriodRecord in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1, returnTempStudentThresholdPeriodRecordID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "get", return_params_list = return_params)

def modifyTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1, setTempStudentThresholdPeriodRecordID = None, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setCreatedTime = None, setDate = None, setModifiedTime = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentSectionID = None, setTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentThresholdPeriodRecordID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentThresholdPeriodRecord(EntityID = 1, setTempStudentThresholdPeriodRecordID = None, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setCreatedTime = None, setDate = None, setModifiedTime = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentSectionID = None, setTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentThresholdPeriodRecordID = False, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "delete")


def getEveryThresholdResetRange(searchConditions = [], EntityID = 1, returnThresholdResetRangeID = False, returnAttendanceLettersRan = False, returnAttendanceTypeCodes = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnIsForTardyKiosk = False, returnModifiedTime = False, returnNumberOfDays = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ThresholdResetRange in the district.

    This function returns a dataframe of every ThresholdResetRange in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getThresholdResetRange(ThresholdResetRangeID, EntityID = 1, returnThresholdResetRangeID = False, returnAttendanceLettersRan = False, returnAttendanceTypeCodes = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnIsForTardyKiosk = False, returnModifiedTime = False, returnNumberOfDays = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "get", return_params_list = return_params)

def modifyThresholdResetRange(ThresholdResetRangeID, EntityID = 1, setThresholdResetRangeID = None, setAttendanceLettersRan = None, setAttendanceTypeCodes = None, setCountType = None, setCountTypeCode = None, setCreatedTime = None, setDateDisplay = None, setDateHigh = None, setDateLow = None, setDateType = None, setDateTypeCode = None, setDayCountType = None, setDayCountTypeCode = None, setEntityID = None, setIsForAttendanceLetters = None, setIsForTardyKiosk = None, setModifiedTime = None, setNumberOfDays = None, setNumberPerDay = None, setResetRangeAttendanceTypes = None, setSchoolYearID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThresholdResetRangeID = False, returnAttendanceLettersRan = False, returnAttendanceTypeCodes = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnIsForTardyKiosk = False, returnModifiedTime = False, returnNumberOfDays = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createThresholdResetRange(EntityID = 1, setThresholdResetRangeID = None, setAttendanceLettersRan = None, setAttendanceTypeCodes = None, setCountType = None, setCountTypeCode = None, setCreatedTime = None, setDateDisplay = None, setDateHigh = None, setDateLow = None, setDateType = None, setDateTypeCode = None, setDayCountType = None, setDayCountTypeCode = None, setEntityID = None, setIsForAttendanceLetters = None, setIsForTardyKiosk = None, setModifiedTime = None, setNumberOfDays = None, setNumberPerDay = None, setResetRangeAttendanceTypes = None, setSchoolYearID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThresholdResetRangeID = False, returnAttendanceLettersRan = False, returnAttendanceTypeCodes = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnDateType = False, returnDateTypeCode = False, returnDayCountType = False, returnDayCountTypeCode = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnIsForTardyKiosk = False, returnModifiedTime = False, returnNumberOfDays = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteThresholdResetRange(ThresholdResetRangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "delete")


def getEveryThresholdResetRangeAttendancePeriod(searchConditions = [], EntityID = 1, returnThresholdResetRangeAttendancePeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ThresholdResetRangeAttendancePeriod in the district.

    This function returns a dataframe of every ThresholdResetRangeAttendancePeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1, returnThresholdResetRangeAttendancePeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "get", return_params_list = return_params)

def modifyThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1, setThresholdResetRangeAttendancePeriodID = None, setAttendancePeriodID = None, setCreatedTime = None, setModifiedTime = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThresholdResetRangeAttendancePeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createThresholdResetRangeAttendancePeriod(EntityID = 1, setThresholdResetRangeAttendancePeriodID = None, setAttendancePeriodID = None, setCreatedTime = None, setModifiedTime = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThresholdResetRangeAttendancePeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "delete")


def getEveryThresholdResetRangeAttendanceType(searchConditions = [], EntityID = 1, returnThresholdResetRangeAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ThresholdResetRangeAttendanceType in the district.

    This function returns a dataframe of every ThresholdResetRangeAttendanceType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1, returnThresholdResetRangeAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "get", return_params_list = return_params)

def modifyThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1, setThresholdResetRangeAttendanceTypeID = None, setAttendanceTypeID = None, setCreatedTime = None, setModifiedTime = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThresholdResetRangeAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createThresholdResetRangeAttendanceType(EntityID = 1, setThresholdResetRangeAttendanceTypeID = None, setAttendanceTypeID = None, setCreatedTime = None, setModifiedTime = None, setThresholdResetRangeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThresholdResetRangeAttendanceTypeID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "delete")