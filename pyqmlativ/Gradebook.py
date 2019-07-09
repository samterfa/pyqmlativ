# This module contains Gradebook functions.

from . import make_request

def getAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "delete")

	return(response)

def getAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "delete")

	return(response)

def getAssessment(AssessmentID, EntityID = 1, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "get", params_list = params_list)

	return(response)

def deleteAssessment(AssessmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "delete")

	return(response)

def getAssignment(AssignmentID, EntityID = 1, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteAssignment(AssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "delete")

	return(response)

def getAssignmentAttachment(AssignmentAttachmentID, EntityID = 1, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "get", params_list = params_list)

	return(response)

def deleteAssignmentAttachment(AssignmentAttachmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "delete")

	return(response)

def getAssignmentQuestion(AssignmentQuestionID, EntityID = 1, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "get", params_list = params_list)

	return(response)

def deleteAssignmentQuestion(AssignmentQuestionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "delete")

	return(response)

def getCalculationGroup(CalculationGroupID, EntityID = 1, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroup(CalculationGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "delete")

	return(response)

def getCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "delete")

	return(response)

def getCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "delete")

	return(response)

def getCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "delete")

	return(response)

def getCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "delete")

	return(response)

def getCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "delete")

	return(response)

def getCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "delete")

	return(response)

def getCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "delete")

	return(response)

def getCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "delete")

	return(response)

def getCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "delete")

	return(response)

def getCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "delete")

	return(response)

def getCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "delete")

	return(response)

def getCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "delete")

	return(response)

def getCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "delete")

	return(response)

def getCategory(CategoryID, EntityID = 1, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteCategory(CategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "delete")

	return(response)

def getCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "delete")

	return(response)

def getClassGroup(ClassGroupID, EntityID = 1, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteClassGroup(ClassGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "delete")

	return(response)

def getClassGroupSection(ClassGroupSectionID, EntityID = 1, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteClassGroupSection(ClassGroupSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "delete")

	return(response)

def getClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "get", params_list = params_list)

	return(response)

def deleteClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "delete")

	return(response)

def getClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "get", params_list = params_list)

	return(response)

def deleteClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "delete")

	return(response)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getConfigEntity(ConfigEntityID, EntityID = 1, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntity(ConfigEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "delete")

	return(response)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "delete")

	return(response)

def getCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "delete")

	return(response)

def getDropLowScoreRun(DropLowScoreRunID, EntityID = 1, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "get", params_list = params_list)

	return(response)

def deleteDropLowScoreRun(DropLowScoreRunID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "delete")

	return(response)

def getDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "delete")

	return(response)

def getGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "delete")

	return(response)

def getGradingScaleGroup(GradingScaleGroupID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteGradingScaleGroup(GradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "delete")

	return(response)

def getGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "delete")

	return(response)

def getMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "get", params_list = params_list)

	return(response)

def deleteMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "delete")

	return(response)

def getMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "get", params_list = params_list)

	return(response)

def deleteMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "delete")

	return(response)

def getQuestion(QuestionID, EntityID = 1, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestion(QuestionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "delete")

	return(response)

def getQuestionAnswer(QuestionAnswerID, EntityID = 1, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedMedia = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestionAnswer(QuestionAnswerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "delete")

	return(response)

def getQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "delete")

	return(response)

def getQuestionMedia(QuestionMediaID, EntityID = 1, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "get", params_list = params_list)

	return(response)

def deleteQuestionMedia(QuestionMediaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "delete")

	return(response)

def getScoreClarifier(ScoreClarifierID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "get", params_list = params_list)

	return(response)

def deleteScoreClarifier(ScoreClarifierID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "delete")

	return(response)

def getSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "delete")

	return(response)

def getSectionCategory(SectionCategoryID, EntityID = 1, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionCategory(SectionCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "delete")

	return(response)

def getSectionGradeBucket(SectionGradeBucketID, EntityID = 1, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradeBucket(SectionGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "delete")

	return(response)

def getSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "delete")

	return(response)

def getSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "delete")

	return(response)

def getSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "delete")

	return(response)

def getSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "delete")

	return(response)

def getSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "delete")

	return(response)

def getStudentAnswer(StudentAnswerID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAnswer(StudentAnswerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "delete")

	return(response)

def getStudentAssignment(StudentAssignmentID, EntityID = 1, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAssignment(StudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "delete")

	return(response)

def getStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "delete")

	return(response)

def getStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "delete")

	return(response)

def getStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "delete")

	return(response)

def getStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "delete")

	return(response)

def getStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "delete")

	return(response)

def getStudentGroup(StudentGroupID, EntityID = 1, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroup(StudentGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "delete")

	return(response)

def getStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "delete")

	return(response)

def getStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "delete")

	return(response)

def getStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "delete")

	return(response)

def getStudentQuestion(StudentQuestionID, EntityID = 1, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentQuestion(StudentQuestionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "delete")

	return(response)

def getStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "delete")

	return(response)

def getStudentSectionNote(StudentSectionNoteID, EntityID = 1, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSectionNote(StudentSectionNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "delete")

	return(response)

def getSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "delete")

	return(response)

def getSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "delete")

	return(response)

def getTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "delete")

	return(response)

def getTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "delete")

	return(response)

def getTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "delete")

	return(response)

def getTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "delete")

	return(response)

def getTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "delete")

	return(response)

def getTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "delete")

	return(response)

def getTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "delete")

	return(response)

def getTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "delete")

	return(response)

def getTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "delete")

	return(response)

def getTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "delete")

	return(response)

def getTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "delete")

	return(response)

def getTempAssignmentError(TempAssignmentErrorID, EntityID = 1, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAssignmentError(TempAssignmentErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "delete")

	return(response)

def getTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "delete")

	return(response)

def getTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "delete")

	return(response)

def getTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "delete")

	return(response)

def getTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "delete")

	return(response)

def getTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "delete")

	return(response)

def getTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "delete")

	return(response)

def getTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "delete")

	return(response)

def getTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "delete")

	return(response)

def getTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "delete")

	return(response)

def getTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "delete")

	return(response)

def getTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "delete")

	return(response)

def getTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "delete")

	return(response)

def getTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "delete")

	return(response)

def getTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "delete")

	return(response)

def getTempSectionAssignment(TempSectionAssignmentID, EntityID = 1, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionAssignment(TempSectionAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "delete")

	return(response)

def getTempSectionCategory(TempSectionCategoryID, EntityID = 1, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionCategory(TempSectionCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "delete")

	return(response)

def getTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "delete")

	return(response)

def getTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "delete")

	return(response)

def getTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "delete")

	return(response)

def getTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "get", params_list = params_list)

	return(response)

def deleteTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "delete")

	return(response)

def getTempStudentAssignment(TempStudentAssignmentID, EntityID = 1, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentAssignment(TempStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "delete")

	return(response)

def getTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "delete")

	return(response)

def getTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "delete")

	return(response)

def getVendorAssignment(VendorAssignmentID, EntityID = 1, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteVendorAssignment(VendorAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "delete")

	return(response)

def getVendorCategory(VendorCategoryID, EntityID = 1, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteVendorCategory(VendorCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "delete")

	return(response)

def getVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "get", params_list = params_list)

	return(response)

def deleteVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "delete")

	return(response)