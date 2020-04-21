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