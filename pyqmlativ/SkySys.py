# This module contains SkySys functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryApplySchemaChangeAllChangesConfirmation(searchConditions = [], EntityID = 1, returnApplySchemaChangeAllChangesConfirmationID = False, returnApplySchemaChangeRunID = False, returnChangeType = False, returnCreatedTime = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModuleID = False, returnModulePendingName = False, returnObjectID = False, returnObjectPendingName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ApplySchemaChangeAllChangesConfirmation in the district.

	This function returns a dataframe of every ApplySchemaChangeAllChangesConfirmation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryApplySchemaChangeFieldSelection(searchConditions = [], EntityID = 1, returnApplySchemaChangeFieldSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldChangeType = False, returnFieldCurrentName = False, returnFieldHasChangedRelationships = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ApplySchemaChangeFieldSelection in the district.

	This function returns a dataframe of every ApplySchemaChangeFieldSelection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryApplySchemaChangeObjectSelection(searchConditions = [], EntityID = 1, returnApplySchemaChangeObjectSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectChangeType = False, returnObjectCurrentName = False, returnObjectHasChangedFields = False, returnObjectHasChangedRelationships = False, returnObjectID = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ApplySchemaChangeObjectSelection in the district.

	This function returns a dataframe of every ApplySchemaChangeObjectSelection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryApplySchemaChangeRelationshipSelection(searchConditions = [], EntityID = 1, returnApplySchemaChangeRelationshipSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnRelationshipChangeType = False, returnRelationshipCurrentName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ApplySchemaChangeRelationshipSelection in the district.

	This function returns a dataframe of every ApplySchemaChangeRelationshipSelection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryApplySchemaChangeRun(searchConditions = [], EntityID = 1, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnExecutedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ApplySchemaChangeRun in the district.

	This function returns a dataframe of every ApplySchemaChangeRun in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttachment(searchConditions = [], EntityID = 1, returnAttachmentID = False, returnAttachmentTypeID = False, returnComment = False, returnCreatedTime = False, returnCurrentUserCanReadAttachmentsOfThisAttachmentType = False, returnMediaID = False, returnModifiedTime = False, returnObjectID = False, returnSourceID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Attachment in the district.

	This function returns a dataframe of every Attachment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAttachmentType(searchConditions = [], EntityID = 1, returnAttachmentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserCanCreateAttachmentsOfThisAttachmentType = False, returnCustomizationID = False, returnDescription = False, returnEffectiveIsDefault = False, returnEffectiveShowInActivityAccess = False, returnEffectiveShowInAdministrativeAccess = False, returnEffectiveShowInEmployeeAccess = False, returnEffectiveShowInFamilyAccess = False, returnEffectiveShowInNewStudentEnrollment = False, returnEffectiveShowInStudentAccess = False, returnEffectiveShowInStudentServices = False, returnEffectiveShowInTeacherAccess = False, returnIncludeWithEmail = False, returnIsDefault = False, returnModifiedTime = False, returnObjectID = False, returnShowInActivityAccess = False, returnShowInAdministrativeAccess = False, returnShowInEmployeeAccess = False, returnShowInFamilyAccess = False, returnShowInNewStudentEnrollment = False, returnShowInStudentAccess = False, returnShowInStudentServices = False, returnShowInTeacherAccess = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardShowInActivityAccess = False, returnSkywardShowInAdministrativeAccess = False, returnSkywardShowInEmployeeAccess = False, returnSkywardShowInFamilyAccess = False, returnSkywardShowInNewStudentEnrollment = False, returnSkywardShowInStudentAccess = False, returnSkywardShowInStudentServices = False, returnSkywardShowInTeacherAccess = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AttachmentType in the district.

	This function returns a dataframe of every AttachmentType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBenchmarkingQuestion(searchConditions = [], EntityID = 1, returnBenchmarkingQuestionID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BenchmarkingQuestion in the district.

	This function returns a dataframe of every BenchmarkingQuestion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBenchmarkingQuestionAnswer(searchConditions = [], EntityID = 1, returnBenchmarkingQuestionAnswerID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyInstanceID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNumericValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BenchmarkingQuestionAnswer in the district.

	This function returns a dataframe of every BenchmarkingQuestionAnswer in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBenchmarkingSurvey(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyID = False, returnBannerMessage = False, returnCreatedTime = False, returnEndTime = False, returnHeaderMessage = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BenchmarkingSurvey in the district.

	This function returns a dataframe of every BenchmarkingSurvey in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBenchmarkingSurveyDelay(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyDelayID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnResumeTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BenchmarkingSurveyDelay in the district.

	This function returns a dataframe of every BenchmarkingSurveyDelay in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBenchmarkingSurveyInstance(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyInstanceID = False, returnBenchmarkingSurveyID = False, returnComment = False, returnContactEmail = False, returnCreatedTime = False, returnModifiedTime = False, returnTakenOnMobile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BenchmarkingSurveyInstance in the district.

	This function returns a dataframe of every BenchmarkingSurveyInstance in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBenchmarkingSurveyQuestion(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyQuestionID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BenchmarkingSurveyQuestion in the district.

	This function returns a dataframe of every BenchmarkingSurveyQuestion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBrowse(searchConditions = [], EntityID = 1, returnBrowseID = False, returnApplyEntityDistrictFilter = False, returnApplyFiscalYearFilter = False, returnApplySchoolYearFilter = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnEffectiveDataModule = False, returnEffectiveDataObject = False, returnFormattedBrowsePath = False, returnIsReference = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnObjectScreenNamePath = False, returnScreen = False, returnScreenNamePath = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUseAudit = False, returnUseOldPagingSystem = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Browse in the district.

	This function returns a dataframe of every Browse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBrowseFilter(searchConditions = [], EntityID = 1, returnBrowseFilterID = False, returnBrowseFilterIDClonedFrom = False, returnBrowseID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnFilterID = False, returnFilterTemplate = False, returnFilterTemplateData = False, returnIsAutoCreated = False, returnIsBase = False, returnIsCurrent = False, returnIsDefault = False, returnIsEnabled = False, returnModifiedTime = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BrowseFilter in the district.

	This function returns a dataframe of every BrowseFilter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBrowseFilterLastUsed(searchConditions = [], EntityID = 1, returnBrowseFilterLastUsedID = False, returnBrowseFilterID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BrowseFilterLastUsed in the district.

	This function returns a dataframe of every BrowseFilterLastUsed in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBrowseMenu(searchConditions = [], EntityID = 1, returnBrowseMenuID = False, returnAppendDataObjectNameToDisplayName = False, returnBrowseID = False, returnCondition = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayInBrowse = False, returnDisplayInDetails = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnEffectiveTarget = False, returnFilter = False, returnImage = False, returnImageCode = False, returnImageText = False, returnIncludeInRowMoreMenu = False, returnIsDefault = False, returnIsEnabled = False, returnIsRowMenu = False, returnIsSkywardBrowseMenu = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPostData = False, returnPrimaryKeyBindSource = False, returnRenderCondition = False, returnScreen = False, returnSkywardDescription = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardTarget = False, returnTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BrowseMenu in the district.

	This function returns a dataframe of every BrowseMenu in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBrowseView(searchConditions = [], EntityID = 1, returnBrowseViewID = False, returnBrowseID = False, returnBrowseType = False, returnBrowseViewIDClonedFrom = False, returnColumns = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnHasSelectAllCheckBox = False, returnIsDefault = False, returnIsEnabled = False, returnIsModifiedView = False, returnIsSkywardView = False, returnIsUserView = False, returnJsonData = False, returnModifiedTime = False, returnRowsPerPage = False, returnSearchColumns = False, returnShowFooter = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BrowseView in the district.

	This function returns a dataframe of every BrowseView in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBrowseViewLastUsed(searchConditions = [], EntityID = 1, returnBrowseViewLastUsedID = False, returnBrowseID = False, returnBrowseViewID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BrowseViewLastUsed in the district.

	This function returns a dataframe of every BrowseViewLastUsed in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBulkLoad(searchConditions = [], EntityID = 1, returnBulkLoadID = False, returnCreatedTime = False, returnMask = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BulkLoad in the district.

	This function returns a dataframe of every BulkLoad in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBusinessMigrationHistory(searchConditions = [], EntityID = 1, returnBusinessMigrationHistoryID = False, returnCreatedTime = False, returnFullClassName = False, returnHasRun = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BusinessMigrationHistory in the district.

	This function returns a dataframe of every BusinessMigrationHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCacheInitialization(searchConditions = [], EntityID = 1, returnCacheInitializationID = False, returnApplication = False, returnCacheName = False, returnCacheVersionCount = False, returnCreatedTime = False, returnHostName = False, returnInitializationTimeMilliseconds = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CacheInitialization in the district.

	This function returns a dataframe of every CacheInitialization in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCharacterLimitGroup(searchConditions = [], EntityID = 1, returnCharacterLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMaxLength = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CharacterLimitGroup in the district.

	This function returns a dataframe of every CharacterLimitGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAllowMobileAccess = False, returnBrowseTimeoutEnabled = False, returnBrowseTimeoutSeconds = False, returnBrowseTimeoutSecondsMobile = False, returnCreatedTime = False, returnCurrencyIDBase = False, returnCustomRelationshipSync = False, returnCustomRelationshipSyncPollInterval = False, returnCustomViewSync = False, returnDaysToStoreAPIUsageHistory = False, returnDaysToStoreSystemLog = False, returnDaysToStoreUsageHistory = False, returnEnvironmentPurpose = False, returnEnvironmentPurposeBarColor = False, returnFileDestinationIDSkylertExport = False, returnFileDestinationIDThirdPartyExportImportLocation = False, returnLockDelayMinutes = False, returnLockMessage = False, returnLockoutText = False, returnLockTime = False, returnLogThreshold = False, returnLogThresholdCode = False, returnMaximumAttachmentSize = False, returnMediaIDLogo = False, returnModifiedTime = False, returnProductType = False, returnProductTypeCode = False, returnSecondsToLocked = False, returnSendingEmailAddress = False, returnSendingEmailAlias = False, returnSerialNumber = False, returnSMTPPassword = False, returnSMTPUsername = False, returnStateID = False, returnStatisticsExpiresTime = False, returnSystemTimeOffset = False, returnTimeZoneCode = False, returnTrainingTimeOffset = False, returnUseLicensing = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStatisticInfo = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCrossReference(searchConditions = [], EntityID = 1, returnCrossReferenceID = False, returnCreatedTime = False, returnFileValue = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CrossReference in the district.

	This function returns a dataframe of every CrossReference in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCustomScreen(searchConditions = [], EntityID = 1, returnCustomScreenID = False, returnCreatedTime = False, returnHasPendingChanges = False, returnIsProfileScreen = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPortal = False, returnPortalCode = False, returnProfileObjectName = False, returnScreenPath = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CustomScreen in the district.

	This function returns a dataframe of every CustomScreen in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCustomScreenElement(searchConditions = [], EntityID = 1, returnCustomScreenElementID = False, returnCreatedTime = False, returnCustomScreenElementType = False, returnCustomScreenElementTypeDisplayText = False, returnCustomScreenID = False, returnData = False, returnDisplayOrder = False, returnDisplayType = False, returnGuidFieldPath = False, returnIsReadOnly = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CustomScreenElement in the district.

	This function returns a dataframe of every CustomScreenElement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDashboard(searchConditions = [], EntityID = 1, returnDashboardID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Dashboard in the district.

	This function returns a dataframe of every Dashboard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDatabaseConnection(searchConditions = [], EntityID = 1, returnConnectionID = False, returnAuthScheme = False, returnClientNetAddress = False, returnClientTcpPort = False, returnConnectTime = False, returnLastRead = False, returnLastWrite = False, returnLocalNetAddress = False, returnLocalTcpPort = False, returnMostRecentSessionID = False, returnMostRecentSqlHandle = False, returnNetPacketSize = False, returnNetTransport = False, returnNumReads = False, returnNumWrites = False, returnParentConnectionID = False, returnProtocolType = False, returnSessionID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DatabaseConnection in the district.

	This function returns a dataframe of every DatabaseConnection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDatabaseRequest(searchConditions = [], EntityID = 1, returnSessionID = False, returnApplicationName = False, returnBlockedBySessionID = False, returnCommand = False, returnCPUTime = False, returnDatabase = False, returnDegreesOfParallelism = False, returnElapsedTime = False, returnEstimatedComplete = False, returnExecutingStatement = False, returnFullQuery = False, returnGrantedMemory = False, returnHostname = False, returnIdealMemory = False, returnLastWaitType = False, returnOpenResultSets = False, returnOpenTransactions = False, returnPercentComplete = False, returnQueryCost = False, returnReads = False, returnRequestID = False, returnRequiredMemory = False, returnTimeoutSeconds = False, returnUsedMemory = False, returnUser = False, returnWaitTime = False, returnWaitType = False, returnWrites = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DatabaseRequest in the district.

	This function returns a dataframe of every DatabaseRequest in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDatabaseSession(searchConditions = [], EntityID = 1, returnSessionID = False, returnAuthenticatingDatabaseID = False, returnClientInterfaceName = False, returnClientVersion = False, returnCpuTime = False, returnDatabaseID = False, returnHostName = False, returnHostProcessID = False, returnIsUserProcess = False, returnLastRequestEndTime = False, returnLastRequestStartTime = False, returnLastSuccessfullLogon = False, returnLastUnsuccessfullLogon = False, returnLogicalReads = False, returnLoginName = False, returnLoginTime = False, returnMemoryUsage = False, returnNtDomain = False, returnNtUserName = False, returnOpenTransactionCount = False, returnOriginalLoginName = False, returnPrevError = False, returnProgramName = False, returnReads = False, returnRowCount = False, returnStatus = False, returnTotalElapsedTime = False, returnTotalScheduledTime = False, returnTransactionIsolationLevel = False, returnUnsuccessfulLogons = False, returnWrites = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DatabaseSession in the district.

	This function returns a dataframe of every DatabaseSession in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDatabaseTransaction(searchConditions = [], EntityID = 1, returnTransactionID = False, returnName = False, returnTransactionBeginTime = False, returnTransactionState = False, returnTransactionType = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DatabaseTransaction in the district.

	This function returns a dataframe of every DatabaseTransaction in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDataMigrationHistory(searchConditions = [], EntityID = 1, returnDataMigrationHistoryID = False, returnCreatedTime = False, returnMigrationNumber = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkipped = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DataMigrationHistory in the district.

	This function returns a dataframe of every DataMigrationHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEmail(searchConditions = [], EntityID = 1, returnEmailID = False, returnBody = False, returnCarbonCopy = False, returnCreatedTime = False, returnEndTime = False, returnHostname = False, returnHTMLBody = False, returnMessageID = False, returnModifiedTime = False, returnPriority = False, returnPriorityCode = False, returnProcessID = False, returnRecipient = False, returnSendingAddress = False, returnSendingAlias = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Email in the district.

	This function returns a dataframe of every Email in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEmailAttachment(searchConditions = [], EntityID = 1, returnEmailAttachmentID = False, returnCreatedTime = False, returnEmailID = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EmailAttachment in the district.

	This function returns a dataframe of every EmailAttachment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryExternalLink(searchConditions = [], EntityID = 1, returnExternalLinkID = False, returnCreatedTime = False, returnDescription = False, returnDisplayInAdministrativeAccess = False, returnDisplayInEmployeeAccess = False, returnDisplayInFamilyAccess = False, returnDisplayInNewStudentEnrollment = False, returnDisplayInStudentAccess = False, returnDisplayInStudentServicesAccess = False, returnDisplayInTeacherAccess = False, returnDistrictID = False, returnIcon = False, returnIconCode = False, returnLinkText = False, returnModifiedTime = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ExternalLink in the district.

	This function returns a dataframe of every ExternalLink in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryExternalLinkEntity(searchConditions = [], EntityID = 1, returnExternalLinkEntityID = False, returnCreatedTime = False, returnEntityID = False, returnExternalLinkID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ExternalLinkEntity in the district.

	This function returns a dataframe of every ExternalLinkEntity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFeedback(searchConditions = [], EntityID = 1, returnFeedbackID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnSubScreen = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Feedback in the district.

	This function returns a dataframe of every Feedback in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryField(searchConditions = [], EntityID = 1, returnFieldID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentFieldWidth = False, returnCurrentIsRequired = False, returnCurrentName = False, returnCurrentPrecision = False, returnCurrentRelationshipOrFieldName = False, returnCurrentScale = False, returnCurrentSize = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFormattedFieldPath = False, returnHasChangedRelationships = False, returnIsDeniable = False, returnIsForeignKeyOfRelationship = False, returnIsInDB = False, returnIsPrimaryKey = False, returnIsSkywardField = False, returnModifiedTime = False, returnObjectID = False, returnPendingDisplayName = False, returnPendingFieldWidth = False, returnPendingIsRequired = False, returnPendingName = False, returnPendingPrecision = False, returnPendingRelationshipOrFieldName = False, returnPendingScale = False, returnPendingSize = False, returnPendingType = False, returnPendingTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUniqueIDString = False, returnUserCanEdit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceDataTypeCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Field in the district.

	This function returns a dataframe of every Field in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFieldMapping(searchConditions = [], EntityID = 1, returnFieldMappingID = False, returnActionIfSourceValueIsBlank = False, returnActionIfSourceValueIsBlankCode = False, returnCreatedTime = False, returnFieldID = False, returnImportDataObjectSourceID = False, returnImportDataObjectSourceIDMappedValue = False, returnMappingType = False, returnMappingTypeCode = False, returnModifiedTime = False, returnSourceDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FieldMapping in the district.

	This function returns a dataframe of every FieldMapping in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFileDestination(searchConditions = [], EntityID = 1, returnFileDestinationID = False, returnAllowRead = False, returnAllowWrite = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnIdentifyingInformation = False, returnIsFTPConnection = False, returnIsUNCPath = False, returnModifiedTime = False, returnName = False, returnUNCPathID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FileDestination in the district.

	This function returns a dataframe of every FileDestination in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFileDestinationResult(searchConditions = [], EntityID = 1, returnFileDestinationResultID = False, returnCreatedTime = False, returnFileDestinationID = False, returnFileName = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FileDestinationResult in the district.

	This function returns a dataframe of every FileDestinationResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFilter(searchConditions = [], EntityID = 1, returnFilterID = False, returnComment = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDistrictID = False, returnEntityID = False, returnFilterDataAdvanced = False, returnFilterDataAdvancedCondition = False, returnFilterDataColumn = False, returnFilterDataColumnCondition = False, returnFilterIDClonedFrom = False, returnFiscalYearID = False, returnFriendlyFilter = False, returnIsReusable = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Filter in the district.

	This function returns a dataframe of every Filter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFTPConnection(searchConditions = [], EntityID = 1, returnFTPConnectionID = False, returnAllowInvalidCertificate = False, returnCreatedTime = False, returnDescription = False, returnHost = False, returnMediaIDSSHKey = False, returnModifiedTime = False, returnName = False, returnPassword = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnRemoteDirectory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FTPConnection in the district.

	This function returns a dataframe of every FTPConnection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFTPProcessType(searchConditions = [], EntityID = 1, returnFTPProcessTypeID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnModuleName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FTPProcessType in the district.

	This function returns a dataframe of every FTPProcessType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFTPProcessTypeConnection(searchConditions = [], EntityID = 1, returnFTPProcessTypeConnectionID = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnFTPProcessTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FTPProcessTypeConnection in the district.

	This function returns a dataframe of every FTPProcessTypeConnection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFTPResult(searchConditions = [], EntityID = 1, returnFTPResultID = False, returnCreatedTime = False, returnFileName = False, returnFTPConnectionID = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FTPResult in the district.

	This function returns a dataframe of every FTPResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryImport(searchConditions = [], EntityID = 1, returnImportID = False, returnAcceptedFileTypes = False, returnColumnsJSON = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDefinition = False, returnDelimiter = False, returnDescription = False, returnFileHasHeaderRow = False, returnFileType = False, returnFileTypeCode = False, returnHasPromptsFromDefinition = False, returnIsFixedWidth = False, returnIsSkywardImport = False, returnModifiedTime = False, returnName = False, returnNumberOfHeaderRows = False, returnPromptList = False, returnPromptListJson = False, returnSkywardID = False, returnTextQualifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Import in the district.

	This function returns a dataframe of every Import in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryImportDataObjectSource(searchConditions = [], EntityID = 1, returnImportDataObjectSourceID = False, returnAction = False, returnActionCode = False, returnCanAddFieldMapping = False, returnCreatedTime = False, returnHasFieldMappings = False, returnImportID = False, returnIsPrimary = False, returnMatchAction = False, returnMatchActionCode = False, returnModifiedTime = False, returnName = False, returnNoMatchAction = False, returnNoMatchActionCode = False, returnObjectID = False, returnUniqueKey = False, returnUpdateSearchCondition = False, returnUpdateSearchXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ImportDataObjectSource in the district.

	This function returns a dataframe of every ImportDataObjectSource in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryImportModulePath(searchConditions = [], EntityID = 1, returnImportModulePathID = False, returnCreatedTime = False, returnImportID = False, returnModifiedTime = False, returnModulePathID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ImportModulePath in the district.

	This function returns a dataframe of every ImportModulePath in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryImportResult(searchConditions = [], EntityID = 1, returnImportResultID = False, returnCanBeDeleted = False, returnCreatedTime = False, returnFailedRecordCount = False, returnHasMediaFailedRows = False, returnImportID = False, returnLastProcessedRowNumber = False, returnMediaIDFailedRows = False, returnMediaIDOriginalImportedData = False, returnModifiedTime = False, returnResultRowCount = False, returnStatus = False, returnStatusCode = False, returnSuccessfulRecordCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWarningRecordCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ImportResult in the district.

	This function returns a dataframe of every ImportResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryImportResultRow(searchConditions = [], EntityID = 1, returnImportResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnFailedRowFileRowNumber = False, returnImportFileRowNumber = False, returnImportResultID = False, returnModifiedTime = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ImportResultRow in the district.

	This function returns a dataframe of every ImportResultRow in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryImportResultRowDetail(searchConditions = [], EntityID = 1, returnImportResultRowDetailID = False, returnActionType = False, returnActionTypeCode = False, returnBeforeImportModifiedTime = False, returnCreatedTime = False, returnImportResultRowID = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ImportResultRowDetail in the district.

	This function returns a dataframe of every ImportResultRowDetail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryIndexStatisticsAlwaysUpdate(searchConditions = [], EntityID = 1, returnIndexStatisticsAlwaysUpdateID = False, returnSchemaName = False, returnSkywardHash = False, returnSkywardID = False, returnTableName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every IndexStatisticsAlwaysUpdate in the district.

	This function returns a dataframe of every IndexStatisticsAlwaysUpdate in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryKiosk(searchConditions = [], EntityID = 1, returnKioskID = False, returnCreatedTime = False, returnIPAddress = False, returnIsTardyKiosk = False, returnModifiedTime = False, returnName = False, returnPrinterType = False, returnPrinterTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Kiosk in the district.

	This function returns a dataframe of every Kiosk in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLog(searchConditions = [], EntityID = 1, returnLogID = False, returnActivityContext = False, returnApplication = False, returnApplicationMonitoringIdentifier = False, returnBindingEscapedMessage = False, returnClassification = False, returnClassificationCode = False, returnCreatedTime = False, returnDataObjectID = False, returnDataObjectType = False, returnDetails = False, returnHostname = False, returnMessage = False, returnModifiedTime = False, returnProcessID = False, returnSeverity = False, returnSeverityCode = False, returnSourceFile = False, returnStackTrace = False, returnSystemVersion = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Log in the district.

	This function returns a dataframe of every Log in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLoginHistory(searchConditions = [], EntityID = 1, returnLoginHistoryID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnEnteredUserName = False, returnHostAddress = False, returnIsSuccessfulLogin = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every LoginHistory in the district.

	This function returns a dataframe of every LoginHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMedia(searchConditions = [], EntityID = 1, returnMediaID = False, returnBytes = False, returnCreatedTime = False, returnHash = False, returnLibraryType = False, returnLibraryTypeCode = False, returnMediaDataID = False, returnMediaDataIDLargeThumbnail = False, returnMediaDataIDSmallThumbnail = False, returnMediaTypeID = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStorageLocation = False, returnStorageLocationCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Media in the district.

	This function returns a dataframe of every Media in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMediaType(searchConditions = [], EntityID = 1, returnMediaTypeID = False, returnAllowAttachment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMimeType = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MediaType in the district.

	This function returns a dataframe of every MediaType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMenuCategory(searchConditions = [], EntityID = 1, returnMenuCategoryID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveIsDefault = False, returnIsDefault = False, returnIsEnabled = False, returnIsSkywardMenuCategory = False, returnMenuModuleID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MenuCategory in the district.

	This function returns a dataframe of every MenuCategory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMenuModule(searchConditions = [], EntityID = 1, returnMenuModuleID = False, returnCreatedTime = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnImage = False, returnImageCode = False, returnIsEnabled = False, returnIsSkywardMenuModule = False, returnModifiedTime = False, returnModuleSkywardID = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MenuModule in the district.

	This function returns a dataframe of every MenuModule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMenuScreen(searchConditions = [], EntityID = 1, returnMenuScreenID = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnIsEnabled = False, returnIsForMenuSecurity = False, returnIsSkywardMenuScreen = False, returnMenuCategoryID = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnOptionType = False, returnOptionTypeCode = False, returnPostData = False, returnProfileID = False, returnScreen = False, returnShouldShowInMenu = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MenuScreen in the district.

	This function returns a dataframe of every MenuScreen in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryModule(searchConditions = [], EntityID = 1, returnModuleID = False, returnChangeType = False, returnContainsAtLeastOneNonTempDataObject = False, returnCreatedTime = False, returnCurrentName = False, returnDisplayName = False, returnEffectiveName = False, returnHasChangedFields = False, returnHasChangedObjects = False, returnHasChangedRelationships = False, returnIsInDB = False, returnIsSkywardModule = False, returnModifiedTime = False, returnPendingName = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Module in the district.

	This function returns a dataframe of every Module in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryModulePath(searchConditions = [], EntityID = 1, returnModulePathID = False, returnAliasAction = False, returnAliasIsWorkflow = False, returnAliasModule = False, returnAliasObject = False, returnAverageLoadTimeMilliseconds = False, returnController = False, returnControllerDataObjectTypeIdentifier = False, returnControllerScreen = False, returnControllerSkywardID = False, returnCreateAccess = False, returnCreateAccessCode = False, returnCreatedTime = False, returnDataObjectTypeIdentifier = False, returnDataObjectTypeName = False, returnDataObjectTypeNameObjectID = False, returnDeleteAccess = False, returnDeleteAccessCode = False, returnFullAlias = False, returnIsAnonymous = False, returnIsFullPageLoad = False, returnIsListScreen = False, returnIsProfileScreen = False, returnIsSession = False, returnIsSkywardDefined = False, returnMassCreateAccess = False, returnMassCreateAccessCode = False, returnMassDeleteAccess = False, returnMassDeleteAccessCode = False, returnMassUpdateAccess = False, returnMassUpdateAccessCode = False, returnMaximumLoadTimeMilliseconds = False, returnMinimumLoadTimeMilliseconds = False, returnMobileCreateAccess = False, returnMobileCreateAccessCode = False, returnMobileDeleteAccess = False, returnMobileDeleteAccessCode = False, returnMobileMassCreateAccess = False, returnMobileMassCreateAccessCode = False, returnMobileMassDeleteAccess = False, returnMobileMassDeleteAccessCode = False, returnMobileMassUpdateAccess = False, returnMobileMassUpdateAccessCode = False, returnMobileReadAccess = False, returnMobileReadAccessCode = False, returnMobileUpdateAccess = False, returnMobileUpdateAccessCode = False, returnModifiedTime = False, returnModule = False, returnModuleController = False, returnNonReadOnlyImpersonationBlacklist = False, returnPageLoadCount = False, returnPortal = False, returnPortalCode = False, returnProfile_Module = False, returnProfile_Object = False, returnProfileID = False, returnReadAccess = False, returnReadAccessCode = False, returnReadOnlyImpersonationWhitelist = False, returnScreen = False, returnScreenLayoutChanges = False, returnScreenXML = False, returnShowReportType = False, returnShowReportTypeCode = False, returnSkipAntiForgeryTokenCheck = False, returnSkipLicense = False, returnSkywardHash = False, returnSkywardID = False, returnUpdateAccess = False, returnUpdateAccessCode = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidateSessionForFullPageLoad = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ModulePath in the district.

	This function returns a dataframe of every ModulePath in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryObject(searchConditions = [], EntityID = 1, returnObjectID = False, returnAllowAttachments = False, returnChangeType = False, returnCodeGuidFieldPath = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCustomizationID = False, returnDescriptionGuidFieldPath = False, returnEffectiveDisplayName = False, returnEffectiveName = False, returnFormattedObjectPath = False, returnHasChangedFields = False, returnHasChangedRelationships = False, returnHasDefaultSortGroup = False, returnIsInDB = False, returnIsSkywardObject = False, returnIsTempDataObject = False, returnIsView = False, returnModifiedTime = False, returnModuleID = False, returnNotForDisplayInImporting = False, returnNotForDisplayInReporting = False, returnPendingDisplayName = False, returnPendingFormattedObjectPath = False, returnPendingName = False, returnScope = False, returnScopeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewSQL = False, returnViewSQLText = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Object in the district.

	This function returns a dataframe of every Object in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlinePaymentLog(searchConditions = [], EntityID = 1, returnOnlinePaymentLogID = False, returnCreatedTime = False, returnEndpoint = False, returnEndpointCode = False, returnModifiedTime = False, returnRequestXML = False, returnResponseXML = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlinePaymentLog in the district.

	This function returns a dataframe of every OnlinePaymentLog in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlinePaymentVendor(searchConditions = [], EntityID = 1, returnOnlinePaymentVendorID = False, returnCreatedTime = False, returnEntitySummary = False, returnFeeManagementOnlinePaymentCodeDefault = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnName = False, returnURL = False, returnURLDisplayText = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlinePaymentVendor in the district.

	This function returns a dataframe of every OnlinePaymentVendor in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlinePaymentVendorEntity(searchConditions = [], EntityID = 1, returnOnlinePaymentVendorEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlinePaymentVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlinePaymentVendorEntity in the district.

	This function returns a dataframe of every OnlinePaymentVendorEntity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPaymentNoticeLog(searchConditions = [], EntityID = 1, returnPaymentNoticeLogID = False, returnComponentConfirmationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnOnlinePaymentLogID = False, returnPaymentDetailIDFeeManagement = False, returnPaymentDetailIDFoodService = False, returnSuccess = False, returnTransactionConfirmationNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPaidBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PaymentNoticeLog in the district.

	This function returns a dataframe of every PaymentNoticeLog in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProfile(searchConditions = [], EntityID = 1, returnProfileID = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Profile in the district.

	This function returns a dataframe of every Profile in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProfileModule(searchConditions = [], EntityID = 1, returnProfileModuleID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnProfileID = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ProfileModule in the district.

	This function returns a dataframe of every ProfileModule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProfileScreen(searchConditions = [], EntityID = 1, returnProfileScreenID = False, returnAttachmentTypeGUID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnProfileModuleID = False, returnRender = False, returnScreen = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ProfileScreen in the district.

	This function returns a dataframe of every ProfileScreen in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPrompt(searchConditions = [], EntityID = 1, returnPromptID = False, returnColumns = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnDisplayOrder = False, returnFieldPath = False, returnFilter = False, returnFilterCondition = False, returnInputType = False, returnIsSkywardPrompt = False, returnLabel = False, returnLinkedPromptGuid = False, returnModifiedTime = False, returnPresenceType = False, returnPresenceTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Prompt in the district.

	This function returns a dataframe of every Prompt in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQuickEntryText(searchConditions = [], EntityID = 1, returnQuickEntryTextID = False, returnCreatedTime = False, returnEntry = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QuickEntryText in the district.

	This function returns a dataframe of every QuickEntryText in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRelationship(searchConditions = [], EntityID = 1, returnRelationshipID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentCondition = False, returnCurrentConditionXML = False, returnCurrentDeleteBehavior = False, returnCurrentDeleteBehaviorCode = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFieldIDForeignKeyCurrent = False, returnFieldIDForeignKeyPending = False, returnIsInDB = False, returnIsSkywardRelationship = False, returnModifiedTime = False, returnObjectIDForeignCurrent = False, returnObjectIDForeignPending = False, returnObjectIDPrimary = False, returnPendingCondition = False, returnPendingConditionXML = False, returnPendingDeleteBehavior = False, returnPendingDeleteBehaviorCode = False, returnPendingDisplayName = False, returnPendingName = False, returnPendingType = False, returnPendingTypeCode = False, returnRelationshipIDRelated = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Relationship in the district.

	This function returns a dataframe of every Relationship in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduledImport(searchConditions = [], EntityID = 1, returnScheduledImportID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnEntityID = False, returnEntityIDList = False, returnFileHasHeaderRow = False, returnFiscalYearID = False, returnImportID = False, returnModifiedTime = False, returnName = False, returnNetworkFilePath = False, returnPromptBoundValues = False, returnPromptBoundValuesXML = False, returnPromptsAreUpToDate = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduledImport in the district.

	This function returns a dataframe of every ScheduledImport in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduledTask(searchConditions = [], EntityID = 1, returnScheduledTaskID = False, returnCreatedTime = False, returnDayOfTheMonth = False, returnEffectiveStartTime = False, returnEndDate = False, returnFrequency = False, returnFrequencyCode = False, returnFriday = False, returnIsActive = False, returnIsMonthly = False, returnIsProductionOnly = False, returnIsSelfGeneratedFromWorkflow = False, returnIsWeekly = False, returnModifiedTime = False, returnMonday = False, returnName = False, returnParameters = False, returnParametersDictionary = False, returnRepeatInterval = False, returnRepeats = False, returnRepeatUntil = False, returnSaturday = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardStartTime = False, returnStartDate = False, returnStartTime = False, returnSunday = False, returnThursday = False, returnTuesday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWednesday = False, returnWeekOfTheMonth = False, returnWorkflowID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduledTask in the district.

	This function returns a dataframe of every ScheduledTask in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduledTaskInstance(searchConditions = [], EntityID = 1, returnScheduledTaskInstanceID = False, returnCreatedTime = False, returnExecutionTime = False, returnIsPaused = False, returnModifiedTime = False, returnName = False, returnScheduledTaskID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduledTaskInstance in the district.

	This function returns a dataframe of every ScheduledTaskInstance in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScheduledTaskParameterData(searchConditions = [], EntityID = 1, returnScheduledTaskParameterDataID = False, returnCalendarYearID = False, returnCreatedTime = False, returnDistrictID = False, returnEntityID = False, returnFiscalYearID = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowVersionIDAsOfScheduling = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScheduledTaskParameterData in the district.

	This function returns a dataframe of every ScheduledTaskParameterData in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchemaHistory(searchConditions = [], EntityID = 1, returnSchemaHistoryID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnField = False, returnIndex = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPreviousField = False, returnPreviousIndex = False, returnPreviousModule = False, returnPreviousObject = False, returnReleaseVersion = False, returnScope = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchemaHistory in the district.

	This function returns a dataframe of every SchemaHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySkywardConfiguration(searchConditions = [], EntityID = 1, returnSkywardConfigurationID = False, returnAppPoolDecryptionKey = False, returnAppPoolValidationKey = False, returnCreatedTime = False, returnEncryptionKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SkywardConfiguration in the district.

	This function returns a dataframe of every SkywardConfiguration in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStandardFilter(searchConditions = [], EntityID = 1, returnStandardFilterID = False, returnButtonText = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDisplayName = False, returnFilter = False, returnFilterCondition = False, returnIsSkywardFilter = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StandardFilter in the district.

	This function returns a dataframe of every StandardFilter in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStandardFilterPrompt(searchConditions = [], EntityID = 1, returnStandardFilterPromptID = False, returnCreatedTime = False, returnModifiedTime = False, returnPromptID = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StandardFilterPrompt in the district.

	This function returns a dataframe of every StandardFilterPrompt in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStandardNormalDistribution(searchConditions = [], EntityID = 1, returnStandardNormalDistributionID = False, returnCreatedTime = False, returnModifiedTime = False, returnProbability = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZScore = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StandardNormalDistribution in the district.

	This function returns a dataframe of every StandardNormalDistribution in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryState(searchConditions = [], EntityID = 1, returnStateID = False, returnCode = False, returnCountryCode = False, returnCreatedTime = False, returnDisplayName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every State in the district.

	This function returns a dataframe of every State in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySurvey(searchConditions = [], EntityID = 1, returnSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Survey in the district.

	This function returns a dataframe of every Survey in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySurveyAnswer(searchConditions = [], EntityID = 1, returnSurveyAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyInstanceID = False, returnSurveyQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SurveyAnswer in the district.

	This function returns a dataframe of every SurveyAnswer in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySurveyInstance(searchConditions = [], EntityID = 1, returnSurveyInstanceID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyID = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SurveyInstance in the district.

	This function returns a dataframe of every SurveyInstance in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySurveyQuestion(searchConditions = [], EntityID = 1, returnSurveyQuestionID = False, returnCreatedTime = False, returnInverse = False, returnModifiedTime = False, returnQuestion = False, returnSkywardHash = False, returnSkywardID = False, returnSortNumber = False, returnSurveyID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SurveyQuestion in the district.

	This function returns a dataframe of every SurveyQuestion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySystemVersion(searchConditions = [], EntityID = 1, returnSystemVersionID = False, returnBuild = False, returnCreatedTime = False, returnMajor = False, returnMinor = False, returnModifiedTime = False, returnRevision = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVersion = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SystemVersion in the district.

	This function returns a dataframe of every SystemVersion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAttachmentError(searchConditions = [], EntityID = 1, returnTempAttachmentErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAttachmentError in the district.

	This function returns a dataframe of every TempAttachmentError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempBrowseViewColumn(searchConditions = [], EntityID = 1, returnTempBrowseViewColumnID = False, returnColumnHeaderText = False, returnColumnIndex = False, returnCreatedTime = False, returnFieldName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempBrowseViewColumn in the district.

	This function returns a dataframe of every TempBrowseViewColumn in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempDiagnostic(searchConditions = [], EntityID = 1, returnTempDiagnosticID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempDiagnostic in the district.

	This function returns a dataframe of every TempDiagnostic in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedTileYearUpdate(searchConditions = [], EntityID = 1, returnTempFailedTileYearUpdateID = False, returnCreatedTime = False, returnFailedMessage = False, returnModifiedTime = False, returnTileID = False, returnTileName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedTileYearUpdate in the district.

	This function returns a dataframe of every TempFailedTileYearUpdate in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFieldSelection(searchConditions = [], EntityID = 1, returnTempFieldSelectionID = False, returnCreatedTime = False, returnFieldID = False, returnFieldName = False, returnModifiedTime = False, returnModuleName = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFieldSelection in the district.

	This function returns a dataframe of every TempFieldSelection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempImportPreviewResultRow(searchConditions = [], EntityID = 1, returnTempImportPreviewResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnImportFileRowNumber = False, returnModifiedTime = False, returnPreviewData = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempImportPreviewResultRow in the district.

	This function returns a dataframe of every TempImportPreviewResultRow in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempLoginHistory(searchConditions = [], EntityID = 1, returnTempLoginHistoryID = False, returnBrowserType = False, returnCreatedTime = False, returnDeviceType = False, returnModifiedTime = False, returnOperatingSystemType = False, returnSuccesfulNumberOfLogins = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempLoginHistory in the district.

	This function returns a dataframe of every TempLoginHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempMassChangeResult(searchConditions = [], EntityID = 1, returnTempMassChangeResultID = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnObjectIdentifier = False, returnResult = False, returnResultCode = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempMassChangeResult in the district.

	This function returns a dataframe of every TempMassChangeResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempMedia(searchConditions = [], EntityID = 1, returnTempMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnModuleID = False, returnObjectID = False, returnProcessID = False, returnProcessIndicator = False, returnProcessIndicatorCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempMedia in the district.

	This function returns a dataframe of every TempMedia in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempUploadImportLog(searchConditions = [], EntityID = 1, returnTempUploadImportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempUploadImportLog in the district.

	This function returns a dataframe of every TempUploadImportLog in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempUsageHistory(searchConditions = [], EntityID = 1, returnTempUsageHistoryID = False, returnAverageServerResponseTime = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUsageHistoryRecordTotal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempUsageHistory in the district.

	This function returns a dataframe of every TempUsageHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempValidateBusinessObject(searchConditions = [], EntityID = 1, returnTempValidateBusinessObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempValidateBusinessObject in the district.

	This function returns a dataframe of every TempValidateBusinessObject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTheme(searchConditions = [], EntityID = 1, returnThemeID = False, returnCreatedTime = False, returnImageName = False, returnIsDefault = False, returnIsSkywardTheme = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnThemeColors = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Theme in the district.

	This function returns a dataframe of every Theme in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryThreadActivity(searchConditions = [], EntityID = 1, returnThreadActivityID = False, returnCreatedTime = False, returnLastSuccess = False, returnLastSuccessTime = False, returnModifiedTime = False, returnServerName = False, returnServiceName = False, returnStartTime = False, returnThreadName = False, returnThreadQueue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ThreadActivity in the district.

	This function returns a dataframe of every ThreadActivity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTile(searchConditions = [], EntityID = 1, returnTileID = False, returnAggregationType = False, returnAggregationTypeCode = False, returnAnimate = False, returnAnimateClockwise = False, returnAxisLabelColor = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnChartTileOptions = False, returnChartTitle = False, returnChartType = False, returnChartTypeCode = False, returnCreatedTime = False, returnDashboardID = False, returnDisplayOrder = False, returnDisplayText = False, returnHeight = False, returnIconColor = False, returnIconColorHex = False, returnIconColorRgba = False, returnIsMulticolor = False, returnLabelDisplayType = False, returnLabelDisplayTypeCode = False, returnModifiedTime = False, returnNumberPrefix = False, returnNumberSuffix = False, returnParameters = False, returnPlotHoverEffect = False, returnRotateValues = False, returnShowAlternateHGridColor = False, returnShowAlternateVGridColor = False, returnShowPercentValues = False, returnShowValues = False, returnSizeType = False, returnSizeTypeCode = False, returnTextColor = False, returnTextColorHex = False, returnTextColorRgba = False, returnTileColorType = False, returnTileColorTypeCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseRoundEdges = False, returnWidth = False, returnXAxisLabel = False, returnXAxisVariable = False, returnYAxisLabel = False, returnYAxisVariable = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Tile in the district.

	This function returns a dataframe of every Tile in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUNCPath(searchConditions = [], EntityID = 1, returnUNCPathID = False, returnCreatedTime = False, returnDomain = False, returnLocation = False, returnModifiedTime = False, returnPassword = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UNCPath in the district.

	This function returns a dataframe of every UNCPath in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUpdateTracker(searchConditions = [], EntityID = 1, returnUpdateTrackerID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnUpdateType = False, returnUpdateTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UpdateTracker in the district.

	This function returns a dataframe of every UpdateTracker in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUsageHistory(searchConditions = [], EntityID = 1, returnUsageHistoryID = False, returnBrowseFilterID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDataObjectID = False, returnEntityID = False, returnFiscalYearID = False, returnFriendlyName = False, returnHostAddress = False, returnHostname = False, returnImpersonationID = False, returnIsFullPageLoad = False, returnModifiedTime = False, returnModule = False, returnModulePath = False, returnNetworkTimeMilliseconds = False, returnObject = False, returnPageGUID = False, returnResponseSize = False, returnSchoolYearID = False, returnScreen = False, returnServerResponseTimeMilliseconds = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWindowGUID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UsageHistory in the district.

	This function returns a dataframe of every UsageHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserDock(searchConditions = [], EntityID = 1, returnUserDockID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserDock in the district.

	This function returns a dataframe of every UserDock in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserFavorite(searchConditions = [], EntityID = 1, returnUserFavoriteID = False, returnCreatedTime = False, returnDisplayOrder = False, returnFriendlyName = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserFavorite in the district.

	This function returns a dataframe of every UserFavorite in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserImportApproval(searchConditions = [], EntityID = 1, returnUserImportApprovalID = False, returnApprovalDate = False, returnCreatedTime = False, returnIsExpired = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserImportApproval in the district.

	This function returns a dataframe of every UserImportApproval in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUserMenuModule(searchConditions = [], EntityID = 1, returnUserMenuModuleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnMenuModuleID = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UserMenuModule in the district.

	This function returns a dataframe of every UserMenuModule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUsernameStructure(searchConditions = [], EntityID = 1, returnUsernameStructureID = False, returnCharacterLimitGroupID = False, returnCreatedTime = False, returnGroupTruncationOrder = False, returnIsEmployeeEmail = False, returnIsEmployeeUser = False, returnIsGuardianUser = False, returnIsStaffUser = False, returnIsStudentEmail = False, returnIsStudentUser = False, returnLimitCharacterNumber = False, returnLimitCharacterType = False, returnLimitCharacterTypeCode = False, returnMinimumLength = False, returnMinimumTiebreakerLength = False, returnModifiedTime = False, returnPartType = False, returnPartTypeCode = False, returnRank = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UsernameStructure in the district.

	This function returns a dataframe of every UsernameStructure in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryValidationRule(searchConditions = [], EntityID = 1, returnValidationRuleID = False, returnApplyOnDelete = False, returnApplyOnInsert = False, returnApplyOnUpdate = False, returnCondition = False, returnConditionData = False, returnCreatedTime = False, returnField = False, returnIgnoreOnAutoDeleteRelationship = False, returnIsActive = False, returnIsRequiredField = False, returnIsSkywardValidationRule = False, returnMessage = False, returnModifiedTime = False, returnModule = False, returnNullRelationshipBehavior = False, returnNullRelationshipBehaviorCode = False, returnObject = False, returnScreen = False, returnSeverityType = False, returnSeverityTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ValidationRule in the district.

	This function returns a dataframe of every ValidationRule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryValueSource(searchConditions = [], EntityID = 1, returnValueSourceID = False, returnBooleanValue = False, returnColumn = False, returnColumnIndex = False, returnCreatedTime = False, returnDataObjectFieldPathIDDisplay = False, returnDataType = False, returnDataTypeCode = False, returnDateTimeDateValue = False, returnDateTimeTimeValue = False, returnDecimalValue = False, returnFieldIDKey = False, returnFilterSearchCondition = False, returnFilterXML = False, returnImportID = False, returnMissingCrossReferenceAction = False, returnModifiedTime = False, returnName = False, returnNumberValue = False, returnPositionStart = False, returnPromptType = False, returnPromptTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSourceType = False, returnSourceTypeCode = False, returnSourceTypeInstance = False, returnTextValue = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnWidth = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ValueSource in the district.

	This function returns a dataframe of every ValueSource in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)