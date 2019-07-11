# This module contains Gradebook functions.

from .Utilities import make_request

import pandas as pd

def getEveryAcademicStandardGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradingScaleGroupID = True, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1, returnreturnAcademicStandardGradingScaleGroupID = False, returnreturnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnreturnCalculationGroupID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnGradingScaleGroupID = False, returnreturnIsAHistoricRecord = False, returnreturnIsDefaultGroup = False, returnreturnModifiedTime = False, returnreturnStandardCount = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "delete")

	return(response)

def getEveryAcademicStandardGradingScaleGroupAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradingScaleGroupAcademicStandardID = True, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1, returnreturnAcademicStandardGradingScaleGroupAcademicStandardID = False, returnreturnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnreturnAcademicStandardGradingScaleGroupID = False, returnreturnCalculationGroupAcademicStandardID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "delete")

	return(response)

def getEveryAssessment(EntityID = 1, page = 1, pageSize = 100, returnAssessmentID = True, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAssessment(AssessmentID, EntityID = 1, returnreturnAssessmentID = False, returnreturnAssignedDate = False, returnreturnAssignmentCount = False, returnreturnCanDelete = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayRestoreButton = False, returnreturnDueDate = False, returnreturnIsDeleted = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "get", params_list = params_list)

	return(response)

def deleteAssessment(AssessmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "delete")

	return(response)

def getEveryAssignment(EntityID = 1, page = 1, pageSize = 100, returnAssignmentID = True, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAssignment(AssignmentID, EntityID = 1, returnreturnAssignmentID = False, returnreturnAcademicStandardID = False, returnreturnAcademicStandards = False, returnreturnActiveStudentCount = False, returnreturnActiveStudentGroups = False, returnreturnAllowAutoScore = False, returnreturnAllStudentAssignmentsAreNotStarted = False, returnreturnAnswerRevealTime = False, returnreturnAssessmentID = False, returnreturnAssignedDate = False, returnreturnAssignmentIDParent = False, returnreturnAssignmentQuestionCount = False, returnreturnAssignmentSyncKey = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnAutoScore = False, returnreturnAveragePercent = False, returnreturnCalculatedPointsAllowedFromQuestions = False, returnreturnCanDelete = False, returnreturnCategoryID = False, returnreturnChildAssignmentCount = False, returnreturnClassesSyncedTo = False, returnreturnCreatedTime = False, returnreturnCreateStudentGroupAssignmentErrorMessage = False, returnreturnDefaultPointsPerQuestion = False, returnreturnDescription = False, returnreturnDisplayRestoreButton = False, returnreturnDueDate = False, returnreturnDueDateInCurrentOpenExtendedGradingPeriod = False, returnreturnDueDateInTransactionForGivenStudentSection = False, returnreturnDueDateIsInGivenDateRange = False, returnreturnEffectiveAcademicStandardID = False, returnreturnEndTime = False, returnreturnHasInstructions = False, returnreturnHasParent = False, returnreturnHasQuestions = False, returnreturnHasStudentAssignments = False, returnreturnHasStudentAssignmentsWithScoreOrGradeMark = False, returnreturnHasStudentFamilyAttachmentsToDisplay = False, returnreturnHasStudentGroupAssignments = False, returnreturnHasUngradedStudentAssignments = False, returnreturnHasWholeNumberWeight = False, returnreturnHideScoreUntilTime = False, returnreturnInstructions = False, returnreturnIsActiveOrUnlocked = False, returnreturnIsAHistoricRecord = False, returnreturnIsAvailableForStudentGroup = False, returnreturnIsAvailableForStudentSection = False, returnreturnIsDeleted = False, returnreturnIsOnlineAssignment = False, returnreturnIsParent = False, returnreturnIsPastEndTime = False, returnreturnIsSynced = False, returnreturnMaxScore = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnQuestionCount = False, returnreturnRandomizeQuestions = False, returnreturnRelatedAssignmentsHaveAcademicStandards = False, returnreturnRelatedAssignmentsHaveSubjects = False, returnreturnScoreDisplayType = False, returnreturnScoreDisplayTypeCode = False, returnreturnScoredStudentAssignmentCount = False, returnreturnSectionID = False, returnreturnSendNotificationWhenAnswersRevealed = False, returnreturnSendNotificationWhenAssignmentReadyToTake = False, returnreturnShowCorrectAnswers = False, returnreturnShowScore = False, returnreturnStartTime = False, returnreturnStudentFamilyAccessAttachmentCount = False, returnreturnSubjectID = False, returnreturnSubjects = False, returnreturnUseGradeMarkScoring = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeight = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteAssignment(AssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "delete")

	return(response)

def getEveryAssignmentAttachment(EntityID = 1, page = 1, pageSize = 100, returnAssignmentAttachmentID = True, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAssignmentAttachment(AssignmentAttachmentID, EntityID = 1, returnreturnAssignmentAttachmentID = False, returnreturnAssignmentID = False, returnreturnAttachmentID = False, returnreturnCreatedTime = False, returnreturnDisplayInStudentFamilyAccess = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "get", params_list = params_list)

	return(response)

def deleteAssignmentAttachment(AssignmentAttachmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "delete")

	return(response)

def getEveryAssignmentQuestion(EntityID = 1, page = 1, pageSize = 100, returnAssignmentQuestionID = True, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAssignmentQuestion(AssignmentQuestionID, EntityID = 1, returnreturnAssignmentQuestionID = False, returnreturnAllowPartialCredit = False, returnreturnAssignmentID = False, returnreturnCreatedTime = False, returnreturnDisplayOrder = False, returnreturnModifiedTime = False, returnreturnPointsAllowed = False, returnreturnQuestionAnswerCount = False, returnreturnQuestionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "get", params_list = params_list)

	return(response)

def deleteAssignmentQuestion(AssignmentQuestionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "delete")

	return(response)

def getEveryCalculationGroup(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupID = True, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroup(CalculationGroupID, EntityID = 1, returnreturnCalculationGroupID = False, returnreturnAllowAcademicStandardWeightingTeacherOverride = False, returnreturnAllowAssignmentPointsTeacherOverride = False, returnreturnAllowCategoryOverride = False, returnreturnAllowCategoryWeightingTeacherOverride = False, returnreturnAllowDecayingAverageTeacherOverride = False, returnreturnAllowedTeacherOverrideCalculationTypes = False, returnreturnAllowGradeBucketWeightingTeacherOverride = False, returnreturnAllowNotGradedTeacherOverride = False, returnreturnAllowSubjectiveTeacherOverride = False, returnreturnAllowSubjectWeightingTeacherOverride = False, returnreturnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnreturnCalculationGroupIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDecayingAveragePercent = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnFilter = False, returnreturnHasAcademicStandards = False, returnreturnHasAcademicStandardWeightingOverrides = False, returnreturnHasAssignmentPointsOverrides = False, returnreturnHasCategoryWeightingOverrides = False, returnreturnHasDecayingAverage = False, returnreturnHasDecayingAverageOverrides = False, returnreturnHasDefaultCloneFilter = False, returnreturnHasGradeBucketWeightingOverrides = False, returnreturnHasNotGradedOverrides = False, returnreturnHasSubjectiveOverrides = False, returnreturnHasSubjects = False, returnreturnHasSubjectWeightingOverrides = False, returnreturnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnreturnIsAHistoricRecord = False, returnreturnIsDefaultGroup = False, returnreturnLimitTeacherOverridesToCategoriesInGroup = False, returnreturnModifiedTime = False, returnreturnRank = False, returnreturnSchoolYearID = False, returnreturnSearchConditionFilter = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroup(CalculationGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "delete")

	return(response)

def getEveryCalculationGroupAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardID = True, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1, returnreturnCalculationGroupAcademicStandardID = False, returnreturnAcademicStandardID = False, returnreturnCalculateForSingleBucket = False, returnreturnCalculationGroupAcademicStandardIDClonedFrom = False, returnreturnCalculationGroupAcademicStandardIDParent = False, returnreturnCalculationGroupID = False, returnreturnCreatedTime = False, returnreturnDisplayOnReportCard = False, returnreturnEntityGroupKey = False, returnreturnHasAssignments = False, returnreturnHasGradingScale = False, returnreturnHasParentSubject = False, returnreturnLevel = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "delete")

	return(response)

def getEveryCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = True, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1, returnreturnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = False, returnreturnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnreturnCalculationGroupAcademicStandardID = False, returnreturnCalculationGroupAcademicStandardIDAtLevel = False, returnreturnCalculationGroupHierarchyDepthID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "delete")

	return(response)

def getEveryCalculationGroupAcademicStandardGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardGradeBucketID = True, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1, returnreturnCalculationGroupAcademicStandardGradeBucketID = False, returnreturnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnreturnCalculationGroupAcademicStandardID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCalculationType = False, returnreturnCalculationTypeCode = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnHasAcademicStandardWeighting = False, returnreturnHasAssignments = False, returnreturnHasCalculationGroupSubjectWeight = False, returnreturnHasCalculationGroupWeight = False, returnreturnHasCategoryWeighting = False, returnreturnIsAHistoricRecord = False, returnreturnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnreturnIsWeightedOnInASectionOverride = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "delete")

	return(response)

def getEveryCalculationGroupAcademicStandardWeighting(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1, returnreturnCalculationGroupAcademicStandardWeightingID = False, returnreturnAcademicStandardAdjustedPercentEarned = False, returnreturnAcademicStandardAdjustedPointsEarned = False, returnreturnAcademicStandardAdjustedWeightFormula = False, returnreturnAcademicStandardIDToWeight = False, returnreturnAdjustedWeightPercent = False, returnreturnCalculationGroupAcademicStandardGradeBucketID = False, returnreturnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnreturnCategoryAdjustedPercentEarned = False, returnreturnCategoryAdjustedPointsEarned = False, returnreturnCategoryAdjustedWeightFormula = False, returnreturnCategoryIDToWeight = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnHasAssignments = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnPercentEarnedCategory = False, returnreturnPointsEarnedCategory = False, returnreturnUseForWeightSum = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "delete")

	return(response)

def getEveryCalculationGroupCategory(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupCategoryID = True, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1, returnreturnCalculationGroupCategoryID = False, returnreturnCalculationGroupCategoryIDClonedFrom = False, returnreturnCalculationGroupID = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnHasAssignments = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "delete")

	return(response)

def getEveryCalculationGroupCourse(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupCourseID = True, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1, returnreturnCalculationGroupCourseID = False, returnreturnCalculationGroupCourseIDClonedFrom = False, returnreturnCalculationGroupID = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "delete")

	return(response)

def getEveryCalculationGroupGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupGradeBucketID = True, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1, returnreturnCalculationGroupGradeBucketID = False, returnreturnAllowCalculationTypeOverride = False, returnreturnAllowWeightOverride = False, returnreturnCalculationGroupGradeBucketIDClonedFrom = False, returnreturnCalculationGroupID = False, returnreturnCalculationType = False, returnreturnCalculationTypeCode = False, returnreturnCourseCount = False, returnreturnCreatedTime = False, returnreturnEffectiveCalculationType = False, returnreturnEffectiveCalculationTypeCode = False, returnreturnEntityGroupKey = False, returnreturnGetCopySectionLengthXMLFilter = False, returnreturnGradeMarkScoringType = False, returnreturnGradeMarkScoringTypeCode = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnHasAcademicStandards = False, returnreturnHasAcademicStandardWeighting = False, returnreturnHasCategoryWeighting = False, returnreturnHasGradeBucketWeighting = False, returnreturnHasSubjects = False, returnreturnHasSubjectWeighting = False, returnreturnInnerCalculationGroupGradeBucketsCount = False, returnreturnInUseBySections = False, returnreturnIsAHistoricRecord = False, returnreturnIsMissingStudentGradeBucketAcademicStandards = False, returnreturnIsMissingStudentGradeBucketSubjects = False, returnreturnModifiedTime = False, returnreturnNumberOfCategories = False, returnreturnRoundBucketPercent = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercentTotal = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "delete")

	return(response)

def getEveryCalculationGroupHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupHierarchyDepthID = True, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1, returnreturnCalculationGroupHierarchyDepthID = False, returnreturnCalculationGroupHierarchyDepthIDClonedFrom = False, returnreturnCalculationGroupID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDepthLevel = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "delete")

	return(response)

def getEveryCalculationGroupSubject(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectID = True, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1, returnreturnCalculationGroupSubjectID = False, returnreturnCalculationGroupID = False, returnreturnCalculationGroupSubjectIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnHasAssignments = False, returnreturnHasGradingScale = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnSubjectID = False, returnreturnTopLevelAcademicStandardHierarchyDepthDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "delete")

	return(response)

def getEveryCalculationGroupSubjectAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectAcademicStandardID = True, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1, returnreturnCalculationGroupSubjectAcademicStandardID = False, returnreturnAcademicStandardID = False, returnreturnCalculationGroupID = False, returnreturnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnSubjectID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "delete")

	return(response)

def getEveryCalculationGroupSubjectGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1, returnreturnCalculationGroupSubjectGradeBucketID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnreturnCalculationGroupSubjectID = False, returnreturnCalculationType = False, returnreturnCalculationTypeCode = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnHasAssignments = False, returnreturnHasCalculationGroupWeight = False, returnreturnHasCategoryWeighting = False, returnreturnHasSubjectAcademicStandards = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "delete")

	return(response)

def getEveryCalculationGroupSubjectWeighting(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1, returnreturnCalculationGroupSubjectWeightingID = False, returnreturnAcademicStandardAdjustedPercentEarned = False, returnreturnAcademicStandardAdjustedPointsEarned = False, returnreturnAcademicStandardAdjustedWeightFormula = False, returnreturnAcademicStandardIDToWeight = False, returnreturnAdjustedWeightPercent = False, returnreturnCalculationGroupSubjectGradeBucketID = False, returnreturnCalculationGroupSubjectWeightingIDClonedFrom = False, returnreturnCategoryAdjustedPercentEarned = False, returnreturnCategoryAdjustedPointsEarned = False, returnreturnCategoryAdjustedWeightFormula = False, returnreturnCategoryIDToWeight = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnHasAssignments = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnPercentEarnedCategory = False, returnreturnPointsEarnedCategory = False, returnreturnUseForWeightSum = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "delete")

	return(response)

def getEveryCalculationGroupWeighting(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1, returnreturnCalculationGroupWeightingID = False, returnreturnAcademicStandardAdjustedPercentEarned = False, returnreturnAcademicStandardAdjustedPointsEarned = False, returnreturnAcademicStandardIDToWeight = False, returnreturnAcademicStandardWeightFormula = False, returnreturnAdjustedAcademicStandardWeightPercent = False, returnreturnAdjustedCategoryWeightPercent = False, returnreturnAdjustedGradeBucketWeightPercent = False, returnreturnAdjustedSubjectWeightPercent = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCalculationGroupWeightingIDClonedFrom = False, returnreturnCategoryAdjustedPercentEarned = False, returnreturnCategoryAdjustedPointsEarned = False, returnreturnCategoryIDToWeight = False, returnreturnCategoryWeightFormula = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGradeBucketAdjustedPercentEarned = False, returnreturnGradeBucketAdjustedPointsEarned = False, returnreturnGradeBucketWeightFormula = False, returnreturnGradingPeriodGradeBucketIDToWeight = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnPercentEarnedForCategory = False, returnreturnPointsEarnedForCategory = False, returnreturnRequiredGrade = False, returnreturnRoundBucketPercent = False, returnreturnSubjectAdjustedPercentEarned = False, returnreturnSubjectAdjustedPointsEarned = False, returnreturnSubjectIDToWeight = False, returnreturnSubjectWeightFormula = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "delete")

	return(response)

def getEveryCategory(EntityID = 1, page = 1, pageSize = 100, returnCategoryID = True, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCategory(CategoryID, EntityID = 1, returnreturnCategoryID = False, returnreturnAssignmentCount = False, returnreturnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnreturnBackgroundColor = False, returnreturnCalculationGroupAllowCategoryOverride = False, returnreturnCategoryIDClonedFrom = False, returnreturnCategoryUsedInCategoryWeightingDefaultSetup = False, returnreturnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDescriptionWithCategoryWeightPercent = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnGradeBucketTypeCategory = False, returnreturnHasAssignments = False, returnreturnHasSpecificCalculationGroupAcademicStandardWeight = False, returnreturnHasSpecificCalculationGroupSubjectWeight = False, returnreturnHasSpecificCalculationGroupWeight = False, returnreturnIsAHistoricRecord = False, returnreturnIsValidInCalculationGroup = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnTextColor = False, returnreturnUseForSpecificGradeBucketType = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightingAllowedForGradeBucketType = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteCategory(CategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "delete")

	return(response)

def getEveryCategoryGradeBucketType(EntityID = 1, page = 1, pageSize = 100, returnCategoryGradeBucketTypeID = True, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1, returnreturnCategoryGradeBucketTypeID = False, returnreturnCategoryGradeBucketTypeIDClonedFrom = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGradeBucketTypeID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "delete")

	return(response)

def getEveryClassGroup(EntityID = 1, page = 1, pageSize = 100, returnClassGroupID = True, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getClassGroup(ClassGroupID, EntityID = 1, returnreturnClassGroupID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnSchoolYearID = False, returnreturnStaffID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteClassGroup(ClassGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "delete")

	return(response)

def getEveryClassGroupSection(EntityID = 1, page = 1, pageSize = 100, returnClassGroupSectionID = True, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getClassGroupSection(ClassGroupSectionID, EntityID = 1, returnreturnClassGroupSectionID = False, returnreturnClassGroupID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteClassGroupSection(ClassGroupSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "delete")

	return(response)

def getEveryClosedGradingPeriodGradeChange(EntityID = 1, page = 1, pageSize = 100, returnClosedGradingPeriodGradeChangeID = True, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1, returnreturnClosedGradingPeriodGradeChangeID = False, returnreturnCalculatedCompletedTime = False, returnreturnCompletedTime = False, returnreturnCreatedTime = False, returnreturnDisplayCompleteButton = False, returnreturnDisplayMassReviewDenyButton = False, returnreturnGradingPeriodID = False, returnreturnModifiedTime = False, returnreturnReason = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "get", params_list = params_list)

	return(response)

def deleteClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "delete")

	return(response)

def getEveryClosedGradingPeriodStudentGradeBucketChange(EntityID = 1, page = 1, pageSize = 100, returnClosedGradingPeriodStudentGradeBucketChangeID = True, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1, returnreturnClosedGradingPeriodStudentGradeBucketChangeID = False, returnreturnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnreturnClosedGradingPeriodGradeChangeID = False, returnreturnClosedGradingPeriodGradeChangeStatus = False, returnreturnClosedGradingPeriodGradeChangeStatusCode = False, returnreturnCreatedTime = False, returnreturnGradeMarkIDNew = False, returnreturnGradeMarkIDOriginal = False, returnreturnHasSnapshot = False, returnreturnIsDisabled = False, returnreturnIsGradeChangePastDueAndInProgress = False, returnreturnModifiedTime = False, returnreturnNewPercent = False, returnreturnOriginalPercent = False, returnreturnStaffMeetID = False, returnreturnStudentGradeBucketID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "get", params_list = params_list)

	return(response)

def deleteClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "delete")

	return(response)

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnreturnConfigDistrictID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnreturnConfigDistrictYearID = False, returnreturnConfigDistrictYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUseCurriculumSubjectsInGradebook = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getEveryConfigEntity(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntity(ConfigEntityID, EntityID = 1, returnreturnConfigEntityID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnRunInMonitorByScheduledTask = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntity(ConfigEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "delete")

	return(response)

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnreturnConfigEntityGroupYearID = False, returnreturnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnreturnAllowGracePeriodAtEndOfGradingPeriod = False, returnreturnAllowMultipleAssignmentAttempts = False, returnreturnAllowNegativePercentAdjustment = False, returnreturnAllowOnlineAssignments = False, returnreturnAllowPercentAdjustment = False, returnreturnAllowRetainedFutureScoring = False, returnreturnAllowStudentGroups = False, returnreturnAllowTeacherComments = False, returnreturnAllowTeachersToAddStudentNotes = False, returnreturnAllowTeachersToOverrideDefaultMaxScore = False, returnreturnAllowTeachersToOverrideDefaultMaxWeight = False, returnreturnAllowTeachersToTransferGrades = False, returnreturnAssignmentMaxScore = False, returnreturnAssignmentMaxWeight = False, returnreturnAutoApproveGradeChangeRequest = False, returnreturnCapCalculationAt100Percent = False, returnreturnCapWeightedCategoryCalculationAt100Percent = False, returnreturnClosedGradingPeriodGradeChangeCutOff = False, returnreturnClosedGradingPeriodGradeChangePermissionType = False, returnreturnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnreturnConfigEntityGroupYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDisplayNonGradedClassesForTeachers = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnFailingGradeThresholdPercent = False, returnreturnGradingPeriodEditExtensionDays = False, returnreturnGradingPeriodEditExtensionEndTime = False, returnreturnModifiedTime = False, returnreturnNumberOfDaysUntilNewStudentIconAppears = False, returnreturnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnreturnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnreturnSchoolYearID = False, returnreturnScoreClarifierIDFailing = False, returnreturnUseFailingGradeScoreClarifier = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getEveryCourseGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnCourseGradingScaleGroupID = True, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1, returnreturnCourseGradingScaleGroupID = False, returnreturnAllowSectionOverride = False, returnreturnCourseGradingScaleGroupIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnFilter = False, returnreturnGradingScaleGroupID = False, returnreturnIsAHistoricRecord = False, returnreturnIsDefaultGroup = False, returnreturnLimitTeacherOverridesToGradeMarksInGroup = False, returnreturnModifiedTime = False, returnreturnRank = False, returnreturnSchoolYearID = False, returnreturnSearchConditionFilter = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "delete")

	return(response)

def getEveryCourseGradingScaleGroupCourse(EntityID = 1, page = 1, pageSize = 100, returnCourseGradingScaleGroupCourseID = True, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1, returnreturnCourseGradingScaleGroupCourseID = False, returnreturnCourseGradingScaleGroupID = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "delete")

	return(response)

def getEveryDropLowScoreRun(EntityID = 1, page = 1, pageSize = 100, returnDropLowScoreRunID = True, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDropLowScoreRun(DropLowScoreRunID, EntityID = 1, returnreturnDropLowScoreRunID = False, returnreturnAffectedStudentAssignmentCount = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCreatedTime = False, returnreturnIsEffective = False, returnreturnModifiedTime = False, returnreturnRunTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "get", params_list = params_list)

	return(response)

def deleteDropLowScoreRun(DropLowScoreRunID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "delete")

	return(response)

def getEveryDropLowScoreRunStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnDropLowScoreRunStudentAssignmentID = True, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1, returnreturnDropLowScoreRunStudentAssignmentID = False, returnreturnCreatedTime = False, returnreturnDropActionType = False, returnreturnDropActionTypeCode = False, returnreturnDropLowScoreRunID = False, returnreturnModifiedTime = False, returnreturnStudentAssignmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "delete")

	return(response)

def getEveryGradesheetAssignmentSetting(EntityID = 1, page = 1, pageSize = 100, returnGradesheetAssignmentSettingID = True, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1, returnreturnGradesheetAssignmentSettingID = False, returnreturnCreatedTime = False, returnreturnDefaultAttemptType = False, returnreturnDefaultAttemptTypeCode = False, returnreturnIsDateAscending = False, returnreturnMaxScoreDefault = False, returnreturnModifiedTime = False, returnreturnSortBy = False, returnreturnSortByCode = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "delete")

	return(response)

def getEveryGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnGradingScaleGroupID = True, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradingScaleGroup(GradingScaleGroupID, EntityID = 1, returnreturnGradingScaleGroupID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayGradeMarkPercentages = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGradeMarkIDMastered = False, returnreturnGradingScaleGroupExistsInSpecifcEntity = False, returnreturnGradingScaleGroupIDClonedFrom = False, returnreturnGradingScaleType = False, returnreturnGradingScaleTypeCode = False, returnreturnHasAcademicStandardGradingScaleGroups = False, returnreturnHasCourseGradingScaleGroups = False, returnreturnHasSectionGradingScaleGroups = False, returnreturnHasStudentGradingScaleGroups = False, returnreturnHasSubjectGradingScaleGroups = False, returnreturnIsAHistoricRecord = False, returnreturnIsDefaultAcademicStandardGradingScaleGroup = False, returnreturnIsDefaultSubjectGradingScaleGroup = False, returnreturnIsDummySectionContainer = False, returnreturnIsPointsBasedScale = False, returnreturnIsSectionRelatedGradingScaleGroup = False, returnreturnMaxScore = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnSectionIDTeacherOverride = False, returnreturnUseAsMastery = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteGradingScaleGroup(GradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "delete")

	return(response)

def getEveryGradingScaleGroupGradeMark(EntityID = 1, page = 1, pageSize = 100, returnGradingScaleGroupGradeMarkID = True, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1, returnreturnGradingScaleGroupGradeMarkID = False, returnreturnAllowSubjective = False, returnreturnColor = False, returnreturnCreatedTime = False, returnreturnDefaultCalculationPercent = False, returnreturnDefaultCalculationPoints = False, returnreturnEntityGroupKey = False, returnreturnGradeMarkID = False, returnreturnGradingScaleGroupGradeMarkIDClonedFrom = False, returnreturnGradingScaleGroupID = False, returnreturnModifiedTime = False, returnreturnPercentHigh = False, returnreturnPercentLow = False, returnreturnPointsHigh = False, returnreturnPointsLow = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "delete")

	return(response)

def getEveryMonitorSummaryByClass(EntityID = 1, page = 1, pageSize = 100, returnMonitorSummaryByClassID = True, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1, returnreturnMonitorSummaryByClassID = False, returnreturnAssignmentCountForTerm = False, returnreturnAssignmentCountYTD = False, returnreturnClosedGradingPeriodGradeChangeCount = False, returnreturnCreatedTime = False, returnreturnCurrentGradingPeriod = False, returnreturnExcusedAbsencesYTD = False, returnreturnFutureAssignmentCountForTerm = False, returnreturnGradedAssignmentCountForTerm = False, returnreturnLastAccessedGradebookTime = False, returnreturnLastScoredGradebookTime = False, returnreturnLastUpdatedTime = False, returnreturnMissingAssignmentCountForTerm = False, returnreturnModifiedTime = False, returnreturnNoCountAssignmentCountForTerm = False, returnreturnNonGradedAssignmentCountForTerm = False, returnreturnOffenseCountYTD = False, returnreturnOtherAbsencesYTD = False, returnreturnScoreClarifierAssignmentCountForTerm = False, returnreturnScoredAssignmentRange0CurrentTerm = False, returnreturnScoredAssignmentRange100to90CurrentTerm = False, returnreturnScoredAssignmentRange49to1CurrentTerm = False, returnreturnScoredAssignmentRange59to50CurrentTerm = False, returnreturnScoredAssignmentRange69to60CurrentTerm = False, returnreturnScoredAssignmentRange79to70CurrentTerm = False, returnreturnScoredAssignmentRange89to80CurrentTerm = False, returnreturnStaffMeetID = False, returnreturnStudentCountForTerm = False, returnreturnTardiesYTD = False, returnreturnUnexcusedAbsencesYTD = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "get", params_list = params_list)

	return(response)

def deleteMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "delete")

	return(response)

def getEveryMonitorSummaryByTeacher(EntityID = 1, page = 1, pageSize = 100, returnMonitorSummaryByTeacherID = True, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1, returnreturnMonitorSummaryByTeacherID = False, returnreturnActiveStudentCount = False, returnreturnAssignmentCountForTerm = False, returnreturnCreatedTime = False, returnreturnFutureAssignmentCountForTerm = False, returnreturnGradedAssignmentCountForTerm = False, returnreturnLastAccessedGradebookTime = False, returnreturnLastAssignmentScoredDueDate = False, returnreturnLastScoredAssignmentTime = False, returnreturnLastUpdatedTime = False, returnreturnMissingAssignmentCountForTerm = False, returnreturnModifiedTime = False, returnreturnNoCountAssignmentCountForTerm = False, returnreturnNonGradedAssignmentCountForTerm = False, returnreturnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnreturnSchoolYearID = False, returnreturnScoreClarifierAssignmentCountForTerm = False, returnreturnStaffID = False, returnreturnStaffMeetCount = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "get", params_list = params_list)

	return(response)

def deleteMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "delete")

	return(response)

def getEveryQuestion(EntityID = 1, page = 1, pageSize = 100, returnQuestionID = True, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQuestion(QuestionID, EntityID = 1, returnreturnQuestionID = False, returnreturnAllowStudentAttachments = False, returnreturnAssignmentCount = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnHasAssignmentPastEndTime = False, returnreturnHasAutoScoredAssignment = False, returnreturnHasInstructions = False, returnreturnHasMultipleAssignments = False, returnreturnHasQuestionMedias = False, returnreturnInstructions = False, returnreturnIsEssay = False, returnreturnIsMatching = False, returnreturnIsMultipleChoice = False, returnreturnIsShortAnswer = False, returnreturnIsTrueFalse = False, returnreturnModifiedTime = False, returnreturnStaffID = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUseAnswers = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestion(QuestionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "delete")

	return(response)

def getEveryQuestionAnswer(EntityID = 1, page = 1, pageSize = 100, returnQuestionAnswerID = True, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedMedia = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQuestionAnswer(QuestionAnswerID, EntityID = 1, returnreturnQuestionAnswerID = False, returnreturnChoice = False, returnreturnChoiceOrder = False, returnreturnCreatedTime = False, returnreturnHasAttachedChoiceMedia = False, returnreturnHasAttachedMedia = False, returnreturnIsCorrect = False, returnreturnIsEssay = False, returnreturnIsMultipleChoice = False, returnreturnIsShortAnswer = False, returnreturnIsTrueFalse = False, returnreturnModifiedTime = False, returnreturnQuestionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValue = False, returnreturnValueOrder = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestionAnswer(QuestionAnswerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "delete")

	return(response)

def getEveryQuestionAnswerMedia(EntityID = 1, page = 1, pageSize = 100, returnQuestionAnswerMediaID = True, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1, returnreturnQuestionAnswerMediaID = False, returnreturnCreatedTime = False, returnreturnDisplayFor = False, returnreturnDisplayForCode = False, returnreturnMediaID = False, returnreturnModifiedTime = False, returnreturnQuestionAnswerID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "delete")

	return(response)

def getEveryQuestionMedia(EntityID = 1, page = 1, pageSize = 100, returnQuestionMediaID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQuestionMedia(QuestionMediaID, EntityID = 1, returnreturnQuestionMediaID = False, returnreturnCreatedTime = False, returnreturnMediaID = False, returnreturnModifiedTime = False, returnreturnQuestionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestionMedia(QuestionMediaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "delete")

	return(response)

def getEveryScoreClarifier(EntityID = 1, page = 1, pageSize = 100, returnScoreClarifierID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getScoreClarifier(ScoreClarifierID, EntityID = 1, returnreturnScoreClarifierID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnIsAHistoricRecord = False, returnreturnIsMissing = False, returnreturnModifiedTime = False, returnreturnNoCount = False, returnreturnSchoolYearID = False, returnreturnScoreClarifierIDClonedFrom = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "get", params_list = params_list)

	return(response)

def deleteScoreClarifier(ScoreClarifierID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "delete")

	return(response)

def getEverySectionAcademicStandardWeight(EntityID = 1, page = 1, pageSize = 100, returnSectionAcademicStandardWeightID = True, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1, returnreturnSectionAcademicStandardWeightID = False, returnreturnAcademicStandardID = False, returnreturnAdjustedPercentEarned = False, returnreturnAdjustedPointsEarned = False, returnreturnAdjustedWeightPercent = False, returnreturnCreatedTime = False, returnreturnHasAssignments = False, returnreturnModifiedTime = False, returnreturnSectionGradeBucketID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightFormula = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "delete")

	return(response)

def getEverySectionCategory(EntityID = 1, page = 1, pageSize = 100, returnSectionCategoryID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionCategory(SectionCategoryID, EntityID = 1, returnreturnSectionCategoryID = False, returnreturnAdjustedPercentEarned = False, returnreturnAdjustedPointsEarned = False, returnreturnAdjustedWeightPercent = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnHasAssignments = False, returnreturnModifiedTime = False, returnreturnPercentEarnedForCategory = False, returnreturnPointsEarnedForCategory = False, returnreturnSectionGradeBucketID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightFormula = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionCategory(SectionCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "delete")

	return(response)

def getEverySectionGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionGradeBucket(SectionGradeBucketID, EntityID = 1, returnreturnSectionGradeBucketID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCalculationModifiedTime = False, returnreturnCalculationType = False, returnreturnCalculationTypeCode = False, returnreturnCreatedTime = False, returnreturnEffectiveCalculationType = False, returnreturnEffectiveCalculationTypeCode = False, returnreturnHasSectionAcademicStandardWeights = False, returnreturnHasSectionCategories = False, returnreturnHasSectionGradeBucketWeights = False, returnreturnHasSectionSubjectWeights = False, returnreturnIsAHistoricRecord = False, returnreturnIsCalculationTypeOverridden = False, returnreturnIsOverridden = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradeBucket(SectionGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "delete")

	return(response)

def getEverySectionGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1, returnreturnSectionGradeBucketSettingID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnMaxExtraCredit = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUseMaxExtraCredit = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "delete")

	return(response)

def getEverySectionGradeBucketWeight(EntityID = 1, page = 1, pageSize = 100, returnSectionGradeBucketWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1, returnreturnSectionGradeBucketWeightID = False, returnreturnAdjustedPercentEarned = False, returnreturnAdjustedPointsEarned = False, returnreturnAdjustedWeightPercent = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnRoundBucketPercent = False, returnreturnSectionGradeBucketIDComposite = False, returnreturnSectionGradeBucketIDFeeder = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightFormula = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "delete")

	return(response)

def getEverySectionGradingPeriodData(EntityID = 1, page = 1, pageSize = 100, returnSectionGradingPeriodDataID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1, returnreturnSectionGradingPeriodDataID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodID = False, returnreturnIsCompleted = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "delete")

	return(response)

def getEverySectionGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnSectionGradingScaleGroupID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1, returnreturnSectionGradingScaleGroupID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnGradingScaleGroupID = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnSectionGradingScaleGroupIDClonedFrom = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "delete")

	return(response)

def getEverySectionSubjectWeight(EntityID = 1, page = 1, pageSize = 100, returnSectionSubjectWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1, returnreturnSectionSubjectWeightID = False, returnreturnAdjustedPercentEarned = False, returnreturnAdjustedPointsEarned = False, returnreturnAdjustedWeightPercent = False, returnreturnCreatedTime = False, returnreturnHasAssignments = False, returnreturnModifiedTime = False, returnreturnSectionGradeBucketID = False, returnreturnSubjectID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightFormula = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "delete")

	return(response)

def getEveryStudentAnswer(EntityID = 1, page = 1, pageSize = 100, returnStudentAnswerID = True, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAnswer(StudentAnswerID, EntityID = 1, returnreturnStudentAnswerID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnQuestionAnswerID = False, returnreturnStudentQuestionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValue = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAnswer(StudentAnswerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "delete")

	return(response)

def getEveryStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnStudentAssignmentID = True, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAssignment(StudentAssignmentID, EntityID = 1, returnreturnStudentAssignmentID = False, returnreturnAllQuestionsScored = False, returnreturnAnsweredQuestionCount = False, returnreturnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnreturnAnswerKeyIsAvailableToView = False, returnreturnAssignmentDueDateAttendance = False, returnreturnAssignmentID = False, returnreturnAttemptCount = False, returnreturnCalculatedPoints = False, returnreturnCannotBeTakenByStudent = False, returnreturnComments = False, returnreturnCreatedTime = False, returnreturnCurrentQuestionNumber = False, returnreturnFormattedPointsEarnedPercent = False, returnreturnFormattedPointsEarnedPercentCheckDisplay = False, returnreturnGradeMarkCode = False, returnreturnGradeMarkID = False, returnreturnHasAnswers = False, returnreturnHasStudentSectionTransaction = False, returnreturnIsDropped = False, returnreturnIsExpired = False, returnreturnIsFutureRetainedScore = False, returnreturnIsGraded = False, returnreturnIsMissing = False, returnreturnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnreturnIsScored = False, returnreturnIsTransferredScore = False, returnreturnModifiedTime = False, returnreturnNoCount = False, returnreturnOnlineAssignmentNotificationSent = False, returnreturnOnlineAssignmentReviewNotificationSent = False, returnreturnPointsEarned = False, returnreturnPointsEarnedPercent = False, returnreturnPointsEarnedWithSlash = False, returnreturnPointsEarnedWithSlashCheckDisplay = False, returnreturnScore = False, returnreturnScoreClarifierID = False, returnreturnScoreDisplayValue = False, returnreturnScoreDisplayValueNoGradeMark = False, returnreturnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnreturnSectionID = False, returnreturnStudentOnlineAssignmentDisplayPointsEarned = False, returnreturnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnreturnStudentQuestionCount = False, returnreturnStudentSectionID = False, returnreturnSubmissionStatus = False, returnreturnSubmissionStatusCode = False, returnreturnSubmissionStatusCodeToUse = False, returnreturnSubmissionStatusToUse = False, returnreturnSubmissionTime = False, returnreturnTimeLastScored = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAssignment(StudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "delete")

	return(response)

def getEveryStudentAssignmentAttempt(EntityID = 1, page = 1, pageSize = 100, returnStudentAssignmentAttemptID = True, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1, returnreturnStudentAssignmentAttemptID = False, returnreturnComments = False, returnreturnCreatedTime = False, returnreturnDateAttempted = False, returnreturnGradeMarkID = False, returnreturnIsUsed = False, returnreturnModifiedTime = False, returnreturnScore = False, returnreturnStudentAssignmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "delete")

	return(response)

def getEveryStudentGradeBucketAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketAcademicStandardID = True, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1, returnreturnStudentGradeBucketAcademicStandardID = False, returnreturnAcademicStandardID = False, returnreturnCalculatedPoints = False, returnreturnCreatedTime = False, returnreturnEarnedPoints = False, returnreturnGradeMarkID = False, returnreturnGradeMarkIDOverride = False, returnreturnGradeMarkOverrideComment = False, returnreturnGradeMarkToUse = False, returnreturnIsAdminOverride = False, returnreturnIsUsingPointsBasedScale = False, returnreturnModifiedTime = False, returnreturnPercent = False, returnreturnPercentAdjustment = False, returnreturnPercentAdjustmentComment = False, returnreturnPercentFormatted = False, returnreturnPercentWithAdjustment = False, returnreturnPercentWithAdjustmentFormatted = False, returnreturnPercentWithAdjustmentWithGradeMarkToUse = False, returnreturnPercentWithGradeMark = False, returnreturnPossiblePoints = False, returnreturnSectionID = False, returnreturnStudentGradeBucketID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "delete")

	return(response)

def getEveryStudentGradeBucketSubject(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketSubjectID = True, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1, returnreturnStudentGradeBucketSubjectID = False, returnreturnCalculatedPoints = False, returnreturnCreatedTime = False, returnreturnEarnedPoints = False, returnreturnGradeMarkExists = False, returnreturnGradeMarkID = False, returnreturnGradeMarkIDOverride = False, returnreturnGradeMarkOverrideComment = False, returnreturnGradeMarkToUse = False, returnreturnIsAdminOverride = False, returnreturnIsUsingPointsBasedScale = False, returnreturnModifiedTime = False, returnreturnPercent = False, returnreturnPercentAdjustment = False, returnreturnPercentAdjustmentComment = False, returnreturnPercentFormatted = False, returnreturnPercentWithAdjustment = False, returnreturnPercentWithAdjustmentFormatted = False, returnreturnPercentWithAdjustmentWithGradeMarkToUse = False, returnreturnPercentWithGradeMark = False, returnreturnPossiblePoints = False, returnreturnSectionID = False, returnreturnStudentGradeBucketID = False, returnreturnSubjectID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "delete")

	return(response)

def getEveryStudentGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentGradingScaleGroupID = True, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1, returnreturnStudentGradingScaleGroupID = False, returnreturnAllowTeachersToModify = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGradingScaleGroupID = False, returnreturnHasAttachedStudentSections = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStudentGradingScaleGroupIDClonedFrom = False, returnreturnStudentGradingScaleGroupStudentSectionCount = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "delete")

	return(response)

def getEveryStudentGradingScaleGroupStudentSection(EntityID = 1, page = 1, pageSize = 100, returnStudentGradingScaleGroupStudentSectionID = True, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1, returnreturnStudentGradingScaleGroupStudentSectionID = False, returnreturnCreatedTime = False, returnreturnGradeBuckets = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnStudentGradingScaleGroupID = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "delete")

	return(response)

def getEveryStudentGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGroup(StudentGroupID, EntityID = 1, returnreturnStudentGroupID = False, returnreturnAssignmentCount = False, returnreturnCanBeDeleted = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnIsActive = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnSectionID = False, returnreturnStartDate = False, returnreturnStudentCount = False, returnreturnStudentGroupSyncKey = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroup(StudentGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "delete")

	return(response)

def getEveryStudentGroupAssignment(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1, returnreturnStudentGroupAssignmentID = False, returnreturnAssignmentID = False, returnreturnCreatedTime = False, returnreturnDeleteErrorMessage = False, returnreturnModifiedTime = False, returnreturnStudentGroupID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "delete")

	return(response)

def getEveryStudentGroupStudentSection(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupStudentSectionID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1, returnreturnStudentGroupStudentSectionID = False, returnreturnAssignmentCount = False, returnreturnCanBeDeleted = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnScoredAssignmentCount = False, returnreturnStartDate = False, returnreturnStudentGroupID = False, returnreturnStudentSectionID = False, returnreturnUnableToDeleteMessage = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "delete")

	return(response)

def getEveryStudentGroupTeacherSectionSetting(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupTeacherSectionSettingID = True, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1, returnreturnStudentGroupTeacherSectionSettingID = False, returnreturnColor = False, returnreturnCreatedTime = False, returnreturnDisplay = False, returnreturnModifiedTime = False, returnreturnStudentGroupID = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "delete")

	return(response)

def getEveryStudentQuestion(EntityID = 1, page = 1, pageSize = 100, returnStudentQuestionID = True, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentQuestion(StudentQuestionID, EntityID = 1, returnreturnStudentQuestionID = False, returnreturnAssignmentQuestionID = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnScore = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnStatusStudentDisplay = False, returnreturnStudentAssignmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentQuestion(StudentQuestionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "delete")

	return(response)

def getEveryStudentSectionGradingScaleGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionGradingScaleGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1, returnreturnStudentSectionGradingScaleGradeBucketID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnStudentGradingScaleGroupStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "delete")

	return(response)

def getEveryStudentSectionNote(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionNoteID = True, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentSectionNote(StudentSectionNoteID, EntityID = 1, returnreturnStudentSectionNoteID = False, returnreturnCreatedTime = False, returnreturnCurrentUserCanModify = False, returnreturnLimitToThisSection = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnOtherTeachersHaveAccess = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSectionNote(StudentSectionNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "delete")

	return(response)

def getEverySubjectGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnSubjectGradingScaleGroupID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1, returnreturnSubjectGradingScaleGroupID = False, returnreturnCalculationGroupID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnGradingScaleGroupID = False, returnreturnIsAHistoricRecord = False, returnreturnIsDefaultGroup = False, returnreturnModifiedTime = False, returnreturnSubjectCount = False, returnreturnSubjectGradingScaleGroupIDClonedFrom = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "delete")

	return(response)

def getEverySubjectGradingScaleGroupSubject(EntityID = 1, page = 1, pageSize = 100, returnSubjectGradingScaleGroupSubjectID = True, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1, returnreturnSubjectGradingScaleGroupSubjectID = False, returnreturnCalculationGroupSubjectID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnModifiedTime = False, returnreturnSubjectGradingScaleGroupID = False, returnreturnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "delete")

	return(response)

def getEveryTeacherSectionAcademicStandardGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionAcademicStandardGradeBucketSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1, returnreturnTeacherSectionAcademicStandardGradeBucketSettingID = False, returnreturnAcademicStandardID = False, returnreturnCreatedTime = False, returnreturnDisplay = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnIsExpanded = False, returnreturnModifiedTime = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionCategoryAnalyticsSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionCategoryAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1, returnreturnTeacherSectionCategoryAnalyticsSettingID = False, returnreturnAnalysisType = False, returnreturnAnalysisTypeCode = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionGradeBucketAnalyticsSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionGradeBucketAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1, returnreturnTeacherSectionGradeBucketAnalyticsSettingID = False, returnreturnAnalysisType = False, returnreturnAnalysisTypeCode = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1, returnreturnTeacherSectionGradeBucketSettingID = False, returnreturnCreatedTime = False, returnreturnGradeBucketDisplayType = False, returnreturnGradeBucketDisplayTypeCode = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnIsExpanded = False, returnreturnModifiedTime = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionGradingPeriodSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionGradingPeriodSettingID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1, returnreturnTeacherSectionGradingPeriodSettingID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodID = False, returnreturnIncludeMissingAssignments = False, returnreturnModifiedTime = False, returnreturnShowAssessments = False, returnreturnShowAssignments = False, returnreturnShowGradeBuckets = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionSettingID = True, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1, returnreturnTeacherSectionSettingID = False, returnreturnBrowseViewID = False, returnreturnCalculationGroupGradeBucketIDLocked = False, returnreturnClassGroupID = False, returnreturnCreatedTime = False, returnreturnDisplayAssignmentAttendanceIndicator = False, returnreturnDisplayAssignmentStudentGroupColors = False, returnreturnDisplayAttendance = False, returnreturnDisplayGradebookAverages = False, returnreturnDisplayMissingAssignment = False, returnreturnDisplayStudentGradeLevel = False, returnreturnDisplayStudentGradingPeriodCommentIndicator = False, returnreturnDisplayStudentGroupColors = False, returnreturnDisplayStudentGroups = False, returnreturnDisplayStudentNumber = False, returnreturnDisplayUnscoredPastDueAssignments = False, returnreturnHasCustomClassRosterSort = False, returnreturnHideAssignmentCategoryColors = False, returnreturnHideLockedColumns = False, returnreturnIsAHistoricRecord = False, returnreturnManualDateEntryEndDate = False, returnreturnManualDateEntryStartDate = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnShowGradebookLockedColumnButton = False, returnreturnStudentNameDisplayType = False, returnreturnStudentNameDisplayTypeCode = False, returnreturnStudentsToDisplay = False, returnreturnStudentsToDisplayCode = False, returnreturnUseCustomClassRosterSort = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDOwner = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionStandardsDisplayAcademicStandardSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1, returnreturnTeacherSectionStandardsDisplayAcademicStandardSettingID = False, returnreturnAcademicStandardID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionStandardsDisplayGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionStandardsDisplayGradeBucketSettingID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1, returnreturnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnShowBucket = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionStudentSectionSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionStudentSectionSettingID = True, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1, returnreturnTeacherSectionStudentSectionSettingID = False, returnreturnCreatedTime = False, returnreturnDisplayOrder = False, returnreturnModifiedTime = False, returnreturnStudentSectionID = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "delete")

	return(response)

def getEveryTeacherSectionSubjectGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionSubjectGradeBucketSettingID = True, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1, returnreturnTeacherSectionSubjectGradeBucketSettingID = False, returnreturnAllLinkedAcademicStandardsAreDisplayed = False, returnreturnCreatedTime = False, returnreturnDisplay = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnIsExpanded = False, returnreturnModifiedTime = False, returnreturnSubjectID = False, returnreturnTeacherSectionSettingID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "delete")

	return(response)

def getEveryTempAdjustedCategory(EntityID = 1, page = 1, pageSize = 100, returnTempAdjustedCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1, returnreturnTempAdjustedCategoryID = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnTempSectionCategoryID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "delete")

	return(response)

def getEveryTempAssignmentError(EntityID = 1, page = 1, pageSize = 100, returnTempAssignmentErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAssignmentError(TempAssignmentErrorID, EntityID = 1, returnreturnTempAssignmentErrorID = False, returnreturnCreatedTime = False, returnreturnErrorNumber = False, returnreturnErrorText = False, returnreturnModifiedTime = False, returnreturnTempSectionAssignmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAssignmentError(TempAssignmentErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "delete")

	return(response)

def getEveryTempCalcGroupBucketRemoveStandardOrSubjectResult(EntityID = 1, page = 1, pageSize = 100, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = True, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1, returnreturnTempCalcGroupBucketRemoveStandardOrSubjectResultID = False, returnreturnCreatedTime = False, returnreturnErrorText = False, returnreturnIsError = False, returnreturnModifiedTime = False, returnreturnStandardOrSubjectDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "delete")

	return(response)

def getEveryTempCalculationGroupAcademicStandardWeighting(EntityID = 1, page = 1, pageSize = 100, returnTempCalculationGroupAcademicStandardWeightingID = True, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1, returnreturnTempCalculationGroupAcademicStandardWeightingID = False, returnreturnCalculationGroupAcademicStandardGradeBucketID = False, returnreturnCategoryDescription = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "delete")

	return(response)

def getEveryTempCalculationGroupSubjectWeighting(EntityID = 1, page = 1, pageSize = 100, returnTempCalculationGroupSubjectWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1, returnreturnTempCalculationGroupSubjectWeightingID = False, returnreturnAcademicStandardDescription = False, returnreturnAcademicStandardFullKey = False, returnreturnAcademicStandardID = False, returnreturnCalculationGroupSubjectGradeBucketID = False, returnreturnCategoryDescription = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "delete")

	return(response)

def getEveryTempCalculationGroupWeighting(EntityID = 1, page = 1, pageSize = 100, returnTempCalculationGroupWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1, returnreturnTempCalculationGroupWeightingID = False, returnreturnAcademicStandardDescription = False, returnreturnAcademicStandardFullKey = False, returnreturnAcademicStandardID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCategoryDescription = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnGradeBucketLabel = False, returnreturnGradeBucketOrder = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnSubjectDescription = False, returnreturnSubjectID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "delete")

	return(response)

def getEveryTempCloneGradebookSection(EntityID = 1, page = 1, pageSize = 100, returnTempCloneGradebookSectionID = True, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1, returnreturnTempCloneGradebookSectionID = False, returnreturnCanClone = False, returnreturnCreatedTime = False, returnreturnErrorMessage = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "delete")

	return(response)

def getEveryTempCourseMoveCourse(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMoveCourseID = True, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1, returnreturnTempCourseMoveCourseID = False, returnreturnCodeDescription = False, returnreturnCourseCode = False, returnreturnCourseDescription = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnGroupCourseID = False, returnreturnIsValidUpdate = False, returnreturnModifiedTime = False, returnreturnNewCalculationGroupDescription = False, returnreturnNewCalculationGroupID = False, returnreturnOriginalCalculationGroupDescription = False, returnreturnOriginalCalculationGroupID = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "delete")

	return(response)

def getEveryTempCourseMoveError(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMoveErrorID = True, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1, returnreturnTempCourseMoveErrorID = False, returnreturnBucketLabel = False, returnreturnCreatedTime = False, returnreturnErrorCode = False, returnreturnErrorMessage = False, returnreturnErrorType = False, returnreturnErrorTypeCode = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "delete")

	return(response)

def getEveryTempCourseMoveSectionError(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMoveSectionErrorID = True, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1, returnreturnTempCourseMoveSectionErrorID = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnErrorMessage = False, returnreturnModifiedTime = False, returnreturnSectionCode = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "delete")

	return(response)

def getEveryTempDropLowScoreStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnTempDropLowScoreStudentAssignmentID = True, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1, returnreturnTempDropLowScoreStudentAssignmentID = False, returnreturnAssignmentName = False, returnreturnComments = False, returnreturnCreatedTime = False, returnreturnDropActionType = False, returnreturnDropActionTypeCode = False, returnreturnDropCode = False, returnreturnDropLowScore = False, returnreturnDueDate = False, returnreturnMaxScore = False, returnreturnModifiedTime = False, returnreturnNewGrade = False, returnreturnNoDropReason = False, returnreturnOriginalGrade = False, returnreturnScore = False, returnreturnStudentAssignmentID = False, returnreturnStudentDisplaySortCode = False, returnreturnStudentName = False, returnreturnStudentSectionID = False, returnreturnUndoDropActionType = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeight = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "delete")

	return(response)

def getEveryTempGradebookCloneError(EntityID = 1, page = 1, pageSize = 100, returnTempGradebookCloneErrorID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1, returnreturnTempGradebookCloneErrorID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCreatedTime = False, returnreturnField = False, returnreturnGradeBucketLabel = False, returnreturnMessage = False, returnreturnModifiedTime = False, returnreturnRecordType = False, returnreturnRecordTypeCode = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "delete")

	return(response)

def getEveryTempGradebookGroupError(EntityID = 1, page = 1, pageSize = 100, returnTempGradebookGroupErrorID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1, returnreturnTempGradebookGroupErrorID = False, returnreturnCalculationGroupID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityID = False, returnreturnErrorText = False, returnreturnGradingScaleGroupID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "delete")

	return(response)

def getEveryTempGradeMarkError(EntityID = 1, page = 1, pageSize = 100, returnTempGradeMarkErrorID = True, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1, returnreturnTempGradeMarkErrorID = False, returnreturnCreatedTime = False, returnreturnDisplayOrder = False, returnreturnGradeMarkCode = False, returnreturnGradeMarkID = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "delete")

	return(response)

def getEveryTempGradingPeriodGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1, returnreturnTempGradingPeriodGradeBucketID = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnErrorCount = False, returnreturnGradeBucketLabelWithDates = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnSectionLengthCodeDescription = False, returnreturnStartDate = False, returnreturnStatusDisplayWithExtensionDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "delete")

	return(response)

def getEveryTempGradingPeriodGradeBucketError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodGradeBucketErrorID = True, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1, returnreturnTempGradingPeriodGradeBucketErrorID = False, returnreturnCalculationGroupID = False, returnreturnCalculationType = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnErrorNumber = False, returnreturnErrorText = False, returnreturnGradeBucketLabelWithDates = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnSectionLengthCodeDescription = False, returnreturnStartDate = False, returnreturnStatusDisplayWithExtensionDate = False, returnreturnSubjectOrStandardDescription = False, returnreturnSubjectOrStandardKey = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "delete")

	return(response)

def getEveryTempSectionAssignment(EntityID = 1, page = 1, pageSize = 100, returnTempSectionAssignmentID = True, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempSectionAssignment(TempSectionAssignmentID, EntityID = 1, returnreturnTempSectionAssignmentID = False, returnreturnAnswerRevealDate = False, returnreturnAnswerRevealDateAndTime = False, returnreturnAnswerRevealTime = False, returnreturnAssignedDate = False, returnreturnAssignmentID = False, returnreturnAssignmentName = False, returnreturnAttachmentCount = False, returnreturnCategoryDescription = False, returnreturnCreatedTime = False, returnreturnCurrentPeriod = False, returnreturnDueDate = False, returnreturnEndDate = False, returnreturnEndDateAndTime = False, returnreturnEndTime = False, returnreturnEntityID = False, returnreturnErrorCount = False, returnreturnHideScoreUntilDate = False, returnreturnHideScoreUntilDateAndTime = False, returnreturnHideScoreUntilTime = False, returnreturnIsOnlineAssignment = False, returnreturnMaxScore = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnSectionDetails = False, returnreturnSectionID = False, returnreturnSectionLengthEndDate = False, returnreturnSectionLengthStartDate = False, returnreturnShowCorrectAnswers = False, returnreturnStartDate = False, returnreturnStartDateAndTime = False, returnreturnStartTime = False, returnreturnSync = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeight = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionAssignment(TempSectionAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "delete")

	return(response)

def getEveryTempSectionCategory(EntityID = 1, page = 1, pageSize = 100, returnTempSectionCategoryID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempSectionCategory(TempSectionCategoryID, EntityID = 1, returnreturnTempSectionCategoryID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCalculationGroupID = False, returnreturnCanClone = False, returnreturnCategoryCode = False, returnreturnCategoryID = False, returnreturnCategoryIDIsInvalid = False, returnreturnCreatedTime = False, returnreturnErrorMessages = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionCategory(TempSectionCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "delete")

	return(response)

def getEveryTempSectionGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1, returnreturnTempSectionGradeBucketID = False, returnreturnCalculationGroupGradeBucketID = False, returnreturnCanClone = False, returnreturnChildRecords = False, returnreturnCreatedTime = False, returnreturnCurrentAllowCategoryOverride = False, returnreturnCurrentCalculationType = False, returnreturnCurrentCalculationTypeCode = False, returnreturnEndDate = False, returnreturnErrorMessages = False, returnreturnExclude = False, returnreturnGradeBucketLabel = False, returnreturnGradeBucketTypeID = False, returnreturnHasLeftOverPercentage = False, returnreturnIsCalculationTypeOverridden = False, returnreturnIsSpecificGradeBucket = False, returnreturnModifiedTime = False, returnreturnNewCalculationType = False, returnreturnNewCalculationTypeCode = False, returnreturnOrder = False, returnreturnSectionGradeBucketID = False, returnreturnSectionID = False, returnreturnStartDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "delete")

	return(response)

def getEveryTempSectionGradeBucketWeight(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradeBucketWeightID = True, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1, returnreturnTempSectionGradeBucketWeightID = False, returnreturnAcademicStandardIDToWeight = False, returnreturnCalculationGroupGradeBucketIDComposite = False, returnreturnCalculationGroupGradeBucketIDFeeder = False, returnreturnCanClone = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnSubjectIDToWeight = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercent = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "delete")

	return(response)

def getEveryTempSectionGradingScale(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradingScaleID = True, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1, returnreturnTempSectionGradingScaleID = False, returnreturnCanClone = False, returnreturnChildGradeBuckets = False, returnreturnCreatedTime = False, returnreturnErrorMessage = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "delete")

	return(response)

def getEveryTempSectionGradingScaleGroupToCreate(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradingScaleGroupToCreateID = True, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1, returnreturnTempSectionGradingScaleGroupToCreateID = False, returnreturnCourseCode = False, returnreturnCourseDescriptionCodeSectionCode = False, returnreturnCourseGradingScaleGroupCourseID = False, returnreturnCourseGradingScaleGroupID = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnGradingPeriodGradeBucketsToRetainJson = False, returnreturnInvalidGradeMarks = False, returnreturnIsValidInNewGroup = False, returnreturnModifiedTime = False, returnreturnNewCourseGradingScaleGroupDescription = False, returnreturnNewCourseGradingScaleGroupID = False, returnreturnReason = False, returnreturnRequiresSectionGradingScaleGroups = False, returnreturnSectionCode = False, returnreturnSectionID = False, returnreturnSectionLengthCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "delete")

	return(response)

def getEveryTempStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnTempStudentAssignmentID = True, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentAssignment(TempStudentAssignmentID, EntityID = 1, returnreturnTempStudentAssignmentID = False, returnreturnAssignmentDescription = False, returnreturnAssignmentID = False, returnreturnAssignmentName = False, returnreturnCreatedTime = False, returnreturnDueDate = False, returnreturnDueDateIsInGivenDateRange = False, returnreturnInclude = False, returnreturnIsMissing = False, returnreturnMaxScore = False, returnreturnModifiedTime = False, returnreturnNoCount = False, returnreturnScore = False, returnreturnScoreClarifierCode = False, returnreturnScoreClarifierID = False, returnreturnSectionID = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeight = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentAssignment(TempStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "delete")

	return(response)

def getEveryTempStudentGradingScaleGroupStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGradingScaleGroupStudentSectionID = True, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1, returnreturnTempStudentGradingScaleGroupStudentSectionID = False, returnreturnCourseDescriptionCodeSectionCode = False, returnreturnCreatedTime = False, returnreturnErrorText = False, returnreturnGradingPeriodGradeBuckets = False, returnreturnHasError = False, returnreturnModifiedTime = False, returnreturnSectionID = False, returnreturnSectionLengthCode = False, returnreturnSectionLengthID = False, returnreturnStudentFullNameLFM = False, returnreturnStudentGradingScaleGroupStudentSectionID = False, returnreturnStudentID = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "delete")

	return(response)

def getEveryTempUnDropLowScoreStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempUnDropLowScoreStudentSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1, returnreturnTempUnDropLowScoreStudentSectionID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNewGrade = False, returnreturnOriginalGrade = False, returnreturnStudentDisplaySortCode = False, returnreturnStudentName = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "delete")

	return(response)

def getEveryVendorAssignment(EntityID = 1, page = 1, pageSize = 100, returnVendorAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVendorAssignment(VendorAssignmentID, EntityID = 1, returnreturnVendorAssignmentID = False, returnreturnAssignmentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnOneRosterVendorID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVendorSourceID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteVendorAssignment(VendorAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "delete")

	return(response)

def getEveryVendorCategory(EntityID = 1, page = 1, pageSize = 100, returnVendorCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVendorCategory(VendorCategoryID, EntityID = 1, returnreturnVendorCategoryID = False, returnreturnCategoryID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnOneRosterVendorID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVendorSourceID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteVendorCategory(VendorCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "delete")

	return(response)

def getEveryVendorStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnVendorStudentAssignmentID = True, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1, returnreturnVendorStudentAssignmentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnOneRosterVendorID = False, returnreturnStudentAssignmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVendorSourceID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "delete")

	return(response)