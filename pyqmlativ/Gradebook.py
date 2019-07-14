# This module contains Gradebook functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryAcademicStandardGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradingScaleGroupID = True, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1, returnAcademicStandardGradingScaleGroupID = True, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1, setAcademicStandardGradingScaleGroupIDClonedFrom = None, setCalculationGroupID = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsDefaultGroup = None, setRelationships = None, returnAcademicStandardGradingScaleGroupID = True, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardGradingScaleGroup(EntityID = 1, setAcademicStandardGradingScaleGroupIDClonedFrom = None, setCalculationGroupID = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsDefaultGroup = None, setRelationships = None, returnAcademicStandardGradingScaleGroupID = True, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardGradingScaleGroupAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradingScaleGroupAcademicStandardID = True, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1, returnAcademicStandardGradingScaleGroupAcademicStandardID = True, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1, setAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = None, setAcademicStandardGradingScaleGroupID = None, setCalculationGroupAcademicStandardID = None, setEntityGroupKey = None, setRelationships = None, returnAcademicStandardGradingScaleGroupAcademicStandardID = True, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardGradingScaleGroupAcademicStandard(EntityID = 1, setAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = None, setAcademicStandardGradingScaleGroupID = None, setCalculationGroupAcademicStandardID = None, setEntityGroupKey = None, setRelationships = None, returnAcademicStandardGradingScaleGroupAcademicStandardID = True, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAssessment(EntityID = 1, page = 1, pageSize = 100, returnAssessmentID = True, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAssessment(AssessmentID, EntityID = 1, returnAssessmentID = True, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "get", return_params_list = return_params_list)

def modifyAssessment(AssessmentID, EntityID = 1, setAssignedDate = None, setCategoryID = None, setDescription = None, setDueDate = None, setIsDeleted = None, setName = None, setSectionID = None, setRelationships = None, returnAssessmentID = True, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAssessment(EntityID = 1, setAssignedDate = None, setCategoryID = None, setDescription = None, setDueDate = None, setIsDeleted = None, setName = None, setSectionID = None, setRelationships = None, returnAssessmentID = True, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAssessment(AssessmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAssignment(EntityID = 1, page = 1, pageSize = 100, returnAssignmentID = True, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAssignment(AssignmentID, EntityID = 1, returnAssignmentID = True, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "get", return_params_list = return_params_list)

def modifyAssignment(AssignmentID, EntityID = 1, setAcademicStandardID = None, setAnswerRevealTime = None, setAssessmentID = None, setAssignedDate = None, setAssignmentIDParent = None, setAssignmentSyncKey = None, setAutoScore = None, setCategoryID = None, setDefaultPointsPerQuestion = None, setDescription = None, setDueDate = None, setEndTime = None, setHideScoreUntilTime = None, setInstructions = None, setIsDeleted = None, setIsOnlineAssignment = None, setIsParent = None, setMaxScore = None, setName = None, setRandomizeQuestions = None, setScoreDisplayType = None, setScoreDisplayTypeCode = None, setSectionID = None, setSendNotificationWhenAnswersRevealed = None, setSendNotificationWhenAssignmentReadyToTake = None, setShowCorrectAnswers = None, setStartTime = None, setSubjectID = None, setUseGradeMarkScoring = None, setWeight = None, setRelationships = None, returnAssignmentID = True, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAssignment(EntityID = 1, setAcademicStandardID = None, setAnswerRevealTime = None, setAssessmentID = None, setAssignedDate = None, setAssignmentIDParent = None, setAssignmentSyncKey = None, setAutoScore = None, setCategoryID = None, setDefaultPointsPerQuestion = None, setDescription = None, setDueDate = None, setEndTime = None, setHideScoreUntilTime = None, setInstructions = None, setIsDeleted = None, setIsOnlineAssignment = None, setIsParent = None, setMaxScore = None, setName = None, setRandomizeQuestions = None, setScoreDisplayType = None, setScoreDisplayTypeCode = None, setSectionID = None, setSendNotificationWhenAnswersRevealed = None, setSendNotificationWhenAssignmentReadyToTake = None, setShowCorrectAnswers = None, setStartTime = None, setSubjectID = None, setUseGradeMarkScoring = None, setWeight = None, setRelationships = None, returnAssignmentID = True, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAssignment(AssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAssignmentAttachment(EntityID = 1, page = 1, pageSize = 100, returnAssignmentAttachmentID = True, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAssignmentAttachment(AssignmentAttachmentID, EntityID = 1, returnAssignmentAttachmentID = True, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "get", return_params_list = return_params_list)

def modifyAssignmentAttachment(AssignmentAttachmentID, EntityID = 1, setAssignmentID = None, setAttachmentID = None, setDisplayInStudentFamilyAccess = None, setRelationships = None, returnAssignmentAttachmentID = True, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAssignmentAttachment(EntityID = 1, setAssignmentID = None, setAttachmentID = None, setDisplayInStudentFamilyAccess = None, setRelationships = None, returnAssignmentAttachmentID = True, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAssignmentAttachment(AssignmentAttachmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAssignmentQuestion(EntityID = 1, page = 1, pageSize = 100, returnAssignmentQuestionID = True, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAssignmentQuestion(AssignmentQuestionID, EntityID = 1, returnAssignmentQuestionID = True, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "get", return_params_list = return_params_list)

def modifyAssignmentQuestion(AssignmentQuestionID, EntityID = 1, setAllowPartialCredit = None, setAssignmentID = None, setDisplayOrder = None, setPointsAllowed = None, setQuestionID = None, setRelationships = None, returnAssignmentQuestionID = True, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAssignmentQuestion(EntityID = 1, setAllowPartialCredit = None, setAssignmentID = None, setDisplayOrder = None, setPointsAllowed = None, setQuestionID = None, setRelationships = None, returnAssignmentQuestionID = True, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAssignmentQuestion(AssignmentQuestionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroup(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupID = True, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroup(CalculationGroupID, EntityID = 1, returnCalculationGroupID = True, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroup(CalculationGroupID, EntityID = 1, setAllowAcademicStandardWeightingTeacherOverride = None, setAllowAssignmentPointsTeacherOverride = None, setAllowCategoryOverride = None, setAllowCategoryWeightingTeacherOverride = None, setAllowDecayingAverageTeacherOverride = None, setAllowGradeBucketWeightingTeacherOverride = None, setAllowNotGradedTeacherOverride = None, setAllowSubjectiveTeacherOverride = None, setAllowSubjectWeightingTeacherOverride = None, setAllowTotalPointsAndGradeBucketWeightingTeacherOverride = None, setCalculationGroupIDClonedFrom = None, setDecayingAveragePercent = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setIsDefaultGroup = None, setLimitTeacherOverridesToCategoriesInGroup = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setRelationships = None, returnCalculationGroupID = True, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroup(EntityID = 1, setAllowAcademicStandardWeightingTeacherOverride = None, setAllowAssignmentPointsTeacherOverride = None, setAllowCategoryOverride = None, setAllowCategoryWeightingTeacherOverride = None, setAllowDecayingAverageTeacherOverride = None, setAllowGradeBucketWeightingTeacherOverride = None, setAllowNotGradedTeacherOverride = None, setAllowSubjectiveTeacherOverride = None, setAllowSubjectWeightingTeacherOverride = None, setAllowTotalPointsAndGradeBucketWeightingTeacherOverride = None, setCalculationGroupIDClonedFrom = None, setDecayingAveragePercent = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setIsDefaultGroup = None, setLimitTeacherOverridesToCategoriesInGroup = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setRelationships = None, returnCalculationGroupID = True, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroup(CalculationGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardID = True, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1, returnCalculationGroupAcademicStandardID = True, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1, setAcademicStandardID = None, setCalculateForSingleBucket = None, setCalculationGroupAcademicStandardIDClonedFrom = None, setCalculationGroupAcademicStandardIDParent = None, setCalculationGroupID = None, setDisplayOnReportCard = None, setEntityGroupKey = None, setLevel = None, setOrder = None, setRelationships = None, returnCalculationGroupAcademicStandardID = True, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupAcademicStandard(EntityID = 1, setAcademicStandardID = None, setCalculateForSingleBucket = None, setCalculationGroupAcademicStandardIDClonedFrom = None, setCalculationGroupAcademicStandardIDParent = None, setCalculationGroupID = None, setDisplayOnReportCard = None, setEntityGroupKey = None, setLevel = None, setOrder = None, setRelationships = None, returnCalculationGroupAcademicStandardID = True, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = True, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = True, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1, setCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupAcademicStandardIDAtLevel = None, setCalculationGroupHierarchyDepthID = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = True, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(EntityID = 1, setCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupAcademicStandardIDAtLevel = None, setCalculationGroupHierarchyDepthID = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = True, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupAcademicStandardGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardGradeBucketID = True, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1, returnCalculationGroupAcademicStandardGradeBucketID = True, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1, setCalculationGroupAcademicStandardGradeBucketIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCalculationType = None, setCalculationTypeCode = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupAcademicStandardGradeBucketID = True, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupAcademicStandardGradeBucket(EntityID = 1, setCalculationGroupAcademicStandardGradeBucketIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCalculationType = None, setCalculationTypeCode = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupAcademicStandardGradeBucketID = True, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupAcademicStandardWeighting(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupAcademicStandardWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1, returnCalculationGroupAcademicStandardWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupAcademicStandardGradeBucketID = None, setCalculationGroupAcademicStandardWeightingIDClonedFrom = None, setCategoryIDToWeight = None, setEntityGroupKey = None, setWeightPercent = None, setRelationships = None, returnCalculationGroupAcademicStandardWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupAcademicStandardWeighting(EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupAcademicStandardGradeBucketID = None, setCalculationGroupAcademicStandardWeightingIDClonedFrom = None, setCategoryIDToWeight = None, setEntityGroupKey = None, setWeightPercent = None, setRelationships = None, returnCalculationGroupAcademicStandardWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupCategory(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupCategoryID = True, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1, returnCalculationGroupCategoryID = True, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1, setCalculationGroupCategoryIDClonedFrom = None, setCalculationGroupID = None, setCategoryID = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupCategoryID = True, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupCategory(EntityID = 1, setCalculationGroupCategoryIDClonedFrom = None, setCalculationGroupID = None, setCategoryID = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupCategoryID = True, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupCourse(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupCourseID = True, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1, returnCalculationGroupCourseID = True, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1, setCalculationGroupCourseIDClonedFrom = None, setCalculationGroupID = None, setCourseID = None, setRelationships = None, returnCalculationGroupCourseID = True, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupCourse(EntityID = 1, setCalculationGroupCourseIDClonedFrom = None, setCalculationGroupID = None, setCourseID = None, setRelationships = None, returnCalculationGroupCourseID = True, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupGradeBucketID = True, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1, returnCalculationGroupGradeBucketID = True, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1, setAllowCalculationTypeOverride = None, setAllowWeightOverride = None, setCalculationGroupGradeBucketIDClonedFrom = None, setCalculationGroupID = None, setCalculationType = None, setCalculationTypeCode = None, setEntityGroupKey = None, setGetCopySectionLengthXMLFilter = None, setGradeMarkScoringType = None, setGradeMarkScoringTypeCode = None, setGradingPeriodGradeBucketID = None, setRoundBucketPercent = None, setRelationships = None, returnCalculationGroupGradeBucketID = True, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupGradeBucket(EntityID = 1, setAllowCalculationTypeOverride = None, setAllowWeightOverride = None, setCalculationGroupGradeBucketIDClonedFrom = None, setCalculationGroupID = None, setCalculationType = None, setCalculationTypeCode = None, setEntityGroupKey = None, setGetCopySectionLengthXMLFilter = None, setGradeMarkScoringType = None, setGradeMarkScoringTypeCode = None, setGradingPeriodGradeBucketID = None, setRoundBucketPercent = None, setRelationships = None, returnCalculationGroupGradeBucketID = True, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupHierarchyDepthID = True, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1, returnCalculationGroupHierarchyDepthID = True, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1, setCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupID = None, setCode = None, setDepthLevel = None, setDescription = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupHierarchyDepthID = True, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupHierarchyDepth(EntityID = 1, setCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupID = None, setCode = None, setDepthLevel = None, setDescription = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupHierarchyDepthID = True, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupSubject(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectID = True, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1, returnCalculationGroupSubjectID = True, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1, setCalculationGroupID = None, setCalculationGroupSubjectIDClonedFrom = None, setEntityGroupKey = None, setOrder = None, setSubjectID = None, setRelationships = None, returnCalculationGroupSubjectID = True, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupSubject(EntityID = 1, setCalculationGroupID = None, setCalculationGroupSubjectIDClonedFrom = None, setEntityGroupKey = None, setOrder = None, setSubjectID = None, setRelationships = None, returnCalculationGroupSubjectID = True, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupSubjectAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectAcademicStandardID = True, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1, returnCalculationGroupSubjectAcademicStandardID = True, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1, setAcademicStandardID = None, setCalculationGroupID = None, setCalculationGroupSubjectAcademicStandardIDClonedFrom = None, setEntityGroupKey = None, setSubjectID = None, setRelationships = None, returnCalculationGroupSubjectAcademicStandardID = True, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupSubjectAcademicStandard(EntityID = 1, setAcademicStandardID = None, setCalculationGroupID = None, setCalculationGroupSubjectAcademicStandardIDClonedFrom = None, setEntityGroupKey = None, setSubjectID = None, setRelationships = None, returnCalculationGroupSubjectAcademicStandardID = True, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupSubjectGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1, returnCalculationGroupSubjectGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1, setCalculationGroupGradeBucketID = None, setCalculationGroupSubjectGradeBucketIDClonedFrom = None, setCalculationGroupSubjectID = None, setCalculationType = None, setCalculationTypeCode = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupSubjectGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupSubjectGradeBucket(EntityID = 1, setCalculationGroupGradeBucketID = None, setCalculationGroupSubjectGradeBucketIDClonedFrom = None, setCalculationGroupSubjectID = None, setCalculationType = None, setCalculationTypeCode = None, setEntityGroupKey = None, setRelationships = None, returnCalculationGroupSubjectGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupSubjectWeighting(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupSubjectWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1, returnCalculationGroupSubjectWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupSubjectGradeBucketID = None, setCalculationGroupSubjectWeightingIDClonedFrom = None, setCategoryIDToWeight = None, setEntityGroupKey = None, setWeightPercent = None, setRelationships = None, returnCalculationGroupSubjectWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupSubjectWeighting(EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupSubjectGradeBucketID = None, setCalculationGroupSubjectWeightingIDClonedFrom = None, setCategoryIDToWeight = None, setEntityGroupKey = None, setWeightPercent = None, setRelationships = None, returnCalculationGroupSubjectWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCalculationGroupWeighting(EntityID = 1, page = 1, pageSize = 100, returnCalculationGroupWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1, returnCalculationGroupWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "get", return_params_list = return_params_list)

def modifyCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupGradeBucketID = None, setCalculationGroupWeightingIDClonedFrom = None, setCategoryIDToWeight = None, setEntityGroupKey = None, setGradingPeriodGradeBucketIDToWeight = None, setRequiredGrade = None, setRoundBucketPercent = None, setSubjectIDToWeight = None, setWeightPercent = None, setRelationships = None, returnCalculationGroupWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCalculationGroupWeighting(EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupGradeBucketID = None, setCalculationGroupWeightingIDClonedFrom = None, setCategoryIDToWeight = None, setEntityGroupKey = None, setGradingPeriodGradeBucketIDToWeight = None, setRequiredGrade = None, setRoundBucketPercent = None, setSubjectIDToWeight = None, setWeightPercent = None, setRelationships = None, returnCalculationGroupWeightingID = True, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCategory(EntityID = 1, page = 1, pageSize = 100, returnCategoryID = True, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCategory(CategoryID, EntityID = 1, returnCategoryID = True, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "get", return_params_list = return_params_list)

def modifyCategory(CategoryID, EntityID = 1, setBackgroundColor = None, setCategoryIDClonedFrom = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setSchoolYearID = None, setTextColor = None, setUseForSpecificGradeBucketType = None, setRelationships = None, returnCategoryID = True, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCategory(EntityID = 1, setBackgroundColor = None, setCategoryIDClonedFrom = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setSchoolYearID = None, setTextColor = None, setUseForSpecificGradeBucketType = None, setRelationships = None, returnCategoryID = True, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCategory(CategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCategoryGradeBucketType(EntityID = 1, page = 1, pageSize = 100, returnCategoryGradeBucketTypeID = True, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1, returnCategoryGradeBucketTypeID = True, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "get", return_params_list = return_params_list)

def modifyCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1, setCategoryGradeBucketTypeIDClonedFrom = None, setCategoryID = None, setEntityGroupKey = None, setGradeBucketTypeID = None, setRelationships = None, returnCategoryGradeBucketTypeID = True, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCategoryGradeBucketType(EntityID = 1, setCategoryGradeBucketTypeIDClonedFrom = None, setCategoryID = None, setEntityGroupKey = None, setGradeBucketTypeID = None, setRelationships = None, returnCategoryGradeBucketTypeID = True, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryClassGroup(EntityID = 1, page = 1, pageSize = 100, returnClassGroupID = True, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getClassGroup(ClassGroupID, EntityID = 1, returnClassGroupID = True, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "get", return_params_list = return_params_list)

def modifyClassGroup(ClassGroupID, EntityID = 1, setEntityID = None, setName = None, setSchoolYearID = None, setStaffID = None, setRelationships = None, returnClassGroupID = True, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createClassGroup(EntityID = 1, setEntityID = None, setName = None, setSchoolYearID = None, setStaffID = None, setRelationships = None, returnClassGroupID = True, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteClassGroup(ClassGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryClassGroupSection(EntityID = 1, page = 1, pageSize = 100, returnClassGroupSectionID = True, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getClassGroupSection(ClassGroupSectionID, EntityID = 1, returnClassGroupSectionID = True, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "get", return_params_list = return_params_list)

def modifyClassGroupSection(ClassGroupSectionID, EntityID = 1, setClassGroupID = None, setSectionID = None, setRelationships = None, returnClassGroupSectionID = True, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createClassGroupSection(EntityID = 1, setClassGroupID = None, setSectionID = None, setRelationships = None, returnClassGroupSectionID = True, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteClassGroupSection(ClassGroupSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryClosedGradingPeriodGradeChange(EntityID = 1, page = 1, pageSize = 100, returnClosedGradingPeriodGradeChangeID = True, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1, returnClosedGradingPeriodGradeChangeID = True, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "get", return_params_list = return_params_list)

def modifyClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1, setCalculatedCompletedTime = None, setCompletedTime = None, setDisplayMassReviewDenyButton = None, setGradingPeriodID = None, setReason = None, setSectionID = None, setRelationships = None, returnClosedGradingPeriodGradeChangeID = True, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createClosedGradingPeriodGradeChange(EntityID = 1, setCalculatedCompletedTime = None, setCompletedTime = None, setDisplayMassReviewDenyButton = None, setGradingPeriodID = None, setReason = None, setSectionID = None, setRelationships = None, returnClosedGradingPeriodGradeChangeID = True, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryClosedGradingPeriodStudentGradeBucketChange(EntityID = 1, page = 1, pageSize = 100, returnClosedGradingPeriodStudentGradeBucketChangeID = True, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1, returnClosedGradingPeriodStudentGradeBucketChangeID = True, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "get", return_params_list = return_params_list)

def modifyClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1, setClosedGradingPeriodGradeChangeID = None, setClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeStatusCode = None, setGradeMarkIDNew = None, setGradeMarkIDOriginal = None, setHasSnapshot = None, setNewPercent = None, setOriginalPercent = None, setStaffMeetID = None, setStudentGradeBucketID = None, setRelationships = None, returnClosedGradingPeriodStudentGradeBucketChangeID = True, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createClosedGradingPeriodStudentGradeBucketChange(EntityID = 1, setClosedGradingPeriodGradeChangeID = None, setClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeStatusCode = None, setGradeMarkIDNew = None, setGradeMarkIDOriginal = None, setHasSnapshot = None, setNewPercent = None, setOriginalPercent = None, setStaffMeetID = None, setStudentGradeBucketID = None, setRelationships = None, returnClosedGradingPeriodStudentGradeBucketChangeID = True, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setDistrictID = None, setRelationships = None, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrict(EntityID = 1, setDistrictID = None, setRelationships = None, returnConfigDistrictID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setSchoolYearID = None, setUseCurriculumSubjectsInGradebook = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setSchoolYearID = None, setUseCurriculumSubjectsInGradebook = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntity(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntity(ConfigEntityID, EntityID = 1, returnConfigEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntity(ConfigEntityID, EntityID = 1, setEntityID = None, setRunInMonitorByScheduledTask = None, setRelationships = None, returnConfigEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntity(EntityID = 1, setEntityID = None, setRunInMonitorByScheduledTask = None, setRelationships = None, returnConfigEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntity(ConfigEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = True, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = None, setAllowGracePeriodAtEndOfGradingPeriod = None, setAllowMultipleAssignmentAttempts = None, setAllowNegativePercentAdjustment = None, setAllowOnlineAssignments = None, setAllowPercentAdjustment = None, setAllowRetainedFutureScoring = None, setAllowStudentGroups = None, setAllowTeacherComments = None, setAllowTeachersToAddStudentNotes = None, setAllowTeachersToOverrideDefaultMaxScore = None, setAllowTeachersToOverrideDefaultMaxWeight = None, setAllowTeachersToTransferGrades = None, setAssignmentMaxScore = None, setAssignmentMaxWeight = None, setAutoApproveGradeChangeRequest = None, setCapCalculationAt100Percent = None, setCapWeightedCategoryCalculationAt100Percent = None, setClosedGradingPeriodGradeChangeCutOff = None, setClosedGradingPeriodGradeChangePermissionType = None, setClosedGradingPeriodGradeChangePermissionTypeCode = None, setConfigEntityGroupYearIDClonedFrom = None, setDisplayNonGradedClassesForTeachers = None, setEntityGroupKey = None, setEntityID = None, setFailingGradeThresholdPercent = None, setGradingPeriodEditExtensionDays = None, setGradingPeriodEditExtensionEndTime = None, setNumberOfDaysUntilNewStudentIconAppears = None, setNumberOfDaysUntilUnscoredAssignmentsAreMissing = None, setOnlyShowGradebooksWithActiveStudentSectionTransactions = None, setSchoolYearID = None, setScoreClarifierIDFailing = None, setUseFailingGradeScoreClarifier = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = None, setAllowGracePeriodAtEndOfGradingPeriod = None, setAllowMultipleAssignmentAttempts = None, setAllowNegativePercentAdjustment = None, setAllowOnlineAssignments = None, setAllowPercentAdjustment = None, setAllowRetainedFutureScoring = None, setAllowStudentGroups = None, setAllowTeacherComments = None, setAllowTeachersToAddStudentNotes = None, setAllowTeachersToOverrideDefaultMaxScore = None, setAllowTeachersToOverrideDefaultMaxWeight = None, setAllowTeachersToTransferGrades = None, setAssignmentMaxScore = None, setAssignmentMaxWeight = None, setAutoApproveGradeChangeRequest = None, setCapCalculationAt100Percent = None, setCapWeightedCategoryCalculationAt100Percent = None, setClosedGradingPeriodGradeChangeCutOff = None, setClosedGradingPeriodGradeChangePermissionType = None, setClosedGradingPeriodGradeChangePermissionTypeCode = None, setConfigEntityGroupYearIDClonedFrom = None, setDisplayNonGradedClassesForTeachers = None, setEntityGroupKey = None, setEntityID = None, setFailingGradeThresholdPercent = None, setGradingPeriodEditExtensionDays = None, setGradingPeriodEditExtensionEndTime = None, setNumberOfDaysUntilNewStudentIconAppears = None, setNumberOfDaysUntilUnscoredAssignmentsAreMissing = None, setOnlyShowGradebooksWithActiveStudentSectionTransactions = None, setSchoolYearID = None, setScoreClarifierIDFailing = None, setUseFailingGradeScoreClarifier = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnCourseGradingScaleGroupID = True, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1, returnCourseGradingScaleGroupID = True, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "get", return_params_list = return_params_list)

def modifyCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1, setAllowSectionOverride = None, setCourseGradingScaleGroupIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setGradingScaleGroupID = None, setIsDefaultGroup = None, setLimitTeacherOverridesToGradeMarksInGroup = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setRelationships = None, returnCourseGradingScaleGroupID = True, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseGradingScaleGroup(EntityID = 1, setAllowSectionOverride = None, setCourseGradingScaleGroupIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setGradingScaleGroupID = None, setIsDefaultGroup = None, setLimitTeacherOverridesToGradeMarksInGroup = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setRelationships = None, returnCourseGradingScaleGroupID = True, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseGradingScaleGroupCourse(EntityID = 1, page = 1, pageSize = 100, returnCourseGradingScaleGroupCourseID = True, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1, returnCourseGradingScaleGroupCourseID = True, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "get", return_params_list = return_params_list)

def modifyCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1, setCourseGradingScaleGroupID = None, setCourseID = None, setRelationships = None, returnCourseGradingScaleGroupCourseID = True, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseGradingScaleGroupCourse(EntityID = 1, setCourseGradingScaleGroupID = None, setCourseID = None, setRelationships = None, returnCourseGradingScaleGroupCourseID = True, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDropLowScoreRun(EntityID = 1, page = 1, pageSize = 100, returnDropLowScoreRunID = True, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDropLowScoreRun(DropLowScoreRunID, EntityID = 1, returnDropLowScoreRunID = True, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "get", return_params_list = return_params_list)

def modifyDropLowScoreRun(DropLowScoreRunID, EntityID = 1, setCalculationGroupGradeBucketID = None, setIsEffective = None, setRunTime = None, setSectionID = None, setRelationships = None, returnDropLowScoreRunID = True, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDropLowScoreRun(EntityID = 1, setCalculationGroupGradeBucketID = None, setIsEffective = None, setRunTime = None, setSectionID = None, setRelationships = None, returnDropLowScoreRunID = True, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDropLowScoreRun(DropLowScoreRunID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDropLowScoreRunStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnDropLowScoreRunStudentAssignmentID = True, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1, returnDropLowScoreRunStudentAssignmentID = True, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1, setDropActionType = None, setDropActionTypeCode = None, setDropLowScoreRunID = None, setStudentAssignmentID = None, setRelationships = None, returnDropLowScoreRunStudentAssignmentID = True, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDropLowScoreRunStudentAssignment(EntityID = 1, setDropActionType = None, setDropActionTypeCode = None, setDropLowScoreRunID = None, setStudentAssignmentID = None, setRelationships = None, returnDropLowScoreRunStudentAssignmentID = True, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradesheetAssignmentSetting(EntityID = 1, page = 1, pageSize = 100, returnGradesheetAssignmentSettingID = True, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1, returnGradesheetAssignmentSettingID = True, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "get", return_params_list = return_params_list)

def modifyGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1, setDefaultAttemptType = None, setDefaultAttemptTypeCode = None, setIsDateAscending = None, setMaxScoreDefault = None, setSortBy = None, setSortByCode = None, setTeacherSectionSettingID = None, setRelationships = None, returnGradesheetAssignmentSettingID = True, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradesheetAssignmentSetting(EntityID = 1, setDefaultAttemptType = None, setDefaultAttemptTypeCode = None, setIsDateAscending = None, setMaxScoreDefault = None, setSortBy = None, setSortByCode = None, setTeacherSectionSettingID = None, setRelationships = None, returnGradesheetAssignmentSettingID = True, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnGradingScaleGroupID = True, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradingScaleGroup(GradingScaleGroupID, EntityID = 1, returnGradingScaleGroupID = True, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "get", return_params_list = return_params_list)

def modifyGradingScaleGroup(GradingScaleGroupID, EntityID = 1, setDescription = None, setDisplayGradeMarkPercentages = None, setEntityGroupKey = None, setEntityID = None, setGradeMarkIDMastered = None, setGradingScaleGroupIDClonedFrom = None, setGradingScaleType = None, setGradingScaleTypeCode = None, setIsDefaultAcademicStandardGradingScaleGroup = None, setIsDefaultSubjectGradingScaleGroup = None, setIsPointsBasedScale = None, setMaxScore = None, setSchoolYearID = None, setSectionIDTeacherOverride = None, setUseAsMastery = None, setRelationships = None, returnGradingScaleGroupID = True, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradingScaleGroup(EntityID = 1, setDescription = None, setDisplayGradeMarkPercentages = None, setEntityGroupKey = None, setEntityID = None, setGradeMarkIDMastered = None, setGradingScaleGroupIDClonedFrom = None, setGradingScaleType = None, setGradingScaleTypeCode = None, setIsDefaultAcademicStandardGradingScaleGroup = None, setIsDefaultSubjectGradingScaleGroup = None, setIsPointsBasedScale = None, setMaxScore = None, setSchoolYearID = None, setSectionIDTeacherOverride = None, setUseAsMastery = None, setRelationships = None, returnGradingScaleGroupID = True, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradingScaleGroup(GradingScaleGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradingScaleGroupGradeMark(EntityID = 1, page = 1, pageSize = 100, returnGradingScaleGroupGradeMarkID = True, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1, returnGradingScaleGroupGradeMarkID = True, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "get", return_params_list = return_params_list)

def modifyGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1, setAllowSubjective = None, setColor = None, setDefaultCalculationPercent = None, setDefaultCalculationPoints = None, setEntityGroupKey = None, setGradeMarkID = None, setGradingScaleGroupGradeMarkIDClonedFrom = None, setGradingScaleGroupID = None, setPercentHigh = None, setPercentLow = None, setPointsHigh = None, setPointsLow = None, setRelationships = None, returnGradingScaleGroupGradeMarkID = True, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradingScaleGroupGradeMark(EntityID = 1, setAllowSubjective = None, setColor = None, setDefaultCalculationPercent = None, setDefaultCalculationPoints = None, setEntityGroupKey = None, setGradeMarkID = None, setGradingScaleGroupGradeMarkIDClonedFrom = None, setGradingScaleGroupID = None, setPercentHigh = None, setPercentLow = None, setPointsHigh = None, setPointsLow = None, setRelationships = None, returnGradingScaleGroupGradeMarkID = True, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMonitorSummaryByClass(EntityID = 1, page = 1, pageSize = 100, returnMonitorSummaryByClassID = True, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1, returnMonitorSummaryByClassID = True, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "get", return_params_list = return_params_list)

def modifyMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1, setRelationships = None, returnMonitorSummaryByClassID = True, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMonitorSummaryByClass(EntityID = 1, setRelationships = None, returnMonitorSummaryByClassID = True, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMonitorSummaryByTeacher(EntityID = 1, page = 1, pageSize = 100, returnMonitorSummaryByTeacherID = True, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1, returnMonitorSummaryByTeacherID = True, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "get", return_params_list = return_params_list)

def modifyMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1, setRelationships = None, returnMonitorSummaryByTeacherID = True, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMonitorSummaryByTeacher(EntityID = 1, setRelationships = None, returnMonitorSummaryByTeacherID = True, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQuestion(EntityID = 1, page = 1, pageSize = 100, returnQuestionID = True, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQuestion(QuestionID, EntityID = 1, returnQuestionID = True, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "get", return_params_list = return_params_list)

def modifyQuestion(QuestionID, EntityID = 1, setAllowStudentAttachments = None, setDescription = None, setInstructions = None, setStaffID = None, setType = None, setTypeCode = None, setRelationships = None, returnQuestionID = True, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQuestion(EntityID = 1, setAllowStudentAttachments = None, setDescription = None, setInstructions = None, setStaffID = None, setType = None, setTypeCode = None, setRelationships = None, returnQuestionID = True, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQuestion(QuestionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQuestionAnswer(EntityID = 1, page = 1, pageSize = 100, returnQuestionAnswerID = True, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedMedia = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQuestionAnswer(QuestionAnswerID, EntityID = 1, returnQuestionAnswerID = True, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedMedia = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "get", return_params_list = return_params_list)

def modifyQuestionAnswer(QuestionAnswerID, EntityID = 1, setChoice = None, setChoiceOrder = None, setIsCorrect = None, setQuestionID = None, setValue = None, setValueOrder = None, setRelationships = None, returnQuestionAnswerID = True, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedMedia = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQuestionAnswer(EntityID = 1, setChoice = None, setChoiceOrder = None, setIsCorrect = None, setQuestionID = None, setValue = None, setValueOrder = None, setRelationships = None, returnQuestionAnswerID = True, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedMedia = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQuestionAnswer(QuestionAnswerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQuestionAnswerMedia(EntityID = 1, page = 1, pageSize = 100, returnQuestionAnswerMediaID = True, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1, returnQuestionAnswerMediaID = True, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "get", return_params_list = return_params_list)

def modifyQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1, setDisplayFor = None, setDisplayForCode = None, setMediaID = None, setQuestionAnswerID = None, setRelationships = None, returnQuestionAnswerMediaID = True, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQuestionAnswerMedia(EntityID = 1, setDisplayFor = None, setDisplayForCode = None, setMediaID = None, setQuestionAnswerID = None, setRelationships = None, returnQuestionAnswerMediaID = True, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQuestionMedia(EntityID = 1, page = 1, pageSize = 100, returnQuestionMediaID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQuestionMedia(QuestionMediaID, EntityID = 1, returnQuestionMediaID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "get", return_params_list = return_params_list)

def modifyQuestionMedia(QuestionMediaID, EntityID = 1, setMediaID = None, setQuestionID = None, setRelationships = None, returnQuestionMediaID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQuestionMedia(EntityID = 1, setMediaID = None, setQuestionID = None, setRelationships = None, returnQuestionMediaID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQuestionMedia(QuestionMediaID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryScoreClarifier(EntityID = 1, page = 1, pageSize = 100, returnScoreClarifierID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getScoreClarifier(ScoreClarifierID, EntityID = 1, returnScoreClarifierID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "get", return_params_list = return_params_list)

def modifyScoreClarifier(ScoreClarifierID, EntityID = 1, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIsMissing = None, setNoCount = None, setSchoolYearID = None, setScoreClarifierIDClonedFrom = None, setRelationships = None, returnScoreClarifierID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createScoreClarifier(EntityID = 1, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIsMissing = None, setNoCount = None, setSchoolYearID = None, setScoreClarifierIDClonedFrom = None, setRelationships = None, returnScoreClarifierID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteScoreClarifier(ScoreClarifierID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionAcademicStandardWeight(EntityID = 1, page = 1, pageSize = 100, returnSectionAcademicStandardWeightID = True, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1, returnSectionAcademicStandardWeightID = True, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "get", return_params_list = return_params_list)

def modifySectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1, setAcademicStandardID = None, setSectionGradeBucketID = None, setWeightPercent = None, setRelationships = None, returnSectionAcademicStandardWeightID = True, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionAcademicStandardWeight(EntityID = 1, setAcademicStandardID = None, setSectionGradeBucketID = None, setWeightPercent = None, setRelationships = None, returnSectionAcademicStandardWeightID = True, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionCategory(EntityID = 1, page = 1, pageSize = 100, returnSectionCategoryID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionCategory(SectionCategoryID, EntityID = 1, returnSectionCategoryID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "get", return_params_list = return_params_list)

def modifySectionCategory(SectionCategoryID, EntityID = 1, setCategoryID = None, setSectionGradeBucketID = None, setWeightPercent = None, setRelationships = None, returnSectionCategoryID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionCategory(EntityID = 1, setCategoryID = None, setSectionGradeBucketID = None, setWeightPercent = None, setRelationships = None, returnSectionCategoryID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionCategory(SectionCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionGradeBucket(SectionGradeBucketID, EntityID = 1, returnSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifySectionGradeBucket(SectionGradeBucketID, EntityID = 1, setCalculationGroupGradeBucketID = None, setCalculationType = None, setCalculationTypeCode = None, setIsCalculationTypeOverridden = None, setSectionID = None, setRelationships = None, returnSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionGradeBucket(EntityID = 1, setCalculationGroupGradeBucketID = None, setCalculationType = None, setCalculationTypeCode = None, setIsCalculationTypeOverridden = None, setSectionID = None, setRelationships = None, returnSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionGradeBucket(SectionGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1, returnSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "get", return_params_list = return_params_list)

def modifySectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1, setGradingPeriodGradeBucketID = None, setMaxExtraCredit = None, setSectionID = None, setUseMaxExtraCredit = None, setRelationships = None, returnSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionGradeBucketSetting(EntityID = 1, setGradingPeriodGradeBucketID = None, setMaxExtraCredit = None, setSectionID = None, setUseMaxExtraCredit = None, setRelationships = None, returnSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionGradeBucketWeight(EntityID = 1, page = 1, pageSize = 100, returnSectionGradeBucketWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1, returnSectionGradeBucketWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "get", return_params_list = return_params_list)

def modifySectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1, setSectionGradeBucketIDComposite = None, setSectionGradeBucketIDFeeder = None, setWeightPercent = None, setRelationships = None, returnSectionGradeBucketWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionGradeBucketWeight(EntityID = 1, setSectionGradeBucketIDComposite = None, setSectionGradeBucketIDFeeder = None, setWeightPercent = None, setRelationships = None, returnSectionGradeBucketWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionGradingPeriodData(EntityID = 1, page = 1, pageSize = 100, returnSectionGradingPeriodDataID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1, returnSectionGradingPeriodDataID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "get", return_params_list = return_params_list)

def modifySectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1, setGradingPeriodID = None, setIsCompleted = None, setSectionID = None, setRelationships = None, returnSectionGradingPeriodDataID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionGradingPeriodData(EntityID = 1, setGradingPeriodID = None, setIsCompleted = None, setSectionID = None, setRelationships = None, returnSectionGradingPeriodDataID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnSectionGradingScaleGroupID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1, returnSectionGradingScaleGroupID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "get", return_params_list = return_params_list)

def modifySectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1, setGradingPeriodGradeBucketID = None, setGradingScaleGroupID = None, setSectionGradingScaleGroupIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSectionGradingScaleGroupID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionGradingScaleGroup(EntityID = 1, setGradingPeriodGradeBucketID = None, setGradingScaleGroupID = None, setSectionGradingScaleGroupIDClonedFrom = None, setSectionID = None, setRelationships = None, returnSectionGradingScaleGroupID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionSubjectWeight(EntityID = 1, page = 1, pageSize = 100, returnSectionSubjectWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1, returnSectionSubjectWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "get", return_params_list = return_params_list)

def modifySectionSubjectWeight(SectionSubjectWeightID, EntityID = 1, setSectionGradeBucketID = None, setSubjectID = None, setWeightPercent = None, setRelationships = None, returnSectionSubjectWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionSubjectWeight(EntityID = 1, setSectionGradeBucketID = None, setSubjectID = None, setWeightPercent = None, setRelationships = None, returnSectionSubjectWeightID = True, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAnswer(EntityID = 1, page = 1, pageSize = 100, returnStudentAnswerID = True, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAnswer(StudentAnswerID, EntityID = 1, returnStudentAnswerID = True, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "get", return_params_list = return_params_list)

def modifyStudentAnswer(StudentAnswerID, EntityID = 1, setQuestionAnswerID = None, setStudentQuestionID = None, setValue = None, setRelationships = None, returnStudentAnswerID = True, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAnswer(EntityID = 1, setQuestionAnswerID = None, setStudentQuestionID = None, setValue = None, setRelationships = None, returnStudentAnswerID = True, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAnswer(StudentAnswerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnStudentAssignmentID = True, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAssignment(StudentAssignmentID, EntityID = 1, returnStudentAssignmentID = True, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyStudentAssignment(StudentAssignmentID, EntityID = 1, setAssignmentID = None, setCalculatedPoints = None, setComments = None, setGradeMarkID = None, setIsDropped = None, setIsGraded = None, setIsMissing = None, setNoCount = None, setOnlineAssignmentNotificationSent = None, setOnlineAssignmentReviewNotificationSent = None, setScore = None, setScoreClarifierID = None, setSectionID = None, setStudentSectionID = None, setSubmissionStatus = None, setSubmissionStatusCode = None, setSubmissionTime = None, setTimeLastScored = None, setRelationships = None, returnStudentAssignmentID = True, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAssignment(EntityID = 1, setAssignmentID = None, setCalculatedPoints = None, setComments = None, setGradeMarkID = None, setIsDropped = None, setIsGraded = None, setIsMissing = None, setNoCount = None, setOnlineAssignmentNotificationSent = None, setOnlineAssignmentReviewNotificationSent = None, setScore = None, setScoreClarifierID = None, setSectionID = None, setStudentSectionID = None, setSubmissionStatus = None, setSubmissionStatusCode = None, setSubmissionTime = None, setTimeLastScored = None, setRelationships = None, returnStudentAssignmentID = True, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAssignment(StudentAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentAssignmentAttempt(EntityID = 1, page = 1, pageSize = 100, returnStudentAssignmentAttemptID = True, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1, returnStudentAssignmentAttemptID = True, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "get", return_params_list = return_params_list)

def modifyStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1, setComments = None, setDateAttempted = None, setGradeMarkID = None, setIsUsed = None, setScore = None, setStudentAssignmentID = None, setRelationships = None, returnStudentAssignmentAttemptID = True, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentAssignmentAttempt(EntityID = 1, setComments = None, setDateAttempted = None, setGradeMarkID = None, setIsUsed = None, setScore = None, setStudentAssignmentID = None, setRelationships = None, returnStudentAssignmentAttemptID = True, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGradeBucketAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketAcademicStandardID = True, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1, returnStudentGradeBucketAcademicStandardID = True, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1, setAcademicStandardID = None, setCalculatedPoints = None, setEarnedPoints = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentWithAdjustment = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setRelationships = None, returnStudentGradeBucketAcademicStandardID = True, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGradeBucketAcademicStandard(EntityID = 1, setAcademicStandardID = None, setCalculatedPoints = None, setEarnedPoints = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentWithAdjustment = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setRelationships = None, returnStudentGradeBucketAcademicStandardID = True, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGradeBucketSubject(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketSubjectID = True, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1, returnStudentGradeBucketSubjectID = True, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "get", return_params_list = return_params_list)

def modifyStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1, setCalculatedPoints = None, setEarnedPoints = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentWithAdjustment = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setSubjectID = None, setRelationships = None, returnStudentGradeBucketSubjectID = True, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGradeBucketSubject(EntityID = 1, setCalculatedPoints = None, setEarnedPoints = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentWithAdjustment = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setSubjectID = None, setRelationships = None, returnStudentGradeBucketSubjectID = True, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentGradingScaleGroupID = True, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1, returnStudentGradingScaleGroupID = True, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "get", return_params_list = return_params_list)

def modifyStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1, setAllowTeachersToModify = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setGradingScaleGroupID = None, setSchoolYearID = None, setStudentGradingScaleGroupIDClonedFrom = None, setRelationships = None, returnStudentGradingScaleGroupID = True, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGradingScaleGroup(EntityID = 1, setAllowTeachersToModify = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setGradingScaleGroupID = None, setSchoolYearID = None, setStudentGradingScaleGroupIDClonedFrom = None, setRelationships = None, returnStudentGradingScaleGroupID = True, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGradingScaleGroupStudentSection(EntityID = 1, page = 1, pageSize = 100, returnStudentGradingScaleGroupStudentSectionID = True, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1, returnStudentGradingScaleGroupStudentSectionID = True, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1, setStudentGradingScaleGroupID = None, setStudentSectionID = None, setRelationships = None, returnStudentGradingScaleGroupStudentSectionID = True, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGradingScaleGroupStudentSection(EntityID = 1, setStudentGradingScaleGroupID = None, setStudentSectionID = None, setRelationships = None, returnStudentGradingScaleGroupStudentSectionID = True, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGroup(StudentGroupID, EntityID = 1, returnStudentGroupID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "get", return_params_list = return_params_list)

def modifyStudentGroup(StudentGroupID, EntityID = 1, setEndDate = None, setName = None, setSectionID = None, setStartDate = None, setStudentGroupSyncKey = None, setRelationships = None, returnStudentGroupID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGroup(EntityID = 1, setEndDate = None, setName = None, setSectionID = None, setStartDate = None, setStudentGroupSyncKey = None, setRelationships = None, returnStudentGroupID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGroup(StudentGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGroupAssignment(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1, returnStudentGroupAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1, setAssignmentID = None, setStudentGroupID = None, setRelationships = None, returnStudentGroupAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGroupAssignment(EntityID = 1, setAssignmentID = None, setStudentGroupID = None, setRelationships = None, returnStudentGroupAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGroupStudentSection(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupStudentSectionID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1, returnStudentGroupStudentSectionID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1, setEndDate = None, setStartDate = None, setStudentGroupID = None, setStudentSectionID = None, setRelationships = None, returnStudentGroupStudentSectionID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGroupStudentSection(EntityID = 1, setEndDate = None, setStartDate = None, setStudentGroupID = None, setStudentSectionID = None, setRelationships = None, returnStudentGroupStudentSectionID = True, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGroupTeacherSectionSetting(EntityID = 1, page = 1, pageSize = 100, returnStudentGroupTeacherSectionSettingID = True, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1, returnStudentGroupTeacherSectionSettingID = True, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "get", return_params_list = return_params_list)

def modifyStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1, setColor = None, setDisplay = None, setStudentGroupID = None, setTeacherSectionSettingID = None, setRelationships = None, returnStudentGroupTeacherSectionSettingID = True, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGroupTeacherSectionSetting(EntityID = 1, setColor = None, setDisplay = None, setStudentGroupID = None, setTeacherSectionSettingID = None, setRelationships = None, returnStudentGroupTeacherSectionSettingID = True, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentQuestion(EntityID = 1, page = 1, pageSize = 100, returnStudentQuestionID = True, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentQuestion(StudentQuestionID, EntityID = 1, returnStudentQuestionID = True, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "get", return_params_list = return_params_list)

def modifyStudentQuestion(StudentQuestionID, EntityID = 1, setAssignmentQuestionID = None, setOrder = None, setScore = None, setStatus = None, setStatusCode = None, setStudentAssignmentID = None, setRelationships = None, returnStudentQuestionID = True, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentQuestion(EntityID = 1, setAssignmentQuestionID = None, setOrder = None, setScore = None, setStatus = None, setStatusCode = None, setStudentAssignmentID = None, setRelationships = None, returnStudentQuestionID = True, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentQuestion(StudentQuestionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSectionGradingScaleGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionGradingScaleGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1, returnStudentSectionGradingScaleGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1, setGradingPeriodGradeBucketID = None, setStudentGradingScaleGroupStudentSectionID = None, setRelationships = None, returnStudentSectionGradingScaleGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSectionGradingScaleGradeBucket(EntityID = 1, setGradingPeriodGradeBucketID = None, setStudentGradingScaleGroupStudentSectionID = None, setRelationships = None, returnStudentSectionGradingScaleGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSectionNote(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionNoteID = True, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSectionNote(StudentSectionNoteID, EntityID = 1, returnStudentSectionNoteID = True, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "get", return_params_list = return_params_list)

def modifyStudentSectionNote(StudentSectionNoteID, EntityID = 1, setLimitToThisSection = None, setNote = None, setOtherTeachersHaveAccess = None, setStudentSectionID = None, setRelationships = None, returnStudentSectionNoteID = True, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSectionNote(EntityID = 1, setLimitToThisSection = None, setNote = None, setOtherTeachersHaveAccess = None, setStudentSectionID = None, setRelationships = None, returnStudentSectionNoteID = True, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSectionNote(StudentSectionNoteID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubjectGradingScaleGroup(EntityID = 1, page = 1, pageSize = 100, returnSubjectGradingScaleGroupID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1, returnSubjectGradingScaleGroupID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "get", return_params_list = return_params_list)

def modifySubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1, setCalculationGroupID = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsDefaultGroup = None, setSubjectGradingScaleGroupIDClonedFrom = None, setRelationships = None, returnSubjectGradingScaleGroupID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubjectGradingScaleGroup(EntityID = 1, setCalculationGroupID = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsDefaultGroup = None, setSubjectGradingScaleGroupIDClonedFrom = None, setRelationships = None, returnSubjectGradingScaleGroupID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubjectGradingScaleGroupSubject(EntityID = 1, page = 1, pageSize = 100, returnSubjectGradingScaleGroupSubjectID = True, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1, returnSubjectGradingScaleGroupSubjectID = True, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "get", return_params_list = return_params_list)

def modifySubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1, setCalculationGroupSubjectID = None, setEntityGroupKey = None, setSubjectGradingScaleGroupID = None, setSubjectGradingScaleGroupSubjectIDClonedFrom = None, setRelationships = None, returnSubjectGradingScaleGroupSubjectID = True, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubjectGradingScaleGroupSubject(EntityID = 1, setCalculationGroupSubjectID = None, setEntityGroupKey = None, setSubjectGradingScaleGroupID = None, setSubjectGradingScaleGroupSubjectIDClonedFrom = None, setRelationships = None, returnSubjectGradingScaleGroupSubjectID = True, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionAcademicStandardGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionAcademicStandardGradeBucketSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1, returnTeacherSectionAcademicStandardGradeBucketSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1, setAcademicStandardID = None, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionAcademicStandardGradeBucketSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionAcademicStandardGradeBucketSetting(EntityID = 1, setAcademicStandardID = None, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionAcademicStandardGradeBucketSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionCategoryAnalyticsSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionCategoryAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1, returnTeacherSectionCategoryAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1, setAnalysisType = None, setAnalysisTypeCode = None, setCategoryID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionCategoryAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionCategoryAnalyticsSetting(EntityID = 1, setAnalysisType = None, setAnalysisTypeCode = None, setCategoryID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionCategoryAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionGradeBucketAnalyticsSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionGradeBucketAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1, returnTeacherSectionGradeBucketAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1, setAnalysisType = None, setAnalysisTypeCode = None, setCalculationGroupGradeBucketID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionGradeBucketAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionGradeBucketAnalyticsSetting(EntityID = 1, setAnalysisType = None, setAnalysisTypeCode = None, setCalculationGroupGradeBucketID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionGradeBucketAnalyticsSettingID = True, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1, returnTeacherSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1, setGradeBucketDisplayType = None, setGradeBucketDisplayTypeCode = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionGradeBucketSetting(EntityID = 1, setGradeBucketDisplayType = None, setGradeBucketDisplayTypeCode = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionGradeBucketSettingID = True, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionGradingPeriodSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionGradingPeriodSettingID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1, returnTeacherSectionGradingPeriodSettingID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1, setGradingPeriodID = None, setIncludeMissingAssignments = None, setShowAssessments = None, setShowAssignments = None, setShowGradeBuckets = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionGradingPeriodSettingID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionGradingPeriodSetting(EntityID = 1, setGradingPeriodID = None, setIncludeMissingAssignments = None, setShowAssessments = None, setShowAssignments = None, setShowGradeBuckets = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionGradingPeriodSettingID = True, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionSettingID = True, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1, returnTeacherSectionSettingID = True, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1, setBrowseViewID = None, setCalculationGroupGradeBucketIDLocked = None, setClassGroupID = None, setDisplayAssignmentAttendanceIndicator = None, setDisplayAssignmentStudentGroupColors = None, setDisplayAttendance = None, setDisplayGradebookAverages = None, setDisplayMissingAssignment = None, setDisplayStudentGradeLevel = None, setDisplayStudentGradingPeriodCommentIndicator = None, setDisplayStudentGroupColors = None, setDisplayStudentGroups = None, setDisplayStudentNumber = None, setDisplayUnscoredPastDueAssignments = None, setHideAssignmentCategoryColors = None, setHideLockedColumns = None, setManualDateEntryEndDate = None, setManualDateEntryStartDate = None, setSectionID = None, setStudentNameDisplayType = None, setStudentNameDisplayTypeCode = None, setStudentsToDisplay = None, setStudentsToDisplayCode = None, setUseCustomClassRosterSort = None, setUserIDOwner = None, setRelationships = None, returnTeacherSectionSettingID = True, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionSetting(EntityID = 1, setBrowseViewID = None, setCalculationGroupGradeBucketIDLocked = None, setClassGroupID = None, setDisplayAssignmentAttendanceIndicator = None, setDisplayAssignmentStudentGroupColors = None, setDisplayAttendance = None, setDisplayGradebookAverages = None, setDisplayMissingAssignment = None, setDisplayStudentGradeLevel = None, setDisplayStudentGradingPeriodCommentIndicator = None, setDisplayStudentGroupColors = None, setDisplayStudentGroups = None, setDisplayStudentNumber = None, setDisplayUnscoredPastDueAssignments = None, setHideAssignmentCategoryColors = None, setHideLockedColumns = None, setManualDateEntryEndDate = None, setManualDateEntryStartDate = None, setSectionID = None, setStudentNameDisplayType = None, setStudentNameDisplayTypeCode = None, setStudentsToDisplay = None, setStudentsToDisplayCode = None, setUseCustomClassRosterSort = None, setUserIDOwner = None, setRelationships = None, returnTeacherSectionSettingID = True, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionStandardsDisplayAcademicStandardSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1, setAcademicStandardID = None, setTeacherSectionStandardsDisplayGradeBucketSettingID = None, setRelationships = None, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionStandardsDisplayAcademicStandardSetting(EntityID = 1, setAcademicStandardID = None, setTeacherSectionStandardsDisplayGradeBucketSettingID = None, setRelationships = None, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionStandardsDisplayGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionStandardsDisplayGradeBucketSettingID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1, returnTeacherSectionStandardsDisplayGradeBucketSettingID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1, setCalculationGroupGradeBucketID = None, setShowBucket = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionStandardsDisplayGradeBucketSettingID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionStandardsDisplayGradeBucketSetting(EntityID = 1, setCalculationGroupGradeBucketID = None, setShowBucket = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionStandardsDisplayGradeBucketSettingID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionStudentSectionSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionStudentSectionSettingID = True, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1, returnTeacherSectionStudentSectionSettingID = True, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1, setDisplayOrder = None, setStudentSectionID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionStudentSectionSettingID = True, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionStudentSectionSetting(EntityID = 1, setDisplayOrder = None, setStudentSectionID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionStudentSectionSettingID = True, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherSectionSubjectGradeBucketSetting(EntityID = 1, page = 1, pageSize = 100, returnTeacherSectionSubjectGradeBucketSettingID = True, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1, returnTeacherSectionSubjectGradeBucketSettingID = True, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "get", return_params_list = return_params_list)

def modifyTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setSubjectID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionSubjectGradeBucketSettingID = True, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherSectionSubjectGradeBucketSetting(EntityID = 1, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setSubjectID = None, setTeacherSectionSettingID = None, setRelationships = None, returnTeacherSectionSubjectGradeBucketSettingID = True, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAdjustedCategory(EntityID = 1, page = 1, pageSize = 100, returnTempAdjustedCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1, returnTempAdjustedCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "get", return_params_list = return_params_list)

def modifyTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1, setCategoryID = None, setTempSectionCategoryID = None, setRelationships = None, returnTempAdjustedCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAdjustedCategory(EntityID = 1, setCategoryID = None, setTempSectionCategoryID = None, setRelationships = None, returnTempAdjustedCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAssignmentError(EntityID = 1, page = 1, pageSize = 100, returnTempAssignmentErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAssignmentError(TempAssignmentErrorID, EntityID = 1, returnTempAssignmentErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempAssignmentError(TempAssignmentErrorID, EntityID = 1, setErrorNumber = None, setErrorText = None, setTempSectionAssignmentID = None, setRelationships = None, returnTempAssignmentErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAssignmentError(EntityID = 1, setErrorNumber = None, setErrorText = None, setTempSectionAssignmentID = None, setRelationships = None, returnTempAssignmentErrorID = True, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAssignmentError(TempAssignmentErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCalcGroupBucketRemoveStandardOrSubjectResult(EntityID = 1, page = 1, pageSize = 100, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = True, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = True, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "get", return_params_list = return_params_list)

def modifyTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1, setErrorText = None, setIsError = None, setStandardOrSubjectDescription = None, setRelationships = None, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = True, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCalcGroupBucketRemoveStandardOrSubjectResult(EntityID = 1, setErrorText = None, setIsError = None, setStandardOrSubjectDescription = None, setRelationships = None, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = True, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCalculationGroupAcademicStandardWeighting(EntityID = 1, page = 1, pageSize = 100, returnTempCalculationGroupAcademicStandardWeightingID = True, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1, returnTempCalculationGroupAcademicStandardWeightingID = True, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "get", return_params_list = return_params_list)

def modifyTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1, setCalculationGroupAcademicStandardGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setWeightPercent = None, setRelationships = None, returnTempCalculationGroupAcademicStandardWeightingID = True, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCalculationGroupAcademicStandardWeighting(EntityID = 1, setCalculationGroupAcademicStandardGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setWeightPercent = None, setRelationships = None, returnTempCalculationGroupAcademicStandardWeightingID = True, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCalculationGroupSubjectWeighting(EntityID = 1, page = 1, pageSize = 100, returnTempCalculationGroupSubjectWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1, returnTempCalculationGroupSubjectWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "get", return_params_list = return_params_list)

def modifyTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupSubjectGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setWeightPercent = None, setRelationships = None, returnTempCalculationGroupSubjectWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCalculationGroupSubjectWeighting(EntityID = 1, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupSubjectGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setWeightPercent = None, setRelationships = None, returnTempCalculationGroupSubjectWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCalculationGroupWeighting(EntityID = 1, page = 1, pageSize = 100, returnTempCalculationGroupWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1, returnTempCalculationGroupWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "get", return_params_list = return_params_list)

def modifyTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setGradeBucketLabel = None, setGradeBucketOrder = None, setGradingPeriodGradeBucketID = None, setSubjectDescription = None, setSubjectID = None, setWeightPercent = None, setRelationships = None, returnTempCalculationGroupWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCalculationGroupWeighting(EntityID = 1, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setGradeBucketLabel = None, setGradeBucketOrder = None, setGradingPeriodGradeBucketID = None, setSubjectDescription = None, setSubjectID = None, setWeightPercent = None, setRelationships = None, returnTempCalculationGroupWeightingID = True, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCloneGradebookSection(EntityID = 1, page = 1, pageSize = 100, returnTempCloneGradebookSectionID = True, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1, returnTempCloneGradebookSectionID = True, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1, setCanClone = None, setErrorMessage = None, setSectionID = None, setRelationships = None, returnTempCloneGradebookSectionID = True, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCloneGradebookSection(EntityID = 1, setCanClone = None, setErrorMessage = None, setSectionID = None, setRelationships = None, returnTempCloneGradebookSectionID = True, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourseMoveCourse(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMoveCourseID = True, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1, returnTempCourseMoveCourseID = True, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "get", return_params_list = return_params_list)

def modifyTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1, setCodeDescription = None, setCourseCode = None, setCourseDescription = None, setCourseID = None, setEntityID = None, setGroupCourseID = None, setIsValidUpdate = None, setNewCalculationGroupDescription = None, setNewCalculationGroupID = None, setOriginalCalculationGroupDescription = None, setOriginalCalculationGroupID = None, setSchoolYearID = None, setRelationships = None, returnTempCourseMoveCourseID = True, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourseMoveCourse(EntityID = 1, setCodeDescription = None, setCourseCode = None, setCourseDescription = None, setCourseID = None, setEntityID = None, setGroupCourseID = None, setIsValidUpdate = None, setNewCalculationGroupDescription = None, setNewCalculationGroupID = None, setOriginalCalculationGroupDescription = None, setOriginalCalculationGroupID = None, setSchoolYearID = None, setRelationships = None, returnTempCourseMoveCourseID = True, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourseMoveError(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMoveErrorID = True, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1, returnTempCourseMoveErrorID = True, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1, setBucketLabel = None, setErrorCode = None, setErrorMessage = None, setErrorType = None, setErrorTypeCode = None, setSectionID = None, setRelationships = None, returnTempCourseMoveErrorID = True, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourseMoveError(EntityID = 1, setBucketLabel = None, setErrorCode = None, setErrorMessage = None, setErrorType = None, setErrorTypeCode = None, setSectionID = None, setRelationships = None, returnTempCourseMoveErrorID = True, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCourseMoveSectionError(EntityID = 1, page = 1, pageSize = 100, returnTempCourseMoveSectionErrorID = True, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1, returnTempCourseMoveSectionErrorID = True, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1, setCourseID = None, setErrorMessage = None, setSectionCode = None, setSectionID = None, setRelationships = None, returnTempCourseMoveSectionErrorID = True, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCourseMoveSectionError(EntityID = 1, setCourseID = None, setErrorMessage = None, setSectionCode = None, setSectionID = None, setRelationships = None, returnTempCourseMoveSectionErrorID = True, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempDropLowScoreStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnTempDropLowScoreStudentAssignmentID = True, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1, returnTempDropLowScoreStudentAssignmentID = True, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1, setAssignmentName = None, setComments = None, setDropActionType = None, setDropActionTypeCode = None, setDropCode = None, setDropLowScore = None, setDueDate = None, setMaxScore = None, setNewGrade = None, setNoDropReason = None, setOriginalGrade = None, setScore = None, setStudentAssignmentID = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setWeight = None, setRelationships = None, returnTempDropLowScoreStudentAssignmentID = True, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempDropLowScoreStudentAssignment(EntityID = 1, setAssignmentName = None, setComments = None, setDropActionType = None, setDropActionTypeCode = None, setDropCode = None, setDropLowScore = None, setDueDate = None, setMaxScore = None, setNewGrade = None, setNoDropReason = None, setOriginalGrade = None, setScore = None, setStudentAssignmentID = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setWeight = None, setRelationships = None, returnTempDropLowScoreStudentAssignmentID = True, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradebookCloneError(EntityID = 1, page = 1, pageSize = 100, returnTempGradebookCloneErrorID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1, returnTempGradebookCloneErrorID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1, setCalculationGroupGradeBucketID = None, setField = None, setGradeBucketLabel = None, setMessage = None, setRecordType = None, setRecordTypeCode = None, setSectionID = None, setRelationships = None, returnTempGradebookCloneErrorID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradebookCloneError(EntityID = 1, setCalculationGroupGradeBucketID = None, setField = None, setGradeBucketLabel = None, setMessage = None, setRecordType = None, setRecordTypeCode = None, setSectionID = None, setRelationships = None, returnTempGradebookCloneErrorID = True, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradebookGroupError(EntityID = 1, page = 1, pageSize = 100, returnTempGradebookGroupErrorID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1, returnTempGradebookGroupErrorID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1, setCalculationGroupID = None, setDescription = None, setEntityID = None, setErrorText = None, setGradingScaleGroupID = None, setRelationships = None, returnTempGradebookGroupErrorID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradebookGroupError(EntityID = 1, setCalculationGroupID = None, setDescription = None, setEntityID = None, setErrorText = None, setGradingScaleGroupID = None, setRelationships = None, returnTempGradebookGroupErrorID = True, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeMarkError(EntityID = 1, page = 1, pageSize = 100, returnTempGradeMarkErrorID = True, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1, returnTempGradeMarkErrorID = True, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1, setDisplayOrder = None, setGradeMarkCode = None, setGradeMarkID = None, setSectionID = None, setRelationships = None, returnTempGradeMarkErrorID = True, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeMarkError(EntityID = 1, setDisplayOrder = None, setGradeMarkCode = None, setGradeMarkID = None, setSectionID = None, setRelationships = None, returnTempGradeMarkErrorID = True, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradingPeriodGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1, returnTempGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1, setEndDate = None, setErrorCount = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setRelationships = None, returnTempGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradingPeriodGradeBucket(EntityID = 1, setEndDate = None, setErrorCount = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setRelationships = None, returnTempGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradingPeriodGradeBucketError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodGradeBucketErrorID = True, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1, returnTempGradingPeriodGradeBucketErrorID = True, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1, setCalculationGroupID = None, setCalculationType = None, setEndDate = None, setErrorNumber = None, setErrorText = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setSubjectOrStandardDescription = None, setSubjectOrStandardKey = None, setRelationships = None, returnTempGradingPeriodGradeBucketErrorID = True, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradingPeriodGradeBucketError(EntityID = 1, setCalculationGroupID = None, setCalculationType = None, setEndDate = None, setErrorNumber = None, setErrorText = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setSubjectOrStandardDescription = None, setSubjectOrStandardKey = None, setRelationships = None, returnTempGradingPeriodGradeBucketErrorID = True, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionAssignment(EntityID = 1, page = 1, pageSize = 100, returnTempSectionAssignmentID = True, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionAssignment(TempSectionAssignmentID, EntityID = 1, returnTempSectionAssignmentID = True, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionAssignment(TempSectionAssignmentID, EntityID = 1, setAnswerRevealDate = None, setAnswerRevealDateAndTime = None, setAnswerRevealTime = None, setAssignedDate = None, setAssignmentID = None, setAssignmentName = None, setAttachmentCount = None, setCategoryDescription = None, setCurrentPeriod = None, setDueDate = None, setEndDate = None, setEndDateAndTime = None, setEndTime = None, setEntityID = None, setErrorCount = None, setHideScoreUntilDate = None, setHideScoreUntilDateAndTime = None, setHideScoreUntilTime = None, setIsOnlineAssignment = None, setMaxScore = None, setSchoolYearID = None, setSectionDetails = None, setSectionID = None, setSectionLengthEndDate = None, setSectionLengthStartDate = None, setShowCorrectAnswers = None, setStartDate = None, setStartDateAndTime = None, setStartTime = None, setSync = None, setWeight = None, setRelationships = None, returnTempSectionAssignmentID = True, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionAssignment(EntityID = 1, setAnswerRevealDate = None, setAnswerRevealDateAndTime = None, setAnswerRevealTime = None, setAssignedDate = None, setAssignmentID = None, setAssignmentName = None, setAttachmentCount = None, setCategoryDescription = None, setCurrentPeriod = None, setDueDate = None, setEndDate = None, setEndDateAndTime = None, setEndTime = None, setEntityID = None, setErrorCount = None, setHideScoreUntilDate = None, setHideScoreUntilDateAndTime = None, setHideScoreUntilTime = None, setIsOnlineAssignment = None, setMaxScore = None, setSchoolYearID = None, setSectionDetails = None, setSectionID = None, setSectionLengthEndDate = None, setSectionLengthStartDate = None, setShowCorrectAnswers = None, setStartDate = None, setStartDateAndTime = None, setStartTime = None, setSync = None, setWeight = None, setRelationships = None, returnTempSectionAssignmentID = True, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionAssignment(TempSectionAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionCategory(EntityID = 1, page = 1, pageSize = 100, returnTempSectionCategoryID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionCategory(TempSectionCategoryID, EntityID = 1, returnTempSectionCategoryID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionCategory(TempSectionCategoryID, EntityID = 1, setCalculationGroupGradeBucketID = None, setCalculationGroupID = None, setCanClone = None, setCategoryCode = None, setCategoryID = None, setCategoryIDIsInvalid = None, setErrorMessages = None, setSectionID = None, setWeightPercent = None, setRelationships = None, returnTempSectionCategoryID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionCategory(EntityID = 1, setCalculationGroupGradeBucketID = None, setCalculationGroupID = None, setCanClone = None, setCategoryCode = None, setCategoryID = None, setCategoryIDIsInvalid = None, setErrorMessages = None, setSectionID = None, setWeightPercent = None, setRelationships = None, returnTempSectionCategoryID = True, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionCategory(TempSectionCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1, returnTempSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1, setCalculationGroupGradeBucketID = None, setCanClone = None, setChildRecords = None, setCurrentAllowCategoryOverride = None, setCurrentCalculationType = None, setCurrentCalculationTypeCode = None, setEndDate = None, setErrorMessages = None, setExclude = None, setGradeBucketLabel = None, setGradeBucketTypeID = None, setHasLeftOverPercentage = None, setIsCalculationTypeOverridden = None, setIsSpecificGradeBucket = None, setNewCalculationType = None, setNewCalculationTypeCode = None, setOrder = None, setSectionGradeBucketID = None, setSectionID = None, setStartDate = None, setRelationships = None, returnTempSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionGradeBucket(EntityID = 1, setCalculationGroupGradeBucketID = None, setCanClone = None, setChildRecords = None, setCurrentAllowCategoryOverride = None, setCurrentCalculationType = None, setCurrentCalculationTypeCode = None, setEndDate = None, setErrorMessages = None, setExclude = None, setGradeBucketLabel = None, setGradeBucketTypeID = None, setHasLeftOverPercentage = None, setIsCalculationTypeOverridden = None, setIsSpecificGradeBucket = None, setNewCalculationType = None, setNewCalculationTypeCode = None, setOrder = None, setSectionGradeBucketID = None, setSectionID = None, setStartDate = None, setRelationships = None, returnTempSectionGradeBucketID = True, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionGradeBucketWeight(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradeBucketWeightID = True, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1, returnTempSectionGradeBucketWeightID = True, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupGradeBucketIDComposite = None, setCalculationGroupGradeBucketIDFeeder = None, setCanClone = None, setSectionID = None, setSubjectIDToWeight = None, setWeightPercent = None, setRelationships = None, returnTempSectionGradeBucketWeightID = True, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionGradeBucketWeight(EntityID = 1, setAcademicStandardIDToWeight = None, setCalculationGroupGradeBucketIDComposite = None, setCalculationGroupGradeBucketIDFeeder = None, setCanClone = None, setSectionID = None, setSubjectIDToWeight = None, setWeightPercent = None, setRelationships = None, returnTempSectionGradeBucketWeightID = True, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionGradingScale(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradingScaleID = True, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1, returnTempSectionGradingScaleID = True, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1, setCanClone = None, setChildGradeBuckets = None, setErrorMessage = None, setSectionID = None, setRelationships = None, returnTempSectionGradingScaleID = True, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionGradingScale(EntityID = 1, setCanClone = None, setChildGradeBuckets = None, setErrorMessage = None, setSectionID = None, setRelationships = None, returnTempSectionGradingScaleID = True, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempSectionGradingScaleGroupToCreate(EntityID = 1, page = 1, pageSize = 100, returnTempSectionGradingScaleGroupToCreateID = True, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1, returnTempSectionGradingScaleGroupToCreateID = True, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "get", return_params_list = return_params_list)

def modifyTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1, setCourseCode = None, setCourseDescriptionCodeSectionCode = None, setCourseGradingScaleGroupCourseID = None, setCourseGradingScaleGroupID = None, setCourseID = None, setDescription = None, setGradingPeriodGradeBucketsToRetainJson = None, setInvalidGradeMarks = None, setIsValidInNewGroup = None, setNewCourseGradingScaleGroupDescription = None, setNewCourseGradingScaleGroupID = None, setReason = None, setRequiresSectionGradingScaleGroups = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setRelationships = None, returnTempSectionGradingScaleGroupToCreateID = True, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempSectionGradingScaleGroupToCreate(EntityID = 1, setCourseCode = None, setCourseDescriptionCodeSectionCode = None, setCourseGradingScaleGroupCourseID = None, setCourseGradingScaleGroupID = None, setCourseID = None, setDescription = None, setGradingPeriodGradeBucketsToRetainJson = None, setInvalidGradeMarks = None, setIsValidInNewGroup = None, setNewCourseGradingScaleGroupDescription = None, setNewCourseGradingScaleGroupID = None, setReason = None, setRequiresSectionGradingScaleGroups = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setRelationships = None, returnTempSectionGradingScaleGroupToCreateID = True, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnTempStudentAssignmentID = True, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentAssignment(TempStudentAssignmentID, EntityID = 1, returnTempStudentAssignmentID = True, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentAssignment(TempStudentAssignmentID, EntityID = 1, setAssignmentDescription = None, setAssignmentID = None, setAssignmentName = None, setDueDate = None, setInclude = None, setIsMissing = None, setMaxScore = None, setNoCount = None, setScore = None, setScoreClarifierCode = None, setScoreClarifierID = None, setSectionID = None, setStudentSectionID = None, setWeight = None, setRelationships = None, returnTempStudentAssignmentID = True, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentAssignment(EntityID = 1, setAssignmentDescription = None, setAssignmentID = None, setAssignmentName = None, setDueDate = None, setInclude = None, setIsMissing = None, setMaxScore = None, setNoCount = None, setScore = None, setScoreClarifierCode = None, setScoreClarifierID = None, setSectionID = None, setStudentSectionID = None, setWeight = None, setRelationships = None, returnTempStudentAssignmentID = True, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentAssignment(TempStudentAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentGradingScaleGroupStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGradingScaleGroupStudentSectionID = True, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1, returnTempStudentGradingScaleGroupStudentSectionID = True, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1, setCourseDescriptionCodeSectionCode = None, setErrorText = None, setGradingPeriodGradeBuckets = None, setHasError = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthID = None, setStudentFullNameLFM = None, setStudentGradingScaleGroupStudentSectionID = None, setStudentID = None, setStudentSectionID = None, setRelationships = None, returnTempStudentGradingScaleGroupStudentSectionID = True, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentGradingScaleGroupStudentSection(EntityID = 1, setCourseDescriptionCodeSectionCode = None, setErrorText = None, setGradingPeriodGradeBuckets = None, setHasError = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthID = None, setStudentFullNameLFM = None, setStudentGradingScaleGroupStudentSectionID = None, setStudentID = None, setStudentSectionID = None, setRelationships = None, returnTempStudentGradingScaleGroupStudentSectionID = True, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempUnDropLowScoreStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempUnDropLowScoreStudentSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1, returnTempUnDropLowScoreStudentSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1, setNewGrade = None, setOriginalGrade = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setRelationships = None, returnTempUnDropLowScoreStudentSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempUnDropLowScoreStudentSection(EntityID = 1, setNewGrade = None, setOriginalGrade = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setRelationships = None, returnTempUnDropLowScoreStudentSectionID = True, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryVendorAssignment(EntityID = 1, page = 1, pageSize = 100, returnVendorAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getVendorAssignment(VendorAssignmentID, EntityID = 1, returnVendorAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyVendorAssignment(VendorAssignmentID, EntityID = 1, setAssignmentID = None, setOneRosterVendorID = None, setVendorSourceID = None, setRelationships = None, returnVendorAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createVendorAssignment(EntityID = 1, setAssignmentID = None, setOneRosterVendorID = None, setVendorSourceID = None, setRelationships = None, returnVendorAssignmentID = True, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteVendorAssignment(VendorAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryVendorCategory(EntityID = 1, page = 1, pageSize = 100, returnVendorCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getVendorCategory(VendorCategoryID, EntityID = 1, returnVendorCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "get", return_params_list = return_params_list)

def modifyVendorCategory(VendorCategoryID, EntityID = 1, setCategoryID = None, setOneRosterVendorID = None, setVendorSourceID = None, setRelationships = None, returnVendorCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createVendorCategory(EntityID = 1, setCategoryID = None, setOneRosterVendorID = None, setVendorSourceID = None, setRelationships = None, returnVendorCategoryID = True, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteVendorCategory(VendorCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryVendorStudentAssignment(EntityID = 1, page = 1, pageSize = 100, returnVendorStudentAssignmentID = True, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1, returnVendorStudentAssignmentID = True, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "get", return_params_list = return_params_list)

def modifyVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1, setOneRosterVendorID = None, setStudentAssignmentID = None, setVendorSourceID = None, setRelationships = None, returnVendorStudentAssignmentID = True, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createVendorStudentAssignment(EntityID = 1, setOneRosterVendorID = None, setStudentAssignmentID = None, setVendorSourceID = None, setRelationships = None, returnVendorStudentAssignmentID = True, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")