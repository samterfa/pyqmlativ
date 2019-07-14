# This module contains Discipline functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryActionAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnActionAttendanceTypeID = True, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getActionAttendanceType(ActionAttendanceTypeID, EntityID = 1, returnActionAttendanceTypeID = True, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "get", return_params_list = return_params_list)

def modifyActionAttendanceType(ActionAttendanceTypeID, EntityID = 1, setActionID = None, setAttendanceTypeID = None, setEntityGroupKey = None, setRelationships = None, returnActionAttendanceTypeID = True, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createActionAttendanceType(EntityID = 1, setActionID = None, setAttendanceTypeID = None, setEntityGroupKey = None, setRelationships = None, returnActionAttendanceTypeID = True, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteActionAttendanceType(ActionAttendanceTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAction(EntityID = 1, page = 1, pageSize = 100, returnActionID = True, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAction(ActionID, EntityID = 1, returnActionID = True, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "get", return_params_list = return_params_list)

def modifyAction(ActionID, EntityID = 1, setActionIDClonedFrom = None, setActionTypeID = None, setCode = None, setCreateAttendanceForActionDetail = None, setDefaultDuration = None, setDefaultLocationID = None, setDescription = None, setDistrictID = None, setDurationType = None, setDurationTypeCode = None, setFederalDisciplineCategoryID = None, setRestraintSeclusion = None, setRestraintSeclusionCode = None, setSchoolYearID = None, setStateActionTypeMNID = None, setSuppressCreationOfActionDetails = None, setTransferToAlternativeSchool = None, setRelationships = None, returnActionID = True, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAction(EntityID = 1, setActionIDClonedFrom = None, setActionTypeID = None, setCode = None, setCreateAttendanceForActionDetail = None, setDefaultDuration = None, setDefaultLocationID = None, setDescription = None, setDistrictID = None, setDurationType = None, setDurationTypeCode = None, setFederalDisciplineCategoryID = None, setRestraintSeclusion = None, setRestraintSeclusionCode = None, setSchoolYearID = None, setStateActionTypeMNID = None, setSuppressCreationOfActionDetails = None, setTransferToAlternativeSchool = None, setRelationships = None, returnActionID = True, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAction(ActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryActionType(EntityID = 1, page = 1, pageSize = 100, returnActionTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getActionType(ActionTypeID, EntityID = 1, returnActionTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "get", return_params_list = return_params_list)

def modifyActionType(ActionTypeID, EntityID = 1, setCode = None, setDescription = None, setIsInvalid = None, setSkywardHash = None, setSkywardID = None, setValidYearHigh = None, setValidYearLow = None, setRelationships = None, returnActionTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createActionType(EntityID = 1, setCode = None, setDescription = None, setIsInvalid = None, setSkywardHash = None, setSkywardID = None, setValidYearHigh = None, setValidYearLow = None, setRelationships = None, returnActionTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteActionType(ActionTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = True, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setAllowActionRecommendationsOnReferrals = None, setAllowActionTypeUpdate = None, setAllowDurationTypeUpdate = None, setAllowOnlyOneOffensePerIncident = None, setAllowUseOfWarning = None, setConfigDistrictYearIDClonedFrom = None, setDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = None, setDefaultActionValueFromPreviousPerson = None, setDefaultDisciplineScreenDateAndTimes = None, setDefaultOffenseValueFromPreviousPerson = None, setDisplayInvolvedPersonsFromAllEntities = None, setDisplayStudentOffensesForAllEntities = None, setDisplayWarningsInFamilyAndStudentAccess = None, setDistrictID = None, setRestartIncidentNumberThisYear = None, setSchoolYearID = None, setUseIncidentBuildingAndRoom = None, setUsePerceivedMotivation = None, setRelationships = None, returnConfigDistrictYearID = True, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setAllowActionRecommendationsOnReferrals = None, setAllowActionTypeUpdate = None, setAllowDurationTypeUpdate = None, setAllowOnlyOneOffensePerIncident = None, setAllowUseOfWarning = None, setConfigDistrictYearIDClonedFrom = None, setDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = None, setDefaultActionValueFromPreviousPerson = None, setDefaultDisciplineScreenDateAndTimes = None, setDefaultOffenseValueFromPreviousPerson = None, setDisplayInvolvedPersonsFromAllEntities = None, setDisplayStudentOffensesForAllEntities = None, setDisplayWarningsInFamilyAndStudentAccess = None, setDistrictID = None, setRestartIncidentNumberThisYear = None, setSchoolYearID = None, setUseIncidentBuildingAndRoom = None, setUsePerceivedMotivation = None, setRelationships = None, returnConfigDistrictYearID = True, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = True, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setActionStatusDefaultValue = None, setActionStatusDefaultValueCode = None, setConfigEntityGroupYearIDClonedFrom = None, setDefaultActionStatusCode = None, setDetentionsOnFri = None, setDetentionsOnMon = None, setDetentionsOnSat = None, setDetentionsOnSun = None, setDetentionsOnThu = None, setDetentionsOnTue = None, setDetentionsOnWed = None, setEntityGroupKey = None, setEntityID = None, setExpulsionsOnFri = None, setExpulsionsOnMon = None, setExpulsionsOnSat = None, setExpulsionsOnSun = None, setExpulsionsOnThu = None, setExpulsionsOnTue = None, setExpulsionsOnWed = None, setIncludeDisciplinaryActionAndDetailsOnLetter = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setInSchoolSuspensionsOnFri = None, setInSchoolSuspensionsOnMon = None, setInSchoolSuspensionsOnSat = None, setInSchoolSuspensionsOnSun = None, setInSchoolSuspensionsOnThu = None, setInSchoolSuspensionsOnTue = None, setInSchoolSuspensionsOnWed = None, setOutOfSchoolSuspensionsOnFri = None, setOutOfSchoolSuspensionsOnMon = None, setOutOfSchoolSuspensionsOnSat = None, setOutOfSchoolSuspensionsOnSun = None, setOutOfSchoolSuspensionsOnThu = None, setOutOfSchoolSuspensionsOnTue = None, setOutOfSchoolSuspensionsOnWed = None, setSchoolYearID = None, setTardyKioskDisciplineSlipTitle = None, setUseAlternateActionDetails = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setActionStatusDefaultValue = None, setActionStatusDefaultValueCode = None, setConfigEntityGroupYearIDClonedFrom = None, setDefaultActionStatusCode = None, setDetentionsOnFri = None, setDetentionsOnMon = None, setDetentionsOnSat = None, setDetentionsOnSun = None, setDetentionsOnThu = None, setDetentionsOnTue = None, setDetentionsOnWed = None, setEntityGroupKey = None, setEntityID = None, setExpulsionsOnFri = None, setExpulsionsOnMon = None, setExpulsionsOnSat = None, setExpulsionsOnSun = None, setExpulsionsOnThu = None, setExpulsionsOnTue = None, setExpulsionsOnWed = None, setIncludeDisciplinaryActionAndDetailsOnLetter = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setInSchoolSuspensionsOnFri = None, setInSchoolSuspensionsOnMon = None, setInSchoolSuspensionsOnSat = None, setInSchoolSuspensionsOnSun = None, setInSchoolSuspensionsOnThu = None, setInSchoolSuspensionsOnTue = None, setInSchoolSuspensionsOnWed = None, setOutOfSchoolSuspensionsOnFri = None, setOutOfSchoolSuspensionsOnMon = None, setOutOfSchoolSuspensionsOnSat = None, setOutOfSchoolSuspensionsOnSun = None, setOutOfSchoolSuspensionsOnThu = None, setOutOfSchoolSuspensionsOnTue = None, setOutOfSchoolSuspensionsOnWed = None, setSchoolYearID = None, setTardyKioskDisciplineSlipTitle = None, setUseAlternateActionDetails = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityYear(ConfigEntityYearID, EntityID = 1, setConfigEntityYearIDClonedFrom = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityYear(EntityID = 1, setConfigEntityYearIDClonedFrom = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnAllowIncidentSuppression = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = True, returnAllowIncidentSuppression = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params_list)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setAllowIncidentSuppression = None, setReportIDDisciplineLetter = None, setRelationships = None, returnConfigSystemID = True, returnAllowIncidentSuppression = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigSystem(EntityID = 1, setAllowIncidentSuppression = None, setReportIDDisciplineLetter = None, setRelationships = None, returnConfigSystemID = True, returnAllowIncidentSuppression = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterRunHistory(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterRunHistoryID = True, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1, returnDisciplineLetterRunHistoryID = True, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1, setDate = None, setDisciplineLetterTemplateID = None, setEndDate = None, setEntityID = None, setFilterType = None, setFilterTypeCode = None, setGracePeriod = None, setIncidentType = None, setIncidentTypeCode = None, setIsActive = None, setReportRunInfoID = None, setRunDescription = None, setStartDate = None, setRelationships = None, returnDisciplineLetterRunHistoryID = True, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterRunHistory(EntityID = 1, setDate = None, setDisciplineLetterTemplateID = None, setEndDate = None, setEntityID = None, setFilterType = None, setFilterTypeCode = None, setGracePeriod = None, setIncidentType = None, setIncidentTypeCode = None, setIsActive = None, setReportRunInfoID = None, setRunDescription = None, setStartDate = None, setRelationships = None, returnDisciplineLetterRunHistoryID = True, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterRunHistoryAction(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterRunHistoryActionID = True, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1, returnDisciplineLetterRunHistoryActionID = True, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1, setActionID = None, setDisciplineLetterRunHistoryID = None, setRelationships = None, returnDisciplineLetterRunHistoryActionID = True, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterRunHistoryAction(EntityID = 1, setActionID = None, setDisciplineLetterRunHistoryID = None, setRelationships = None, returnDisciplineLetterRunHistoryActionID = True, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterRunHistoryOffense(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterRunHistoryOffenseID = True, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1, returnDisciplineLetterRunHistoryOffenseID = True, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1, setDisciplineLetterRunHistoryID = None, setOffenseID = None, setRelationships = None, returnDisciplineLetterRunHistoryOffenseID = True, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterRunHistoryOffense(EntityID = 1, setDisciplineLetterRunHistoryID = None, setOffenseID = None, setRelationships = None, returnDisciplineLetterRunHistoryOffenseID = True, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterTemplate(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateID = True, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1, returnDisciplineLetterTemplateID = True, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1, setAdvisorNameFormat = None, setAdvisorNameFormatCode = None, setBody = None, setColumnHeaderLabel1 = None, setColumnHeaderLabel10 = None, setColumnHeaderLabel2 = None, setColumnHeaderLabel3 = None, setColumnHeaderLabel4 = None, setColumnHeaderLabel5 = None, setColumnHeaderLabel6 = None, setColumnHeaderLabel7 = None, setColumnHeaderLabel8 = None, setColumnHeaderLabel9 = None, setDescription = None, setDisciplineLetterTemplateIDClonedFrom = None, setDistrictID = None, setFooter = None, setGuardianNameFormat = None, setGuardianNameFormatCode = None, setHeader = None, setIsDefault = None, setMediaIDLogo = None, setSchoolYearID = None, setStudentNameFormat = None, setStudentNameFormatCode = None, setSuperintendentNameFormat = None, setSuperintendentNameFormatCode = None, setRelationships = None, returnDisciplineLetterTemplateID = True, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterTemplate(EntityID = 1, setAdvisorNameFormat = None, setAdvisorNameFormatCode = None, setBody = None, setColumnHeaderLabel1 = None, setColumnHeaderLabel10 = None, setColumnHeaderLabel2 = None, setColumnHeaderLabel3 = None, setColumnHeaderLabel4 = None, setColumnHeaderLabel5 = None, setColumnHeaderLabel6 = None, setColumnHeaderLabel7 = None, setColumnHeaderLabel8 = None, setColumnHeaderLabel9 = None, setDescription = None, setDisciplineLetterTemplateIDClonedFrom = None, setDistrictID = None, setFooter = None, setGuardianNameFormat = None, setGuardianNameFormatCode = None, setHeader = None, setIsDefault = None, setMediaIDLogo = None, setSchoolYearID = None, setStudentNameFormat = None, setStudentNameFormatCode = None, setSuperintendentNameFormat = None, setSuperintendentNameFormatCode = None, setRelationships = None, returnDisciplineLetterTemplateID = True, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterTemplateEntity(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateEntityID = True, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1, returnDisciplineLetterTemplateEntityID = True, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1, setDisciplineLetterTemplateID = None, setEntityID = None, setRelationships = None, returnDisciplineLetterTemplateEntityID = True, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterTemplateEntity(EntityID = 1, setDisciplineLetterTemplateID = None, setEntityID = None, setRelationships = None, returnDisciplineLetterTemplateEntityID = True, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterTemplateField(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateFieldID = True, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1, returnDisciplineLetterTemplateFieldID = True, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(DisciplineLetterTemplateFieldID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1, setDescription = None, setFieldPath = None, setFriendlyName = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnDisciplineLetterTemplateFieldID = True, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(DisciplineLetterTemplateFieldID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterTemplateField(EntityID = 1, setDescription = None, setFieldPath = None, setFriendlyName = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnDisciplineLetterTemplateFieldID = True, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterTemplateHeaderColumn(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateHeaderColumnID = True, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1, returnDisciplineLetterTemplateHeaderColumnID = True, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1, setDisciplineLetterTemplateHeaderColumnIDClonedFrom = None, setDisciplineLetterTemplateHeaderRowID = None, setFieldType = None, setFieldTypeCode = None, setFreeformText = None, setLabelOverride = None, setSortNumber = None, setRelationships = None, returnDisciplineLetterTemplateHeaderColumnID = True, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterTemplateHeaderColumn(EntityID = 1, setDisciplineLetterTemplateHeaderColumnIDClonedFrom = None, setDisciplineLetterTemplateHeaderRowID = None, setFieldType = None, setFieldTypeCode = None, setFreeformText = None, setLabelOverride = None, setSortNumber = None, setRelationships = None, returnDisciplineLetterTemplateHeaderColumnID = True, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDisciplineLetterTemplateHeaderRow(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1, returnDisciplineLetterTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "get", return_params_list = return_params_list)

def modifyDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1, setColumnCount = None, setDisciplineLetterTemplateHeaderRowIDClonedFrom = None, setDisciplineLetterTemplateID = None, setSortNumber = None, setRelationships = None, returnDisciplineLetterTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDisciplineLetterTemplateHeaderRow(EntityID = 1, setColumnCount = None, setDisciplineLetterTemplateHeaderRowIDClonedFrom = None, setDisciplineLetterTemplateID = None, setSortNumber = None, setRelationships = None, returnDisciplineLetterTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDrug(EntityID = 1, page = 1, pageSize = 100, returnDrugID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDrug(DrugID, EntityID = 1, returnDrugID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "get", return_params_list = return_params_list)

def modifyDrug(DrugID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setDrugIDClonedFrom = None, setSchoolYearID = None, setStateDrugTypeMNID = None, setRelationships = None, returnDrugID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDrug(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setDrugIDClonedFrom = None, setSchoolYearID = None, setStateDrugTypeMNID = None, setRelationships = None, returnDrugID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDrug(DrugID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncident(EntityID = 1, page = 1, pageSize = 100, returnIncidentID = True, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncident(IncidentID, EntityID = 1, returnIncidentID = True, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "get", return_params_list = return_params_list)

def modifyIncident(IncidentID, EntityID = 1, setActionIDRecommended = None, setBuildingID = None, setDamageCost = None, setDateTime = None, setDateTimeDate = None, setDateTimeTime = None, setDescription = None, setDistrictID = None, setEntityID = None, setIncidentNumber = None, setIsSuppressed = None, setLocationID = None, setNumberOfNonEnrolledOffenders = None, setNumberOfNonEnrolledVictims = None, setReferredByFreeformName = None, setReferredByNameID = None, setReferredByType = None, setReferredByTypeCode = None, setReportedToLawEnforcement = None, setRoomID = None, setSchoolYearID = None, setStateDIRSTimeMNID = None, setType = None, setTypeCode = None, setRelationships = None, returnIncidentID = True, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncident(EntityID = 1, setActionIDRecommended = None, setBuildingID = None, setDamageCost = None, setDateTime = None, setDateTimeDate = None, setDateTimeTime = None, setDescription = None, setDistrictID = None, setEntityID = None, setIncidentNumber = None, setIsSuppressed = None, setLocationID = None, setNumberOfNonEnrolledOffenders = None, setNumberOfNonEnrolledVictims = None, setReferredByFreeformName = None, setReferredByNameID = None, setReferredByType = None, setReferredByTypeCode = None, setReportedToLawEnforcement = None, setRoomID = None, setSchoolYearID = None, setStateDIRSTimeMNID = None, setType = None, setTypeCode = None, setRelationships = None, returnIncidentID = True, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncident(IncidentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffense(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseID = True, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffense(IncidentOffenseID, EntityID = 1, returnIncidentOffenseID = True, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffense(IncidentOffenseID, EntityID = 1, setIncidentID = None, setIsPrimaryOffense = None, setOffenseID = None, setRelationships = None, returnIncidentOffenseID = True, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffense(EntityID = 1, setIncidentID = None, setIsPrimaryOffense = None, setOffenseID = None, setRelationships = None, returnIncidentOffenseID = True, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffense(IncidentOffenseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffenseNameActionDetail(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameActionDetailID = True, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1, returnIncidentOffenseNameActionDetailID = True, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1, setBuildingID = None, setComment = None, setDurationServed = None, setDurationToServe = None, setIncidentOffenseNameActionID = None, setIsAlternate = None, setIsGuardianNotified = None, setLocationID = None, setRoomID = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setRelationships = None, returnIncidentOffenseNameActionDetailID = True, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffenseNameActionDetail(EntityID = 1, setBuildingID = None, setComment = None, setDurationServed = None, setDurationToServe = None, setIncidentOffenseNameActionID = None, setIsAlternate = None, setIsGuardianNotified = None, setLocationID = None, setRoomID = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setRelationships = None, returnIncidentOffenseNameActionDetailID = True, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffenseNameActionDetailPeriod(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameActionDetailPeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1, returnIncidentOffenseNameActionDetailPeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1, setAttendancePeriodID = None, setIncidentOffenseNameActionDetailID = None, setRelationships = None, returnIncidentOffenseNameActionDetailPeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffenseNameActionDetailPeriod(EntityID = 1, setAttendancePeriodID = None, setIncidentOffenseNameActionDetailID = None, setRelationships = None, returnIncidentOffenseNameActionDetailPeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffenseNameAction(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameActionID = True, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnIsGuardianNotified = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1, returnIncidentOffenseNameActionID = True, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnIsGuardianNotified = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1, setActionID = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationServedOverride = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setIncidentOffenseNameID = None, setIsGuardianNotified = None, setLocationID = None, setOrderedDate = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDFollowUpOfficer = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setRelationships = None, returnIncidentOffenseNameActionID = True, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnIsGuardianNotified = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffenseNameAction(EntityID = 1, setActionID = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationServedOverride = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setIncidentOffenseNameID = None, setIsGuardianNotified = None, setLocationID = None, setOrderedDate = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDFollowUpOfficer = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setRelationships = None, returnIncidentOffenseNameActionID = True, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnIsGuardianNotified = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffenseNameDrug(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1, returnIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1, setDrugID = None, setIncidentOffenseNameID = None, setRelationships = None, returnIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffenseNameDrug(EntityID = 1, setDrugID = None, setIncidentOffenseNameID = None, setRelationships = None, returnIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffenseName(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffenseName(IncidentOffenseNameID, EntityID = 1, returnIncidentOffenseNameID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffenseName(IncidentOffenseNameID, EntityID = 1, setFreeformName = None, setIncidentOffenseID = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsGuardianNotified = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setNameID = None, setOffenderArrestedByLawEnforcement = None, setOffenseLevelID = None, setPerceivedMotivationID = None, setReportedToLawEnforcement = None, setStaffIDDisciplineOfficer = None, setStatement = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setWasSeriousBodilyInjury = None, setRelationships = None, returnIncidentOffenseNameID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffenseName(EntityID = 1, setFreeformName = None, setIncidentOffenseID = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsGuardianNotified = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setNameID = None, setOffenderArrestedByLawEnforcement = None, setOffenseLevelID = None, setPerceivedMotivationID = None, setReportedToLawEnforcement = None, setStaffIDDisciplineOfficer = None, setStatement = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setWasSeriousBodilyInjury = None, setRelationships = None, returnIncidentOffenseNameID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffenseName(IncidentOffenseNameID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffenseNameReportRunHistory(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameReportRunHistoryID = True, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1, returnIncidentOffenseNameReportRunHistoryID = True, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1, setAttachmentID = None, setColumnHeaderData1 = None, setColumnHeaderData10 = None, setColumnHeaderData2 = None, setColumnHeaderData3 = None, setColumnHeaderData4 = None, setColumnHeaderData5 = None, setColumnHeaderData6 = None, setColumnHeaderData7 = None, setColumnHeaderData8 = None, setColumnHeaderData9 = None, setDisciplineLetterRunHistoryID = None, setIncidentOffenseNameID = None, setIsActive = None, setStudentID = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setRelationships = None, returnIncidentOffenseNameReportRunHistoryID = True, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffenseNameReportRunHistory(EntityID = 1, setAttachmentID = None, setColumnHeaderData1 = None, setColumnHeaderData10 = None, setColumnHeaderData2 = None, setColumnHeaderData3 = None, setColumnHeaderData4 = None, setColumnHeaderData5 = None, setColumnHeaderData6 = None, setColumnHeaderData7 = None, setColumnHeaderData8 = None, setColumnHeaderData9 = None, setDisciplineLetterRunHistoryID = None, setIncidentOffenseNameID = None, setIsActive = None, setStudentID = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setRelationships = None, returnIncidentOffenseNameReportRunHistoryID = True, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryIncidentOffenseNameWeapon(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1, returnIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "get", return_params_list = return_params_list)

def modifyIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setIncidentOffenseNameID = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setWeaponID = None, setRelationships = None, returnIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createIncidentOffenseNameWeapon(EntityID = 1, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setIncidentOffenseNameID = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setWeaponID = None, setRelationships = None, returnIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLocation(EntityID = 1, page = 1, pageSize = 100, returnLocationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLocation(LocationID, EntityID = 1, returnLocationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "get", return_params_list = return_params_list)

def modifyLocation(LocationID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEdFiIncidentLocationID = None, setStateIncidentLocationMNID = None, setRelationships = None, returnLocationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLocation(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEdFiIncidentLocationID = None, setStateIncidentLocationMNID = None, setRelationships = None, returnLocationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLocation(LocationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNextIncidentNumber(EntityID = 1, page = 1, pageSize = 100, returnNextIncidentNumberID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNextIncidentNumber(NextIncidentNumberID, EntityID = 1, returnNextIncidentNumberID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "get", return_params_list = return_params_list)

def modifyNextIncidentNumber(NextIncidentNumberID, EntityID = 1, setDistrictID = None, setSchoolYearID = None, setSequenceNumber = None, setRelationships = None, returnNextIncidentNumberID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNextIncidentNumber(EntityID = 1, setDistrictID = None, setSchoolYearID = None, setSequenceNumber = None, setRelationships = None, returnNextIncidentNumberID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNextIncidentNumber(NextIncidentNumberID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOffense(EntityID = 1, page = 1, pageSize = 100, returnOffenseID = True, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOffense(OffenseID, EntityID = 1, returnOffenseID = True, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "get", return_params_list = return_params_list)

def modifyOffense(OffenseID, EntityID = 1, setAllowActionRecommendations = None, setCode = None, setDefaultActionID = None, setDescription = None, setDistrictID = None, setFederalOffenseCategoryID = None, setHarassmentBullying = None, setHarassmentBullyingCode = None, setIsDrugRelated = None, setIsInjuryThreat = None, setIsWeaponRelated = None, setOffenseIDClonedFrom = None, setOffenseLevelIDDefault = None, setRestrictActions = None, setSchoolYearID = None, setUseForReferral = None, setRelationships = None, returnOffenseID = True, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOffense(EntityID = 1, setAllowActionRecommendations = None, setCode = None, setDefaultActionID = None, setDescription = None, setDistrictID = None, setFederalOffenseCategoryID = None, setHarassmentBullying = None, setHarassmentBullyingCode = None, setIsDrugRelated = None, setIsInjuryThreat = None, setIsWeaponRelated = None, setOffenseIDClonedFrom = None, setOffenseLevelIDDefault = None, setRestrictActions = None, setSchoolYearID = None, setUseForReferral = None, setRelationships = None, returnOffenseID = True, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOffense(OffenseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOffenseAction(EntityID = 1, page = 1, pageSize = 100, returnOffenseActionID = True, returnActionID = False, returnCreatedTime = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOffenseAction(OffenseActionID, EntityID = 1, returnOffenseActionID = True, returnActionID = False, returnCreatedTime = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "get", return_params_list = return_params_list)

def modifyOffenseAction(OffenseActionID, EntityID = 1, setActionID = None, setIsReferralAction = None, setOffenseActionIDClonedFrom = None, setOffenseID = None, setRelationships = None, returnOffenseActionID = True, returnActionID = False, returnCreatedTime = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOffenseAction(EntityID = 1, setActionID = None, setIsReferralAction = None, setOffenseActionIDClonedFrom = None, setOffenseID = None, setRelationships = None, returnOffenseActionID = True, returnActionID = False, returnCreatedTime = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOffenseAction(OffenseActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOffenseLevel(EntityID = 1, page = 1, pageSize = 100, returnOffenseLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOffenseLevel(OffenseLevelID, EntityID = 1, returnOffenseLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "get", return_params_list = return_params_list)

def modifyOffenseLevel(OffenseLevelID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setOffenseLevelIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnOffenseLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOffenseLevel(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setOffenseLevelIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnOffenseLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOffenseLevel(OffenseLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPerceivedMotivation(EntityID = 1, page = 1, pageSize = 100, returnPerceivedMotivationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPerceivedMotivation(PerceivedMotivationID, EntityID = 1, returnPerceivedMotivationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "get", return_params_list = return_params_list)

def modifyPerceivedMotivation(PerceivedMotivationID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setPerceivedMotivationIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnPerceivedMotivationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPerceivedMotivation(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setPerceivedMotivationIDClonedFrom = None, setSchoolYearID = None, setRelationships = None, returnPerceivedMotivationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePerceivedMotivation(PerceivedMotivationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentInvolvedPerson(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentInvolvedPerson(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentInvolvedPerson(TempIncidentInvolvedPersonID, EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentInvolvedPerson(EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPerson/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentInvolvedPerson(TempIncidentInvolvedPersonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentInvolvedPersonIN(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnIsSeclusion = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentInvolvedPersonIN(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnIsSeclusion = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentInvolvedPersonIN(TempIncidentInvolvedPersonID, EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsChemicalRestraint = None, setIsMechanicalRestraint = None, setIsPhysicalRestraint = None, setIsSeclusion = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStaffIDResourceOfficer = None, setStateArrestReasonINID = None, setStateArrestTypeINID = None, setStateCriminalEventINID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnIsSeclusion = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentInvolvedPersonIN(EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsChemicalRestraint = None, setIsMechanicalRestraint = None, setIsPhysicalRestraint = None, setIsSeclusion = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStaffIDResourceOfficer = None, setStateArrestReasonINID = None, setStateArrestTypeINID = None, setStateCriminalEventINID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsChemicalRestraint = False, returnIsMechanicalRestraint = False, returnIsPhysicalRestraint = False, returnIsSeclusion = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStaffIDResourceOfficer = False, returnStateArrestReasonINID = False, returnStateArrestTypeINID = False, returnStateCriminalEventINID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonIN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentInvolvedPersonIN(TempIncidentInvolvedPersonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentInvolvedPersonMN(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentInvolvedPersonMN(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentInvolvedPersonMN(TempIncidentInvolvedPersonID, EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setNameID = None, setOffenderArrestedByLawEnforcement = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setReportedToLawEnforcement = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setStudentID = None, setStudentNumber = None, setWasSeriousBodilyInjury = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentInvolvedPersonMN(EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInjuryOccured = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPhysicalAssault = None, setIsPhysicalAssaultState = None, setNameID = None, setOffenderArrestedByLawEnforcement = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setReportedToLawEnforcement = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateOffenderActivityMNID = None, setStateVictimCostMNID = None, setStateVictimTypeMNID = None, setStudentID = None, setStudentNumber = None, setWasSeriousBodilyInjury = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnModifiedTime = False, returnNameID = False, returnOffenderArrestedByLawEnforcement = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnReportedToLawEnforcement = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentInvolvedPersonMN(TempIncidentInvolvedPersonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentInvolvedPersonPA(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentInvolvedPersonPA(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentInvolvedPersonPA(TempIncidentInvolvedPersonID, EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setIncidentVictimComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setLocalLawEnforcementNotified = None, setMedicalTreatmentRequired = None, setNameID = None, setNameOfLocalLawEnforcementContacted = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateAdjudicationPAID = None, setStateArrestedPAID = None, setStateInjurySeverityPAID = None, setStateOffenderTypePAID = None, setStateVictimTypePAID = None, setStateWeaponDetectedMethodPAID = None, setStudentAssistanceProgramReferral = None, setStudentID = None, setStudentNumber = None, setWeaponDetectionComment = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentInvolvedPersonPA(EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setIncidentVictimComment = None, setInvolvementType = None, setInvolvementTypeCode = None, setLocalLawEnforcementNotified = None, setMedicalTreatmentRequired = None, setNameID = None, setNameOfLocalLawEnforcementContacted = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateAdjudicationPAID = None, setStateArrestedPAID = None, setStateInjurySeverityPAID = None, setStateOffenderTypePAID = None, setStateVictimTypePAID = None, setStateWeaponDetectedMethodPAID = None, setStudentAssistanceProgramReferral = None, setStudentID = None, setStudentNumber = None, setWeaponDetectionComment = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnIncidentVictimComment = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnLocalLawEnforcementNotified = False, returnMedicalTreatmentRequired = False, returnModifiedTime = False, returnNameID = False, returnNameOfLocalLawEnforcementContacted = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateAdjudicationPAID = False, returnStateArrestedPAID = False, returnStateInjurySeverityPAID = False, returnStateOffenderTypePAID = False, returnStateVictimTypePAID = False, returnStateWeaponDetectedMethodPAID = False, returnStudentAssistanceProgramReferral = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponDetectionComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonPA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentInvolvedPersonPA(TempIncidentInvolvedPersonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentInvolvedPersonTX(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentInvolvedPersonID = True, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentInvolvedPersonTX(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = True, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentInvolvedPersonTX(TempIncidentInvolvedPersonID, EntityID = 1, setCampusIDOfDisciplinaryResponsibility = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentInvolvedPersonTX(EntityID = 1, setCampusIDOfDisciplinaryResponsibility = None, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCampusIDOfDisciplinaryResponsibility = False, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonTX/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentInvolvedPersonTX(TempIncidentInvolvedPersonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentInvolvedPersonWA(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentInvolvedPersonWA(TempIncidentInvolvedPersonID, EntityID = 1, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(TempIncidentInvolvedPersonID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentInvolvedPersonWA(TempIncidentInvolvedPersonID, EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateReportedOffense = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/" + str(TempIncidentInvolvedPersonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentInvolvedPersonWA(EntityID = 1, setExcludePrimaryOffense = None, setExistingIncidentOffenseNamesToDelete = None, setFreeformName = None, setFullName = None, setIncidentOffenseNameKey = None, setIncidentOffenseNameType = None, setIncidentOffenseNameTypeCode = None, setInvolvementType = None, setInvolvementTypeCode = None, setNameID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setPrimaryOffenseID = None, setSecondaryOffensesBackingData = None, setStaffID = None, setStaffIDDisciplineOfficer = None, setStateReportedOffense = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempIncidentInvolvedPersonID = True, returnCreatedTime = False, returnExcludePrimaryOffense = False, returnExistingIncidentOffenseNamesToDelete = False, returnFreeformName = False, returnFullName = False, returnIncidentOffenseNameKey = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnModifiedTime = False, returnNameID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnPrimaryOffenseID = False, returnSecondaryOffensesBackingData = False, returnSecondaryOffensesBackingDataDictionary = False, returnStaffID = False, returnStaffIDDisciplineOfficer = False, returnStateReportedOffense = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentInvolvedPersonWA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentInvolvedPersonWA(TempIncidentInvolvedPersonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffense(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseID = True, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffense(TempIncidentOffenseID, EntityID = 1, returnTempIncidentOffenseID = True, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(TempIncidentOffenseID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffense(TempIncidentOffenseID, EntityID = 1, setExistingIncidentID = None, setIsPrimaryOffense = None, setOffenseID = None, setRelationships = None, returnTempIncidentOffenseID = True, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/" + str(TempIncidentOffenseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffense(EntityID = 1, setExistingIncidentID = None, setIsPrimaryOffense = None, setOffenseID = None, setRelationships = None, returnTempIncidentOffenseID = True, returnCreatedTime = False, returnExistingIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffense/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffense(TempIncidentOffenseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseName(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameID = True, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseName(TempIncidentOffenseNameID, EntityID = 1, returnTempIncidentOffenseNameID = True, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(TempIncidentOffenseNameID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseName(TempIncidentOffenseNameID, EntityID = 1, setExistingIncidentOffenseNameID = None, setFullName = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPrimaryOffense = None, setOffenseCodeDescription = None, setOffenseID = None, setOffenseLevelID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setStudentNumber = None, setTempIncidentInvolvedPersonID = None, setTempIncidentOffenseID = None, setRelationships = None, returnTempIncidentOffenseNameID = True, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/" + str(TempIncidentOffenseNameID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseName(EntityID = 1, setExistingIncidentOffenseNameID = None, setFullName = None, setInvolvementType = None, setInvolvementTypeCode = None, setIsPrimaryOffense = None, setOffenseCodeDescription = None, setOffenseID = None, setOffenseLevelID = None, setPerceivedMotivationCodeDescription = None, setPerceivedMotivationID = None, setStudentNumber = None, setTempIncidentInvolvedPersonID = None, setTempIncidentOffenseID = None, setRelationships = None, returnTempIncidentOffenseNameID = True, returnCreatedTime = False, returnExistingIncidentOffenseNameID = False, returnFullName = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOffenseID = False, returnOffenseLevelID = False, returnPerceivedMotivationCodeDescription = False, returnPerceivedMotivationID = False, returnStudentNumber = False, returnTempIncidentInvolvedPersonID = False, returnTempIncidentOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseName/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseName(TempIncidentOffenseNameID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameAction(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameAction(EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameActionDetail(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionDetailID = True, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1, returnTempIncidentOffenseNameActionDetailID = True, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1, setActionCodeDescription = None, setCreateAttendance = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setFullName = None, setIncidentOffenseNameActionDetailID = None, setInvolvementType = None, setIsAlternate = None, setIsPrimaryOffense = None, setLocationID = None, setNewStatus = None, setNewStatusCode = None, setOffenseCodeDescription = None, setOldStatus = None, setOldStatusCode = None, setPartialDayPeriods = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setTempIncidentOffenseNameActionID = None, setRelationships = None, returnTempIncidentOffenseNameActionDetailID = True, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameActionDetail(EntityID = 1, setActionCodeDescription = None, setCreateAttendance = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setFullName = None, setIncidentOffenseNameActionDetailID = None, setInvolvementType = None, setIsAlternate = None, setIsPrimaryOffense = None, setLocationID = None, setNewStatus = None, setNewStatusCode = None, setOffenseCodeDescription = None, setOldStatus = None, setOldStatusCode = None, setPartialDayPeriods = None, setScheduledTime = None, setScheduledTimeDate = None, setScheduledTimeTime = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setTempIncidentOffenseNameActionID = None, setRelationships = None, returnTempIncidentOffenseNameActionDetailID = True, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameActionDetailRecord(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionDetailRecordID = True, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1, returnTempIncidentOffenseNameActionDetailRecordID = True, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1, setBuilding = None, setBuildingID = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setIncidentOffenseNameActionID = None, setIsAlternate = None, setIsGuardianNotified = None, setLocation = None, setLocationID = None, setRoomID = None, setRoomNumber = None, setScheduledTime = None, setStaffFollowUpOfficerName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setRelationships = None, returnTempIncidentOffenseNameActionDetailRecordID = True, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameActionDetailRecord(EntityID = 1, setBuilding = None, setBuildingID = None, setDurationServed = None, setDurationToServe = None, setDurationType = None, setIncidentOffenseNameActionID = None, setIsAlternate = None, setIsGuardianNotified = None, setLocation = None, setLocationID = None, setRoomID = None, setRoomNumber = None, setScheduledTime = None, setStaffFollowUpOfficerName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setRelationships = None, returnTempIncidentOffenseNameActionDetailRecordID = True, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameActionIN(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameActionIN(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameActionIN(TempIncidentOffenseNameActionID, EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateEducationalServiceProvidedINID = None, setStateSuspensionReasonINID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameActionIN(EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateEducationalServiceProvidedINID = None, setStateSuspensionReasonINID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateEducationalServiceProvidedINID = False, returnStateSuspensionReasonINID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionIN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameActionIN(TempIncidentOffenseNameActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameActionMN(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameActionMN(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameActionMN(TempIncidentOffenseNameActionID, EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameActionMN(EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDateExpulsionExclusionEnds = None, setDIRSActionExplanation = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setExclusionThroughYearEnd = None, setExpulsionModified = None, setExpulsionThroughYearEnd = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReturnBeforeYearEnd = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateDIRSAESTypeMNID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameActionMN(TempIncidentOffenseNameActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameActionPA(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameActionPA(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameActionPA(TempIncidentOffenseNameActionID, EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setAssignedAlternativeEducation = None, setBuildingID = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReceivedEducationalServices = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameActionPA(EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setAssignedAlternativeEducation = None, setBuildingID = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setReceivedEducationalServices = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnAssignedAlternativeEducation = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnReceivedEducationalServices = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionPA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameActionPA(TempIncidentOffenseNameActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameActionWA(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameActionWA(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameActionWA(TempIncidentOffenseNameActionID, EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDateReadmissionPetitionGranted = None, setDateReadmissionPetitionSubmitted = None, setDateReengagementMeetingHeld = None, setDurationOfExclusionaryActionDays = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setPlacedInInterimAlternativeEducationalSetting = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateAcademicServiceWAID = None, setStateAppealCodeWAID = None, setStateBehaviorServiceWAID = None, setStatePetitionExtensionExpulsionWAID = None, setStateReengagementPlanWAID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setTotalAmountOfExclusionaryTime = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameActionWA(EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBuildingID = None, setComment = None, setDateReadmissionPetitionGranted = None, setDateReadmissionPetitionSubmitted = None, setDateReengagementMeetingHeld = None, setDurationOfExclusionaryActionDays = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setPlacedInInterimAlternativeEducationalSetting = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateAcademicServiceWAID = None, setStateAppealCodeWAID = None, setStateBehaviorServiceWAID = None, setStatePetitionExtensionExpulsionWAID = None, setStateReengagementPlanWAID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setTotalAmountOfExclusionaryTime = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateReadmissionPetitionGranted = False, returnDateReadmissionPetitionSubmitted = False, returnDateReengagementMeetingHeld = False, returnDurationOfExclusionaryActionDays = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnPlacedInInterimAlternativeEducationalSetting = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateAcademicServiceWAID = False, returnStateAppealCodeWAID = False, returnStateBehaviorServiceWAID = False, returnStatePetitionExtensionExpulsionWAID = False, returnStateReengagementPlanWAID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnTotalAmountOfExclusionaryTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameActionWA(TempIncidentOffenseNameActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameActionWI(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameActionWI(TempIncidentOffenseNameActionID, EntityID = 1, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(TempIncidentOffenseNameActionID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameActionWI(TempIncidentOffenseNameActionID, EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBehaviorDetailedDescription = None, setBuildingID = None, setCausedSeriousBodilyInjury = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setHasEarlyReinstatementCondition = None, setIAESRemovalType = None, setIAESRemovalTypeCode = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateModifiedTermWIID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/" + str(TempIncidentOffenseNameActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameActionWI(EntityID = 1, setActionCodeDescription = None, setActionID = None, setActionTypeCode = None, setActionTypeID = None, setBehaviorDetailedDescription = None, setBuildingID = None, setCausedSeriousBodilyInjury = None, setComment = None, setDurationToServe = None, setDurationType = None, setDurationTypeCode = None, setEntityID = None, setFullName = None, setHasEarlyReinstatementCondition = None, setIAESRemovalType = None, setIAESRemovalTypeCode = None, setInvolvementType = None, setIsGuardianNotified = None, setIsPrimaryOffense = None, setLocationID = None, setOffenseCodeDescription = None, setOrderedDate = None, setPerceivedMotivationCodeDescription = None, setRoomID = None, setStaffIDAuthorizedBy = None, setStaffIDAuthorizedByName = None, setStaffIDFollowUpOfficer = None, setStateModifiedTermWIID = None, setStatus = None, setStatusCode = None, setStudentNumber = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnActionID = False, returnActionTypeCode = False, returnActionTypeID = False, returnBehaviorDetailedDescription = False, returnBuildingID = False, returnCausedSeriousBodilyInjury = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnFullName = False, returnHasEarlyReinstatementCondition = False, returnIAESRemovalType = False, returnIAESRemovalTypeCode = False, returnInvolvementType = False, returnIsGuardianNotified = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDAuthorizedByName = False, returnStaffIDFollowUpOfficer = False, returnStateModifiedTermWIID = False, returnStatus = False, returnStatusCode = False, returnStudentNumber = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionWI/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameActionWI(TempIncidentOffenseNameActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameDrug(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameDrug(TempIncidentOffenseNameDrugID, EntityID = 1, returnTempIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(TempIncidentOffenseNameDrugID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameDrug(TempIncidentOffenseNameDrugID, EntityID = 1, setDrugID = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/" + str(TempIncidentOffenseNameDrugID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameDrug(EntityID = 1, setDrugID = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameDrugID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameDrug/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameDrug(TempIncidentOffenseNameDrugID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameParentalInvolvementPA(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameParentalInvolvementPAID = True, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameParentalInvolvementPA(TempIncidentOffenseNameParentalInvolvementPAID, EntityID = 1, returnTempIncidentOffenseNameParentalInvolvementPAID = True, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(TempIncidentOffenseNameParentalInvolvementPAID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameParentalInvolvementPA(TempIncidentOffenseNameParentalInvolvementPAID, EntityID = 1, setComment = None, setStateParentalInvolvementPAID = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameParentalInvolvementPAID = True, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/" + str(TempIncidentOffenseNameParentalInvolvementPAID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameParentalInvolvementPA(EntityID = 1, setComment = None, setStateParentalInvolvementPAID = None, setTempIncidentOffenseNameID = None, setRelationships = None, returnTempIncidentOffenseNameParentalInvolvementPAID = True, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameParentalInvolvementPAID = False, returnModifiedTime = False, returnStateParentalInvolvementPAID = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameParentalInvolvementPA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameParentalInvolvementPA(TempIncidentOffenseNameParentalInvolvementPAID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameReportRunHistoryRecord(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameReportRunHistoryRecordID = True, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1, returnTempIncidentOffenseNameReportRunHistoryRecordID = True, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1, setColumnHeader1 = None, setColumnHeader10 = None, setColumnHeader2 = None, setColumnHeader3 = None, setColumnHeader4 = None, setColumnHeader5 = None, setColumnHeader6 = None, setColumnHeader7 = None, setColumnHeader8 = None, setColumnHeader9 = None, setDateTime = None, setIncident = None, setIncidentNumber = None, setIncidentOffenseNameID = None, setOffense = None, setStudentID = None, setStudentName = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setRelationships = None, returnTempIncidentOffenseNameReportRunHistoryRecordID = True, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameReportRunHistoryRecord(EntityID = 1, setColumnHeader1 = None, setColumnHeader10 = None, setColumnHeader2 = None, setColumnHeader3 = None, setColumnHeader4 = None, setColumnHeader5 = None, setColumnHeader6 = None, setColumnHeader7 = None, setColumnHeader8 = None, setColumnHeader9 = None, setDateTime = None, setIncident = None, setIncidentNumber = None, setIncidentOffenseNameID = None, setOffense = None, setStudentID = None, setStudentName = None, setUnboundBody = None, setUnboundFooter = None, setUnboundHeader = None, setRelationships = None, returnTempIncidentOffenseNameReportRunHistoryRecordID = True, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameWeapon(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameWeapon(TempIncidentOffenseNameWeaponID, EntityID = 1, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(TempIncidentOffenseNameWeaponID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameWeapon(TempIncidentOffenseNameWeaponID, EntityID = 1, setTempIncidentOffenseNameID = None, setWeaponID = None, setRelationships = None, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/" + str(TempIncidentOffenseNameWeaponID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameWeapon(EntityID = 1, setTempIncidentOffenseNameID = None, setWeaponID = None, setRelationships = None, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnIncidentOffenseNameWeaponID = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeapon/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameWeapon(TempIncidentOffenseNameWeaponID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempIncidentOffenseNameWeaponMN(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempIncidentOffenseNameWeaponMN(TempIncidentOffenseNameWeaponID, EntityID = 1, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(TempIncidentOffenseNameWeaponID), verb = "get", return_params_list = return_params_list)

def modifyTempIncidentOffenseNameWeaponMN(TempIncidentOffenseNameWeaponID, EntityID = 1, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setTempIncidentOffenseNameID = None, setWeaponID = None, setRelationships = None, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/" + str(TempIncidentOffenseNameWeaponID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempIncidentOffenseNameWeaponMN(EntityID = 1, setGunFoundInTrunk = None, setGunWasInCase = None, setGunWasLoaded = None, setMeetsFederalStatuteOfDangerousWeapon = None, setMeetsStateStatuteOfDangerousWeapon = None, setTempIncidentOffenseNameID = None, setWeaponID = None, setRelationships = None, returnTempIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameWeaponID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnTempIncidentOffenseNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameWeaponMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempIncidentOffenseNameWeaponMN(TempIncidentOffenseNameWeaponID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryWeapon(EntityID = 1, page = 1, pageSize = 100, returnWeaponID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getWeapon(WeaponID, EntityID = 1, returnWeaponID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "get", return_params_list = return_params_list)

def modifyWeapon(WeaponID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setSchoolYearID = None, setStatePelletGunTypeMNID = None, setStateWeaponTypeMNID = None, setWeaponIDClonedFrom = None, setRelationships = None, returnWeaponID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createWeapon(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setSchoolYearID = None, setStatePelletGunTypeMNID = None, setStateWeaponTypeMNID = None, setWeaponIDClonedFrom = None, setRelationships = None, returnWeaponID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteWeapon(WeaponID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")