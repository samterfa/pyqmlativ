# This module contains Reporting functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryBurstAction(searchConditions = [], EntityID = 1, returnBurstActionID = False, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BurstAction in the district.

	This function returns a dataframe of every BurstAction in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReport(searchConditions = [], EntityID = 1, returnDataMiningReportID = False, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReport in the district.

	This function returns a dataframe of every DataMiningReport in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReportField(searchConditions = [], EntityID = 1, returnDataMiningReportFieldID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReportField in the district.

	This function returns a dataframe of every DataMiningReportField in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReportFieldFilter(searchConditions = [], EntityID = 1, returnDataMiningReportFieldFilterID = False, returnComparisonType = False, returnComparisonTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReportFieldFilter in the district.

	This function returns a dataframe of every DataMiningReportFieldFilter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReportFieldParameter(searchConditions = [], EntityID = 1, returnDataMiningReportFieldParameterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReportFieldParameter in the district.

	This function returns a dataframe of every DataMiningReportFieldParameter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReportFieldSort(searchConditions = [], EntityID = 1, returnDataMiningReportFieldSortID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReportFieldSort in the district.

	This function returns a dataframe of every DataMiningReportFieldSort in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReportSortBreak(searchConditions = [], EntityID = 1, returnDataMiningReportSortBreakID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReportSortBreak in the district.

	This function returns a dataframe of every DataMiningReportSortBreak in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReportSubtopic(searchConditions = [], EntityID = 1, returnDataMiningReportSubtopicID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowCount = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReportSubtopic in the district.

	This function returns a dataframe of every DataMiningReportSubtopic in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMiningReportSubtopicStandardFilter(searchConditions = [], EntityID = 1, returnDataMiningReportSubtopicStandardFilterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMiningReportSubtopicStandardFilter in the district.

	This function returns a dataframe of every DataMiningReportSubtopicStandardFilter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPage(searchConditions = [], EntityID = 1, returnPageID = False, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Page in the district.

	This function returns a dataframe of every Page in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPageBurst(searchConditions = [], EntityID = 1, returnPageBurstID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PageBurst in the district.

	This function returns a dataframe of every PageBurst in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPromptTemplate(searchConditions = [], EntityID = 1, returnPromptTemplateID = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PromptTemplate in the district.

	This function returns a dataframe of every PromptTemplate in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReport(searchConditions = [], EntityID = 1, returnReportID = False, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDefinitionWasModified = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasErrors = False, returnHasNoUnpublishedChanges = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptForFiscalYear = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Report in the district.

	This function returns a dataframe of every Report in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportError(searchConditions = [], EntityID = 1, returnReportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportError in the district.

	This function returns a dataframe of every ReportError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportMenuModule(searchConditions = [], EntityID = 1, returnReportMenuModuleID = False, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportMenuModule in the district.

	This function returns a dataframe of every ReportMenuModule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportQueue(searchConditions = [], EntityID = 1, returnReportQueueID = False, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnIsViewableReport = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportQueue in the district.

	This function returns a dataframe of every ReportQueue in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportQueueBurstAction(searchConditions = [], EntityID = 1, returnReportQueueBurstActionID = False, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportQueueBurstAction in the district.

	This function returns a dataframe of every ReportQueueBurstAction in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportQueueSQL(searchConditions = [], EntityID = 1, returnReportQueueSQLID = False, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportQueueSQL in the district.

	This function returns a dataframe of every ReportQueueSQL in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportRole(searchConditions = [], EntityID = 1, returnReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportRole in the district.

	This function returns a dataframe of every ReportRole in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportRunInfo(searchConditions = [], EntityID = 1, returnReportRunInfoID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportRunInfo in the district.

	This function returns a dataframe of every ReportRunInfo in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryReportStyle(searchConditions = [], EntityID = 1, returnReportStyleID = False, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ReportStyle in the district.

	This function returns a dataframe of every ReportStyle in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduledReport(searchConditions = [], EntityID = 1, returnScheduledReportID = False, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduledReport in the district.

	This function returns a dataframe of every ScheduledReport in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySecurityLocationReportSet(searchConditions = [], EntityID = 1, returnSecurityLocationReportSetID = False, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SecurityLocationReportSet in the district.

	This function returns a dataframe of every SecurityLocationReportSet in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySecurityLocationReportSetReportRunInfo(searchConditions = [], EntityID = 1, returnSecurityLocationReportSetReportRunInfoID = False, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SecurityLocationReportSetReportRunInfo in the district.

	This function returns a dataframe of every SecurityLocationReportSetReportRunInfo in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySort(searchConditions = [], EntityID = 1, returnSortID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Sort in the district.

	This function returns a dataframe of every Sort in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySortBreak(searchConditions = [], EntityID = 1, returnSortBreakID = False, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SortBreak in the district.

	This function returns a dataframe of every SortBreak in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySortGroup(searchConditions = [], EntityID = 1, returnSortGroupID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SortGroup in the district.

	This function returns a dataframe of every SortGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubject(searchConditions = [], EntityID = 1, returnSubjectID = False, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPromptForFiscalYear = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Subject in the district.

	This function returns a dataframe of every Subject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubjectSecurityLocation(searchConditions = [], EntityID = 1, returnSubjectSecurityLocationID = False, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubjectSecurityLocation in the district.

	This function returns a dataframe of every SubjectSecurityLocation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubtopic(searchConditions = [], EntityID = 1, returnSubtopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnCustomizationID = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Subtopic in the district.

	This function returns a dataframe of every Subtopic in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubtopicField(searchConditions = [], EntityID = 1, returnSubtopicFieldID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubtopicField in the district.

	This function returns a dataframe of every SubtopicField in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubtopicStandardFilter(searchConditions = [], EntityID = 1, returnSubtopicStandardFilterID = False, returnCreatedTime = False, returnDisplayOnReport = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubtopicStandardFilter in the district.

	This function returns a dataframe of every SubtopicStandardFilter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySummaryReportParameter(searchConditions = [], EntityID = 1, returnSummaryReportParameterID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SummaryReportParameter in the district.

	This function returns a dataframe of every SummaryReportParameter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySummaryReportPrompt(searchConditions = [], EntityID = 1, returnSummaryReportPromptID = False, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SummaryReportPrompt in the district.

	This function returns a dataframe of every SummaryReportPrompt in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySummaryReportSection(searchConditions = [], EntityID = 1, returnSummaryReportSectionID = False, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SummaryReportSection in the district.

	This function returns a dataframe of every SummaryReportSection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySummaryReportSectionColumn(searchConditions = [], EntityID = 1, returnSummaryReportSectionColumnID = False, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SummaryReportSectionColumn in the district.

	This function returns a dataframe of every SummaryReportSectionColumn in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempReportRole(searchConditions = [], EntityID = 1, returnTempReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnReportIsSkywardReport = False, returnReportName = False, returnReportPortal = False, returnReportPrimaryMenuModuleDisplayName = False, returnReportReportType = False, returnReportRoleID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempReportRole in the district.

	This function returns a dataframe of every TempReportRole in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSubtopicRelationshipOption(searchConditions = [], EntityID = 1, returnTempSubtopicRelationshipOptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnRelationshipPath = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSubtopicRelationshipOption in the district.

	This function returns a dataframe of every TempSubtopicRelationshipOption in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempUploadDataMiningReportLog(searchConditions = [], EntityID = 1, returnTempUploadDataMiningReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempUploadDataMiningReportLog in the district.

	This function returns a dataframe of every TempUploadDataMiningReportLog in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTopic(searchConditions = [], EntityID = 1, returnTopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnNameWithParentTopicName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Topic in the district.

	This function returns a dataframe of every Topic in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUploadReportLog(searchConditions = [], EntityID = 1, returnUploadReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UploadReportLog in the district.

	This function returns a dataframe of every UploadReportLog in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserReportPrompt(searchConditions = [], EntityID = 1, returnUserReportPromptID = False, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserReportPrompt in the district.

	This function returns a dataframe of every UserReportPrompt in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserSetting(searchConditions = [], EntityID = 1, returnUserSettingID = False, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserSetting in the district.

	This function returns a dataframe of every UserSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)