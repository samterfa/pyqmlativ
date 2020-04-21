# This module contains Gradebook functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAcademicStandardGradingScaleGroup(searchConditions = [], EntityID = 1, returnAcademicStandardGradingScaleGroupID = False, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardGradingScaleGroup in the district.

	This function returns a dataframe of every AcademicStandardGradingScaleGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardGradingScaleGroupAcademicStandard(searchConditions = [], EntityID = 1, returnAcademicStandardGradingScaleGroupAcademicStandardID = False, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardGradingScaleGroupAcademicStandard in the district.

	This function returns a dataframe of every AcademicStandardGradingScaleGroupAcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAssessment(searchConditions = [], EntityID = 1, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Assessment in the district.

	This function returns a dataframe of every Assessment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAssignment(searchConditions = [], EntityID = 1, returnAssignmentID = False, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDClonedFrom = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Assignment in the district.

	This function returns a dataframe of every Assignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAssignmentAttachment(searchConditions = [], EntityID = 1, returnAssignmentAttachmentID = False, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AssignmentAttachment in the district.

	This function returns a dataframe of every AssignmentAttachment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAssignmentQuestion(searchConditions = [], EntityID = 1, returnAssignmentQuestionID = False, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AssignmentQuestion in the district.

	This function returns a dataframe of every AssignmentQuestion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroup(searchConditions = [], EntityID = 1, returnCalculationGroupID = False, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentAveragePercentTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentAveragePercentOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroup in the district.

	This function returns a dataframe of every CalculationGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupAcademicStandard(searchConditions = [], EntityID = 1, returnCalculationGroupAcademicStandardID = False, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnIsDescendantOfSpecifiedAcademicStandard = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupAcademicStandard in the district.

	This function returns a dataframe of every CalculationGroupAcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(searchConditions = [], EntityID = 1, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = False, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupAcademicStandardCalculationGroupHierarchyDepth in the district.

	This function returns a dataframe of every CalculationGroupAcademicStandardCalculationGroupHierarchyDepth in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupAcademicStandardGradeBucket(searchConditions = [], EntityID = 1, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupAcademicStandardGradeBucket in the district.

	This function returns a dataframe of every CalculationGroupAcademicStandardGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupAcademicStandardWeighting(searchConditions = [], EntityID = 1, returnCalculationGroupAcademicStandardWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupAcademicStandardWeighting in the district.

	This function returns a dataframe of every CalculationGroupAcademicStandardWeighting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupCategory(searchConditions = [], EntityID = 1, returnCalculationGroupCategoryID = False, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupCategory in the district.

	This function returns a dataframe of every CalculationGroupCategory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupCourse(searchConditions = [], EntityID = 1, returnCalculationGroupCourseID = False, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupCourse in the district.

	This function returns a dataframe of every CalculationGroupCourse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupGradeBucket(searchConditions = [], EntityID = 1, returnCalculationGroupGradeBucketID = False, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupGradeBucket in the district.

	This function returns a dataframe of every CalculationGroupGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupHierarchyDepth(searchConditions = [], EntityID = 1, returnCalculationGroupHierarchyDepthID = False, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupHierarchyDepth in the district.

	This function returns a dataframe of every CalculationGroupHierarchyDepth in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupSubject(searchConditions = [], EntityID = 1, returnCalculationGroupSubjectID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupSubject in the district.

	This function returns a dataframe of every CalculationGroupSubject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupSubjectAcademicStandard(searchConditions = [], EntityID = 1, returnCalculationGroupSubjectAcademicStandardID = False, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupSubjectAcademicStandard in the district.

	This function returns a dataframe of every CalculationGroupSubjectAcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupSubjectGradeBucket(searchConditions = [], EntityID = 1, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupSubjectGradeBucket in the district.

	This function returns a dataframe of every CalculationGroupSubjectGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupSubjectWeighting(searchConditions = [], EntityID = 1, returnCalculationGroupSubjectWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupSubjectWeighting in the district.

	This function returns a dataframe of every CalculationGroupSubjectWeighting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalculationGroupWeighting(searchConditions = [], EntityID = 1, returnCalculationGroupWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalculationGroupWeighting in the district.

	This function returns a dataframe of every CalculationGroupWeighting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCategory(searchConditions = [], EntityID = 1, returnCategoryID = False, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Category in the district.

	This function returns a dataframe of every Category in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCategoryGradeBucketType(searchConditions = [], EntityID = 1, returnCategoryGradeBucketTypeID = False, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CategoryGradeBucketType in the district.

	This function returns a dataframe of every CategoryGradeBucketType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryClassGroup(searchConditions = [], EntityID = 1, returnClassGroupID = False, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ClassGroup in the district.

	This function returns a dataframe of every ClassGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryClassGroupSection(searchConditions = [], EntityID = 1, returnClassGroupSectionID = False, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ClassGroupSection in the district.

	This function returns a dataframe of every ClassGroupSection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryClosedGradingPeriodGradeChange(searchConditions = [], EntityID = 1, returnClosedGradingPeriodGradeChangeID = False, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ClosedGradingPeriodGradeChange in the district.

	This function returns a dataframe of every ClosedGradingPeriodGradeChange in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryClosedGradingPeriodStudentGradeBucketChange(searchConditions = [], EntityID = 1, returnClosedGradingPeriodStudentGradeBucketChangeID = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ClosedGradingPeriodStudentGradeBucketChange in the district.

	This function returns a dataframe of every ClosedGradingPeriodStudentGradeBucketChange in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntity(searchConditions = [], EntityID = 1, returnConfigEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigEntity in the district.

	This function returns a dataframe of every ConfigEntity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGradingScaleGroup(searchConditions = [], EntityID = 1, returnCourseGradingScaleGroupID = False, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGradingScaleGroup in the district.

	This function returns a dataframe of every CourseGradingScaleGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGradingScaleGroupCourse(searchConditions = [], EntityID = 1, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGradingScaleGroupCourse in the district.

	This function returns a dataframe of every CourseGradingScaleGroupCourse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDropLowScoreRun(searchConditions = [], EntityID = 1, returnDropLowScoreRunID = False, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DropLowScoreRun in the district.

	This function returns a dataframe of every DropLowScoreRun in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDropLowScoreRunStudentAssignment(searchConditions = [], EntityID = 1, returnDropLowScoreRunStudentAssignmentID = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DropLowScoreRunStudentAssignment in the district.

	This function returns a dataframe of every DropLowScoreRunStudentAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradesheetAssignmentSetting(searchConditions = [], EntityID = 1, returnGradesheetAssignmentSettingID = False, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradesheetAssignmentSetting in the district.

	This function returns a dataframe of every GradesheetAssignmentSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradingScaleGroup(searchConditions = [], EntityID = 1, returnGradingScaleGroupID = False, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradingScaleGroup in the district.

	This function returns a dataframe of every GradingScaleGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradingScaleGroupGradeMark(searchConditions = [], EntityID = 1, returnGradingScaleGroupGradeMarkID = False, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradingScaleGroupGradeMark in the district.

	This function returns a dataframe of every GradingScaleGroupGradeMark in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMonitorSummaryByClass(searchConditions = [], EntityID = 1, returnMonitorSummaryByClassID = False, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MonitorSummaryByClass in the district.

	This function returns a dataframe of every MonitorSummaryByClass in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMonitorSummaryByTeacher(searchConditions = [], EntityID = 1, returnMonitorSummaryByTeacherID = False, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MonitorSummaryByTeacher in the district.

	This function returns a dataframe of every MonitorSummaryByTeacher in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQuestion(searchConditions = [], EntityID = 1, returnQuestionID = False, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Question in the district.

	This function returns a dataframe of every Question in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQuestionAnswer(searchConditions = [], EntityID = 1, returnQuestionAnswerID = False, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedChoiceMediaSafe = False, returnHasAttachedMedia = False, returnHasAttachedMediaSafe = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QuestionAnswer in the district.

	This function returns a dataframe of every QuestionAnswer in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQuestionAnswerMedia(searchConditions = [], EntityID = 1, returnQuestionAnswerMediaID = False, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QuestionAnswerMedia in the district.

	This function returns a dataframe of every QuestionAnswerMedia in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQuestionMedia(searchConditions = [], EntityID = 1, returnQuestionMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QuestionMedia in the district.

	This function returns a dataframe of every QuestionMedia in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoreClarifier(searchConditions = [], EntityID = 1, returnScoreClarifierID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoreClarifier in the district.

	This function returns a dataframe of every ScoreClarifier in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionAcademicStandardWeight(searchConditions = [], EntityID = 1, returnSectionAcademicStandardWeightID = False, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionAcademicStandardWeight in the district.

	This function returns a dataframe of every SectionAcademicStandardWeight in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionCategory(searchConditions = [], EntityID = 1, returnSectionCategoryID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionCategory in the district.

	This function returns a dataframe of every SectionCategory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionGradeBucket(searchConditions = [], EntityID = 1, returnSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionGradeBucket in the district.

	This function returns a dataframe of every SectionGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionGradeBucketSetting(searchConditions = [], EntityID = 1, returnSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionGradeBucketSetting in the district.

	This function returns a dataframe of every SectionGradeBucketSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionGradeBucketWeight(searchConditions = [], EntityID = 1, returnSectionGradeBucketWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionGradeBucketWeight in the district.

	This function returns a dataframe of every SectionGradeBucketWeight in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionGradingPeriodData(searchConditions = [], EntityID = 1, returnSectionGradingPeriodDataID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionGradingPeriodData in the district.

	This function returns a dataframe of every SectionGradingPeriodData in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionGradingScaleGroup(searchConditions = [], EntityID = 1, returnSectionGradingScaleGroupID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionGradingScaleGroup in the district.

	This function returns a dataframe of every SectionGradingScaleGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionSubjectWeight(searchConditions = [], EntityID = 1, returnSectionSubjectWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionSubjectWeight in the district.

	This function returns a dataframe of every SectionSubjectWeight in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffMeetLastScored(searchConditions = [], EntityID = 1, returnStaffMeetLastScoredID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentAssignmentIDLastScored = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffMeetLastScored in the district.

	This function returns a dataframe of every StaffMeetLastScored in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StaffMeetLastScored/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StaffMeetLastScored/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAnswer(searchConditions = [], EntityID = 1, returnStudentAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAnswer in the district.

	This function returns a dataframe of every StudentAnswer in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAssignment(searchConditions = [], EntityID = 1, returnStudentAssignmentID = False, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAssignment in the district.

	This function returns a dataframe of every StudentAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentAssignmentAttempt(searchConditions = [], EntityID = 1, returnStudentAssignmentAttemptID = False, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentAssignmentAttempt in the district.

	This function returns a dataframe of every StudentAssignmentAttempt in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGradeBucketAcademicStandard(searchConditions = [], EntityID = 1, returnStudentGradeBucketAcademicStandardID = False, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGradeBucketAcademicStandard in the district.

	This function returns a dataframe of every StudentGradeBucketAcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGradeBucketSubject(searchConditions = [], EntityID = 1, returnStudentGradeBucketSubjectID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGradeBucketSubject in the district.

	This function returns a dataframe of every StudentGradeBucketSubject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGradingScaleGroup(searchConditions = [], EntityID = 1, returnStudentGradingScaleGroupID = False, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGradingScaleGroup in the district.

	This function returns a dataframe of every StudentGradingScaleGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGradingScaleGroupStudentSection(searchConditions = [], EntityID = 1, returnStudentGradingScaleGroupStudentSectionID = False, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGradingScaleGroupStudentSection in the district.

	This function returns a dataframe of every StudentGradingScaleGroupStudentSection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGroup(searchConditions = [], EntityID = 1, returnStudentGroupID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGroup in the district.

	This function returns a dataframe of every StudentGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGroupAssignment(searchConditions = [], EntityID = 1, returnStudentGroupAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGroupAssignment in the district.

	This function returns a dataframe of every StudentGroupAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGroupStudentSection(searchConditions = [], EntityID = 1, returnStudentGroupStudentSectionID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGroupStudentSection in the district.

	This function returns a dataframe of every StudentGroupStudentSection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGroupTeacherSectionSetting(searchConditions = [], EntityID = 1, returnStudentGroupTeacherSectionSettingID = False, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGroupTeacherSectionSetting in the district.

	This function returns a dataframe of every StudentGroupTeacherSectionSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentQuestion(searchConditions = [], EntityID = 1, returnStudentQuestionID = False, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentQuestion in the district.

	This function returns a dataframe of every StudentQuestion in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionGradingScaleGradeBucket(searchConditions = [], EntityID = 1, returnStudentSectionGradingScaleGradeBucketID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionGradingScaleGradeBucket in the district.

	This function returns a dataframe of every StudentSectionGradingScaleGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionNote(searchConditions = [], EntityID = 1, returnStudentSectionNoteID = False, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionNote in the district.

	This function returns a dataframe of every StudentSectionNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubjectGradingScaleGroup(searchConditions = [], EntityID = 1, returnSubjectGradingScaleGroupID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubjectGradingScaleGroup in the district.

	This function returns a dataframe of every SubjectGradingScaleGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubjectGradingScaleGroupSubject(searchConditions = [], EntityID = 1, returnSubjectGradingScaleGroupSubjectID = False, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubjectGradingScaleGroupSubject in the district.

	This function returns a dataframe of every SubjectGradingScaleGroupSubject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionAcademicStandardGradeBucketSetting(searchConditions = [], EntityID = 1, returnTeacherSectionAcademicStandardGradeBucketSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionAcademicStandardGradeBucketSetting in the district.

	This function returns a dataframe of every TeacherSectionAcademicStandardGradeBucketSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionCategoryAnalyticsSetting(searchConditions = [], EntityID = 1, returnTeacherSectionCategoryAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionCategoryAnalyticsSetting in the district.

	This function returns a dataframe of every TeacherSectionCategoryAnalyticsSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionGradeBucketAnalyticsSetting(searchConditions = [], EntityID = 1, returnTeacherSectionGradeBucketAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionGradeBucketAnalyticsSetting in the district.

	This function returns a dataframe of every TeacherSectionGradeBucketAnalyticsSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionGradeBucketSetting(searchConditions = [], EntityID = 1, returnTeacherSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionGradeBucketSetting in the district.

	This function returns a dataframe of every TeacherSectionGradeBucketSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionGradingPeriodSetting(searchConditions = [], EntityID = 1, returnTeacherSectionGradingPeriodSettingID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionGradingPeriodSetting in the district.

	This function returns a dataframe of every TeacherSectionGradingPeriodSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionSetting(searchConditions = [], EntityID = 1, returnTeacherSectionSettingID = False, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionSetting in the district.

	This function returns a dataframe of every TeacherSectionSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionStandardsDisplayAcademicStandardSetting(searchConditions = [], EntityID = 1, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionStandardsDisplayAcademicStandardSetting in the district.

	This function returns a dataframe of every TeacherSectionStandardsDisplayAcademicStandardSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionStandardsDisplayGradeBucketSetting(searchConditions = [], EntityID = 1, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionStandardsDisplayGradeBucketSetting in the district.

	This function returns a dataframe of every TeacherSectionStandardsDisplayGradeBucketSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionStudentSectionSetting(searchConditions = [], EntityID = 1, returnTeacherSectionStudentSectionSettingID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionStudentSectionSetting in the district.

	This function returns a dataframe of every TeacherSectionStudentSectionSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherSectionSubjectGradeBucketSetting(searchConditions = [], EntityID = 1, returnTeacherSectionSubjectGradeBucketSettingID = False, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherSectionSubjectGradeBucketSetting in the district.

	This function returns a dataframe of every TeacherSectionSubjectGradeBucketSetting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAdjustedCategory(searchConditions = [], EntityID = 1, returnTempAdjustedCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAdjustedCategory in the district.

	This function returns a dataframe of every TempAdjustedCategory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAssignmentError(searchConditions = [], EntityID = 1, returnTempAssignmentErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAssignmentError in the district.

	This function returns a dataframe of every TempAssignmentError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalcGroupBucketRemoveStandardOrSubjectResult(searchConditions = [], EntityID = 1, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = False, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalcGroupBucketRemoveStandardOrSubjectResult in the district.

	This function returns a dataframe of every TempCalcGroupBucketRemoveStandardOrSubjectResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalculationGroupAcademicStandardWeighting(searchConditions = [], EntityID = 1, returnTempCalculationGroupAcademicStandardWeightingID = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalculationGroupAcademicStandardWeighting in the district.

	This function returns a dataframe of every TempCalculationGroupAcademicStandardWeighting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalculationGroupSubjectWeighting(searchConditions = [], EntityID = 1, returnTempCalculationGroupSubjectWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalculationGroupSubjectWeighting in the district.

	This function returns a dataframe of every TempCalculationGroupSubjectWeighting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCalculationGroupWeighting(searchConditions = [], EntityID = 1, returnTempCalculationGroupWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCalculationGroupWeighting in the district.

	This function returns a dataframe of every TempCalculationGroupWeighting in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCloneGradebookSection(searchConditions = [], EntityID = 1, returnTempCloneGradebookSectionID = False, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCloneGradebookSection in the district.

	This function returns a dataframe of every TempCloneGradebookSection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourseMoveCourse(searchConditions = [], EntityID = 1, returnTempCourseMoveCourseID = False, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourseMoveCourse in the district.

	This function returns a dataframe of every TempCourseMoveCourse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourseMoveError(searchConditions = [], EntityID = 1, returnTempCourseMoveErrorID = False, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourseMoveError in the district.

	This function returns a dataframe of every TempCourseMoveError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCourseMoveSectionError(searchConditions = [], EntityID = 1, returnTempCourseMoveSectionErrorID = False, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempCourseMoveSectionError in the district.

	This function returns a dataframe of every TempCourseMoveSectionError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempDropLowScoreStudentAssignment(searchConditions = [], EntityID = 1, returnTempDropLowScoreStudentAssignmentID = False, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempDropLowScoreStudentAssignment in the district.

	This function returns a dataframe of every TempDropLowScoreStudentAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradebookCloneError(searchConditions = [], EntityID = 1, returnTempGradebookCloneErrorID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradebookCloneError in the district.

	This function returns a dataframe of every TempGradebookCloneError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradebookGroupError(searchConditions = [], EntityID = 1, returnTempGradebookGroupErrorID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradebookGroupError in the district.

	This function returns a dataframe of every TempGradebookGroupError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeMarkError(searchConditions = [], EntityID = 1, returnTempGradeMarkErrorID = False, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeMarkError in the district.

	This function returns a dataframe of every TempGradeMarkError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradingPeriodGradeBucket(searchConditions = [], EntityID = 1, returnTempGradingPeriodGradeBucketID = False, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradingPeriodGradeBucket in the district.

	This function returns a dataframe of every TempGradingPeriodGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradingPeriodGradeBucketError(searchConditions = [], EntityID = 1, returnTempGradingPeriodGradeBucketErrorID = False, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradingPeriodGradeBucketError in the district.

	This function returns a dataframe of every TempGradingPeriodGradeBucketError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionAssignment(searchConditions = [], EntityID = 1, returnTempSectionAssignmentID = False, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionAssignment in the district.

	This function returns a dataframe of every TempSectionAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionCategory(searchConditions = [], EntityID = 1, returnTempSectionCategoryID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionCategory in the district.

	This function returns a dataframe of every TempSectionCategory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionGradeBucket(searchConditions = [], EntityID = 1, returnTempSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionGradeBucket in the district.

	This function returns a dataframe of every TempSectionGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionGradeBucketWeight(searchConditions = [], EntityID = 1, returnTempSectionGradeBucketWeightID = False, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionGradeBucketWeight in the district.

	This function returns a dataframe of every TempSectionGradeBucketWeight in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionGradingScale(searchConditions = [], EntityID = 1, returnTempSectionGradingScaleID = False, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionGradingScale in the district.

	This function returns a dataframe of every TempSectionGradingScale in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempSectionGradingScaleGroupToCreate(searchConditions = [], EntityID = 1, returnTempSectionGradingScaleGroupToCreateID = False, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempSectionGradingScaleGroupToCreate in the district.

	This function returns a dataframe of every TempSectionGradingScaleGroupToCreate in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentAssignment(searchConditions = [], EntityID = 1, returnTempStudentAssignmentID = False, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentAssignment in the district.

	This function returns a dataframe of every TempStudentAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentGradingScaleGroupStudentSection(searchConditions = [], EntityID = 1, returnTempStudentGradingScaleGroupStudentSectionID = False, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentGradingScaleGroupStudentSection in the district.

	This function returns a dataframe of every TempStudentGradingScaleGroupStudentSection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempUnDropLowScoreStudentSection(searchConditions = [], EntityID = 1, returnTempUnDropLowScoreStudentSectionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempUnDropLowScoreStudentSection in the district.

	This function returns a dataframe of every TempUnDropLowScoreStudentSection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryUnenteredStudentGradeBucket(searchConditions = [], EntityID = 1, returnStudentGradeBucketID = False, returnCourseDescription = False, returnDisplayPeriodID = False, returnEntityCode = False, returnEntityID = False, returnGradeBucketID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnGradeMarkIDToApply = False, returnGradingPeriodEndDate = False, returnGradingPeriodStartDate = False, returnIsAdminOverride = False, returnPercent = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStudentGradeBucketFlag = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionEndDate = False, returnStudentSectionTransactionStartDate = False, returnUseServiceIDOverride = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every UnenteredStudentGradeBucket in the district.

	This function returns a dataframe of every UnenteredStudentGradeBucket in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/UnenteredStudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/UnenteredStudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVendorAssignment(searchConditions = [], EntityID = 1, returnVendorAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VendorAssignment in the district.

	This function returns a dataframe of every VendorAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVendorCategory(searchConditions = [], EntityID = 1, returnVendorCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VendorCategory in the district.

	This function returns a dataframe of every VendorCategory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVendorStudentAssignment(searchConditions = [], EntityID = 1, returnVendorStudentAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VendorStudentAssignment in the district.

	This function returns a dataframe of every VendorStudentAssignment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)