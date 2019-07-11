# This module contains Discipline functions.

from .Utilities import make_request

import pandas as pd

def getEveryActionAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnActionAttendanceTypeID = True, returnActionID = False, returnAttendanceTypeID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getActionAttendanceType(ActionAttendanceTypeID, EntityID = 1, returnreturnActionAttendanceTypeID = False, returnreturnActionID = False, returnreturnAttendanceTypeID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteActionAttendanceType(ActionAttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionAttendanceType/" + str(ActionAttendanceTypeID), verb = "delete")

	return(response)

def getEveryAction(EntityID = 1, page = 1, pageSize = 100, returnActionID = True, returnActionIDClonedFrom = False, returnActionMNID = False, returnActionTypeID = False, returnCode = False, returnCodeDescription = False, returnCreateAttendanceForActionDetail = False, returnCreatedTime = False, returnDefaultDuration = False, returnDefaultLocationID = False, returnDescription = False, returnDistrictID = False, returnDurationType = False, returnDurationTypeCode = False, returnFederalDisciplineCategoryID = False, returnModifiedTime = False, returnRestraintSeclusion = False, returnRestraintSeclusionCode = False, returnSchoolYearID = False, returnStateActionTypeMNID = False, returnSuppressCreationOfActionDetails = False, returnTransferToAlternativeSchool = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAction(ActionID, EntityID = 1, returnreturnActionID = False, returnreturnActionIDClonedFrom = False, returnreturnActionMNID = False, returnreturnActionTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreateAttendanceForActionDetail = False, returnreturnCreatedTime = False, returnreturnDefaultDuration = False, returnreturnDefaultLocationID = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnDurationType = False, returnreturnDurationTypeCode = False, returnreturnFederalDisciplineCategoryID = False, returnreturnModifiedTime = False, returnreturnRestraintSeclusion = False, returnreturnRestraintSeclusionCode = False, returnreturnSchoolYearID = False, returnreturnStateActionTypeMNID = False, returnreturnSuppressCreationOfActionDetails = False, returnreturnTransferToAlternativeSchool = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "get", params_list = params_list)

	return(response)

def deleteAction(ActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Action/" + str(ActionID), verb = "delete")

	return(response)

def getEveryActionType(EntityID = 1, page = 1, pageSize = 100, returnActionTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsInvalid = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidYearHigh = False, returnValidYearLow = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getActionType(ActionTypeID, EntityID = 1, returnreturnActionTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsInvalid = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValidYearHigh = False, returnreturnValidYearLow = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteActionType(ActionTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ActionType/" + str(ActionTypeID), verb = "delete")

	return(response)

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnAllowActionRecommendationsOnReferrals = False, returnAllowActionTypeUpdate = False, returnAllowDurationTypeUpdate = False, returnAllowOnlyOneOffensePerIncident = False, returnAllowUseOfWarning = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnDefaultActionValueFromPreviousPerson = False, returnDefaultDisciplineScreenDateAndTimes = False, returnDefaultOffenseValueFromPreviousPerson = False, returnDisplayInvolvedPersonsFromAllEntities = False, returnDisplayStudentOffensesForAllEntities = False, returnDisplayWarningsInFamilyAndStudentAccess = False, returnDistrictID = False, returnModifiedTime = False, returnRestartIncidentNumberThisYear = False, returnSchoolYearID = False, returnUseIncidentBuildingAndRoom = False, returnUsePerceivedMotivation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnreturnConfigDistrictYearID = False, returnreturnAllowActionRecommendationsOnReferrals = False, returnreturnAllowActionTypeUpdate = False, returnreturnAllowDurationTypeUpdate = False, returnreturnAllowOnlyOneOffensePerIncident = False, returnreturnAllowUseOfWarning = False, returnreturnConfigDistrictYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDaysToDelayDisplayOfIncidentsInFamilyAndStudentAccess = False, returnreturnDefaultActionValueFromPreviousPerson = False, returnreturnDefaultDisciplineScreenDateAndTimes = False, returnreturnDefaultOffenseValueFromPreviousPerson = False, returnreturnDisplayInvolvedPersonsFromAllEntities = False, returnreturnDisplayStudentOffensesForAllEntities = False, returnreturnDisplayWarningsInFamilyAndStudentAccess = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnRestartIncidentNumberThisYear = False, returnreturnSchoolYearID = False, returnreturnUseIncidentBuildingAndRoom = False, returnreturnUsePerceivedMotivation = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnActionStatusDefaultValue = False, returnActionStatusDefaultValueCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDefaultActionStatusCode = False, returnDetentionsOnFri = False, returnDetentionsOnMon = False, returnDetentionsOnSat = False, returnDetentionsOnSun = False, returnDetentionsOnThu = False, returnDetentionsOnTue = False, returnDetentionsOnWed = False, returnEntityGroupKey = False, returnEntityID = False, returnExpulsionsOnFri = False, returnExpulsionsOnMon = False, returnExpulsionsOnSat = False, returnExpulsionsOnSun = False, returnExpulsionsOnThu = False, returnExpulsionsOnTue = False, returnExpulsionsOnWed = False, returnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnInSchoolSuspensionsOnFri = False, returnInSchoolSuspensionsOnMon = False, returnInSchoolSuspensionsOnSat = False, returnInSchoolSuspensionsOnSun = False, returnInSchoolSuspensionsOnThu = False, returnInSchoolSuspensionsOnTue = False, returnInSchoolSuspensionsOnWed = False, returnModifiedTime = False, returnOutOfSchoolSuspensionsOnFri = False, returnOutOfSchoolSuspensionsOnMon = False, returnOutOfSchoolSuspensionsOnSat = False, returnOutOfSchoolSuspensionsOnSun = False, returnOutOfSchoolSuspensionsOnThu = False, returnOutOfSchoolSuspensionsOnTue = False, returnOutOfSchoolSuspensionsOnWed = False, returnSchoolYearID = False, returnTardyKioskDisciplineSlipTitle = False, returnUseAlternateActionDetails = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnreturnConfigEntityGroupYearID = False, returnreturnActionStatusDefaultValue = False, returnreturnActionStatusDefaultValueCode = False, returnreturnConfigEntityGroupYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDefaultActionStatusCode = False, returnreturnDetentionsOnFri = False, returnreturnDetentionsOnMon = False, returnreturnDetentionsOnSat = False, returnreturnDetentionsOnSun = False, returnreturnDetentionsOnThu = False, returnreturnDetentionsOnTue = False, returnreturnDetentionsOnWed = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnExpulsionsOnFri = False, returnreturnExpulsionsOnMon = False, returnreturnExpulsionsOnSat = False, returnreturnExpulsionsOnSun = False, returnreturnExpulsionsOnThu = False, returnreturnExpulsionsOnTue = False, returnreturnExpulsionsOnWed = False, returnreturnIncludeDisciplinaryActionAndDetailsOnLetter = False, returnreturnIncludeGradeLevelOnLetter = False, returnreturnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnreturnIncludeSchoolOrCampusOnLetter = False, returnreturnIncludeSignatureLineForOfficeOnLetter = False, returnreturnIncludeSignatureLineForParentOnLetter = False, returnreturnIncludeSignatureLineForStudentOnLetter = False, returnreturnIncludeStudentNameAndOrNumberOnLetter = False, returnreturnInSchoolSuspensionsOnFri = False, returnreturnInSchoolSuspensionsOnMon = False, returnreturnInSchoolSuspensionsOnSat = False, returnreturnInSchoolSuspensionsOnSun = False, returnreturnInSchoolSuspensionsOnThu = False, returnreturnInSchoolSuspensionsOnTue = False, returnreturnInSchoolSuspensionsOnWed = False, returnreturnModifiedTime = False, returnreturnOutOfSchoolSuspensionsOnFri = False, returnreturnOutOfSchoolSuspensionsOnMon = False, returnreturnOutOfSchoolSuspensionsOnSat = False, returnreturnOutOfSchoolSuspensionsOnSun = False, returnreturnOutOfSchoolSuspensionsOnThu = False, returnreturnOutOfSchoolSuspensionsOnTue = False, returnreturnOutOfSchoolSuspensionsOnWed = False, returnreturnSchoolYearID = False, returnreturnTardyKioskDisciplineSlipTitle = False, returnreturnUseAlternateActionDetails = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getEveryConfigEntityYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnreturnConfigEntityYearID = False, returnreturnConfigEntityYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "delete")

	return(response)

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnAllowIncidentSuppression = False, returnCreatedTime = False, returnModifiedTime = False, returnReportIDDisciplineLetter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigSystem(ConfigSystemID, EntityID = 1, returnreturnConfigSystemID = False, returnreturnAllowIncidentSuppression = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnReportIDDisciplineLetter = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/ConfigSystem/" + str(ConfigSystemID), verb = "delete")

	return(response)

def getEveryDisciplineLetterRunHistory(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterRunHistoryID = True, returnCreatedTime = False, returnDate = False, returnDisciplineLetterTemplateID = False, returnEndDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIncidentType = False, returnIncidentTypeCode = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnReportRunInfoID = False, returnRunDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1, returnreturnDisciplineLetterRunHistoryID = False, returnreturnCreatedTime = False, returnreturnDate = False, returnreturnDisciplineLetterTemplateID = False, returnreturnEndDate = False, returnreturnEntityID = False, returnreturnFilterType = False, returnreturnFilterTypeCode = False, returnreturnGracePeriod = False, returnreturnIncidentType = False, returnreturnIncidentTypeCode = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnParameterData = False, returnreturnParameterDescription = False, returnreturnReportRunInfoID = False, returnreturnRunDescription = False, returnreturnStartDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterRunHistory(DisciplineLetterRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistory/" + str(DisciplineLetterRunHistoryID), verb = "delete")

	return(response)

def getEveryDisciplineLetterRunHistoryAction(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterRunHistoryActionID = True, returnActionID = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1, returnreturnDisciplineLetterRunHistoryActionID = False, returnreturnActionID = False, returnreturnCreatedTime = False, returnreturnDisciplineLetterRunHistoryID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterRunHistoryAction(DisciplineLetterRunHistoryActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryAction/" + str(DisciplineLetterRunHistoryActionID), verb = "delete")

	return(response)

def getEveryDisciplineLetterRunHistoryOffense(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterRunHistoryOffenseID = True, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1, returnreturnDisciplineLetterRunHistoryOffenseID = False, returnreturnCreatedTime = False, returnreturnDisciplineLetterRunHistoryID = False, returnreturnModifiedTime = False, returnreturnOffenseID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterRunHistoryOffense(DisciplineLetterRunHistoryOffenseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterRunHistoryOffense/" + str(DisciplineLetterRunHistoryOffenseID), verb = "delete")

	return(response)

def getEveryDisciplineLetterTemplate(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateID = True, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBody = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCreatedTime = False, returnDescription = False, returnDisciplineLetterTemplateIDClonedFrom = False, returnDistrictID = False, returnFooter = False, returnForCurrentEntity = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHeader = False, returnIsDefault = False, returnMediaIDLogo = False, returnModifiedTime = False, returnPrintSingleColumn1 = False, returnPrintSingleColumn10 = False, returnPrintSingleColumn2 = False, returnPrintSingleColumn3 = False, returnPrintSingleColumn4 = False, returnPrintSingleColumn5 = False, returnPrintSingleColumn6 = False, returnPrintSingleColumn7 = False, returnPrintSingleColumn8 = False, returnPrintSingleColumn9 = False, returnSchoolYearID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnSuperintendentNameFormat = False, returnSuperintendentNameFormatCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1, returnreturnDisciplineLetterTemplateID = False, returnreturnAdvisorNameFormat = False, returnreturnAdvisorNameFormatCode = False, returnreturnBody = False, returnreturnColumnHeaderLabel1 = False, returnreturnColumnHeaderLabel10 = False, returnreturnColumnHeaderLabel2 = False, returnreturnColumnHeaderLabel3 = False, returnreturnColumnHeaderLabel4 = False, returnreturnColumnHeaderLabel5 = False, returnreturnColumnHeaderLabel6 = False, returnreturnColumnHeaderLabel7 = False, returnreturnColumnHeaderLabel8 = False, returnreturnColumnHeaderLabel9 = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisciplineLetterTemplateIDClonedFrom = False, returnreturnDistrictID = False, returnreturnFooter = False, returnreturnForCurrentEntity = False, returnreturnGuardianNameFormat = False, returnreturnGuardianNameFormatCode = False, returnreturnHasLogo = False, returnreturnHeader = False, returnreturnIsDefault = False, returnreturnMediaIDLogo = False, returnreturnModifiedTime = False, returnreturnPrintSingleColumn1 = False, returnreturnPrintSingleColumn10 = False, returnreturnPrintSingleColumn2 = False, returnreturnPrintSingleColumn3 = False, returnreturnPrintSingleColumn4 = False, returnreturnPrintSingleColumn5 = False, returnreturnPrintSingleColumn6 = False, returnreturnPrintSingleColumn7 = False, returnreturnPrintSingleColumn8 = False, returnreturnPrintSingleColumn9 = False, returnreturnSchoolYearID = False, returnreturnStudentNameFormat = False, returnreturnStudentNameFormatCode = False, returnreturnSuperintendentNameFormat = False, returnreturnSuperintendentNameFormatCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplate(DisciplineLetterTemplateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplate/" + str(DisciplineLetterTemplateID), verb = "delete")

	return(response)

def getEveryDisciplineLetterTemplateEntity(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateEntityID = True, returnCreatedTime = False, returnDisciplineLetterTemplateID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1, returnreturnDisciplineLetterTemplateEntityID = False, returnreturnCreatedTime = False, returnreturnDisciplineLetterTemplateID = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateEntity(DisciplineLetterTemplateEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateEntity/" + str(DisciplineLetterTemplateEntityID), verb = "delete")

	return(response)

def getEveryDisciplineLetterTemplateField(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateFieldID = True, returnCreatedTime = False, returnDescription = False, returnFieldPath = False, returnFriendlyName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1, returnreturnDisciplineLetterTemplateFieldID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnFieldPath = False, returnreturnFriendlyName = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(DisciplineLetterTemplateFieldID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateField(DisciplineLetterTemplateFieldID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateField/" + str(DisciplineLetterTemplateFieldID), verb = "delete")

	return(response)

def getEveryDisciplineLetterTemplateHeaderColumn(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateHeaderColumnID = True, returnColumnNumber = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnDisciplineLetterTemplateHeaderRowID = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnLabelOverride = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1, returnreturnDisciplineLetterTemplateHeaderColumnID = False, returnreturnColumnNumber = False, returnreturnCreatedTime = False, returnreturnDisciplineLetterTemplateHeaderColumnIDClonedFrom = False, returnreturnDisciplineLetterTemplateHeaderRowID = False, returnreturnFieldType = False, returnreturnFieldTypeCode = False, returnreturnFreeformText = False, returnreturnLabelOverride = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateHeaderColumn(DisciplineLetterTemplateHeaderColumnID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderColumn/" + str(DisciplineLetterTemplateHeaderColumnID), verb = "delete")

	return(response)

def getEveryDisciplineLetterTemplateHeaderRow(EntityID = 1, page = 1, pageSize = 100, returnDisciplineLetterTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnDisciplineLetterTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1, returnreturnDisciplineLetterTemplateHeaderRowID = False, returnreturnColumnCount = False, returnreturnCreatedTime = False, returnreturnDisciplineLetterTemplateHeaderRowIDClonedFrom = False, returnreturnDisciplineLetterTemplateID = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "get", params_list = params_list)

	return(response)

def deleteDisciplineLetterTemplateHeaderRow(DisciplineLetterTemplateHeaderRowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/DisciplineLetterTemplateHeaderRow/" + str(DisciplineLetterTemplateHeaderRowID), verb = "delete")

	return(response)

def getEveryDrug(EntityID = 1, page = 1, pageSize = 100, returnDrugID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDrugIDClonedFrom = False, returnDrugMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateDrugTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDrug(DrugID, EntityID = 1, returnreturnDrugID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnDrugIDClonedFrom = False, returnreturnDrugMNID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStateDrugTypeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "get", params_list = params_list)

	return(response)

def deleteDrug(DrugID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Drug/" + str(DrugID), verb = "delete")

	return(response)

def getEveryIncident(EntityID = 1, page = 1, pageSize = 100, returnIncidentID = True, returnActionIDRecommended = False, returnBuildingID = False, returnCreatedTime = False, returnDamageCost = False, returnDateTime = False, returnDateTimeDate = False, returnDateTimeTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnHasActions = False, returnHasActionsForOffenders = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentMNID = False, returnIncidentNumber = False, returnIncidentNumberValue = False, returnIsIncidentOrWarning = False, returnIsReferralOrWarning = False, returnIsSuppressed = False, returnLocationID = False, returnModifiedTime = False, returnNumberOfNonEnrolledOffenders = False, returnNumberOfNonEnrolledVictims = False, returnReferredByFreeformName = False, returnReferredByName = False, returnReferredByNameID = False, returnReferredByType = False, returnReferredByTypeCode = False, returnReportedToLawEnforcement = False, returnRoomID = False, returnSchoolYearID = False, returnStateDIRSTimeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncident(IncidentID, EntityID = 1, returnreturnIncidentID = False, returnreturnActionIDRecommended = False, returnreturnBuildingID = False, returnreturnCreatedTime = False, returnreturnDamageCost = False, returnreturnDateTime = False, returnreturnDateTimeDate = False, returnreturnDateTimeTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEntityID = False, returnreturnHasActions = False, returnreturnHasActionsForOffenders = False, returnreturnHasDrugs = False, returnreturnHasOpenActions = False, returnreturnHasOverdueActionDetails = False, returnreturnHasWeapons = False, returnreturnIncidentMNID = False, returnreturnIncidentNumber = False, returnreturnIncidentNumberValue = False, returnreturnIsIncidentOrWarning = False, returnreturnIsReferralOrWarning = False, returnreturnIsSuppressed = False, returnreturnLocationID = False, returnreturnModifiedTime = False, returnreturnNumberOfNonEnrolledOffenders = False, returnreturnNumberOfNonEnrolledVictims = False, returnreturnReferredByFreeformName = False, returnreturnReferredByName = False, returnreturnReferredByNameID = False, returnreturnReferredByType = False, returnreturnReferredByTypeCode = False, returnreturnReportedToLawEnforcement = False, returnreturnRoomID = False, returnreturnSchoolYearID = False, returnreturnStateDIRSTimeMNID = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "get", params_list = params_list)

	return(response)

def deleteIncident(IncidentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Incident/" + str(IncidentID), verb = "delete")

	return(response)

def getEveryIncidentOffense(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseID = True, returnCreatedTime = False, returnHasActions = False, returnHasDrugs = False, returnHasWeapons = False, returnIncidentID = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffense(IncidentOffenseID, EntityID = 1, returnreturnIncidentOffenseID = False, returnreturnCreatedTime = False, returnreturnHasActions = False, returnreturnHasDrugs = False, returnreturnHasWeapons = False, returnreturnIncidentID = False, returnreturnIsPrimaryOffense = False, returnreturnModifiedTime = False, returnreturnOffenseID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffense(IncidentOffenseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffense/" + str(IncidentOffenseID), verb = "delete")

	return(response)

def getEveryIncidentOffenseNameActionDetail(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameActionDetailID = True, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDurationServed = False, returnDurationServedWithLabel = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLastAlternate = False, returnLocationID = False, returnModifiedTime = False, returnOverdue = False, returnPartialDayPeriods = False, returnPrintComment = False, returnRenderReissueOption = False, returnRoomID = False, returnScheduledTime = False, returnScheduledTimeDate = False, returnScheduledTimeTime = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1, returnreturnIncidentOffenseNameActionDetailID = False, returnreturnBuildingID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnDurationServed = False, returnreturnDurationServedWithLabel = False, returnreturnDurationToServe = False, returnreturnDurationToServeWithLabel = False, returnreturnIncidentOffenseNameActionID = False, returnreturnIsAlternate = False, returnreturnIsGuardianNotified = False, returnreturnLastAlternate = False, returnreturnLocationID = False, returnreturnModifiedTime = False, returnreturnOverdue = False, returnreturnPartialDayPeriods = False, returnreturnPrintComment = False, returnreturnRenderReissueOption = False, returnreturnRoomID = False, returnreturnScheduledTime = False, returnreturnScheduledTimeDate = False, returnreturnScheduledTimeTime = False, returnreturnStaffIDFollowUpOfficer = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameActionDetail(IncidentOffenseNameActionDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetail/" + str(IncidentOffenseNameActionDetailID), verb = "delete")

	return(response)

def getEveryIncidentOffenseNameActionDetailPeriod(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameActionDetailPeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1, returnreturnIncidentOffenseNameActionDetailPeriodID = False, returnreturnAttendancePeriodID = False, returnreturnCreatedTime = False, returnreturnIncidentOffenseNameActionDetailID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameActionDetailPeriod(IncidentOffenseNameActionDetailPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameActionDetailPeriod/" + str(IncidentOffenseNameActionDetailPeriodID), verb = "delete")

	return(response)

def getEveryIncidentOffenseNameAction(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameActionID = True, returnActionID = False, returnActionTypeID = False, returnActualDurationServed = False, returnBuildingID = False, returnComment = False, returnCreatedTime = False, returnDateExpulsionExclusionEnds = False, returnDIRSActionExplanation = False, returnDurationServed = False, returnDurationServedOverride = False, returnDurationToServe = False, returnDurationToServeWithLabel = False, returnDurationType = False, returnDurationTypeCode = False, returnEntityID = False, returnExclusionThroughYearEnd = False, returnExpulsionModified = False, returnExpulsionThroughYearEnd = False, returnFirstActionDetailDateNorthEastExport = False, returnIncidentOffenseNameActionMNID = False, returnIncidentOffenseNameID = False, returnIsGuardianNotified = False, returnLastActionDetailDateNorthEastExport = False, returnLocationID = False, returnModifiedTime = False, returnOrderedDate = False, returnOrderedDateAge = False, returnReturnBeforeYearEnd = False, returnRoomID = False, returnStaffIDAuthorizedBy = False, returnStaffIDFollowUpOfficer = False, returnStateDIRSAESTypeMNID = False, returnStatus = False, returnStatusCode = False, returnTotalDurationServed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1, returnreturnIncidentOffenseNameActionID = False, returnreturnActionID = False, returnreturnActionTypeID = False, returnreturnActualDurationServed = False, returnreturnBuildingID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnDateExpulsionExclusionEnds = False, returnreturnDIRSActionExplanation = False, returnreturnDurationServed = False, returnreturnDurationServedOverride = False, returnreturnDurationToServe = False, returnreturnDurationToServeWithLabel = False, returnreturnDurationType = False, returnreturnDurationTypeCode = False, returnreturnEntityID = False, returnreturnExclusionThroughYearEnd = False, returnreturnExpulsionModified = False, returnreturnExpulsionThroughYearEnd = False, returnreturnFirstActionDetailDateNorthEastExport = False, returnreturnIncidentOffenseNameActionMNID = False, returnreturnIncidentOffenseNameID = False, returnreturnIsGuardianNotified = False, returnreturnLastActionDetailDateNorthEastExport = False, returnreturnLocationID = False, returnreturnModifiedTime = False, returnreturnOrderedDate = False, returnreturnOrderedDateAge = False, returnreturnReturnBeforeYearEnd = False, returnreturnRoomID = False, returnreturnStaffIDAuthorizedBy = False, returnreturnStaffIDFollowUpOfficer = False, returnreturnStateDIRSAESTypeMNID = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnTotalDurationServed = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameAction(IncidentOffenseNameActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameAction/" + str(IncidentOffenseNameActionID), verb = "delete")

	return(response)

def getEveryIncidentOffenseNameDrug(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameDrugID = True, returnCreatedTime = False, returnDrugID = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1, returnreturnIncidentOffenseNameDrugID = False, returnreturnCreatedTime = False, returnreturnDrugID = False, returnreturnIncidentOffenseNameID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameDrug(IncidentOffenseNameDrugID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameDrug/" + str(IncidentOffenseNameDrugID), verb = "delete")

	return(response)

def getEveryIncidentOffenseName(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameID = True, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnFirstDrugCodeforNorthEastExport = False, returnFreeformName = False, returnHasActions = False, returnHasDangerousWeapons = False, returnHasDrugs = False, returnHasOpenActions = False, returnHasOverdueActionDetails = False, returnHasWeapons = False, returnIncidentOffenseID = False, returnIncidentOffenseNameMNID = False, returnIncidentOffenseNameType = False, returnIncidentOffenseNameTypeCode = False, returnInjuryOccured = False, returnInvolvementType = False, returnInvolvementTypeCode = False, returnIsGuardianNotified = False, returnIsPhysicalAssault = False, returnIsPhysicalAssaultState = False, returnIsStudentOffender = False, returnModifiedTime = False, returnNameID = False, returnNorthEastExportAttendancePeriods = False, returnNorthEastExportOffenseCodes = False, returnOffenderArrestedByLawEnforcement = False, returnOffenseLevelID = False, returnPerceivedMotivationID = False, returnPersonalName = False, returnReportedToLawEnforcement = False, returnStaffIDDisciplineOfficer = False, returnStatement = False, returnStateOffenderActivityMNID = False, returnStateVictimCostMNID = False, returnStateVictimTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWasSeriousBodilyInjury = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffenseName(IncidentOffenseNameID, EntityID = 1, returnreturnIncidentOffenseNameID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnFirstDrugCodeforNorthEastExport = False, returnreturnFreeformName = False, returnreturnHasActions = False, returnreturnHasDangerousWeapons = False, returnreturnHasDrugs = False, returnreturnHasOpenActions = False, returnreturnHasOverdueActionDetails = False, returnreturnHasWeapons = False, returnreturnIncidentOffenseID = False, returnreturnIncidentOffenseNameMNID = False, returnreturnIncidentOffenseNameType = False, returnreturnIncidentOffenseNameTypeCode = False, returnreturnInjuryOccured = False, returnreturnInvolvementType = False, returnreturnInvolvementTypeCode = False, returnreturnIsGuardianNotified = False, returnreturnIsPhysicalAssault = False, returnreturnIsPhysicalAssaultState = False, returnreturnIsStudentOffender = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNorthEastExportAttendancePeriods = False, returnreturnNorthEastExportOffenseCodes = False, returnreturnOffenderArrestedByLawEnforcement = False, returnreturnOffenseLevelID = False, returnreturnPerceivedMotivationID = False, returnreturnPersonalName = False, returnreturnReportedToLawEnforcement = False, returnreturnStaffIDDisciplineOfficer = False, returnreturnStatement = False, returnreturnStateOffenderActivityMNID = False, returnreturnStateVictimCostMNID = False, returnreturnStateVictimTypeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWasSeriousBodilyInjury = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseName(IncidentOffenseNameID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseName/" + str(IncidentOffenseNameID), verb = "delete")

	return(response)

def getEveryIncidentOffenseNameReportRunHistory(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameReportRunHistoryID = True, returnAttachmentID = False, returnColumnHeaderData1 = False, returnColumnHeaderData10 = False, returnColumnHeaderData2 = False, returnColumnHeaderData3 = False, returnColumnHeaderData4 = False, returnColumnHeaderData5 = False, returnColumnHeaderData6 = False, returnColumnHeaderData7 = False, returnColumnHeaderData8 = False, returnColumnHeaderData9 = False, returnCreatedTime = False, returnDisciplineLetterRunHistoryID = False, returnIncidentOffenseNameID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1, returnreturnIncidentOffenseNameReportRunHistoryID = False, returnreturnAttachmentID = False, returnreturnColumnHeaderData1 = False, returnreturnColumnHeaderData10 = False, returnreturnColumnHeaderData2 = False, returnreturnColumnHeaderData3 = False, returnreturnColumnHeaderData4 = False, returnreturnColumnHeaderData5 = False, returnreturnColumnHeaderData6 = False, returnreturnColumnHeaderData7 = False, returnreturnColumnHeaderData8 = False, returnreturnColumnHeaderData9 = False, returnreturnCreatedTime = False, returnreturnDisciplineLetterRunHistoryID = False, returnreturnIncidentOffenseNameID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnStudentID = False, returnreturnUnboundBody = False, returnreturnUnboundFooter = False, returnreturnUnboundHeader = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameReportRunHistory(IncidentOffenseNameReportRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameReportRunHistory/" + str(IncidentOffenseNameReportRunHistoryID), verb = "delete")

	return(response)

def getEveryIncidentOffenseNameWeapon(EntityID = 1, page = 1, pageSize = 100, returnIncidentOffenseNameWeaponID = True, returnCreatedTime = False, returnGunFoundInTrunk = False, returnGunWasInCase = False, returnGunWasLoaded = False, returnIncidentOffenseNameID = False, returnIncidentOffenseNameWeaponMNID = False, returnMeetsFederalStatuteOfDangerousWeapon = False, returnMeetsStateStatuteOfDangerousWeapon = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1, returnreturnIncidentOffenseNameWeaponID = False, returnreturnCreatedTime = False, returnreturnGunFoundInTrunk = False, returnreturnGunWasInCase = False, returnreturnGunWasLoaded = False, returnreturnIncidentOffenseNameID = False, returnreturnIncidentOffenseNameWeaponMNID = False, returnreturnMeetsFederalStatuteOfDangerousWeapon = False, returnreturnMeetsStateStatuteOfDangerousWeapon = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeaponID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "get", params_list = params_list)

	return(response)

def deleteIncidentOffenseNameWeapon(IncidentOffenseNameWeaponID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/IncidentOffenseNameWeapon/" + str(IncidentOffenseNameWeaponID), verb = "delete")

	return(response)

def getEveryLocation(EntityID = 1, page = 1, pageSize = 100, returnLocationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiIncidentLocationID = False, returnLocationMNID = False, returnModifiedTime = False, returnStateIncidentLocationMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getLocation(LocationID, EntityID = 1, returnreturnLocationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEdFiIncidentLocationID = False, returnreturnLocationMNID = False, returnreturnModifiedTime = False, returnreturnStateIncidentLocationMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "get", params_list = params_list)

	return(response)

def deleteLocation(LocationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Location/" + str(LocationID), verb = "delete")

	return(response)

def getEveryNextIncidentNumber(EntityID = 1, page = 1, pageSize = 100, returnNextIncidentNumberID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnSequenceNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNextIncidentNumber(NextIncidentNumberID, EntityID = 1, returnreturnNextIncidentNumberID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnSequenceNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "get", params_list = params_list)

	return(response)

def deleteNextIncidentNumber(NextIncidentNumberID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/NextIncidentNumber/" + str(NextIncidentNumberID), verb = "delete")

	return(response)

def getEveryOffense(EntityID = 1, page = 1, pageSize = 100, returnOffenseID = True, returnAllowActionRecommendations = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultActionID = False, returnDescription = False, returnDistrictID = False, returnFederalOffenseCategoryID = False, returnHarassmentBullying = False, returnHarassmentBullyingCode = False, returnIsDrugRelated = False, returnIsInjuryThreat = False, returnIsWeaponRelated = False, returnModifiedTime = False, returnOffenseIDClonedFrom = False, returnOffenseLevelIDDefault = False, returnRestrictActions = False, returnSchoolYearID = False, returnUseForReferral = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOffense(OffenseID, EntityID = 1, returnreturnOffenseID = False, returnreturnAllowActionRecommendations = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDefaultActionID = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnFederalOffenseCategoryID = False, returnreturnHarassmentBullying = False, returnreturnHarassmentBullyingCode = False, returnreturnIsDrugRelated = False, returnreturnIsInjuryThreat = False, returnreturnIsWeaponRelated = False, returnreturnModifiedTime = False, returnreturnOffenseIDClonedFrom = False, returnreturnOffenseLevelIDDefault = False, returnreturnRestrictActions = False, returnreturnSchoolYearID = False, returnreturnUseForReferral = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "get", params_list = params_list)

	return(response)

def deleteOffense(OffenseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Offense/" + str(OffenseID), verb = "delete")

	return(response)

def getEveryOffenseAction(EntityID = 1, page = 1, pageSize = 100, returnOffenseActionID = True, returnActionID = False, returnCreatedTime = False, returnIsReferralAction = False, returnModifiedTime = False, returnOffenseActionIDClonedFrom = False, returnOffenseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOffenseAction(OffenseActionID, EntityID = 1, returnreturnOffenseActionID = False, returnreturnActionID = False, returnreturnCreatedTime = False, returnreturnIsReferralAction = False, returnreturnModifiedTime = False, returnreturnOffenseActionIDClonedFrom = False, returnreturnOffenseID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "get", params_list = params_list)

	return(response)

def deleteOffenseAction(OffenseActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseAction/" + str(OffenseActionID), verb = "delete")

	return(response)

def getEveryOffenseLevel(EntityID = 1, page = 1, pageSize = 100, returnOffenseLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnOffenseLevelIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOffenseLevel(OffenseLevelID, EntityID = 1, returnreturnOffenseLevelID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnOffenseLevelIDClonedFrom = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteOffenseLevel(OffenseLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/OffenseLevel/" + str(OffenseLevelID), verb = "delete")

	return(response)

def getEveryPerceivedMotivation(EntityID = 1, page = 1, pageSize = 100, returnPerceivedMotivationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnPerceivedMotivationIDClonedFrom = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPerceivedMotivation(PerceivedMotivationID, EntityID = 1, returnreturnPerceivedMotivationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnPerceivedMotivationIDClonedFrom = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "get", params_list = params_list)

	return(response)

def deletePerceivedMotivation(PerceivedMotivationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/PerceivedMotivation/" + str(PerceivedMotivationID), verb = "delete")

	return(response)

def getEveryTempIncidentOffenseNameAction(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionID = True, returnActionCodeDescription = False, returnComment = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnInvolvementType = False, returnIsPrimaryOffense = False, returnModifiedTime = False, returnOffenseCodeDescription = False, returnOrderedDate = False, returnPerceivedMotivationCodeDescription = False, returnStaffIDAuthorizedByName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1, returnreturnTempIncidentOffenseNameActionID = False, returnreturnActionCodeDescription = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnDurationToServe = False, returnreturnDurationType = False, returnreturnFullName = False, returnreturnInvolvementType = False, returnreturnIsPrimaryOffense = False, returnreturnModifiedTime = False, returnreturnOffenseCodeDescription = False, returnreturnOrderedDate = False, returnreturnPerceivedMotivationCodeDescription = False, returnreturnStaffIDAuthorizedByName = False, returnreturnStudentNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameAction(TempIncidentOffenseNameActionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameAction/" + str(TempIncidentOffenseNameActionID), verb = "delete")

	return(response)

def getEveryTempIncidentOffenseNameActionDetail(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionDetailID = True, returnActionCodeDescription = False, returnCreateAttendance = False, returnCreatedTime = False, returnDurationToServe = False, returnDurationType = False, returnFullName = False, returnIncidentOffenseNameActionDetailID = False, returnInvolvementType = False, returnIsAlternate = False, returnIsPrimaryOffense = False, returnLocationID = False, returnModifiedTime = False, returnNewStatus = False, returnNewStatusCode = False, returnOffenseCodeDescription = False, returnOldStatus = False, returnOldStatusCode = False, returnPartialDayPeriods = False, returnScheduledTime = False, returnTempIncidentOffenseNameActionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1, returnreturnTempIncidentOffenseNameActionDetailID = False, returnreturnActionCodeDescription = False, returnreturnCreateAttendance = False, returnreturnCreatedTime = False, returnreturnDurationToServe = False, returnreturnDurationType = False, returnreturnFullName = False, returnreturnIncidentOffenseNameActionDetailID = False, returnreturnInvolvementType = False, returnreturnIsAlternate = False, returnreturnIsPrimaryOffense = False, returnreturnLocationID = False, returnreturnModifiedTime = False, returnreturnNewStatus = False, returnreturnNewStatusCode = False, returnreturnOffenseCodeDescription = False, returnreturnOldStatus = False, returnreturnOldStatusCode = False, returnreturnPartialDayPeriods = False, returnreturnScheduledTime = False, returnreturnTempIncidentOffenseNameActionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameActionDetail(TempIncidentOffenseNameActionDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetail/" + str(TempIncidentOffenseNameActionDetailID), verb = "delete")

	return(response)

def getEveryTempIncidentOffenseNameActionDetailRecord(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameActionDetailRecordID = True, returnBuilding = False, returnBuildingID = False, returnCreatedTime = False, returnDurationServed = False, returnDurationToServe = False, returnDurationType = False, returnIncidentOffenseNameActionID = False, returnIsAlternate = False, returnIsGuardianNotified = False, returnLocation = False, returnLocationID = False, returnModifiedTime = False, returnRoomID = False, returnRoomNumber = False, returnScheduledTime = False, returnStaffFollowUpOfficerName = False, returnStaffIDFollowUpOfficer = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1, returnreturnTempIncidentOffenseNameActionDetailRecordID = False, returnreturnBuilding = False, returnreturnBuildingID = False, returnreturnCreatedTime = False, returnreturnDurationServed = False, returnreturnDurationToServe = False, returnreturnDurationType = False, returnreturnIncidentOffenseNameActionID = False, returnreturnIsAlternate = False, returnreturnIsGuardianNotified = False, returnreturnLocation = False, returnreturnLocationID = False, returnreturnModifiedTime = False, returnreturnRoomID = False, returnreturnRoomNumber = False, returnreturnScheduledTime = False, returnreturnStaffFollowUpOfficerName = False, returnreturnStaffIDFollowUpOfficer = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameActionDetailRecord(TempIncidentOffenseNameActionDetailRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameActionDetailRecord/" + str(TempIncidentOffenseNameActionDetailRecordID), verb = "delete")

	return(response)

def getEveryTempIncidentOffenseNameReportRunHistoryRecord(EntityID = 1, page = 1, pageSize = 100, returnTempIncidentOffenseNameReportRunHistoryRecordID = True, returnColumnHeader1 = False, returnColumnHeader10 = False, returnColumnHeader2 = False, returnColumnHeader3 = False, returnColumnHeader4 = False, returnColumnHeader5 = False, returnColumnHeader6 = False, returnColumnHeader7 = False, returnColumnHeader8 = False, returnColumnHeader9 = False, returnCreatedTime = False, returnDateTime = False, returnIncident = False, returnIncidentNumber = False, returnIncidentOffenseNameID = False, returnModifiedTime = False, returnOffense = False, returnStudentID = False, returnStudentName = False, returnUnboundBody = False, returnUnboundFooter = False, returnUnboundHeader = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1, returnreturnTempIncidentOffenseNameReportRunHistoryRecordID = False, returnreturnColumnHeader1 = False, returnreturnColumnHeader10 = False, returnreturnColumnHeader2 = False, returnreturnColumnHeader3 = False, returnreturnColumnHeader4 = False, returnreturnColumnHeader5 = False, returnreturnColumnHeader6 = False, returnreturnColumnHeader7 = False, returnreturnColumnHeader8 = False, returnreturnColumnHeader9 = False, returnreturnCreatedTime = False, returnreturnDateTime = False, returnreturnIncident = False, returnreturnIncidentNumber = False, returnreturnIncidentOffenseNameID = False, returnreturnModifiedTime = False, returnreturnOffense = False, returnreturnStudentID = False, returnreturnStudentName = False, returnreturnUnboundBody = False, returnreturnUnboundFooter = False, returnreturnUnboundHeader = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempIncidentOffenseNameReportRunHistoryRecord(TempIncidentOffenseNameReportRunHistoryRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/TempIncidentOffenseNameReportRunHistoryRecord/" + str(TempIncidentOffenseNameReportRunHistoryRecordID), verb = "delete")

	return(response)

def getEveryWeapon(EntityID = 1, page = 1, pageSize = 100, returnWeaponID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatePelletGunTypeMNID = False, returnStateWeaponTypeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeaponIDClonedFrom = False, returnWeaponMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getWeapon(WeaponID, EntityID = 1, returnreturnWeaponID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStatePelletGunTypeMNID = False, returnreturnStateWeaponTypeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeaponIDClonedFrom = False, returnreturnWeaponMNID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "get", params_list = params_list)

	return(response)

def deleteWeapon(WeaponID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Discipline/Weapon/" + str(WeaponID), verb = "delete")

	return(response)