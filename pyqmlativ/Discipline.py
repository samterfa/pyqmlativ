# This module contains Discipline functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryActionAttendanceType(searchConditions = [], EntityID = 1, returnActionAttendanceTypeID = False, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ActionAttendanceType in the district.

    This function returns a dataframe of every ActionAttendanceType in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getActionAttendanceType(ActionAttendanceTypeID, EntityID = 1, returnActionAttendanceTypeID = False, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "get", return_params_list = return_params)

def modifyActionAttendanceType(ActionAttendanceTypeID, EntityID = 1, setActionAttendanceTypeID = None, setActionID = None, setAttendanceTypeID = None, setCreatedTime = None, setEntityGroupKey = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActionAttendanceTypeID = False, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createActionAttendanceType(EntityID = 1, setActionAttendanceTypeID = None, setActionID = None, setAttendanceTypeID = None, setCreatedTime = None, setEntityGroupKey = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActionAttendanceTypeID = False, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteActionAttendanceType(ActionAttendanceTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "delete")


def getEveryAction(searchConditions = [], EntityID = 1, returnActionID = False, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Action in the district.

    This function returns a dataframe of every Action in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAction(ActionID, EntityID = 1, returnActionID = False, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "get", return_params_list = return_params)

def modifyAction(ActionID, EntityID = 1, setActionID = None, setActionIDClonedFrom = None, setActionMNID = None, setActionTypeID = None, setCode = None, setCodeDescription = None, setCreateAttendanceForActionDetail = None, setCreatedTime = None, setDefaultDuration = None, setDefaultLocationID = None, setDescription = None, setDistrictID = None, setDurationType = None, setDurationTypeCode = None, setFederalDisciplineCategoryID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setRestraintSeclusion = None, setRestraintSeclusionCode = None, setSchoolYearID = None, setStateActionTypeMNID = None, setSuppressCreationOfActionDetails = None, setTransferToAlternativeSchool = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActionID = False, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAction(EntityID = 1, setActionID = None, setActionIDClonedFrom = None, setActionMNID = None, setActionTypeID = None, setCode = None, setCodeDescription = None, setCreateAttendanceForActionDetail = None, setCreatedTime = None, setDefaultDuration = None, setDefaultLocationID = None, setDescription = None, setDistrictID = None, setDurationType = None, setDurationTypeCode = None, setFederalDisciplineCategoryID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setRestraintSeclusion = None, setRestraintSeclusionCode = None, setSchoolYearID = None, setStateActionTypeMNID = None, setSuppressCreationOfActionDetails = None, setTransferToAlternativeSchool = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnActionID = False, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAction(ActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "delete")


def getEveryActionType(searchConditions = [], EntityID = 1, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ActionType in the district.

    This function returns a dataframe of every ActionType in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getActionType(ActionTypeID, EntityID = 1, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "get", return_params_list = return_params)

def modifyActionType(ActionTypeID, EntityID = 1, setActionTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setIsInvalid = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValidYearHigh = None, setValidYearLow = None, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createActionType(EntityID = 1, setActionTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setIsInvalid = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValidYearHigh = None, setValidYearLow = None, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteActionType(ActionTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "delete")


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowInternalComments = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionStatus = False, returnDefaultActionStatusCode = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultGuardianNotifiedOnActionDetailFromAction = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = False, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowInternalComments = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionStatus = False, returnDefaultActionStatusCode = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultGuardianNotifiedOnActionDetailFromAction = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearID = None, setAllowActionRecommendationsOnReferrals = None, setAllowActionTypeUpdate = None, setAllowDurationTypeUpdate = None, setAllowInternalComments = None, setAllowOnlyOneOffensePerIncident = None, setAllowUseOfWarning = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = None, setDefaultActionStatus = None, setDefaultActionStatusCode = None, setDefaultActionValueFromPreviousPerson = None, setDefaultDisciplineScreenDateAndTimes = None, setDefaultGuardianNotifiedOnActionDetailFromAction = None, setDefaultOffenseValueFromPreviousPerson = None, setDisplayInvolvedPersonsFromAllEntities = None, setDisplayStudentOffensesForAllEntities = None, setDisplayWarningsInFamilyAndStudentAccess = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setRestartIncidentNumberThisYear = None, setSchoolYearID = None, setUseIncidentBuildingAndRoom = None, setUsePerceivedMotivation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowInternalComments = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionStatus = False, returnDefaultActionStatusCode = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultGuardianNotifiedOnActionDetailFromAction = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearID = None, setAllowActionRecommendationsOnReferrals = None, setAllowActionTypeUpdate = None, setAllowDurationTypeUpdate = None, setAllowInternalComments = None, setAllowOnlyOneOffensePerIncident = None, setAllowUseOfWarning = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = None, setDefaultActionStatus = None, setDefaultActionStatusCode = None, setDefaultActionValueFromPreviousPerson = None, setDefaultDisciplineScreenDateAndTimes = None, setDefaultGuardianNotifiedOnActionDetailFromAction = None, setDefaultOffenseValueFromPreviousPerson = None, setDisplayInvolvedPersonsFromAllEntities = None, setDisplayStudentOffensesForAllEntities = None, setDisplayWarningsInFamilyAndStudentAccess = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setRestartIncidentNumberThisYear = None, setSchoolYearID = None, setUseIncidentBuildingAndRoom = None, setUsePerceivedMotivation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowInternalComments = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionStatus = False, returnDefaultActionStatusCode = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultGuardianNotifiedOnActionDetailFromAction = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = False, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setConfigEntityGroupYearID = None, setActionStatusDefaultValue = None, setActionStatusDefaultValueCode = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setDefaultActionStatusCode = None, setDetentionsOnFri = None, setDetentionsOnMon = None, setDetentionsOnSat = None, setDetentionsOnSun = None, setDetentionsOnThu = None, setDetentionsOnTue = None, setDetentionsOnWed = None, setEntityGroupKey = None, setEntityID = None, setExpulsionsOnFri = None, setExpulsionsOnMon = None, setExpulsionsOnSat = None, setExpulsionsOnSun = None, setExpulsionsOnThu = None, setExpulsionsOnTue = None, setExpulsionsOnWed = None, setIncludeDisciplinaryActionAndDetailsOnLetter = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setInSchoolSuspensionsOnFri = None, setInSchoolSuspensionsOnMon = None, setInSchoolSuspensionsOnSat = None, setInSchoolSuspensionsOnSun = None, setInSchoolSuspensionsOnThu = None, setInSchoolSuspensionsOnTue = None, setInSchoolSuspensionsOnWed = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setOutOfSchoolSuspensionsOnFri = None, setOutOfSchoolSuspensionsOnMon = None, setOutOfSchoolSuspensionsOnSat = None, setOutOfSchoolSuspensionsOnSun = None, setOutOfSchoolSuspensionsOnThu = None, setOutOfSchoolSuspensionsOnTue = None, setOutOfSchoolSuspensionsOnWed = None, setSchoolYearID = None, setTardyKioskDisciplineSlipTitle = None, setUseAlternateActionDetails = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setConfigEntityGroupYearID = None, setActionStatusDefaultValue = None, setActionStatusDefaultValueCode = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setDefaultActionStatusCode = None, setDetentionsOnFri = None, setDetentionsOnMon = None, setDetentionsOnSat = None, setDetentionsOnSun = None, setDetentionsOnThu = None, setDetentionsOnTue = None, setDetentionsOnWed = None, setEntityGroupKey = None, setEntityID = None, setExpulsionsOnFri = None, setExpulsionsOnMon = None, setExpulsionsOnSat = None, setExpulsionsOnSun = None, setExpulsionsOnThu = None, setExpulsionsOnTue = None, setExpulsionsOnWed = None, setIncludeDisciplinaryActionAndDetailsOnLetter = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setInSchoolSuspensionsOnFri = None, setInSchoolSuspensionsOnMon = None, setInSchoolSuspensionsOnSat = None, setInSchoolSuspensionsOnSun = None, setInSchoolSuspensionsOnThu = None, setInSchoolSuspensionsOnTue = None, setInSchoolSuspensionsOnWed = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setOutOfSchoolSuspensionsOnFri = None, setOutOfSchoolSuspensionsOnMon = None, setOutOfSchoolSuspensionsOnSat = None, setOutOfSchoolSuspensionsOnSun = None, setOutOfSchoolSuspensionsOnThu = None, setOutOfSchoolSuspensionsOnTue = None, setOutOfSchoolSuspensionsOnWed = None, setSchoolYearID = None, setTardyKioskDisciplineSlipTitle = None, setUseAlternateActionDetails = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")


def getEveryConfigEntityYear(searchConditions = [], EntityID = 1, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigEntityYear in the district.

    This function returns a dataframe of every ConfigEntityYear in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityYear(ConfigEntityYearID, EntityID = 1, setConfigEntityYearID = None, setConfigEntityYearIDClonedFrom = None, setCreatedTime = None, setEntityID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityYear(EntityID = 1, setConfigEntityYearID = None, setConfigEntityYearIDClonedFrom = None, setCreatedTime = None, setEntityID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAllowIncidentSuppression = False, returnAllowUpdateHistoricalData = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnAllowIncidentSuppression = False, returnAllowUpdateHistoricalData = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setAllowIncidentSuppression = None, setAllowUpdateHistoricalData = None, setCreatedTime = None, setModifiedTime = None, setReportIDDisciplineLetter = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAllowIncidentSuppression = False, returnAllowUpdateHistoricalData = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setAllowIncidentSuppression = None, setAllowUpdateHistoricalData = None, setCreatedTime = None, setModifiedTime = None, setReportIDDisciplineLetter = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnAllowIncidentSuppression = False, returnAllowUpdateHistoricalData = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryDisciplineLetterRunHistory(searchConditions = [], EntityID = 1, returnDisciplineLetterRunHistoryID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineLetterRunHistory in the district.

    This function returns a dataframe of every DisciplineLetterRunHistory in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1, returnDisciplineLetterRunHistoryID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "get", return_params_list = return_params)

def modifyDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1, setDisciplineLetterRunHistoryID = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCreatedTime = None, setDate = None, setDisciplineLetterTemplateID = None, setEndDate = None, setEntityID = None, setEntityIDList = None, setFilterType = None, setFilterTypeCode = None, setFiscalYearID = None, setGracePeriod = None, setIncidentType = None, setIncidentTypeCode = None, setIsActive = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setParameterData = None, setParameterDescription = None, setReportRunInfoID = None, setRunDescription = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterRunHistoryID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineLetterRunHistory(EntityID = 1, setDisciplineLetterRunHistoryID = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCreatedTime = None, setDate = None, setDisciplineLetterTemplateID = None, setEndDate = None, setEntityID = None, setEntityIDList = None, setFilterType = None, setFilterTypeCode = None, setFiscalYearID = None, setGracePeriod = None, setIncidentType = None, setIncidentTypeCode = None, setIsActive = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setParameterData = None, setParameterDescription = None, setReportRunInfoID = None, setRunDescription = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterRunHistoryID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnEntityIDList = False, returnFilterType = False, returnFilterTypeCode = False, returnFiscalYearID = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "delete")


def getEveryDisciplineLetterRunHistoryAction(searchConditions = [], EntityID = 1, returnDisciplineLetterRunHistoryActionID = False, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineLetterRunHistoryAction in the district.

    This function returns a dataframe of every DisciplineLetterRunHistoryAction in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1, returnDisciplineLetterRunHistoryActionID = False, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "get", return_params_list = return_params)

def modifyDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1, setDisciplineLetterRunHistoryActionID = None, setActionID = None, setCreatedTime = None, setDisciplineLetterRunHistoryID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterRunHistoryActionID = False, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineLetterRunHistoryAction(EntityID = 1, setDisciplineLetterRunHistoryActionID = None, setActionID = None, setCreatedTime = None, setDisciplineLetterRunHistoryID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterRunHistoryActionID = False, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "delete")


def getEveryDisciplineLetterRunHistoryOffense(searchConditions = [], EntityID = 1, returnDisciplineLetterRunHistoryOffenseID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineLetterRunHistoryOffense in the district.

    This function returns a dataframe of every DisciplineLetterRunHistoryOffense in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1, returnDisciplineLetterRunHistoryOffenseID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "get", return_params_list = return_params)

def modifyDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1, setDisciplineLetterRunHistoryOffenseID = None, setCreatedTime = None, setDisciplineLetterRunHistoryID = None, setModifiedTime = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterRunHistoryOffenseID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineLetterRunHistoryOffense(EntityID = 1, setDisciplineLetterRunHistoryOffenseID = None, setCreatedTime = None, setDisciplineLetterRunHistoryID = None, setModifiedTime = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterRunHistoryOffenseID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "delete")


def getEveryDisciplineLetterTemplate(searchConditions = [], EntityID = 1, returnDisciplineLetterTemplateID = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnIsReadOnlyHistoricalRecord = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineLetterTemplate in the district.

    This function returns a dataframe of every DisciplineLetterTemplate in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1, returnDisciplineLetterTemplateID = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnIsReadOnlyHistoricalRecord = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "get", return_params_list = return_params)

def modifyDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1, setDisciplineLetterTemplateID = None, setAdvisorNameFormat = None, setAdvisorNameFormatCode = None, setBody = None, setColumnHeaderLabel1 = None, setColumnHeaderLabel10 = None, setColumnHeaderLabel2 = None, setColumnHeaderLabel3 = None, setColumnHeaderLabel4 = None, setColumnHeaderLabel5 = None, setColumnHeaderLabel6 = None, setColumnHeaderLabel7 = None, setColumnHeaderLabel8 = None, setColumnHeaderLabel9 = None, setCreatedTime = None, setDescription = None, setDisciplineLetterTemplateIDClonedFrom = None, setDistrictID = None, setFooter = None, setForCurrentEntity = None, setGuardianNameFormat = None, setGuardianNameFormatCode = None, setHasLogo = None, setHeader = None, setIsDefault = None, setIsReadOnlyHistoricalRecord = None, setMediaIDLogo = None, setModifiedTime = None, setPrintSingleColumn1 = None, setPrintSingleColumn10 = None, setPrintSingleColumn2 = None, setPrintSingleColumn3 = None, setPrintSingleColumn4 = None, setPrintSingleColumn5 = None, setPrintSingleColumn6 = None, setPrintSingleColumn7 = None, setPrintSingleColumn8 = None, setPrintSingleColumn9 = None, setSchoolYearID = None, setStudentNameFormat = None, setStudentNameFormatCode = None, setSuperintendentNameFormat = None, setSuperintendentNameFormatCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateID = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnIsReadOnlyHistoricalRecord = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineLetterTemplate(EntityID = 1, setDisciplineLetterTemplateID = None, setAdvisorNameFormat = None, setAdvisorNameFormatCode = None, setBody = None, setColumnHeaderLabel1 = None, setColumnHeaderLabel10 = None, setColumnHeaderLabel2 = None, setColumnHeaderLabel3 = None, setColumnHeaderLabel4 = None, setColumnHeaderLabel5 = None, setColumnHeaderLabel6 = None, setColumnHeaderLabel7 = None, setColumnHeaderLabel8 = None, setColumnHeaderLabel9 = None, setCreatedTime = None, setDescription = None, setDisciplineLetterTemplateIDClonedFrom = None, setDistrictID = None, setFooter = None, setForCurrentEntity = None, setGuardianNameFormat = None, setGuardianNameFormatCode = None, setHasLogo = None, setHeader = None, setIsDefault = None, setIsReadOnlyHistoricalRecord = None, setMediaIDLogo = None, setModifiedTime = None, setPrintSingleColumn1 = None, setPrintSingleColumn10 = None, setPrintSingleColumn2 = None, setPrintSingleColumn3 = None, setPrintSingleColumn4 = None, setPrintSingleColumn5 = None, setPrintSingleColumn6 = None, setPrintSingleColumn7 = None, setPrintSingleColumn8 = None, setPrintSingleColumn9 = None, setSchoolYearID = None, setStudentNameFormat = None, setStudentNameFormatCode = None, setSuperintendentNameFormat = None, setSuperintendentNameFormatCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateID = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnIsReadOnlyHistoricalRecord = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "delete")


def getEveryDisciplineLetterTemplateEntity(searchConditions = [], EntityID = 1, returnDisciplineLetterTemplateEntityID = False, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineLetterTemplateEntity in the district.

    This function returns a dataframe of every DisciplineLetterTemplateEntity in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1, returnDisciplineLetterTemplateEntityID = False, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "get", return_params_list = return_params)

def modifyDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1, setDisciplineLetterTemplateEntityID = None, setCreatedTime = None, setDisciplineLetterTemplateID = None, setEntityID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateEntityID = False, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineLetterTemplateEntity(EntityID = 1, setDisciplineLetterTemplateEntityID = None, setCreatedTime = None, setDisciplineLetterTemplateID = None, setEntityID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateEntityID = False, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "delete")


def getEveryDisciplineLetterTemplateHeaderColumn(searchConditions = [], EntityID = 1, returnDisciplineLetterTemplateHeaderColumnID = False, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineLetterTemplateHeaderColumn in the district.

    This function returns a dataframe of every DisciplineLetterTemplateHeaderColumn in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1, returnDisciplineLetterTemplateHeaderColumnID = False, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "get", return_params_list = return_params)

def modifyDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1, setDisciplineLetterTemplateHeaderColumnID = None, setColumnNumber = None, setCreatedTime = None, setDisciplineLetterTemplateHeaderColumnIDClonedFrom = None, setDisciplineLetterTemplateHeaderRowID = None, setFieldType = None, setFieldTypeCode = None, setFreeformText = None, setLabelOverride = None, setModifiedTime = None, setSortNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateHeaderColumnID = False, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineLetterTemplateHeaderColumn(EntityID = 1, setDisciplineLetterTemplateHeaderColumnID = None, setColumnNumber = None, setCreatedTime = None, setDisciplineLetterTemplateHeaderColumnIDClonedFrom = None, setDisciplineLetterTemplateHeaderRowID = None, setFieldType = None, setFieldTypeCode = None, setFreeformText = None, setLabelOverride = None, setModifiedTime = None, setSortNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateHeaderColumnID = False, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "delete")


def getEveryDisciplineLetterTemplateHeaderRow(searchConditions = [], EntityID = 1, returnDisciplineLetterTemplateHeaderRowID = False, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DisciplineLetterTemplateHeaderRow in the district.

    This function returns a dataframe of every DisciplineLetterTemplateHeaderRow in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1, returnDisciplineLetterTemplateHeaderRowID = False, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "get", return_params_list = return_params)

def modifyDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1, setDisciplineLetterTemplateHeaderRowID = None, setColumnCount = None, setCreatedTime = None, setDisciplineLetterTemplateHeaderRowIDClonedFrom = None, setDisciplineLetterTemplateID = None, setModifiedTime = None, setSortNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateHeaderRowID = False, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDisciplineLetterTemplateHeaderRow(EntityID = 1, setDisciplineLetterTemplateHeaderRowID = None, setColumnCount = None, setCreatedTime = None, setDisciplineLetterTemplateHeaderRowIDClonedFrom = None, setDisciplineLetterTemplateID = None, setModifiedTime = None, setSortNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDisciplineLetterTemplateHeaderRowID = False, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "delete")


def getEveryDrug(searchConditions = [], EntityID = 1, returnDrugID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Drug in the district.

    This function returns a dataframe of every Drug in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDrug(DrugID, EntityID = 1, returnDrugID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "get", return_params_list = return_params)

def modifyDrug(DrugID, EntityID = 1, setDrugID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setDrugIDClonedFrom = None, setDrugMNID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSchoolYearID = None, setStateDrugTypeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDrugID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDrug(EntityID = 1, setDrugID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setDrugIDClonedFrom = None, setDrugMNID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSchoolYearID = None, setStateDrugTypeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDrugID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDrug(DrugID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "delete")


def getEveryIncident(searchConditions = [], EntityID = 1, returnIncidentID = False, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Incident in the district.

    This function returns a dataframe of every Incident in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncident(IncidentID, EntityID = 1, returnIncidentID = False, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "get", return_params_list = return_params)

def modifyIncident(IncidentID, EntityID = 1, setIncidentID = None, setActionIDRecommended = None, setBuildingID = None, setCreatedTime = None, setDamageCost = None, setDateTime = None, setDateTimeDate = None, setDateTimeTime = None, setDescription = None, setDistrictID = None, setEntityID = None, setHasActions = None, setHasActionsForOffenders = None, setHasDrugs = None, setHasOpenActions = None, setHasOverdueActionDetails = None, setHasWeapons = None, setIncidentMNID = None, setIncidentNumber = None, setIncidentNumberValue = None, setIsIncidentOrWarning = None, setIsReadOnlyHistoricalRecord = None, setIsReferralOrWarning = None, setIsSuppressed = None, setLocationID = None, setModifiedTime = None, setNumberOfNonEnrolledOffenders = None, setNumberOfNonEnrolledVictims = None, setReferredByFreeformName = None, setReferredByName = None, setReferredByNameID = None, setReferredByType = None, setReferredByTypeCode = None, setReportedToLawEnforcement = None, setRoomID = None, setSchoolYearID = None, setStateDIRSTimeMNID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentID = False, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncident(EntityID = 1, setIncidentID = None, setActionIDRecommended = None, setBuildingID = None, setCreatedTime = None, setDamageCost = None, setDateTime = None, setDateTimeDate = None, setDateTimeTime = None, setDescription = None, setDistrictID = None, setEntityID = None, setHasActions = None, setHasActionsForOffenders = None, setHasDrugs = None, setHasOpenActions = None, setHasOverdueActionDetails = None, setHasWeapons = None, setIncidentMNID = None, setIncidentNumber = None, setIncidentNumberValue = None, setIsIncidentOrWarning = None, setIsReadOnlyHistoricalRecord = None, setIsReferralOrWarning = None, setIsSuppressed = None, setLocationID = None, setModifiedTime = None, setNumberOfNonEnrolledOffenders = None, setNumberOfNonEnrolledVictims = None, setReferredByFreeformName = None, setReferredByName = None, setReferredByNameID = None, setReferredByType = None, setReferredByTypeCode = None, setReportedToLawEnforcement = None, setRoomID = None, setSchoolYearID = None, setStateDIRSTimeMNID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentID = False, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncident(IncidentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "delete")


def getEveryIncidentOffense(searchConditions = [], EntityID = 1, returnIncidentOffenseID = False, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffense in the district.

    This function returns a dataframe of every IncidentOffense in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffense(IncidentOffenseID, EntityID = 1, returnIncidentOffenseID = False, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "get", return_params_list = return_params)

def modifyIncidentOffense(IncidentOffenseID, EntityID = 1, setIncidentOffenseID = None, setCreatedTime = None, setHasActions = None, setHasDrugs = None, setHasWeapons = None, setIncidentID = None, setIsPrimaryOffense = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseID = False, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffense(EntityID = 1, setIncidentOffenseID = None, setCreatedTime = None, setHasActions = None, setHasDrugs = None, setHasWeapons = None, setIncidentID = None, setIsPrimaryOffense = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseID = False, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffense(IncidentOffenseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "delete")


def getEveryIncidentOffenseNameActionDetail(searchConditions = [], EntityID = 1, returnIncidentOffenseNameActionDetailID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnInternalComment = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffenseNameActionDetail in the district.

    This function returns a dataframe of every IncidentOffenseNameActionDetail in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1, returnIncidentOffenseNameActionDetailID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnInternalComment = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "get", return_params_list = return_params)

def modifyIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1, setIncidentOffenseNameActionDetailID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationServed = None, setDurationServedWithLabel = None, setDurationToServe = None, setDurationToServeWithLabel = None, setIncidentOffenseNameActionID = None, setInternalComment = None, setIsAlternate = None, setIsGuardianNotified = None, setIsReadOnlyHistoricalRecord = None, setLastAlternate = None, setLocationID = None, setModifiedTime = None, setOverdue = None, setPartialDayPeriods = None, setPrintComment = None, setRenderReissueOption = None, setRoomID = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameActionDetailID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnInternalComment = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffenseNameActionDetail(EntityID = 1, setIncidentOffenseNameActionDetailID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationServed = None, setDurationServedWithLabel = None, setDurationToServe = None, setDurationToServeWithLabel = None, setIncidentOffenseNameActionID = None, setInternalComment = None, setIsAlternate = None, setIsGuardianNotified = None, setIsReadOnlyHistoricalRecord = None, setLastAlternate = None, setLocationID = None, setModifiedTime = None, setOverdue = None, setPartialDayPeriods = None, setPrintComment = None, setRenderReissueOption = None, setRoomID = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameActionDetailID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnInternalComment = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "delete")


def getEveryIncidentOffenseNameActionDetailPeriod(searchConditions = [], EntityID = 1, returnIncidentOffenseNameActionDetailPeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffenseNameActionDetailPeriod in the district.

    This function returns a dataframe of every IncidentOffenseNameActionDetailPeriod in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1, returnIncidentOffenseNameActionDetailPeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "get", return_params_list = return_params)

def modifyIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1, setIncidentOffenseNameActionDetailPeriodID = None, setAttendancePeriodID = None, setCreatedTime = None, setIncidentOffenseNameActionDetailID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameActionDetailPeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffenseNameActionDetailPeriod(EntityID = 1, setIncidentOffenseNameActionDetailPeriodID = None, setAttendancePeriodID = None, setCreatedTime = None, setIncidentOffenseNameActionDetailID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameActionDetailPeriodID = False, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "delete")


def getEveryIncidentOffenseNameAction(searchConditions = [], EntityID = 1, returnIncidentOffenseNameActionID = False, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnInternalComment = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffenseNameAction in the district.

    This function returns a dataframe of every IncidentOffenseNameAction in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1, returnIncidentOffenseNameActionID = False, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnInternalComment = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "get", return_params_list = return_params)

def modifyIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1, setIncidentOffenseNameActionID = None, setActionID = None, setActionTypeID = None, setActualDurationServed = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationServed = None, setDurationServedOverride = None, setDurationToServe = None, setDurationToServeWithLabel = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setFirstActionDetailDateNorthEastExport = None, setIncidentOffenseNameActionMNID = None, setIncidentOffenseNameID = None, setInternalComment = None, setIsGuardianNotified = None, setIsReadOnlyHistoricalRecord = None, setLastActionDetailDateNorthEastExport = None, setLocationID = None, setModifiedTime = None, setOrderedDate = None, setOrderedDateAge = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStartTimeDate = None, setStartTimeTime = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setTotalDurationServed = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameActionID = False, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnInternalComment = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffenseNameAction(EntityID = 1, setIncidentOffenseNameActionID = None, setActionID = None, setActionTypeID = None, setActualDurationServed = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationServed = None, setDurationServedOverride = None, setDurationToServe = None, setDurationToServeWithLabel = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setFirstActionDetailDateNorthEastExport = None, setIncidentOffenseNameActionMNID = None, setIncidentOffenseNameID = None, setInternalComment = None, setIsGuardianNotified = None, setIsReadOnlyHistoricalRecord = None, setLastActionDetailDateNorthEastExport = None, setLocationID = None, setModifiedTime = None, setOrderedDate = None, setOrderedDateAge = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStartTimeDate = None, setStartTimeTime = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setTotalDurationServed = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameActionID = False, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnInternalComment = False, returnIsGuardianNotified = False, returnIsReadOnlyHistoricalRecord = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "delete")


def getEveryIncidentOffenseNameDrug(searchConditions = [], EntityID = 1, returnIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffenseNameDrug in the district.

    This function returns a dataframe of every IncidentOffenseNameDrug in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1, returnIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "get", return_params_list = return_params)

def modifyIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1, setIncidentOffenseNameDrugID = None, setCreatedTime = None, setDrugID = None, setIncidentOffenseNameID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffenseNameDrug(EntityID = 1, setIncidentOffenseNameDrugID = None, setCreatedTime = None, setDrugID = None, setIncidentOffenseNameID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "delete")


def getEveryIncidentOffenseName(searchConditions = [], EntityID = 1, returnIncidentOffenseNameID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsReadOnlyHistoricalRecord = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffenseName in the district.

    This function returns a dataframe of every IncidentOffenseName in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffenseName(IncidentOffenseNameID, EntityID = 1, returnIncidentOffenseNameID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsReadOnlyHistoricalRecord = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "get", return_params_list = return_params)

def modifyIncidentOffenseName(IncidentOffenseNameID, EntityID = 1, setIncidentOffenseNameID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setDisciplineThresholdID = None, setFirstDrugCodeforNorthEastExport = None, setFreeformName = None, setHasActions = None, setHasDangerousWeapons = None, setHasDrugs = None, setHasOpenActions = None, setHasOverdueActionDetails = None, setHasWeapons = None, setIncidentOffenseID = None, setIncidentOffenseNameMNID = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsGuardianNotified = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setIsReadOnlyHistoricalRecord = None, setIsStudentOffender = None, setModifiedTime = None, setNameID = None, setNorthEastExportAttendancePeriods = None, setNorthEastExportOffenseCodes = None, setOffenderArrestedByLawEnforcement = None, setOffenseLevelID = None, setPerceivedMotivationID = None, setPersonalName = None, setReportedToLawEnforcement = None, setStaffIDDisciplineOfficer = None, setStatement = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWasSeriousBodilyInjury = None, returnIncidentOffenseNameID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsReadOnlyHistoricalRecord = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffenseName(EntityID = 1, setIncidentOffenseNameID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setDisciplineThresholdID = None, setFirstDrugCodeforNorthEastExport = None, setFreeformName = None, setHasActions = None, setHasDangerousWeapons = None, setHasDrugs = None, setHasOpenActions = None, setHasOverdueActionDetails = None, setHasWeapons = None, setIncidentOffenseID = None, setIncidentOffenseNameMNID = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsGuardianNotified = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setIsReadOnlyHistoricalRecord = None, setIsStudentOffender = None, setModifiedTime = None, setNameID = None, setNorthEastExportAttendancePeriods = None, setNorthEastExportOffenseCodes = None, setOffenderArrestedByLawEnforcement = None, setOffenseLevelID = None, setPerceivedMotivationID = None, setPersonalName = None, setReportedToLawEnforcement = None, setStaffIDDisciplineOfficer = None, setStatement = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWasSeriousBodilyInjury = None, returnIncidentOffenseNameID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsReadOnlyHistoricalRecord = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffenseName(IncidentOffenseNameID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "delete")


def getEveryIncidentOffenseNameReportRunHistory(searchConditions = [], EntityID = 1, returnIncidentOffenseNameReportRunHistoryID = False, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffenseNameReportRunHistory in the district.

    This function returns a dataframe of every IncidentOffenseNameReportRunHistory in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1, returnIncidentOffenseNameReportRunHistoryID = False, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "get", return_params_list = return_params)

def modifyIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1, setIncidentOffenseNameReportRunHistoryID = None, setAttachmentID = None, setColumnHeaderData1 = None, setColumnHeaderData10 = None, setColumnHeaderData2 = None, setColumnHeaderData3 = None, setColumnHeaderData4 = None, setColumnHeaderData5 = None, setColumnHeaderData6 = None, setColumnHeaderData7 = None, setColumnHeaderData8 = None, setColumnHeaderData9 = None, setCreatedTime = None, setDisciplineLetterRunHistoryID = None, setIncidentOffenseNameID = None, setIsActive = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setStudentID = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameReportRunHistoryID = False, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffenseNameReportRunHistory(EntityID = 1, setIncidentOffenseNameReportRunHistoryID = None, setAttachmentID = None, setColumnHeaderData1 = None, setColumnHeaderData10 = None, setColumnHeaderData2 = None, setColumnHeaderData3 = None, setColumnHeaderData4 = None, setColumnHeaderData5 = None, setColumnHeaderData6 = None, setColumnHeaderData7 = None, setColumnHeaderData8 = None, setColumnHeaderData9 = None, setCreatedTime = None, setDisciplineLetterRunHistoryID = None, setIncidentOffenseNameID = None, setIsActive = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setStudentID = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnIncidentOffenseNameReportRunHistoryID = False, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "delete")


def getEveryIncidentOffenseNameWeapon(searchConditions = [], EntityID = 1, returnIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnIsReadOnlyHistoricalRecord = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IncidentOffenseNameWeapon in the district.

    This function returns a dataframe of every IncidentOffenseNameWeapon in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1, returnIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnIsReadOnlyHistoricalRecord = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "get", return_params_list = return_params)

def modifyIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1, setIncidentOffenseNameWeaponID = None, setCreatedTime = None, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setIncidentOffenseNameID = None, setIncidentOffenseNameWeaponMNID = None, setIsReadOnlyHistoricalRecord = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponCount = None, setWeaponID = None, returnIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnIsReadOnlyHistoricalRecord = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIncidentOffenseNameWeapon(EntityID = 1, setIncidentOffenseNameWeaponID = None, setCreatedTime = None, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setIncidentOffenseNameID = None, setIncidentOffenseNameWeaponMNID = None, setIsReadOnlyHistoricalRecord = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponCount = None, setWeaponID = None, returnIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnIsReadOnlyHistoricalRecord = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "delete")


def getEveryLocation(searchConditions = [], EntityID = 1, returnLocationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Location in the district.

    This function returns a dataframe of every Location in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLocation(LocationID, EntityID = 1, returnLocationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "get", return_params_list = return_params)

def modifyLocation(LocationID, EntityID = 1, setLocationID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEdFiIncidentLocationID = None, setLocationMNID = None, setModifiedTime = None, setStateIncidentLocationMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLocationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLocation(EntityID = 1, setLocationID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEdFiIncidentLocationID = None, setLocationMNID = None, setModifiedTime = None, setStateIncidentLocationMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLocationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLocation(LocationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "delete")


def getEveryNextIncidentNumber(searchConditions = [], EntityID = 1, returnNextIncidentNumberID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NextIncidentNumber in the district.

    This function returns a dataframe of every NextIncidentNumber in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNextIncidentNumber(NextIncidentNumberID, EntityID = 1, returnNextIncidentNumberID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "get", return_params_list = return_params)

def modifyNextIncidentNumber(NextIncidentNumberID, EntityID = 1, setNextIncidentNumberID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setSequenceNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNextIncidentNumberID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNextIncidentNumber(EntityID = 1, setNextIncidentNumberID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setSequenceNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNextIncidentNumberID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNextIncidentNumber(NextIncidentNumberID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "delete")


def getEveryOffense(searchConditions = [], EntityID = 1, returnOffenseID = False, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsReadOnlyHistoricalRecord = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Offense in the district.

    This function returns a dataframe of every Offense in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOffense(OffenseID, EntityID = 1, returnOffenseID = False, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsReadOnlyHistoricalRecord = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "get", return_params_list = return_params)

def modifyOffense(OffenseID, EntityID = 1, setOffenseID = None, setAllowActionRecommendations = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDefaultActionID = None, setDescription = None, setDistrictID = None, setFederalOffenseCategoryID = None, setHarassmentBullying = None, setHarassmentBullyingCode = None, setIsDrugRelated = None, setIsInjuryThreat = None, setIsReadOnlyHistoricalRecord = None, setIsWeaponRelated = None, setModifiedTime = None, setOffenseIDClonedFrom = None, setOffenseLevelIDDefault = None, setRestrictActions = None, setSchoolYearID = None, setUseForReferral = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOffenseID = False, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsReadOnlyHistoricalRecord = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOffense(EntityID = 1, setOffenseID = None, setAllowActionRecommendations = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDefaultActionID = None, setDescription = None, setDistrictID = None, setFederalOffenseCategoryID = None, setHarassmentBullying = None, setHarassmentBullyingCode = None, setIsDrugRelated = None, setIsInjuryThreat = None, setIsReadOnlyHistoricalRecord = None, setIsWeaponRelated = None, setModifiedTime = None, setOffenseIDClonedFrom = None, setOffenseLevelIDDefault = None, setRestrictActions = None, setSchoolYearID = None, setUseForReferral = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOffenseID = False, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsReadOnlyHistoricalRecord = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOffense(OffenseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "delete")


def getEveryOffenseAction(searchConditions = [], EntityID = 1, returnOffenseActionID = False, returnActionID = False, returnCreatedTime = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OffenseAction in the district.

    This function returns a dataframe of every OffenseAction in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOffenseAction(OffenseActionID, EntityID = 1, returnOffenseActionID = False, returnActionID = False, returnCreatedTime = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "get", return_params_list = return_params)

def modifyOffenseAction(OffenseActionID, EntityID = 1, setOffenseActionID = None, setActionID = None, setCreatedTime = None, setIsReadOnlyHistoricalRecord = None, setIsReferralAction = None, setModifiedTime = None, setOffenseActionIDClonedFrom = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOffenseActionID = False, returnActionID = False, returnCreatedTime = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOffenseAction(EntityID = 1, setOffenseActionID = None, setActionID = None, setCreatedTime = None, setIsReadOnlyHistoricalRecord = None, setIsReferralAction = None, setModifiedTime = None, setOffenseActionIDClonedFrom = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOffenseActionID = False, returnActionID = False, returnCreatedTime = False, returnIsReadOnlyHistoricalRecord = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOffenseAction(OffenseActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "delete")


def getEveryOffenseLevel(searchConditions = [], EntityID = 1, returnOffenseLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OffenseLevel in the district.

    This function returns a dataframe of every OffenseLevel in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOffenseLevel(OffenseLevelID, EntityID = 1, returnOffenseLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "get", return_params_list = return_params)

def modifyOffenseLevel(OffenseLevelID, EntityID = 1, setOffenseLevelID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setOffenseLevelIDClonedFrom = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOffenseLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOffenseLevel(EntityID = 1, setOffenseLevelID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setOffenseLevelIDClonedFrom = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOffenseLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOffenseLevel(OffenseLevelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "delete")


def getEveryPerceivedMotivation(searchConditions = [], EntityID = 1, returnPerceivedMotivationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PerceivedMotivation in the district.

    This function returns a dataframe of every PerceivedMotivation in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPerceivedMotivation(PerceivedMotivationID, EntityID = 1, returnPerceivedMotivationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "get", return_params_list = return_params)

def modifyPerceivedMotivation(PerceivedMotivationID, EntityID = 1, setPerceivedMotivationID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setPerceivedMotivationIDClonedFrom = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPerceivedMotivationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPerceivedMotivation(EntityID = 1, setPerceivedMotivationID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setPerceivedMotivationIDClonedFrom = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPerceivedMotivationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePerceivedMotivation(PerceivedMotivationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "delete")


def getEveryTempIncidentInvolvedPerson(searchConditions = [], EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentInvolvedPerson in the district.

    This function returns a dataframe of every TempIncidentInvolvedPerson in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentInvolvedPerson(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params)

def modifyTempIncidentInvolvedPerson(TempIncidentInvolvedPersonID, EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentInvolvedPerson(EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentInvolvedPerson(TempIncidentInvolvedPersonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(TempIncidentInvolvedPersonID), verb = "delete")


def getEveryTempIncidentInvolvedPersonIN(searchConditions = [], EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnISSCount = False, returnIsSeclusion = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentInvolvedPersonIN in the district.

    This function returns a dataframe of every TempIncidentInvolvedPersonIN in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentInvolvedPersonIN(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnISSCount = False, returnIsSeclusion = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params)

def modifyTempIncidentInvolvedPersonIN(TempIncidentInvolvedPersonID, EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsChemicalRestraint = None, setIsMechanicalRestraint = None, setIsPhysicalRestraint = None, setISSCount = None, setIsSeclusion = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStaffIDResourceOfficer = None, setStateArrestReasonINID = None, setStateArrestTypeINID = None, setStateCriminalEventINID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnISSCount = False, returnIsSeclusion = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentInvolvedPersonIN(EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsChemicalRestraint = None, setIsMechanicalRestraint = None, setIsPhysicalRestraint = None, setISSCount = None, setIsSeclusion = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStaffIDResourceOfficer = None, setStateArrestReasonINID = None, setStateArrestTypeINID = None, setStateCriminalEventINID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnISSCount = False, returnIsSeclusion = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentInvolvedPersonIN(TempIncidentInvolvedPersonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(TempIncidentInvolvedPersonID), verb = "delete")


def getEveryTempIncidentInvolvedPersonMN(searchConditions = [], EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentInvolvedPersonMN in the district.

    This function returns a dataframe of every TempIncidentInvolvedPersonMN in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentInvolvedPersonMN(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params)

def modifyTempIncidentInvolvedPersonMN(TempIncidentInvolvedPersonID, EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOffenderArrestedByLawEnforcement = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setReportedToLawEnforcement = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWasSeriousBodilyInjury = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentInvolvedPersonMN(EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOffenderArrestedByLawEnforcement = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setReportedToLawEnforcement = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWasSeriousBodilyInjury = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentInvolvedPersonMN(TempIncidentInvolvedPersonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(TempIncidentInvolvedPersonID), verb = "delete")


def getEveryTempIncidentInvolvedPersonPA(searchConditions = [], EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsResidentialPlacementByNonEdAgency = False, returnISSCount = False, returnISSPartialCount = False, returnLLEIncidentNumber = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentInvolvedPersonPA in the district.

    This function returns a dataframe of every TempIncidentInvolvedPersonPA in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentInvolvedPersonPA(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsResidentialPlacementByNonEdAgency = False, returnISSCount = False, returnISSPartialCount = False, returnLLEIncidentNumber = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params)

def modifyTempIncidentInvolvedPersonPA(TempIncidentInvolvedPersonID, EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setIncidentVictimComment = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsResidentialPlacementByNonEdAgency = None, setISSCount = None, setISSPartialCount = None, setLLEIncidentNumber = None, setLocalLawEnforcementNotified = None, setMedicalTreatmentRequired = None, setModifiedTime = None, setNameID = None, setNameOfLocalLawEnforcementContacted = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateAdjudicationPAID = None, setStateArrestedPAID = None, setStateInjurySeverityPAID = None, setStateOffenderTypePAID = None, setStateVictimTypePAID = None, setStateWeaponDetectedMethodPAID = None, setStudentAssistanceProgramReferral = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponDetectionComment = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsResidentialPlacementByNonEdAgency = False, returnISSCount = False, returnISSPartialCount = False, returnLLEIncidentNumber = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentInvolvedPersonPA(EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setIncidentVictimComment = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsResidentialPlacementByNonEdAgency = None, setISSCount = None, setISSPartialCount = None, setLLEIncidentNumber = None, setLocalLawEnforcementNotified = None, setMedicalTreatmentRequired = None, setModifiedTime = None, setNameID = None, setNameOfLocalLawEnforcementContacted = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateAdjudicationPAID = None, setStateArrestedPAID = None, setStateInjurySeverityPAID = None, setStateOffenderTypePAID = None, setStateVictimTypePAID = None, setStateWeaponDetectedMethodPAID = None, setStudentAssistanceProgramReferral = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponDetectionComment = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsResidentialPlacementByNonEdAgency = False, returnISSCount = False, returnISSPartialCount = False, returnLLEIncidentNumber = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentInvolvedPersonPA(TempIncidentInvolvedPersonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(TempIncidentInvolvedPersonID), verb = "delete")


def getEveryTempIncidentInvolvedPersonTX(searchConditions = [], EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentInvolvedPersonTX in the district.

    This function returns a dataframe of every TempIncidentInvolvedPersonTX in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentInvolvedPersonTX(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params)

def modifyTempIncidentInvolvedPersonTX(TempIncidentInvolvedPersonID, EntityID = 1, setTempIncidentInvolvedPersonID = None, setCampusIDOfDisciplinaryResponsibility = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentInvolvedPersonTX(EntityID = 1, setTempIncidentInvolvedPersonID = None, setCampusIDOfDisciplinaryResponsibility = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentInvolvedPersonTX(TempIncidentInvolvedPersonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(TempIncidentInvolvedPersonID), verb = "delete")


def getEveryTempIncidentInvolvedPersonWA(searchConditions = [], EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentInvolvedPersonWA in the district.

    This function returns a dataframe of every TempIncidentInvolvedPersonWA in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentInvolvedPersonWA(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params)

def modifyTempIncidentInvolvedPersonWA(TempIncidentInvolvedPersonID, EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateReportedOffense = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentInvolvedPersonWA(EntityID = 1, setTempIncidentInvolvedPersonID = None, setCreatedTime = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setISSCount = None, setISSPartialCount = None, setModifiedTime = None, setNameID = None, setOSSCount = None, setOSSPartialCount = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setSecondaryOffensesBackingDataDictionary = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateReportedOffense = None, setStudentID = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentInvolvedPersonID = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnISSCount = False, returnISSPartialCount = False, returnModifiedTime = False, returnNameID = False, returnOSSCount = False, returnOSSPartialCount = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentInvolvedPersonWA(TempIncidentInvolvedPersonID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(TempIncidentInvolvedPersonID), verb = "delete")


def getEveryTempIncidentOffense(searchConditions = [], EntityID = 1, returnTempIncidentOffenseID = False, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffense in the district.

    This function returns a dataframe of every TempIncidentOffense in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffense(TempIncidentOffenseID, EntityID = 1, returnTempIncidentOffenseID = False, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(TempIncidentOffenseID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffense(TempIncidentOffenseID, EntityID = 1, setTempIncidentOffenseID = None, setCreatedTime = None, setExistingIncidentID = None, setIsPrimaryOffense = None, setModifiedTime = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseID = False, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(TempIncidentOffenseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffense(EntityID = 1, setTempIncidentOffenseID = None, setCreatedTime = None, setExistingIncidentID = None, setIsPrimaryOffense = None, setModifiedTime = None, setOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseID = False, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffense(TempIncidentOffenseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(TempIncidentOffenseID), verb = "delete")


def getEveryTempIncidentOffenseName(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameID = False, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseName in the district.

    This function returns a dataframe of every TempIncidentOffenseName in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseName(TempIncidentOffenseNameID, EntityID = 1, returnTempIncidentOffenseNameID = False, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(TempIncidentOffenseNameID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseName(TempIncidentOffenseNameID, EntityID = 1, setTempIncidentOffenseNameID = None, setCreatedTime = None, setExistingIncidentOffenseNameID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPrimaryOffense = None, setModifiedTime = None, setOffenseCodeDescription = None, setOffenseID = None, setOffenseLevelID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setStudentNumber = None, setTempIncidentInvolvedPersonID = None, setTempIncidentOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameID = False, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(TempIncidentOffenseNameID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseName(EntityID = 1, setTempIncidentOffenseNameID = None, setCreatedTime = None, setExistingIncidentOffenseNameID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPrimaryOffense = None, setModifiedTime = None, setOffenseCodeDescription = None, setOffenseID = None, setOffenseLevelID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setStudentNumber = None, setTempIncidentInvolvedPersonID = None, setTempIncidentOffenseID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameID = False, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseName(TempIncidentOffenseNameID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(TempIncidentOffenseNameID), verb = "delete")


def getEveryTempIncidentOffenseNameAction(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameAction in the district.

    This function returns a dataframe of every TempIncidentOffenseNameAction in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameAction(EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "delete")


def getEveryTempIncidentOffenseNameActionDetail(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionDetailID = False, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameActionDetail in the district.

    This function returns a dataframe of every TempIncidentOffenseNameActionDetail in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1, returnTempIncidentOffenseNameActionDetailID = False, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1, setTempIncidentOffenseNameActionDetailID = None, setActionCodeDescription = None, setCreateAttendance = None, setCreatedTime = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setFullName = None, setIncidentOffenseNameActionDetailID = None, setInvolvementType = None, setIsAlternate = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setNewStatus = None, setNewStatusCode = None, setOffenseCodeDescription = None, setOldStatus = None, setOldStatusCode = None, setPartialDayPeriods = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setTempIncidentOffenseNameActionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionDetailID = False, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameActionDetail(EntityID = 1, setTempIncidentOffenseNameActionDetailID = None, setActionCodeDescription = None, setCreateAttendance = None, setCreatedTime = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setFullName = None, setIncidentOffenseNameActionDetailID = None, setInvolvementType = None, setIsAlternate = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setNewStatus = None, setNewStatusCode = None, setOffenseCodeDescription = None, setOldStatus = None, setOldStatusCode = None, setPartialDayPeriods = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setTempIncidentOffenseNameActionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionDetailID = False, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "delete")


def getEveryTempIncidentOffenseNameActionDetailRecord(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionDetailRecordID = False, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameActionDetailRecord in the district.

    This function returns a dataframe of every TempIncidentOffenseNameActionDetailRecord in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1, returnTempIncidentOffenseNameActionDetailRecordID = False, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1, setTempIncidentOffenseNameActionDetailRecordID = None, setBuilding = None, setBuildingID = None, setCreatedTime = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setIncidentOffenseNameActionID = None, setIsAlternate = None, setIsGuardianNotified = None, setLocation = None, setLocationID = None, setModifiedTime = None, setRoomID = None, setRoomNumber = None, setScheduledTime = None, setStaffFollowUpOfficerName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionDetailRecordID = False, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameActionDetailRecord(EntityID = 1, setTempIncidentOffenseNameActionDetailRecordID = None, setBuilding = None, setBuildingID = None, setCreatedTime = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setIncidentOffenseNameActionID = None, setIsAlternate = None, setIsGuardianNotified = None, setLocation = None, setLocationID = None, setModifiedTime = None, setRoomID = None, setRoomNumber = None, setScheduledTime = None, setStaffFollowUpOfficerName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionDetailRecordID = False, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "delete")


def getEveryTempIncidentOffenseNameActionIN(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryAction = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameActionIN in the district.

    This function returns a dataframe of every TempIncidentOffenseNameActionIN in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameActionIN(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryAction = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameActionIN(TempIncidentOffenseNameActionID, EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryAction = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateEducationalServiceProvidedINID = None, setStateSuspensionReasonINID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryAction = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameActionIN(EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryAction = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateEducationalServiceProvidedINID = None, setStateSuspensionReasonINID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryAction = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameActionIN(TempIncidentOffenseNameActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(TempIncidentOffenseNameActionID), verb = "delete")


def getEveryTempIncidentOffenseNameActionMN(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameActionMN in the district.

    This function returns a dataframe of every TempIncidentOffenseNameActionMN in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameActionMN(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameActionMN(TempIncidentOffenseNameActionID, EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameActionMN(EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameActionMN(TempIncidentOffenseNameActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(TempIncidentOffenseNameActionID), verb = "delete")


def getEveryTempIncidentOffenseNameActionPA(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameActionPA in the district.

    This function returns a dataframe of every TempIncidentOffenseNameActionPA in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameActionPA(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameActionPA(TempIncidentOffenseNameActionID, EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setAssignedAlternativeEducation = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReceivedEducationalServices = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameActionPA(EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setAssignedAlternativeEducation = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReceivedEducationalServices = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameActionPA(TempIncidentOffenseNameActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(TempIncidentOffenseNameActionID), verb = "delete")


def getEveryTempIncidentOffenseNameActionWA(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameActionWA in the district.

    This function returns a dataframe of every TempIncidentOffenseNameActionWA in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameActionWA(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameActionWA(TempIncidentOffenseNameActionID, EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDateReadmissionPetitionGranted = None, setDateReadmissionPetitionSubmitted = None, setDateReengagementMeetingHeld = None, setDurationOfExclusionaryActionDays = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setPlacedInInterimAlternativeEducationalSetting = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateAcademicServiceWAID = None, setStateAppealCodeWAID = None, setStateBehaviorServiceWAID = None, setStatePetitionExtensionExpulsionWAID = None, setStateReengagementPlanWAID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setTotalAmountOfExclusionaryTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameActionWA(EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setCreatedTime = None, setDateReadmissionPetitionGranted = None, setDateReadmissionPetitionSubmitted = None, setDateReengagementMeetingHeld = None, setDurationOfExclusionaryActionDays = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setPlacedInInterimAlternativeEducationalSetting = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateAcademicServiceWAID = None, setStateAppealCodeWAID = None, setStateBehaviorServiceWAID = None, setStatePetitionExtensionExpulsionWAID = None, setStateReengagementPlanWAID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setTotalAmountOfExclusionaryTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameActionWA(TempIncidentOffenseNameActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(TempIncidentOffenseNameActionID), verb = "delete")


def getEveryTempIncidentOffenseNameActionWI(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameActionWI in the district.

    This function returns a dataframe of every TempIncidentOffenseNameActionWI in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameActionWI(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameActionWI(TempIncidentOffenseNameActionID, EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBehaviorDetailedDescription = None, setBuildingID = None, setCausedSeriousBodilyInjury = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setHasEarlyReinstatementCondition = None, setIAESRemovalType = None, setIAESRemovalTypeCode = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateModifiedTermWIID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameActionWI(EntityID = 1, setTempIncidentOffenseNameActionID = None, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBehaviorDetailedDescription = None, setBuildingID = None, setCausedSeriousBodilyInjury = None, setComment = None, setCreatedTime = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setHasEarlyReinstatementCondition = None, setIAESRemovalType = None, setIAESRemovalTypeCode = None, setInternalComment = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setModifiedTime = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStartTime = None, setStateModifiedTermWIID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameActionID = False, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInternalComment = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStartTime = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameActionWI(TempIncidentOffenseNameActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(TempIncidentOffenseNameActionID), verb = "delete")


def getEveryTempIncidentOffenseNameDrug(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameDrug in the district.

    This function returns a dataframe of every TempIncidentOffenseNameDrug in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameDrug(TempIncidentOffenseNameDrugID, EntityID = 1, returnTempIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(TempIncidentOffenseNameDrugID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameDrug(TempIncidentOffenseNameDrugID, EntityID = 1, setTempIncidentOffenseNameDrugID = None, setCreatedTime = None, setDrugID = None, setIncidentOffenseNameDrugID = None, setModifiedTime = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(TempIncidentOffenseNameDrugID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameDrug(EntityID = 1, setTempIncidentOffenseNameDrugID = None, setCreatedTime = None, setDrugID = None, setIncidentOffenseNameDrugID = None, setModifiedTime = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameDrugID = False, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameDrug(TempIncidentOffenseNameDrugID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(TempIncidentOffenseNameDrugID), verb = "delete")


def getEveryTempIncidentOffenseNameParentalInvolvementPA(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameParentalInvolvementPAID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameParentalInvolvementPA in the district.

    This function returns a dataframe of every TempIncidentOffenseNameParentalInvolvementPA in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameParentalInvolvementPA(TempIncidentOffenseNameParentalInvolvementPAID, EntityID = 1, returnTempIncidentOffenseNameParentalInvolvementPAID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(TempIncidentOffenseNameParentalInvolvementPAID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameParentalInvolvementPA(TempIncidentOffenseNameParentalInvolvementPAID, EntityID = 1, setTempIncidentOffenseNameParentalInvolvementPAID = None, setComment = None, setCreatedTime = None, setIncidentOffenseNameParentalInvolvementPAID = None, setModifiedTime = None, setStateParentalInvolvementPAID = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameParentalInvolvementPAID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(TempIncidentOffenseNameParentalInvolvementPAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameParentalInvolvementPA(EntityID = 1, setTempIncidentOffenseNameParentalInvolvementPAID = None, setComment = None, setCreatedTime = None, setIncidentOffenseNameParentalInvolvementPAID = None, setModifiedTime = None, setStateParentalInvolvementPAID = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameParentalInvolvementPAID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameParentalInvolvementPA(TempIncidentOffenseNameParentalInvolvementPAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(TempIncidentOffenseNameParentalInvolvementPAID), verb = "delete")


def getEveryTempIncidentOffenseNameReportRunHistoryRecord(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameReportRunHistoryRecordID = False, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameReportRunHistoryRecord in the district.

    This function returns a dataframe of every TempIncidentOffenseNameReportRunHistoryRecord in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1, returnTempIncidentOffenseNameReportRunHistoryRecordID = False, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1, setTempIncidentOffenseNameReportRunHistoryRecordID = None, setColumnHeader1 = None, setColumnHeader10 = None, setColumnHeader2 = None, setColumnHeader3 = None, setColumnHeader4 = None, setColumnHeader5 = None, setColumnHeader6 = None, setColumnHeader7 = None, setColumnHeader8 = None, setColumnHeader9 = None, setCreatedTime = None, setDateTime = None, setIncident = None, setIncidentNumber = None, setIncidentOffenseNameID = None, setModifiedTime = None, setOffense = None, setStudentID = None, setStudentName = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameReportRunHistoryRecordID = False, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameReportRunHistoryRecord(EntityID = 1, setTempIncidentOffenseNameReportRunHistoryRecordID = None, setColumnHeader1 = None, setColumnHeader10 = None, setColumnHeader2 = None, setColumnHeader3 = None, setColumnHeader4 = None, setColumnHeader5 = None, setColumnHeader6 = None, setColumnHeader7 = None, setColumnHeader8 = None, setColumnHeader9 = None, setCreatedTime = None, setDateTime = None, setIncident = None, setIncidentNumber = None, setIncidentOffenseNameID = None, setModifiedTime = None, setOffense = None, setStudentID = None, setStudentName = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempIncidentOffenseNameReportRunHistoryRecordID = False, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "delete")


def getEveryTempIncidentOffenseNameWeapon(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameWeapon in the district.

    This function returns a dataframe of every TempIncidentOffenseNameWeapon in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameWeapon(TempIncidentOffenseNameWeaponID, EntityID = 1, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(TempIncidentOffenseNameWeaponID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameWeapon(TempIncidentOffenseNameWeaponID, EntityID = 1, setTempIncidentOffenseNameWeaponID = None, setCreatedTime = None, setIncidentOffenseNameWeaponID = None, setModifiedTime = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponCount = None, setWeaponID = None, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(TempIncidentOffenseNameWeaponID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameWeapon(EntityID = 1, setTempIncidentOffenseNameWeaponID = None, setCreatedTime = None, setIncidentOffenseNameWeaponID = None, setModifiedTime = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponCount = None, setWeaponID = None, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameWeapon(TempIncidentOffenseNameWeaponID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(TempIncidentOffenseNameWeaponID), verb = "delete")


def getEveryTempIncidentOffenseNameWeaponMN(searchConditions = [], EntityID = 1, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempIncidentOffenseNameWeaponMN in the district.

    This function returns a dataframe of every TempIncidentOffenseNameWeaponMN in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempIncidentOffenseNameWeaponMN(TempIncidentOffenseNameWeaponID, EntityID = 1, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(TempIncidentOffenseNameWeaponID), verb = "get", return_params_list = return_params)

def modifyTempIncidentOffenseNameWeaponMN(TempIncidentOffenseNameWeaponID, EntityID = 1, setTempIncidentOffenseNameWeaponID = None, setCreatedTime = None, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setIncidentOffenseNameWeaponID = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setModifiedTime = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponCount = None, setWeaponID = None, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(TempIncidentOffenseNameWeaponID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempIncidentOffenseNameWeaponMN(EntityID = 1, setTempIncidentOffenseNameWeaponID = None, setCreatedTime = None, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setIncidentOffenseNameWeaponID = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setModifiedTime = None, setTempIncidentOffenseNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponCount = None, setWeaponID = None, returnTempIncidentOffenseNameWeaponID = False, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponCount = False, returnWeaponID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempIncidentOffenseNameWeaponMN(TempIncidentOffenseNameWeaponID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(TempIncidentOffenseNameWeaponID), verb = "delete")


def getEveryWeapon(searchConditions = [], EntityID = 1, returnWeaponID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Weapon in the district.

    This function returns a dataframe of every Weapon in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getWeapon(WeaponID, EntityID = 1, returnWeaponID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "get", return_params_list = return_params)

def modifyWeapon(WeaponID, EntityID = 1, setWeaponID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSchoolYearID = None, setStatePelletGunTypeMNID = None, setStateWeaponTypeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponIDClonedFrom = None, setWeaponMNID = None, returnWeaponID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "post", return_params_list = return_params, payload = payload_params)

def createWeapon(EntityID = 1, setWeaponID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setIsReadOnlyHistoricalRecord = None, setModifiedTime = None, setSchoolYearID = None, setStatePelletGunTypeMNID = None, setStateWeaponTypeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeaponIDClonedFrom = None, setWeaponMNID = None, returnWeaponID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsReadOnlyHistoricalRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteWeapon(WeaponID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "delete")


def getEveryWhiteListFieldPath(searchConditions = [], EntityID = 1, returnWhiteListFieldPathID = False, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedForType = False, returnUsedForTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every WhiteListFieldPath in the district.

    This function returns a dataframe of every WhiteListFieldPath in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/WhiteListFieldPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/WhiteListFieldPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getWhiteListFieldPath(WhiteListFieldPathID, EntityID = 1, returnWhiteListFieldPathID = False, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedForType = False, returnUsedForTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/WhiteListFieldPath/" + str(WhiteListFieldPathID), verb = "get", return_params_list = return_params)

def modifyWhiteListFieldPath(WhiteListFieldPathID, EntityID = 1, setWhiteListFieldPathID = None, setCreatedTime = None, setDescription = None, setFieldPath = None, setFriendlyName = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUsedForType = None, setUsedForTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnWhiteListFieldPathID = False, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedForType = False, returnUsedForTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/WhiteListFieldPath/" + str(WhiteListFieldPathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createWhiteListFieldPath(EntityID = 1, setWhiteListFieldPathID = None, setCreatedTime = None, setDescription = None, setFieldPath = None, setFriendlyName = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUsedForType = None, setUsedForTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnWhiteListFieldPathID = False, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedForType = False, returnUsedForTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/WhiteListFieldPath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteWhiteListFieldPath(WhiteListFieldPathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/WhiteListFieldPath/" + str(WhiteListFieldPathID), verb = "delete")