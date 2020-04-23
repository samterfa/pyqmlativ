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

def getAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1, returnAcademicStandardGradingScaleGroupID = False, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1, setAcademicStandardGradingScaleGroupID = None, setAcademicStandardGradingScaleGroupIDClonedFrom = None, setCalculationGroupID = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setModifiedTime = None, setStandardCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradingScaleGroupID = False, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardGradingScaleGroup(EntityID = 1, setAcademicStandardGradingScaleGroupID = None, setAcademicStandardGradingScaleGroupIDClonedFrom = None, setCalculationGroupID = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setModifiedTime = None, setStandardCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradingScaleGroupID = False, returnAcademicStandardGradingScaleGroupIDClonedFrom = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnStandardCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardGradingScaleGroup(AcademicStandardGradingScaleGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroup/" + str(AcademicStandardGradingScaleGroupID), verb = "delete")


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

def getAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1, returnAcademicStandardGradingScaleGroupAcademicStandardID = False, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1, setAcademicStandardGradingScaleGroupAcademicStandardID = None, setAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = None, setAcademicStandardGradingScaleGroupID = None, setCalculationGroupAcademicStandardID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradingScaleGroupAcademicStandardID = False, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardGradingScaleGroupAcademicStandard(EntityID = 1, setAcademicStandardGradingScaleGroupAcademicStandardID = None, setAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = None, setAcademicStandardGradingScaleGroupID = None, setCalculationGroupAcademicStandardID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradingScaleGroupAcademicStandardID = False, returnAcademicStandardGradingScaleGroupAcademicStandardIDClonedFrom = False, returnAcademicStandardGradingScaleGroupID = False, returnCalculationGroupAcademicStandardID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardGradingScaleGroupAcademicStandard(AcademicStandardGradingScaleGroupAcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AcademicStandardGradingScaleGroupAcademicStandard/" + str(AcademicStandardGradingScaleGroupAcademicStandardID), verb = "delete")


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

def getAssessment(AssessmentID, EntityID = 1, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "get", return_params_list = return_params)

def modifyAssessment(AssessmentID, EntityID = 1, setAssessmentID = None, setAssignedDate = None, setAssignmentCount = None, setCanDelete = None, setCategoryID = None, setCreatedTime = None, setDescription = None, setDisplayRestoreButton = None, setDueDate = None, setIsDeleted = None, setModifiedTime = None, setName = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAssessment(EntityID = 1, setAssessmentID = None, setAssignedDate = None, setAssignmentCount = None, setCanDelete = None, setCategoryID = None, setCreatedTime = None, setDescription = None, setDisplayRestoreButton = None, setDueDate = None, setIsDeleted = None, setModifiedTime = None, setName = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentCount = False, returnCanDelete = False, returnCategoryID = False, returnCreatedTime = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnIsDeleted = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAssessment(AssessmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assessment/" + str(AssessmentID), verb = "delete")


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

def getAssignment(AssignmentID, EntityID = 1, returnAssignmentID = False, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDClonedFrom = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "get", return_params_list = return_params)

def modifyAssignment(AssignmentID, EntityID = 1, setAssignmentID = None, setAcademicStandardID = None, setAcademicStandards = None, setActiveStudentCount = None, setActiveStudentGroups = None, setAllowAutoScore = None, setAllStudentAssignmentsAreNotStarted = None, setAnswerRevealTime = None, setAssessmentID = None, setAssignedDate = None, setAssignmentIDClonedFrom = None, setAssignmentIDParent = None, setAssignmentQuestionCount = None, setAssignmentSyncKey = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setAutoScore = None, setAveragePercent = None, setCalculatedPointsAllowedFromQuestions = None, setCanDelete = None, setCategoryID = None, setChildAssignmentCount = None, setClassesSyncedTo = None, setCreatedTime = None, setCreateStudentGroupAssignmentErrorMessage = None, setDefaultPointsPerQuestion = None, setDescription = None, setDisplayRestoreButton = None, setDueDate = None, setDueDateInCurrentOpenExtendedGradingPeriod = None, setDueDateInTransactionForGivenStudentSection = None, setDueDateIsInGivenDateRange = None, setEffectiveAcademicStandardID = None, setEndTime = None, setHasInstructions = None, setHasParent = None, setHasQuestions = None, setHasStudentAssignments = None, setHasStudentAssignmentsWithScoreOrGradeMark = None, setHasStudentFamilyAttachmentsToDisplay = None, setHasStudentGroupAssignments = None, setHasUngradedStudentAssignments = None, setHasWholeNumberWeight = None, setHideScoreUntilTime = None, setInstructions = None, setIsActiveOrUnlocked = None, setIsAHistoricRecord = None, setIsAvailableForStudentGroup = None, setIsAvailableForStudentSection = None, setIsDeleted = None, setIsOnlineAssignment = None, setIsParent = None, setIsPastEndTime = None, setIsSynced = None, setMaxScore = None, setModifiedTime = None, setName = None, setQuestionCount = None, setRandomizeQuestions = None, setRelatedAssignmentsHaveAcademicStandards = None, setRelatedAssignmentsHaveSubjects = None, setScoreDisplayType = None, setScoreDisplayTypeCode = None, setScoredStudentAssignmentCount = None, setSectionID = None, setSendNotificationWhenAnswersRevealed = None, setSendNotificationWhenAssignmentReadyToTake = None, setShowCorrectAnswers = None, setShowScore = None, setStartTime = None, setStudentFamilyAccessAttachmentCount = None, setSubjectID = None, setSubjects = None, setUseGradeMarkScoring = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnAssignmentID = False, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDClonedFrom = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAssignment(EntityID = 1, setAssignmentID = None, setAcademicStandardID = None, setAcademicStandards = None, setActiveStudentCount = None, setActiveStudentGroups = None, setAllowAutoScore = None, setAllStudentAssignmentsAreNotStarted = None, setAnswerRevealTime = None, setAssessmentID = None, setAssignedDate = None, setAssignmentIDClonedFrom = None, setAssignmentIDParent = None, setAssignmentQuestionCount = None, setAssignmentSyncKey = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setAutoScore = None, setAveragePercent = None, setCalculatedPointsAllowedFromQuestions = None, setCanDelete = None, setCategoryID = None, setChildAssignmentCount = None, setClassesSyncedTo = None, setCreatedTime = None, setCreateStudentGroupAssignmentErrorMessage = None, setDefaultPointsPerQuestion = None, setDescription = None, setDisplayRestoreButton = None, setDueDate = None, setDueDateInCurrentOpenExtendedGradingPeriod = None, setDueDateInTransactionForGivenStudentSection = None, setDueDateIsInGivenDateRange = None, setEffectiveAcademicStandardID = None, setEndTime = None, setHasInstructions = None, setHasParent = None, setHasQuestions = None, setHasStudentAssignments = None, setHasStudentAssignmentsWithScoreOrGradeMark = None, setHasStudentFamilyAttachmentsToDisplay = None, setHasStudentGroupAssignments = None, setHasUngradedStudentAssignments = None, setHasWholeNumberWeight = None, setHideScoreUntilTime = None, setInstructions = None, setIsActiveOrUnlocked = None, setIsAHistoricRecord = None, setIsAvailableForStudentGroup = None, setIsAvailableForStudentSection = None, setIsDeleted = None, setIsOnlineAssignment = None, setIsParent = None, setIsPastEndTime = None, setIsSynced = None, setMaxScore = None, setModifiedTime = None, setName = None, setQuestionCount = None, setRandomizeQuestions = None, setRelatedAssignmentsHaveAcademicStandards = None, setRelatedAssignmentsHaveSubjects = None, setScoreDisplayType = None, setScoreDisplayTypeCode = None, setScoredStudentAssignmentCount = None, setSectionID = None, setSendNotificationWhenAnswersRevealed = None, setSendNotificationWhenAssignmentReadyToTake = None, setShowCorrectAnswers = None, setShowScore = None, setStartTime = None, setStudentFamilyAccessAttachmentCount = None, setSubjectID = None, setSubjects = None, setUseGradeMarkScoring = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnAssignmentID = False, returnAcademicStandardID = False, returnAcademicStandards = False, returnActiveStudentCount = False, returnActiveStudentGroups = False, returnAllowAutoScore = False, returnAllStudentAssignmentsAreNotStarted = False, returnAnswerRevealTime = False, returnAssessmentID = False, returnAssignedDate = False, returnAssignmentIDClonedFrom = False, returnAssignmentIDParent = False, returnAssignmentQuestionCount = False, returnAssignmentSyncKey = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnAutoScore = False, returnAveragePercent = False, returnCalculatedPointsAllowedFromQuestions = False, returnCanDelete = False, returnCategoryID = False, returnChildAssignmentCount = False, returnClassesSyncedTo = False, returnCreatedTime = False, returnCreateStudentGroupAssignmentErrorMessage = False, returnDefaultPointsPerQuestion = False, returnDescription = False, returnDisplayRestoreButton = False, returnDueDate = False, returnDueDateInCurrentOpenExtendedGradingPeriod = False, returnDueDateInTransactionForGivenStudentSection = False, returnDueDateIsInGivenDateRange = False, returnEffectiveAcademicStandardID = False, returnEndTime = False, returnHasInstructions = False, returnHasParent = False, returnHasQuestions = False, returnHasStudentAssignments = False, returnHasStudentAssignmentsWithScoreOrGradeMark = False, returnHasStudentFamilyAttachmentsToDisplay = False, returnHasStudentGroupAssignments = False, returnHasUngradedStudentAssignments = False, returnHasWholeNumberWeight = False, returnHideScoreUntilTime = False, returnInstructions = False, returnIsActiveOrUnlocked = False, returnIsAHistoricRecord = False, returnIsAvailableForStudentGroup = False, returnIsAvailableForStudentSection = False, returnIsDeleted = False, returnIsOnlineAssignment = False, returnIsParent = False, returnIsPastEndTime = False, returnIsSynced = False, returnMaxScore = False, returnModifiedTime = False, returnName = False, returnQuestionCount = False, returnRandomizeQuestions = False, returnRelatedAssignmentsHaveAcademicStandards = False, returnRelatedAssignmentsHaveSubjects = False, returnScoreDisplayType = False, returnScoreDisplayTypeCode = False, returnScoredStudentAssignmentCount = False, returnSectionID = False, returnSendNotificationWhenAnswersRevealed = False, returnSendNotificationWhenAssignmentReadyToTake = False, returnShowCorrectAnswers = False, returnShowScore = False, returnStartTime = False, returnStudentFamilyAccessAttachmentCount = False, returnSubjectID = False, returnSubjects = False, returnUseGradeMarkScoring = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAssignment(AssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Assignment/" + str(AssignmentID), verb = "delete")


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

def getAssignmentAttachment(AssignmentAttachmentID, EntityID = 1, returnAssignmentAttachmentID = False, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "get", return_params_list = return_params)

def modifyAssignmentAttachment(AssignmentAttachmentID, EntityID = 1, setAssignmentAttachmentID = None, setAssignmentID = None, setAttachmentID = None, setCreatedTime = None, setDisplayInStudentFamilyAccess = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssignmentAttachmentID = False, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAssignmentAttachment(EntityID = 1, setAssignmentAttachmentID = None, setAssignmentID = None, setAttachmentID = None, setCreatedTime = None, setDisplayInStudentFamilyAccess = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssignmentAttachmentID = False, returnAssignmentID = False, returnAttachmentID = False, returnCreatedTime = False, returnDisplayInStudentFamilyAccess = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAssignmentAttachment(AssignmentAttachmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentAttachment/" + str(AssignmentAttachmentID), verb = "delete")


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

def getAssignmentQuestion(AssignmentQuestionID, EntityID = 1, returnAssignmentQuestionID = False, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "get", return_params_list = return_params)

def modifyAssignmentQuestion(AssignmentQuestionID, EntityID = 1, setAssignmentQuestionID = None, setAllowPartialCredit = None, setAssignmentID = None, setCreatedTime = None, setDisplayOrder = None, setModifiedTime = None, setPointsAllowed = None, setQuestionAnswerCount = None, setQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssignmentQuestionID = False, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAssignmentQuestion(EntityID = 1, setAssignmentQuestionID = None, setAllowPartialCredit = None, setAssignmentID = None, setCreatedTime = None, setDisplayOrder = None, setModifiedTime = None, setPointsAllowed = None, setQuestionAnswerCount = None, setQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssignmentQuestionID = False, returnAllowPartialCredit = False, returnAssignmentID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnPointsAllowed = False, returnQuestionAnswerCount = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAssignmentQuestion(AssignmentQuestionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/AssignmentQuestion/" + str(AssignmentQuestionID), verb = "delete")


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

def getCalculationGroup(CalculationGroupID, EntityID = 1, returnCalculationGroupID = False, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentAveragePercentTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentAveragePercentOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "get", return_params_list = return_params)

def modifyCalculationGroup(CalculationGroupID, EntityID = 1, setCalculationGroupID = None, setAllowAcademicStandardWeightingTeacherOverride = None, setAllowAssignmentAveragePercentTeacherOverride = None, setAllowAssignmentPointsTeacherOverride = None, setAllowCategoryOverride = None, setAllowCategoryWeightingTeacherOverride = None, setAllowDecayingAverageTeacherOverride = None, setAllowedTeacherOverrideCalculationTypes = None, setAllowGradeBucketWeightingTeacherOverride = None, setAllowNotGradedTeacherOverride = None, setAllowSubjectiveTeacherOverride = None, setAllowSubjectWeightingTeacherOverride = None, setAllowTotalPointsAndGradeBucketWeightingTeacherOverride = None, setCalculationGroupIDClonedFrom = None, setCreatedTime = None, setDecayingAveragePercent = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setHasAcademicStandards = None, setHasAcademicStandardWeightingOverrides = None, setHasAssignmentAveragePercentOverrides = None, setHasAssignmentPointsOverrides = None, setHasCategoryWeightingOverrides = None, setHasDecayingAverage = None, setHasDecayingAverageOverrides = None, setHasDefaultCloneFilter = None, setHasGradeBucketWeightingOverrides = None, setHasNotGradedOverrides = None, setHasSubjectiveOverrides = None, setHasSubjects = None, setHasSubjectWeightingOverrides = None, setHasTotalPointsAndGradeBucketWeightingOverrides = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setLimitTeacherOverridesToCategoriesInGroup = None, setModifiedTime = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupID = False, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentAveragePercentTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentAveragePercentOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroup(EntityID = 1, setCalculationGroupID = None, setAllowAcademicStandardWeightingTeacherOverride = None, setAllowAssignmentAveragePercentTeacherOverride = None, setAllowAssignmentPointsTeacherOverride = None, setAllowCategoryOverride = None, setAllowCategoryWeightingTeacherOverride = None, setAllowDecayingAverageTeacherOverride = None, setAllowedTeacherOverrideCalculationTypes = None, setAllowGradeBucketWeightingTeacherOverride = None, setAllowNotGradedTeacherOverride = None, setAllowSubjectiveTeacherOverride = None, setAllowSubjectWeightingTeacherOverride = None, setAllowTotalPointsAndGradeBucketWeightingTeacherOverride = None, setCalculationGroupIDClonedFrom = None, setCreatedTime = None, setDecayingAveragePercent = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setHasAcademicStandards = None, setHasAcademicStandardWeightingOverrides = None, setHasAssignmentAveragePercentOverrides = None, setHasAssignmentPointsOverrides = None, setHasCategoryWeightingOverrides = None, setHasDecayingAverage = None, setHasDecayingAverageOverrides = None, setHasDefaultCloneFilter = None, setHasGradeBucketWeightingOverrides = None, setHasNotGradedOverrides = None, setHasSubjectiveOverrides = None, setHasSubjects = None, setHasSubjectWeightingOverrides = None, setHasTotalPointsAndGradeBucketWeightingOverrides = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setLimitTeacherOverridesToCategoriesInGroup = None, setModifiedTime = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupID = False, returnAllowAcademicStandardWeightingTeacherOverride = False, returnAllowAssignmentAveragePercentTeacherOverride = False, returnAllowAssignmentPointsTeacherOverride = False, returnAllowCategoryOverride = False, returnAllowCategoryWeightingTeacherOverride = False, returnAllowDecayingAverageTeacherOverride = False, returnAllowedTeacherOverrideCalculationTypes = False, returnAllowGradeBucketWeightingTeacherOverride = False, returnAllowNotGradedTeacherOverride = False, returnAllowSubjectiveTeacherOverride = False, returnAllowSubjectWeightingTeacherOverride = False, returnAllowTotalPointsAndGradeBucketWeightingTeacherOverride = False, returnCalculationGroupIDClonedFrom = False, returnCreatedTime = False, returnDecayingAveragePercent = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeightingOverrides = False, returnHasAssignmentAveragePercentOverrides = False, returnHasAssignmentPointsOverrides = False, returnHasCategoryWeightingOverrides = False, returnHasDecayingAverage = False, returnHasDecayingAverageOverrides = False, returnHasDefaultCloneFilter = False, returnHasGradeBucketWeightingOverrides = False, returnHasNotGradedOverrides = False, returnHasSubjectiveOverrides = False, returnHasSubjects = False, returnHasSubjectWeightingOverrides = False, returnHasTotalPointsAndGradeBucketWeightingOverrides = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToCategoriesInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroup(CalculationGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroup/" + str(CalculationGroupID), verb = "delete")


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

def getCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1, returnCalculationGroupAcademicStandardID = False, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnIsDescendantOfSpecifiedAcademicStandard = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1, setCalculationGroupAcademicStandardID = None, setAcademicStandardID = None, setCalculateForSingleBucket = None, setCalculationGroupAcademicStandardIDClonedFrom = None, setCalculationGroupAcademicStandardIDParent = None, setCalculationGroupID = None, setCreatedTime = None, setDisplayOnReportCard = None, setEntityGroupKey = None, setHasAssignments = None, setHasGradingScale = None, setHasParentSubject = None, setIsDescendantOfSpecifiedAcademicStandard = None, setLevel = None, setModifiedTime = None, setOrder = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupAcademicStandardID = False, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnIsDescendantOfSpecifiedAcademicStandard = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupAcademicStandard(EntityID = 1, setCalculationGroupAcademicStandardID = None, setAcademicStandardID = None, setCalculateForSingleBucket = None, setCalculationGroupAcademicStandardIDClonedFrom = None, setCalculationGroupAcademicStandardIDParent = None, setCalculationGroupID = None, setCreatedTime = None, setDisplayOnReportCard = None, setEntityGroupKey = None, setHasAssignments = None, setHasGradingScale = None, setHasParentSubject = None, setIsDescendantOfSpecifiedAcademicStandard = None, setLevel = None, setModifiedTime = None, setOrder = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupAcademicStandardID = False, returnAcademicStandardID = False, returnCalculateForSingleBucket = False, returnCalculationGroupAcademicStandardIDClonedFrom = False, returnCalculationGroupAcademicStandardIDParent = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDisplayOnReportCard = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnHasParentSubject = False, returnIsDescendantOfSpecifiedAcademicStandard = False, returnLevel = False, returnModifiedTime = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupAcademicStandard(CalculationGroupAcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandard/" + str(CalculationGroupAcademicStandardID), verb = "delete")


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

def getCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = False, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1, setCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = None, setCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupAcademicStandardIDAtLevel = None, setCalculationGroupHierarchyDepthID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = False, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(EntityID = 1, setCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = None, setCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupAcademicStandardIDAtLevel = None, setCalculationGroupHierarchyDepthID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthID = False, returnCalculationGroupAcademicStandardCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupAcademicStandardIDAtLevel = False, returnCalculationGroupHierarchyDepthID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupAcademicStandardCalculationGroupHierarchyDepth(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardCalculationGroupHierarchyDepth/" + str(CalculationGroupAcademicStandardCalculationGroupHierarchyDepthID), verb = "delete")


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

def getCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1, setCalculationGroupAcademicStandardGradeBucketID = None, setCalculationGroupAcademicStandardGradeBucketIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setEntityGroupKey = None, setHasAcademicStandardWeighting = None, setHasAssignments = None, setHasCalculationGroupSubjectWeight = None, setHasCalculationGroupWeight = None, setHasCategoryWeighting = None, setIsAHistoricRecord = None, setIsWeightedOnByACalculationGroupSubjectGradeBucket = None, setIsWeightedOnInASectionOverride = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupAcademicStandardGradeBucket(EntityID = 1, setCalculationGroupAcademicStandardGradeBucketID = None, setCalculationGroupAcademicStandardGradeBucketIDClonedFrom = None, setCalculationGroupAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setEntityGroupKey = None, setHasAcademicStandardWeighting = None, setHasAssignments = None, setHasCalculationGroupSubjectWeight = None, setHasCalculationGroupWeight = None, setHasCategoryWeighting = None, setIsAHistoricRecord = None, setIsWeightedOnByACalculationGroupSubjectGradeBucket = None, setIsWeightedOnInASectionOverride = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardGradeBucketIDClonedFrom = False, returnCalculationGroupAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAcademicStandardWeighting = False, returnHasAssignments = False, returnHasCalculationGroupSubjectWeight = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnIsAHistoricRecord = False, returnIsWeightedOnByACalculationGroupSubjectGradeBucket = False, returnIsWeightedOnInASectionOverride = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupAcademicStandardGradeBucket(CalculationGroupAcademicStandardGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardGradeBucket/" + str(CalculationGroupAcademicStandardGradeBucketID), verb = "delete")


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

def getCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1, returnCalculationGroupAcademicStandardWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1, setCalculationGroupAcademicStandardWeightingID = None, setAcademicStandardAdjustedPercentEarned = None, setAcademicStandardAdjustedPointsEarned = None, setAcademicStandardAdjustedWeightFormula = None, setAcademicStandardIDToWeight = None, setAdjustedWeightPercent = None, setCalculationGroupAcademicStandardGradeBucketID = None, setCalculationGroupAcademicStandardWeightingIDClonedFrom = None, setCategoryAdjustedPercentEarned = None, setCategoryAdjustedPointsEarned = None, setCategoryAdjustedWeightFormula = None, setCategoryIDToWeight = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setIsAHistoricRecord = None, setModifiedTime = None, setPercentEarnedCategory = None, setPointsEarnedCategory = None, setUseForWeightSum = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnCalculationGroupAcademicStandardWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupAcademicStandardWeighting(EntityID = 1, setCalculationGroupAcademicStandardWeightingID = None, setAcademicStandardAdjustedPercentEarned = None, setAcademicStandardAdjustedPointsEarned = None, setAcademicStandardAdjustedWeightFormula = None, setAcademicStandardIDToWeight = None, setAdjustedWeightPercent = None, setCalculationGroupAcademicStandardGradeBucketID = None, setCalculationGroupAcademicStandardWeightingIDClonedFrom = None, setCategoryAdjustedPercentEarned = None, setCategoryAdjustedPointsEarned = None, setCategoryAdjustedWeightFormula = None, setCategoryIDToWeight = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setIsAHistoricRecord = None, setModifiedTime = None, setPercentEarnedCategory = None, setPointsEarnedCategory = None, setUseForWeightSum = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnCalculationGroupAcademicStandardWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCalculationGroupAcademicStandardWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupAcademicStandardWeighting(CalculationGroupAcademicStandardWeightingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupAcademicStandardWeighting/" + str(CalculationGroupAcademicStandardWeightingID), verb = "delete")


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

def getCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1, returnCalculationGroupCategoryID = False, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1, setCalculationGroupCategoryID = None, setCalculationGroupCategoryIDClonedFrom = None, setCalculationGroupID = None, setCategoryID = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupCategoryID = False, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupCategory(EntityID = 1, setCalculationGroupCategoryID = None, setCalculationGroupCategoryIDClonedFrom = None, setCalculationGroupID = None, setCategoryID = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupCategoryID = False, returnCalculationGroupCategoryIDClonedFrom = False, returnCalculationGroupID = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupCategory(CalculationGroupCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCategory/" + str(CalculationGroupCategoryID), verb = "delete")


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

def getCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1, returnCalculationGroupCourseID = False, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1, setCalculationGroupCourseID = None, setCalculationGroupCourseIDClonedFrom = None, setCalculationGroupID = None, setCourseID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupCourseID = False, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupCourse(EntityID = 1, setCalculationGroupCourseID = None, setCalculationGroupCourseIDClonedFrom = None, setCalculationGroupID = None, setCourseID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupCourseID = False, returnCalculationGroupCourseIDClonedFrom = False, returnCalculationGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupCourse(CalculationGroupCourseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupCourse/" + str(CalculationGroupCourseID), verb = "delete")


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

def getCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1, returnCalculationGroupGradeBucketID = False, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1, setCalculationGroupGradeBucketID = None, setAllowCalculationTypeOverride = None, setAllowWeightOverride = None, setCalculationGroupGradeBucketIDClonedFrom = None, setCalculationGroupID = None, setCalculationType = None, setCalculationTypeCode = None, setCourseCount = None, setCreatedTime = None, setEffectiveCalculationType = None, setEffectiveCalculationTypeCode = None, setEntityGroupKey = None, setGetCopySectionLengthXMLFilter = None, setGradeMarkScoringType = None, setGradeMarkScoringTypeCode = None, setGradingPeriodGradeBucketID = None, setHasAcademicStandards = None, setHasAcademicStandardWeighting = None, setHasCategoryWeighting = None, setHasGradeBucketWeighting = None, setHasSubjects = None, setHasSubjectWeighting = None, setInnerCalculationGroupGradeBucketsCount = None, setInUseBySections = None, setIsAHistoricRecord = None, setIsMissingStudentGradeBucketAcademicStandards = None, setIsMissingStudentGradeBucketSubjects = None, setModifiedTime = None, setNumberOfCategories = None, setRoundBucketPercent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercentTotal = None, returnCalculationGroupGradeBucketID = False, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupGradeBucket(EntityID = 1, setCalculationGroupGradeBucketID = None, setAllowCalculationTypeOverride = None, setAllowWeightOverride = None, setCalculationGroupGradeBucketIDClonedFrom = None, setCalculationGroupID = None, setCalculationType = None, setCalculationTypeCode = None, setCourseCount = None, setCreatedTime = None, setEffectiveCalculationType = None, setEffectiveCalculationTypeCode = None, setEntityGroupKey = None, setGetCopySectionLengthXMLFilter = None, setGradeMarkScoringType = None, setGradeMarkScoringTypeCode = None, setGradingPeriodGradeBucketID = None, setHasAcademicStandards = None, setHasAcademicStandardWeighting = None, setHasCategoryWeighting = None, setHasGradeBucketWeighting = None, setHasSubjects = None, setHasSubjectWeighting = None, setInnerCalculationGroupGradeBucketsCount = None, setInUseBySections = None, setIsAHistoricRecord = None, setIsMissingStudentGradeBucketAcademicStandards = None, setIsMissingStudentGradeBucketSubjects = None, setModifiedTime = None, setNumberOfCategories = None, setRoundBucketPercent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercentTotal = None, returnCalculationGroupGradeBucketID = False, returnAllowCalculationTypeOverride = False, returnAllowWeightOverride = False, returnCalculationGroupGradeBucketIDClonedFrom = False, returnCalculationGroupID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCourseCount = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnEntityGroupKey = False, returnGetCopySectionLengthXMLFilter = False, returnGradeMarkScoringType = False, returnGradeMarkScoringTypeCode = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandards = False, returnHasAcademicStandardWeighting = False, returnHasCategoryWeighting = False, returnHasGradeBucketWeighting = False, returnHasSubjects = False, returnHasSubjectWeighting = False, returnInnerCalculationGroupGradeBucketsCount = False, returnInUseBySections = False, returnIsAHistoricRecord = False, returnIsMissingStudentGradeBucketAcademicStandards = False, returnIsMissingStudentGradeBucketSubjects = False, returnModifiedTime = False, returnNumberOfCategories = False, returnRoundBucketPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentTotal = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupGradeBucket(CalculationGroupGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupGradeBucket/" + str(CalculationGroupGradeBucketID), verb = "delete")


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

def getCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1, returnCalculationGroupHierarchyDepthID = False, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1, setCalculationGroupHierarchyDepthID = None, setCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupID = None, setCode = None, setCreatedTime = None, setDepthLevel = None, setDescription = None, setDynamicRelationshipID = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupHierarchyDepthID = False, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupHierarchyDepth(EntityID = 1, setCalculationGroupHierarchyDepthID = None, setCalculationGroupHierarchyDepthIDClonedFrom = None, setCalculationGroupID = None, setCode = None, setCreatedTime = None, setDepthLevel = None, setDescription = None, setDynamicRelationshipID = None, setEntityGroupKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupHierarchyDepthID = False, returnCalculationGroupHierarchyDepthIDClonedFrom = False, returnCalculationGroupID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDynamicRelationshipID = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupHierarchyDepth(CalculationGroupHierarchyDepthID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupHierarchyDepth/" + str(CalculationGroupHierarchyDepthID), verb = "delete")


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

def getCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1, returnCalculationGroupSubjectID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1, setCalculationGroupSubjectID = None, setCalculationGroupID = None, setCalculationGroupSubjectIDClonedFrom = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setHasGradingScale = None, setIsAHistoricRecord = None, setModifiedTime = None, setOrder = None, setSubjectID = None, setTopLevelAcademicStandardHierarchyDepthDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupSubjectID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupSubject(EntityID = 1, setCalculationGroupSubjectID = None, setCalculationGroupID = None, setCalculationGroupSubjectIDClonedFrom = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setHasGradingScale = None, setIsAHistoricRecord = None, setModifiedTime = None, setOrder = None, setSubjectID = None, setTopLevelAcademicStandardHierarchyDepthDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupSubjectID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasGradingScale = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnOrder = False, returnSubjectID = False, returnTopLevelAcademicStandardHierarchyDepthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupSubject(CalculationGroupSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubject/" + str(CalculationGroupSubjectID), verb = "delete")


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

def getCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1, returnCalculationGroupSubjectAcademicStandardID = False, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1, setCalculationGroupSubjectAcademicStandardID = None, setAcademicStandardID = None, setCalculationGroupID = None, setCalculationGroupSubjectAcademicStandardIDClonedFrom = None, setCreatedTime = None, setEntityGroupKey = None, setIsAHistoricRecord = None, setModifiedTime = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupSubjectAcademicStandardID = False, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupSubjectAcademicStandard(EntityID = 1, setCalculationGroupSubjectAcademicStandardID = None, setAcademicStandardID = None, setCalculationGroupID = None, setCalculationGroupSubjectAcademicStandardIDClonedFrom = None, setCreatedTime = None, setEntityGroupKey = None, setIsAHistoricRecord = None, setModifiedTime = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupSubjectAcademicStandardID = False, returnAcademicStandardID = False, returnCalculationGroupID = False, returnCalculationGroupSubjectAcademicStandardIDClonedFrom = False, returnCreatedTime = False, returnEntityGroupKey = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupSubjectAcademicStandard(CalculationGroupSubjectAcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectAcademicStandard/" + str(CalculationGroupSubjectAcademicStandardID), verb = "delete")


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

def getCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1, setCalculationGroupSubjectGradeBucketID = None, setCalculationGroupGradeBucketID = None, setCalculationGroupSubjectGradeBucketIDClonedFrom = None, setCalculationGroupSubjectID = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setHasCalculationGroupWeight = None, setHasCategoryWeighting = None, setHasSubjectAcademicStandards = None, setIsAHistoricRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupSubjectGradeBucket(EntityID = 1, setCalculationGroupSubjectGradeBucketID = None, setCalculationGroupGradeBucketID = None, setCalculationGroupSubjectGradeBucketIDClonedFrom = None, setCalculationGroupSubjectID = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setHasCalculationGroupWeight = None, setHasCategoryWeighting = None, setHasSubjectAcademicStandards = None, setIsAHistoricRecord = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupSubjectGradeBucketIDClonedFrom = False, returnCalculationGroupSubjectID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnHasCalculationGroupWeight = False, returnHasCategoryWeighting = False, returnHasSubjectAcademicStandards = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupSubjectGradeBucket(CalculationGroupSubjectGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectGradeBucket/" + str(CalculationGroupSubjectGradeBucketID), verb = "delete")


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

def getCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1, returnCalculationGroupSubjectWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1, setCalculationGroupSubjectWeightingID = None, setAcademicStandardAdjustedPercentEarned = None, setAcademicStandardAdjustedPointsEarned = None, setAcademicStandardAdjustedWeightFormula = None, setAcademicStandardIDToWeight = None, setAdjustedWeightPercent = None, setCalculationGroupSubjectGradeBucketID = None, setCalculationGroupSubjectWeightingIDClonedFrom = None, setCategoryAdjustedPercentEarned = None, setCategoryAdjustedPointsEarned = None, setCategoryAdjustedWeightFormula = None, setCategoryIDToWeight = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setIsAHistoricRecord = None, setModifiedTime = None, setPercentEarnedCategory = None, setPointsEarnedCategory = None, setUseForWeightSum = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnCalculationGroupSubjectWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupSubjectWeighting(EntityID = 1, setCalculationGroupSubjectWeightingID = None, setAcademicStandardAdjustedPercentEarned = None, setAcademicStandardAdjustedPointsEarned = None, setAcademicStandardAdjustedWeightFormula = None, setAcademicStandardIDToWeight = None, setAdjustedWeightPercent = None, setCalculationGroupSubjectGradeBucketID = None, setCalculationGroupSubjectWeightingIDClonedFrom = None, setCategoryAdjustedPercentEarned = None, setCategoryAdjustedPointsEarned = None, setCategoryAdjustedWeightFormula = None, setCategoryIDToWeight = None, setCreatedTime = None, setEntityGroupKey = None, setHasAssignments = None, setIsAHistoricRecord = None, setModifiedTime = None, setPercentEarnedCategory = None, setPointsEarnedCategory = None, setUseForWeightSum = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnCalculationGroupSubjectWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardAdjustedWeightFormula = False, returnAcademicStandardIDToWeight = False, returnAdjustedWeightPercent = False, returnCalculationGroupSubjectGradeBucketID = False, returnCalculationGroupSubjectWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryAdjustedWeightFormula = False, returnCategoryIDToWeight = False, returnCreatedTime = False, returnEntityGroupKey = False, returnHasAssignments = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedCategory = False, returnPointsEarnedCategory = False, returnUseForWeightSum = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupSubjectWeighting(CalculationGroupSubjectWeightingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupSubjectWeighting/" + str(CalculationGroupSubjectWeightingID), verb = "delete")


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

def getCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1, returnCalculationGroupWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "get", return_params_list = return_params)

def modifyCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1, setCalculationGroupWeightingID = None, setAcademicStandardAdjustedPercentEarned = None, setAcademicStandardAdjustedPointsEarned = None, setAcademicStandardIDToWeight = None, setAcademicStandardWeightFormula = None, setAdjustedAcademicStandardWeightPercent = None, setAdjustedCategoryWeightPercent = None, setAdjustedGradeBucketWeightPercent = None, setAdjustedSubjectWeightPercent = None, setCalculationGroupGradeBucketID = None, setCalculationGroupWeightingIDClonedFrom = None, setCategoryAdjustedPercentEarned = None, setCategoryAdjustedPointsEarned = None, setCategoryIDToWeight = None, setCategoryWeightFormula = None, setCreatedTime = None, setEntityGroupKey = None, setGradeBucketAdjustedPercentEarned = None, setGradeBucketAdjustedPointsEarned = None, setGradeBucketWeightFormula = None, setGradingPeriodGradeBucketIDToWeight = None, setIsAHistoricRecord = None, setModifiedTime = None, setPercentEarnedForCategory = None, setPointsEarnedForCategory = None, setRequiredGrade = None, setRoundBucketPercent = None, setSubjectAdjustedPercentEarned = None, setSubjectAdjustedPointsEarned = None, setSubjectIDToWeight = None, setSubjectWeightFormula = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnCalculationGroupWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalculationGroupWeighting(EntityID = 1, setCalculationGroupWeightingID = None, setAcademicStandardAdjustedPercentEarned = None, setAcademicStandardAdjustedPointsEarned = None, setAcademicStandardIDToWeight = None, setAcademicStandardWeightFormula = None, setAdjustedAcademicStandardWeightPercent = None, setAdjustedCategoryWeightPercent = None, setAdjustedGradeBucketWeightPercent = None, setAdjustedSubjectWeightPercent = None, setCalculationGroupGradeBucketID = None, setCalculationGroupWeightingIDClonedFrom = None, setCategoryAdjustedPercentEarned = None, setCategoryAdjustedPointsEarned = None, setCategoryIDToWeight = None, setCategoryWeightFormula = None, setCreatedTime = None, setEntityGroupKey = None, setGradeBucketAdjustedPercentEarned = None, setGradeBucketAdjustedPointsEarned = None, setGradeBucketWeightFormula = None, setGradingPeriodGradeBucketIDToWeight = None, setIsAHistoricRecord = None, setModifiedTime = None, setPercentEarnedForCategory = None, setPointsEarnedForCategory = None, setRequiredGrade = None, setRoundBucketPercent = None, setSubjectAdjustedPercentEarned = None, setSubjectAdjustedPointsEarned = None, setSubjectIDToWeight = None, setSubjectWeightFormula = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnCalculationGroupWeightingID = False, returnAcademicStandardAdjustedPercentEarned = False, returnAcademicStandardAdjustedPointsEarned = False, returnAcademicStandardIDToWeight = False, returnAcademicStandardWeightFormula = False, returnAdjustedAcademicStandardWeightPercent = False, returnAdjustedCategoryWeightPercent = False, returnAdjustedGradeBucketWeightPercent = False, returnAdjustedSubjectWeightPercent = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupWeightingIDClonedFrom = False, returnCategoryAdjustedPercentEarned = False, returnCategoryAdjustedPointsEarned = False, returnCategoryIDToWeight = False, returnCategoryWeightFormula = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketAdjustedPercentEarned = False, returnGradeBucketAdjustedPointsEarned = False, returnGradeBucketWeightFormula = False, returnGradingPeriodGradeBucketIDToWeight = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnRequiredGrade = False, returnRoundBucketPercent = False, returnSubjectAdjustedPercentEarned = False, returnSubjectAdjustedPointsEarned = False, returnSubjectIDToWeight = False, returnSubjectWeightFormula = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalculationGroupWeighting(CalculationGroupWeightingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CalculationGroupWeighting/" + str(CalculationGroupWeightingID), verb = "delete")


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

def getCategory(CategoryID, EntityID = 1, returnCategoryID = False, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "get", return_params_list = return_params)

def modifyCategory(CategoryID, EntityID = 1, setCategoryID = None, setAssignmentCount = None, setAverageStudentAssignmentScoreForCategoryAndStudentSection = None, setBackgroundColor = None, setCalculationGroupAllowCategoryOverride = None, setCategoryIDClonedFrom = None, setCategoryUsedInCategoryWeightingDefaultSetup = None, setCategoryUsedInTotalPointsDefaultCalculationSetup = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDescriptionWithCategoryWeightPercent = None, setDistrictGroupKey = None, setDistrictID = None, setGradeBucketTypeCategory = None, setHasAssignments = None, setHasSpecificCalculationGroupAcademicStandardWeight = None, setHasSpecificCalculationGroupSubjectWeight = None, setHasSpecificCalculationGroupWeight = None, setIsAHistoricRecord = None, setIsValidInCalculationGroup = None, setModifiedTime = None, setSchoolYearID = None, setTextColor = None, setUseForSpecificGradeBucketType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightingAllowedForGradeBucketType = None, returnCategoryID = False, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCategory(EntityID = 1, setCategoryID = None, setAssignmentCount = None, setAverageStudentAssignmentScoreForCategoryAndStudentSection = None, setBackgroundColor = None, setCalculationGroupAllowCategoryOverride = None, setCategoryIDClonedFrom = None, setCategoryUsedInCategoryWeightingDefaultSetup = None, setCategoryUsedInTotalPointsDefaultCalculationSetup = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDescriptionWithCategoryWeightPercent = None, setDistrictGroupKey = None, setDistrictID = None, setGradeBucketTypeCategory = None, setHasAssignments = None, setHasSpecificCalculationGroupAcademicStandardWeight = None, setHasSpecificCalculationGroupSubjectWeight = None, setHasSpecificCalculationGroupWeight = None, setIsAHistoricRecord = None, setIsValidInCalculationGroup = None, setModifiedTime = None, setSchoolYearID = None, setTextColor = None, setUseForSpecificGradeBucketType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightingAllowedForGradeBucketType = None, returnCategoryID = False, returnAssignmentCount = False, returnAverageStudentAssignmentScoreForCategoryAndStudentSection = False, returnBackgroundColor = False, returnCalculationGroupAllowCategoryOverride = False, returnCategoryIDClonedFrom = False, returnCategoryUsedInCategoryWeightingDefaultSetup = False, returnCategoryUsedInTotalPointsDefaultCalculationSetup = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDescriptionWithCategoryWeightPercent = False, returnDistrictGroupKey = False, returnDistrictID = False, returnGradeBucketTypeCategory = False, returnHasAssignments = False, returnHasSpecificCalculationGroupAcademicStandardWeight = False, returnHasSpecificCalculationGroupSubjectWeight = False, returnHasSpecificCalculationGroupWeight = False, returnIsAHistoricRecord = False, returnIsValidInCalculationGroup = False, returnModifiedTime = False, returnSchoolYearID = False, returnTextColor = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightingAllowedForGradeBucketType = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCategory(CategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Category/" + str(CategoryID), verb = "delete")


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

def getCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1, returnCategoryGradeBucketTypeID = False, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "get", return_params_list = return_params)

def modifyCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1, setCategoryGradeBucketTypeID = None, setCategoryGradeBucketTypeIDClonedFrom = None, setCategoryID = None, setCreatedTime = None, setEntityGroupKey = None, setGradeBucketTypeID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCategoryGradeBucketTypeID = False, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCategoryGradeBucketType(EntityID = 1, setCategoryGradeBucketTypeID = None, setCategoryGradeBucketTypeIDClonedFrom = None, setCategoryID = None, setCreatedTime = None, setEntityGroupKey = None, setGradeBucketTypeID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCategoryGradeBucketTypeID = False, returnCategoryGradeBucketTypeIDClonedFrom = False, returnCategoryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGradeBucketTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCategoryGradeBucketType(CategoryGradeBucketTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CategoryGradeBucketType/" + str(CategoryGradeBucketTypeID), verb = "delete")


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

def getClassGroup(ClassGroupID, EntityID = 1, returnClassGroupID = False, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "get", return_params_list = return_params)

def modifyClassGroup(ClassGroupID, EntityID = 1, setClassGroupID = None, setCreatedTime = None, setEntityID = None, setIsAHistoricRecord = None, setModifiedTime = None, setName = None, setSchoolYearID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClassGroupID = False, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createClassGroup(EntityID = 1, setClassGroupID = None, setCreatedTime = None, setEntityID = None, setIsAHistoricRecord = None, setModifiedTime = None, setName = None, setSchoolYearID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClassGroupID = False, returnCreatedTime = False, returnEntityID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteClassGroup(ClassGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroup/" + str(ClassGroupID), verb = "delete")


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

def getClassGroupSection(ClassGroupSectionID, EntityID = 1, returnClassGroupSectionID = False, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "get", return_params_list = return_params)

def modifyClassGroupSection(ClassGroupSectionID, EntityID = 1, setClassGroupSectionID = None, setClassGroupID = None, setCreatedTime = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClassGroupSectionID = False, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createClassGroupSection(EntityID = 1, setClassGroupSectionID = None, setClassGroupID = None, setCreatedTime = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClassGroupSectionID = False, returnClassGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteClassGroupSection(ClassGroupSectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClassGroupSection/" + str(ClassGroupSectionID), verb = "delete")


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

def getClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1, returnClosedGradingPeriodGradeChangeID = False, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "get", return_params_list = return_params)

def modifyClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1, setClosedGradingPeriodGradeChangeID = None, setCalculatedCompletedTime = None, setCompletedTime = None, setCreatedTime = None, setDisplayCompleteButton = None, setDisplayMassReviewDenyButton = None, setGradingPeriodID = None, setModifiedTime = None, setReason = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClosedGradingPeriodGradeChangeID = False, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createClosedGradingPeriodGradeChange(EntityID = 1, setClosedGradingPeriodGradeChangeID = None, setCalculatedCompletedTime = None, setCompletedTime = None, setCreatedTime = None, setDisplayCompleteButton = None, setDisplayMassReviewDenyButton = None, setGradingPeriodID = None, setModifiedTime = None, setReason = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClosedGradingPeriodGradeChangeID = False, returnCalculatedCompletedTime = False, returnCompletedTime = False, returnCreatedTime = False, returnDisplayCompleteButton = False, returnDisplayMassReviewDenyButton = False, returnGradingPeriodID = False, returnModifiedTime = False, returnReason = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteClosedGradingPeriodGradeChange(ClosedGradingPeriodGradeChangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodGradeChange/" + str(ClosedGradingPeriodGradeChangeID), verb = "delete")


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

def getClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1, returnClosedGradingPeriodStudentGradeBucketChangeID = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "get", return_params_list = return_params)

def modifyClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1, setClosedGradingPeriodStudentGradeBucketChangeID = None, setCalculatedClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeID = None, setClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeStatusCode = None, setCreatedTime = None, setGradeMarkIDNew = None, setGradeMarkIDOriginal = None, setHasSnapshot = None, setIsDisabled = None, setIsGradeChangePastDueAndInProgress = None, setModifiedTime = None, setNewPercent = None, setOriginalPercent = None, setStaffMeetID = None, setStudentGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClosedGradingPeriodStudentGradeBucketChangeID = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createClosedGradingPeriodStudentGradeBucketChange(EntityID = 1, setClosedGradingPeriodStudentGradeBucketChangeID = None, setCalculatedClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeID = None, setClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeStatusCode = None, setCreatedTime = None, setGradeMarkIDNew = None, setGradeMarkIDOriginal = None, setHasSnapshot = None, setIsDisabled = None, setIsGradeChangePastDueAndInProgress = None, setModifiedTime = None, setNewPercent = None, setOriginalPercent = None, setStaffMeetID = None, setStudentGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnClosedGradingPeriodStudentGradeBucketChangeID = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCreatedTime = False, returnGradeMarkIDNew = False, returnGradeMarkIDOriginal = False, returnHasSnapshot = False, returnIsDisabled = False, returnIsGradeChangePastDueAndInProgress = False, returnModifiedTime = False, returnNewPercent = False, returnOriginalPercent = False, returnStaffMeetID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteClosedGradingPeriodStudentGradeBucketChange(ClosedGradingPeriodStudentGradeBucketChangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ClosedGradingPeriodStudentGradeBucketChange/" + str(ClosedGradingPeriodStudentGradeBucketChangeID), verb = "delete")


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

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrict(EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")


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

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setUseCurriculumSubjectsInGradebook = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearID = None, setConfigDistrictYearIDClonedFrom = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setUseCurriculumSubjectsInGradebook = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseCurriculumSubjectsInGradebook = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")


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

def getConfigEntity(ConfigEntityID, EntityID = 1, returnConfigEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "get", return_params_list = return_params)

def modifyConfigEntity(ConfigEntityID, EntityID = 1, setConfigEntityID = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setRunInMonitorByScheduledTask = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntity(EntityID = 1, setConfigEntityID = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setRunInMonitorByScheduledTask = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnRunInMonitorByScheduledTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntity(ConfigEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntity/" + str(ConfigEntityID), verb = "delete")


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

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = False, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setConfigEntityGroupYearID = None, setAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = None, setAllowGracePeriodAtEndOfGradingPeriod = None, setAllowMultipleAssignmentAttempts = None, setAllowNegativePercentAdjustment = None, setAllowOnlineAssignments = None, setAllowPercentAdjustment = None, setAllowRetainedFutureScoring = None, setAllowStudentGroups = None, setAllowTeacherComments = None, setAllowTeachersToAddStudentNotes = None, setAllowTeachersToOverrideDefaultMaxScore = None, setAllowTeachersToOverrideDefaultMaxWeight = None, setAllowTeachersToTransferGrades = None, setAssignmentMaxScore = None, setAssignmentMaxWeight = None, setAutoApproveGradeChangeRequest = None, setCapCalculationAt100Percent = None, setCapWeightedCategoryCalculationAt100Percent = None, setClosedGradingPeriodGradeChangeCutOff = None, setClosedGradingPeriodGradeChangePermissionType = None, setClosedGradingPeriodGradeChangePermissionTypeCode = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setDisplayNonGradedClassesForTeachers = None, setEntityGroupKey = None, setEntityID = None, setFailingGradeThresholdPercent = None, setGradingPeriodEditExtensionDays = None, setGradingPeriodEditExtensionEndTime = None, setModifiedTime = None, setNumberOfDaysUntilNewStudentIconAppears = None, setNumberOfDaysUntilUnscoredAssignmentsAreMissing = None, setOnlyShowGradebooksWithActiveStudentSectionTransactions = None, setSchoolYearID = None, setScoreClarifierIDFailing = None, setUseFailingGradeScoreClarifier = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setConfigEntityGroupYearID = None, setAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = None, setAllowGracePeriodAtEndOfGradingPeriod = None, setAllowMultipleAssignmentAttempts = None, setAllowNegativePercentAdjustment = None, setAllowOnlineAssignments = None, setAllowPercentAdjustment = None, setAllowRetainedFutureScoring = None, setAllowStudentGroups = None, setAllowTeacherComments = None, setAllowTeachersToAddStudentNotes = None, setAllowTeachersToOverrideDefaultMaxScore = None, setAllowTeachersToOverrideDefaultMaxWeight = None, setAllowTeachersToTransferGrades = None, setAssignmentMaxScore = None, setAssignmentMaxWeight = None, setAutoApproveGradeChangeRequest = None, setCapCalculationAt100Percent = None, setCapWeightedCategoryCalculationAt100Percent = None, setClosedGradingPeriodGradeChangeCutOff = None, setClosedGradingPeriodGradeChangePermissionType = None, setClosedGradingPeriodGradeChangePermissionTypeCode = None, setConfigEntityGroupYearIDClonedFrom = None, setCreatedTime = None, setDisplayNonGradedClassesForTeachers = None, setEntityGroupKey = None, setEntityID = None, setFailingGradeThresholdPercent = None, setGradingPeriodEditExtensionDays = None, setGradingPeriodEditExtensionEndTime = None, setModifiedTime = None, setNumberOfDaysUntilNewStudentIconAppears = None, setNumberOfDaysUntilUnscoredAssignmentsAreMissing = None, setOnlyShowGradebooksWithActiveStudentSectionTransactions = None, setSchoolYearID = None, setScoreClarifierIDFailing = None, setUseFailingGradeScoreClarifier = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityGroupYearID = False, returnAllowClosedGradingPeriodGradeChangeRequestsToUpdateSnapshotGrades = False, returnAllowGracePeriodAtEndOfGradingPeriod = False, returnAllowMultipleAssignmentAttempts = False, returnAllowNegativePercentAdjustment = False, returnAllowOnlineAssignments = False, returnAllowPercentAdjustment = False, returnAllowRetainedFutureScoring = False, returnAllowStudentGroups = False, returnAllowTeacherComments = False, returnAllowTeachersToAddStudentNotes = False, returnAllowTeachersToOverrideDefaultMaxScore = False, returnAllowTeachersToOverrideDefaultMaxWeight = False, returnAllowTeachersToTransferGrades = False, returnAssignmentMaxScore = False, returnAssignmentMaxWeight = False, returnAutoApproveGradeChangeRequest = False, returnCapCalculationAt100Percent = False, returnCapWeightedCategoryCalculationAt100Percent = False, returnClosedGradingPeriodGradeChangeCutOff = False, returnClosedGradingPeriodGradeChangePermissionType = False, returnClosedGradingPeriodGradeChangePermissionTypeCode = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnDisplayNonGradedClassesForTeachers = False, returnEntityGroupKey = False, returnEntityID = False, returnFailingGradeThresholdPercent = False, returnGradingPeriodEditExtensionDays = False, returnGradingPeriodEditExtensionEndTime = False, returnModifiedTime = False, returnNumberOfDaysUntilNewStudentIconAppears = False, returnNumberOfDaysUntilUnscoredAssignmentsAreMissing = False, returnOnlyShowGradebooksWithActiveStudentSectionTransactions = False, returnSchoolYearID = False, returnScoreClarifierIDFailing = False, returnUseFailingGradeScoreClarifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")


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

def getCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1, returnCourseGradingScaleGroupID = False, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "get", return_params_list = return_params)

def modifyCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1, setCourseGradingScaleGroupID = None, setAllowSectionOverride = None, setCourseGradingScaleGroupIDClonedFrom = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setLimitTeacherOverridesToGradeMarksInGroup = None, setModifiedTime = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCourseGradingScaleGroupID = False, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCourseGradingScaleGroup(EntityID = 1, setCourseGradingScaleGroupID = None, setAllowSectionOverride = None, setCourseGradingScaleGroupIDClonedFrom = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setFilter = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setLimitTeacherOverridesToGradeMarksInGroup = None, setModifiedTime = None, setRank = None, setSchoolYearID = None, setSearchConditionFilter = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCourseGradingScaleGroupID = False, returnAllowSectionOverride = False, returnCourseGradingScaleGroupIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnFilter = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnLimitTeacherOverridesToGradeMarksInGroup = False, returnModifiedTime = False, returnRank = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCourseGradingScaleGroup(CourseGradingScaleGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroup/" + str(CourseGradingScaleGroupID), verb = "delete")


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

def getCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "get", return_params_list = return_params)

def modifyCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1, setCourseGradingScaleGroupCourseID = None, setCourseGradingScaleGroupID = None, setCourseID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCourseGradingScaleGroupCourse(EntityID = 1, setCourseGradingScaleGroupCourseID = None, setCourseGradingScaleGroupID = None, setCourseID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCourseGradingScaleGroupCourse(CourseGradingScaleGroupCourseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/CourseGradingScaleGroupCourse/" + str(CourseGradingScaleGroupCourseID), verb = "delete")


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

def getDropLowScoreRun(DropLowScoreRunID, EntityID = 1, returnDropLowScoreRunID = False, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "get", return_params_list = return_params)

def modifyDropLowScoreRun(DropLowScoreRunID, EntityID = 1, setDropLowScoreRunID = None, setAffectedStudentAssignmentCount = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setIsEffective = None, setModifiedTime = None, setRunTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDropLowScoreRunID = False, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDropLowScoreRun(EntityID = 1, setDropLowScoreRunID = None, setAffectedStudentAssignmentCount = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setIsEffective = None, setModifiedTime = None, setRunTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDropLowScoreRunID = False, returnAffectedStudentAssignmentCount = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnIsEffective = False, returnModifiedTime = False, returnRunTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDropLowScoreRun(DropLowScoreRunID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRun/" + str(DropLowScoreRunID), verb = "delete")


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

def getDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1, returnDropLowScoreRunStudentAssignmentID = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "get", return_params_list = return_params)

def modifyDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1, setDropLowScoreRunStudentAssignmentID = None, setCreatedTime = None, setDropActionType = None, setDropActionTypeCode = None, setDropLowScoreRunID = None, setModifiedTime = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDropLowScoreRunStudentAssignmentID = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDropLowScoreRunStudentAssignment(EntityID = 1, setDropLowScoreRunStudentAssignmentID = None, setCreatedTime = None, setDropActionType = None, setDropActionTypeCode = None, setDropLowScoreRunID = None, setModifiedTime = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDropLowScoreRunStudentAssignmentID = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropLowScoreRunID = False, returnModifiedTime = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDropLowScoreRunStudentAssignment(DropLowScoreRunStudentAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/DropLowScoreRunStudentAssignment/" + str(DropLowScoreRunStudentAssignmentID), verb = "delete")


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

def getGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1, returnGradesheetAssignmentSettingID = False, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "get", return_params_list = return_params)

def modifyGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1, setGradesheetAssignmentSettingID = None, setCreatedTime = None, setDefaultAttemptType = None, setDefaultAttemptTypeCode = None, setIsDateAscending = None, setMaxScoreDefault = None, setModifiedTime = None, setSortBy = None, setSortByCode = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradesheetAssignmentSettingID = False, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGradesheetAssignmentSetting(EntityID = 1, setGradesheetAssignmentSettingID = None, setCreatedTime = None, setDefaultAttemptType = None, setDefaultAttemptTypeCode = None, setIsDateAscending = None, setMaxScoreDefault = None, setModifiedTime = None, setSortBy = None, setSortByCode = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradesheetAssignmentSettingID = False, returnCreatedTime = False, returnDefaultAttemptType = False, returnDefaultAttemptTypeCode = False, returnIsDateAscending = False, returnMaxScoreDefault = False, returnModifiedTime = False, returnSortBy = False, returnSortByCode = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGradesheetAssignmentSetting(GradesheetAssignmentSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradesheetAssignmentSetting/" + str(GradesheetAssignmentSettingID), verb = "delete")


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

def getGradingScaleGroup(GradingScaleGroupID, EntityID = 1, returnGradingScaleGroupID = False, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "get", return_params_list = return_params)

def modifyGradingScaleGroup(GradingScaleGroupID, EntityID = 1, setGradingScaleGroupID = None, setCreatedTime = None, setDescription = None, setDisplayGradeMarkPercentages = None, setEntityGroupKey = None, setEntityID = None, setGradeMarkIDMastered = None, setGradingScaleGroupExistsInSpecifcEntity = None, setGradingScaleGroupIDClonedFrom = None, setGradingScaleType = None, setGradingScaleTypeCode = None, setHasAcademicStandardGradingScaleGroups = None, setHasCourseGradingScaleGroups = None, setHasSectionGradingScaleGroups = None, setHasStudentGradingScaleGroups = None, setHasSubjectGradingScaleGroups = None, setIsAHistoricRecord = None, setIsDefaultAcademicStandardGradingScaleGroup = None, setIsDefaultSubjectGradingScaleGroup = None, setIsDummySectionContainer = None, setIsPointsBasedScale = None, setIsSectionRelatedGradingScaleGroup = None, setMaxScore = None, setModifiedTime = None, setSchoolYearID = None, setSectionIDTeacherOverride = None, setUseAsMastery = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradingScaleGroupID = False, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGradingScaleGroup(EntityID = 1, setGradingScaleGroupID = None, setCreatedTime = None, setDescription = None, setDisplayGradeMarkPercentages = None, setEntityGroupKey = None, setEntityID = None, setGradeMarkIDMastered = None, setGradingScaleGroupExistsInSpecifcEntity = None, setGradingScaleGroupIDClonedFrom = None, setGradingScaleType = None, setGradingScaleTypeCode = None, setHasAcademicStandardGradingScaleGroups = None, setHasCourseGradingScaleGroups = None, setHasSectionGradingScaleGroups = None, setHasStudentGradingScaleGroups = None, setHasSubjectGradingScaleGroups = None, setIsAHistoricRecord = None, setIsDefaultAcademicStandardGradingScaleGroup = None, setIsDefaultSubjectGradingScaleGroup = None, setIsDummySectionContainer = None, setIsPointsBasedScale = None, setIsSectionRelatedGradingScaleGroup = None, setMaxScore = None, setModifiedTime = None, setSchoolYearID = None, setSectionIDTeacherOverride = None, setUseAsMastery = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradingScaleGroupID = False, returnCreatedTime = False, returnDescription = False, returnDisplayGradeMarkPercentages = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkIDMastered = False, returnGradingScaleGroupExistsInSpecifcEntity = False, returnGradingScaleGroupIDClonedFrom = False, returnGradingScaleType = False, returnGradingScaleTypeCode = False, returnHasAcademicStandardGradingScaleGroups = False, returnHasCourseGradingScaleGroups = False, returnHasSectionGradingScaleGroups = False, returnHasStudentGradingScaleGroups = False, returnHasSubjectGradingScaleGroups = False, returnIsAHistoricRecord = False, returnIsDefaultAcademicStandardGradingScaleGroup = False, returnIsDefaultSubjectGradingScaleGroup = False, returnIsDummySectionContainer = False, returnIsPointsBasedScale = False, returnIsSectionRelatedGradingScaleGroup = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionIDTeacherOverride = False, returnUseAsMastery = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGradingScaleGroup(GradingScaleGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroup/" + str(GradingScaleGroupID), verb = "delete")


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

def getGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1, returnGradingScaleGroupGradeMarkID = False, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "get", return_params_list = return_params)

def modifyGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1, setGradingScaleGroupGradeMarkID = None, setAllowSubjective = None, setColor = None, setCreatedTime = None, setDefaultCalculationPercent = None, setDefaultCalculationPoints = None, setEntityGroupKey = None, setGradeMarkID = None, setGradingScaleGroupGradeMarkIDClonedFrom = None, setGradingScaleGroupID = None, setModifiedTime = None, setPercentHigh = None, setPercentLow = None, setPointsHigh = None, setPointsLow = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradingScaleGroupGradeMarkID = False, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "post", return_params_list = return_params, payload = payload_params)

def createGradingScaleGroupGradeMark(EntityID = 1, setGradingScaleGroupGradeMarkID = None, setAllowSubjective = None, setColor = None, setCreatedTime = None, setDefaultCalculationPercent = None, setDefaultCalculationPoints = None, setEntityGroupKey = None, setGradeMarkID = None, setGradingScaleGroupGradeMarkIDClonedFrom = None, setGradingScaleGroupID = None, setModifiedTime = None, setPercentHigh = None, setPercentLow = None, setPointsHigh = None, setPointsLow = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnGradingScaleGroupGradeMarkID = False, returnAllowSubjective = False, returnColor = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultCalculationPoints = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnGradingScaleGroupGradeMarkIDClonedFrom = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnPointsHigh = False, returnPointsLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteGradingScaleGroupGradeMark(GradingScaleGroupGradeMarkID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/GradingScaleGroupGradeMark/" + str(GradingScaleGroupGradeMarkID), verb = "delete")


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

def getMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1, returnMonitorSummaryByClassID = False, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "get", return_params_list = return_params)

def modifyMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1, setMonitorSummaryByClassID = None, setAssignmentCountForTerm = None, setAssignmentCountYTD = None, setClosedGradingPeriodGradeChangeCount = None, setCreatedTime = None, setCurrentGradingPeriod = None, setExcusedAbsencesYTD = None, setFutureAssignmentCountForTerm = None, setGradedAssignmentCountForTerm = None, setLastAccessedGradebookTime = None, setLastScoredGradebookTime = None, setLastUpdatedTime = None, setMissingAssignmentCountForTerm = None, setModifiedTime = None, setNoCountAssignmentCountForTerm = None, setNonGradedAssignmentCountForTerm = None, setOffenseCountYTD = None, setOtherAbsencesYTD = None, setScoreClarifierAssignmentCountForTerm = None, setScoredAssignmentRange0CurrentTerm = None, setScoredAssignmentRange100to90CurrentTerm = None, setScoredAssignmentRange49to1CurrentTerm = None, setScoredAssignmentRange59to50CurrentTerm = None, setScoredAssignmentRange69to60CurrentTerm = None, setScoredAssignmentRange79to70CurrentTerm = None, setScoredAssignmentRange89to80CurrentTerm = None, setStaffMeetID = None, setStudentCountForTerm = None, setTardiesYTD = None, setUnexcusedAbsencesYTD = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMonitorSummaryByClassID = False, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMonitorSummaryByClass(EntityID = 1, setMonitorSummaryByClassID = None, setAssignmentCountForTerm = None, setAssignmentCountYTD = None, setClosedGradingPeriodGradeChangeCount = None, setCreatedTime = None, setCurrentGradingPeriod = None, setExcusedAbsencesYTD = None, setFutureAssignmentCountForTerm = None, setGradedAssignmentCountForTerm = None, setLastAccessedGradebookTime = None, setLastScoredGradebookTime = None, setLastUpdatedTime = None, setMissingAssignmentCountForTerm = None, setModifiedTime = None, setNoCountAssignmentCountForTerm = None, setNonGradedAssignmentCountForTerm = None, setOffenseCountYTD = None, setOtherAbsencesYTD = None, setScoreClarifierAssignmentCountForTerm = None, setScoredAssignmentRange0CurrentTerm = None, setScoredAssignmentRange100to90CurrentTerm = None, setScoredAssignmentRange49to1CurrentTerm = None, setScoredAssignmentRange59to50CurrentTerm = None, setScoredAssignmentRange69to60CurrentTerm = None, setScoredAssignmentRange79to70CurrentTerm = None, setScoredAssignmentRange89to80CurrentTerm = None, setStaffMeetID = None, setStudentCountForTerm = None, setTardiesYTD = None, setUnexcusedAbsencesYTD = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMonitorSummaryByClassID = False, returnAssignmentCountForTerm = False, returnAssignmentCountYTD = False, returnClosedGradingPeriodGradeChangeCount = False, returnCreatedTime = False, returnCurrentGradingPeriod = False, returnExcusedAbsencesYTD = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastScoredGradebookTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnOffenseCountYTD = False, returnOtherAbsencesYTD = False, returnScoreClarifierAssignmentCountForTerm = False, returnScoredAssignmentRange0CurrentTerm = False, returnScoredAssignmentRange100to90CurrentTerm = False, returnScoredAssignmentRange49to1CurrentTerm = False, returnScoredAssignmentRange59to50CurrentTerm = False, returnScoredAssignmentRange69to60CurrentTerm = False, returnScoredAssignmentRange79to70CurrentTerm = False, returnScoredAssignmentRange89to80CurrentTerm = False, returnStaffMeetID = False, returnStudentCountForTerm = False, returnTardiesYTD = False, returnUnexcusedAbsencesYTD = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMonitorSummaryByClass(MonitorSummaryByClassID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByClass/" + str(MonitorSummaryByClassID), verb = "delete")


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

def getMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1, returnMonitorSummaryByTeacherID = False, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "get", return_params_list = return_params)

def modifyMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1, setMonitorSummaryByTeacherID = None, setActiveStudentCount = None, setAssignmentCountForTerm = None, setCreatedTime = None, setFutureAssignmentCountForTerm = None, setGradedAssignmentCountForTerm = None, setLastAccessedGradebookTime = None, setLastAssignmentScoredDueDate = None, setLastScoredAssignmentTime = None, setLastUpdatedTime = None, setMissingAssignmentCountForTerm = None, setModifiedTime = None, setNoCountAssignmentCountForTerm = None, setNonGradedAssignmentCountForTerm = None, setNonGradedAssignmentCountNoStudentAssignmentsForTerm = None, setSchoolYearID = None, setScoreClarifierAssignmentCountForTerm = None, setStaffID = None, setStaffMeetCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMonitorSummaryByTeacherID = False, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMonitorSummaryByTeacher(EntityID = 1, setMonitorSummaryByTeacherID = None, setActiveStudentCount = None, setAssignmentCountForTerm = None, setCreatedTime = None, setFutureAssignmentCountForTerm = None, setGradedAssignmentCountForTerm = None, setLastAccessedGradebookTime = None, setLastAssignmentScoredDueDate = None, setLastScoredAssignmentTime = None, setLastUpdatedTime = None, setMissingAssignmentCountForTerm = None, setModifiedTime = None, setNoCountAssignmentCountForTerm = None, setNonGradedAssignmentCountForTerm = None, setNonGradedAssignmentCountNoStudentAssignmentsForTerm = None, setSchoolYearID = None, setScoreClarifierAssignmentCountForTerm = None, setStaffID = None, setStaffMeetCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMonitorSummaryByTeacherID = False, returnActiveStudentCount = False, returnAssignmentCountForTerm = False, returnCreatedTime = False, returnFutureAssignmentCountForTerm = False, returnGradedAssignmentCountForTerm = False, returnLastAccessedGradebookTime = False, returnLastAssignmentScoredDueDate = False, returnLastScoredAssignmentTime = False, returnLastUpdatedTime = False, returnMissingAssignmentCountForTerm = False, returnModifiedTime = False, returnNoCountAssignmentCountForTerm = False, returnNonGradedAssignmentCountForTerm = False, returnNonGradedAssignmentCountNoStudentAssignmentsForTerm = False, returnSchoolYearID = False, returnScoreClarifierAssignmentCountForTerm = False, returnStaffID = False, returnStaffMeetCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMonitorSummaryByTeacher(MonitorSummaryByTeacherID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/MonitorSummaryByTeacher/" + str(MonitorSummaryByTeacherID), verb = "delete")


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

def getQuestion(QuestionID, EntityID = 1, returnQuestionID = False, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "get", return_params_list = return_params)

def modifyQuestion(QuestionID, EntityID = 1, setQuestionID = None, setAllowStudentAttachments = None, setAssignmentCount = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setDescription = None, setHasAssignmentPastEndTime = None, setHasAutoScoredAssignment = None, setHasInstructions = None, setHasMultipleAssignments = None, setHasQuestionMedias = None, setInstructions = None, setIsEssay = None, setIsMatching = None, setIsMultipleChoice = None, setIsShortAnswer = None, setIsTrueFalse = None, setModifiedTime = None, setStaffID = None, setType = None, setTypeCode = None, setUseAnswers = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQuestionID = False, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQuestion(EntityID = 1, setQuestionID = None, setAllowStudentAttachments = None, setAssignmentCount = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setDescription = None, setHasAssignmentPastEndTime = None, setHasAutoScoredAssignment = None, setHasInstructions = None, setHasMultipleAssignments = None, setHasQuestionMedias = None, setInstructions = None, setIsEssay = None, setIsMatching = None, setIsMultipleChoice = None, setIsShortAnswer = None, setIsTrueFalse = None, setModifiedTime = None, setStaffID = None, setType = None, setTypeCode = None, setUseAnswers = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQuestionID = False, returnAllowStudentAttachments = False, returnAssignmentCount = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnHasAssignmentPastEndTime = False, returnHasAutoScoredAssignment = False, returnHasInstructions = False, returnHasMultipleAssignments = False, returnHasQuestionMedias = False, returnInstructions = False, returnIsEssay = False, returnIsMatching = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnStaffID = False, returnType = False, returnTypeCode = False, returnUseAnswers = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQuestion(QuestionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/Question/" + str(QuestionID), verb = "delete")


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

def getQuestionAnswer(QuestionAnswerID, EntityID = 1, returnQuestionAnswerID = False, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedChoiceMediaSafe = False, returnHasAttachedMedia = False, returnHasAttachedMediaSafe = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "get", return_params_list = return_params)

def modifyQuestionAnswer(QuestionAnswerID, EntityID = 1, setQuestionAnswerID = None, setChoice = None, setChoiceOrder = None, setCreatedTime = None, setHasAttachedChoiceMedia = None, setHasAttachedChoiceMediaSafe = None, setHasAttachedMedia = None, setHasAttachedMediaSafe = None, setIsCorrect = None, setIsEssay = None, setIsMultipleChoice = None, setIsShortAnswer = None, setIsTrueFalse = None, setModifiedTime = None, setQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, setValueOrder = None, returnQuestionAnswerID = False, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedChoiceMediaSafe = False, returnHasAttachedMedia = False, returnHasAttachedMediaSafe = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQuestionAnswer(EntityID = 1, setQuestionAnswerID = None, setChoice = None, setChoiceOrder = None, setCreatedTime = None, setHasAttachedChoiceMedia = None, setHasAttachedChoiceMediaSafe = None, setHasAttachedMedia = None, setHasAttachedMediaSafe = None, setIsCorrect = None, setIsEssay = None, setIsMultipleChoice = None, setIsShortAnswer = None, setIsTrueFalse = None, setModifiedTime = None, setQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, setValueOrder = None, returnQuestionAnswerID = False, returnChoice = False, returnChoiceOrder = False, returnCreatedTime = False, returnHasAttachedChoiceMedia = False, returnHasAttachedChoiceMediaSafe = False, returnHasAttachedMedia = False, returnHasAttachedMediaSafe = False, returnIsCorrect = False, returnIsEssay = False, returnIsMultipleChoice = False, returnIsShortAnswer = False, returnIsTrueFalse = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueOrder = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQuestionAnswer(QuestionAnswerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswer/" + str(QuestionAnswerID), verb = "delete")


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

def getQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1, returnQuestionAnswerMediaID = False, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "get", return_params_list = return_params)

def modifyQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1, setQuestionAnswerMediaID = None, setCreatedTime = None, setDisplayFor = None, setDisplayForCode = None, setMediaID = None, setModifiedTime = None, setQuestionAnswerID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQuestionAnswerMediaID = False, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQuestionAnswerMedia(EntityID = 1, setQuestionAnswerMediaID = None, setCreatedTime = None, setDisplayFor = None, setDisplayForCode = None, setMediaID = None, setModifiedTime = None, setQuestionAnswerID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQuestionAnswerMediaID = False, returnCreatedTime = False, returnDisplayFor = False, returnDisplayForCode = False, returnMediaID = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQuestionAnswerMedia(QuestionAnswerMediaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionAnswerMedia/" + str(QuestionAnswerMediaID), verb = "delete")


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

def getQuestionMedia(QuestionMediaID, EntityID = 1, returnQuestionMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "get", return_params_list = return_params)

def modifyQuestionMedia(QuestionMediaID, EntityID = 1, setQuestionMediaID = None, setCreatedTime = None, setMediaID = None, setModifiedTime = None, setQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQuestionMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQuestionMedia(EntityID = 1, setQuestionMediaID = None, setCreatedTime = None, setMediaID = None, setModifiedTime = None, setQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQuestionMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQuestionMedia(QuestionMediaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/QuestionMedia/" + str(QuestionMediaID), verb = "delete")


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

def getScoreClarifier(ScoreClarifierID, EntityID = 1, returnScoreClarifierID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "get", return_params_list = return_params)

def modifyScoreClarifier(ScoreClarifierID, EntityID = 1, setScoreClarifierID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIsAHistoricRecord = None, setIsMissing = None, setModifiedTime = None, setNoCount = None, setSchoolYearID = None, setScoreClarifierIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScoreClarifierID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScoreClarifier(EntityID = 1, setScoreClarifierID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIsAHistoricRecord = None, setIsMissing = None, setModifiedTime = None, setNoCount = None, setSchoolYearID = None, setScoreClarifierIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScoreClarifierID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIsAHistoricRecord = False, returnIsMissing = False, returnModifiedTime = False, returnNoCount = False, returnSchoolYearID = False, returnScoreClarifierIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScoreClarifier(ScoreClarifierID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/ScoreClarifier/" + str(ScoreClarifierID), verb = "delete")


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

def getSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1, returnSectionAcademicStandardWeightID = False, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "get", return_params_list = return_params)

def modifySectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1, setSectionAcademicStandardWeightID = None, setAcademicStandardID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCreatedTime = None, setHasAssignments = None, setModifiedTime = None, setSectionGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionAcademicStandardWeightID = False, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionAcademicStandardWeight(EntityID = 1, setSectionAcademicStandardWeightID = None, setAcademicStandardID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCreatedTime = None, setHasAssignments = None, setModifiedTime = None, setSectionGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionAcademicStandardWeightID = False, returnAcademicStandardID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionAcademicStandardWeight(SectionAcademicStandardWeightID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionAcademicStandardWeight/" + str(SectionAcademicStandardWeightID), verb = "delete")


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

def getSectionCategory(SectionCategoryID, EntityID = 1, returnSectionCategoryID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "get", return_params_list = return_params)

def modifySectionCategory(SectionCategoryID, EntityID = 1, setSectionCategoryID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCategoryID = None, setCreatedTime = None, setHasAssignments = None, setModifiedTime = None, setPercentEarnedForCategory = None, setPointsEarnedForCategory = None, setSectionGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionCategoryID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionCategory(EntityID = 1, setSectionCategoryID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCategoryID = None, setCreatedTime = None, setHasAssignments = None, setModifiedTime = None, setPercentEarnedForCategory = None, setPointsEarnedForCategory = None, setSectionGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionCategoryID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCategoryID = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnPercentEarnedForCategory = False, returnPointsEarnedForCategory = False, returnSectionGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionCategory(SectionCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionCategory/" + str(SectionCategoryID), verb = "delete")


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

def getSectionGradeBucket(SectionGradeBucketID, EntityID = 1, returnSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "get", return_params_list = return_params)

def modifySectionGradeBucket(SectionGradeBucketID, EntityID = 1, setSectionGradeBucketID = None, setCalculationGroupGradeBucketID = None, setCalculationModifiedTime = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setEffectiveCalculationType = None, setEffectiveCalculationTypeCode = None, setHasSectionAcademicStandardWeights = None, setHasSectionCategories = None, setHasSectionGradeBucketWeights = None, setHasSectionSubjectWeights = None, setIsAHistoricRecord = None, setIsCalculationTypeOverridden = None, setIsOverridden = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionGradeBucket(EntityID = 1, setSectionGradeBucketID = None, setCalculationGroupGradeBucketID = None, setCalculationModifiedTime = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setEffectiveCalculationType = None, setEffectiveCalculationTypeCode = None, setHasSectionAcademicStandardWeights = None, setHasSectionCategories = None, setHasSectionGradeBucketWeights = None, setHasSectionSubjectWeights = None, setIsAHistoricRecord = None, setIsCalculationTypeOverridden = None, setIsOverridden = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCalculationModifiedTime = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnEffectiveCalculationType = False, returnEffectiveCalculationTypeCode = False, returnHasSectionAcademicStandardWeights = False, returnHasSectionCategories = False, returnHasSectionGradeBucketWeights = False, returnHasSectionSubjectWeights = False, returnIsAHistoricRecord = False, returnIsCalculationTypeOverridden = False, returnIsOverridden = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionGradeBucket(SectionGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucket/" + str(SectionGradeBucketID), verb = "delete")


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

def getSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1, returnSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "get", return_params_list = return_params)

def modifySectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1, setSectionGradeBucketSettingID = None, setCreatedTime = None, setGradingPeriodGradeBucketID = None, setMaxExtraCredit = None, setModifiedTime = None, setSectionID = None, setUseMaxExtraCredit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionGradeBucketSetting(EntityID = 1, setSectionGradeBucketSettingID = None, setCreatedTime = None, setGradingPeriodGradeBucketID = None, setMaxExtraCredit = None, setModifiedTime = None, setSectionID = None, setUseMaxExtraCredit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnSectionID = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionGradeBucketSetting(SectionGradeBucketSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketSetting/" + str(SectionGradeBucketSettingID), verb = "delete")


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

def getSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1, returnSectionGradeBucketWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "get", return_params_list = return_params)

def modifySectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1, setSectionGradeBucketWeightID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCreatedTime = None, setModifiedTime = None, setRoundBucketPercent = None, setSectionGradeBucketIDComposite = None, setSectionGradeBucketIDFeeder = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionGradeBucketWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionGradeBucketWeight(EntityID = 1, setSectionGradeBucketWeightID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCreatedTime = None, setModifiedTime = None, setRoundBucketPercent = None, setSectionGradeBucketIDComposite = None, setSectionGradeBucketIDFeeder = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionGradeBucketWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnModifiedTime = False, returnRoundBucketPercent = False, returnSectionGradeBucketIDComposite = False, returnSectionGradeBucketIDFeeder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionGradeBucketWeight(SectionGradeBucketWeightID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradeBucketWeight/" + str(SectionGradeBucketWeightID), verb = "delete")


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

def getSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1, returnSectionGradingPeriodDataID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "get", return_params_list = return_params)

def modifySectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1, setSectionGradingPeriodDataID = None, setCreatedTime = None, setGradingPeriodID = None, setIsCompleted = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradingPeriodDataID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionGradingPeriodData(EntityID = 1, setSectionGradingPeriodDataID = None, setCreatedTime = None, setGradingPeriodID = None, setIsCompleted = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradingPeriodDataID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIsCompleted = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionGradingPeriodData(SectionGradingPeriodDataID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingPeriodData/" + str(SectionGradingPeriodDataID), verb = "delete")


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

def getSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1, returnSectionGradingScaleGroupID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "get", return_params_list = return_params)

def modifySectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1, setSectionGradingScaleGroupID = None, setCreatedTime = None, setGradingPeriodGradeBucketID = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setModifiedTime = None, setSectionGradingScaleGroupIDClonedFrom = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradingScaleGroupID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionGradingScaleGroup(EntityID = 1, setSectionGradingScaleGroupID = None, setCreatedTime = None, setGradingPeriodGradeBucketID = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setModifiedTime = None, setSectionGradingScaleGroupIDClonedFrom = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSectionGradingScaleGroupID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSectionGradingScaleGroupIDClonedFrom = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionGradingScaleGroup(SectionGradingScaleGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionGradingScaleGroup/" + str(SectionGradingScaleGroupID), verb = "delete")


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

def getSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1, returnSectionSubjectWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "get", return_params_list = return_params)

def modifySectionSubjectWeight(SectionSubjectWeightID, EntityID = 1, setSectionSubjectWeightID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCreatedTime = None, setHasAssignments = None, setModifiedTime = None, setSectionGradeBucketID = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionSubjectWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSectionSubjectWeight(EntityID = 1, setSectionSubjectWeightID = None, setAdjustedPercentEarned = None, setAdjustedPointsEarned = None, setAdjustedWeightPercent = None, setCreatedTime = None, setHasAssignments = None, setModifiedTime = None, setSectionGradeBucketID = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightFormula = None, setWeightPercent = None, returnSectionSubjectWeightID = False, returnAdjustedPercentEarned = False, returnAdjustedPointsEarned = False, returnAdjustedWeightPercent = False, returnCreatedTime = False, returnHasAssignments = False, returnModifiedTime = False, returnSectionGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightFormula = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSectionSubjectWeight(SectionSubjectWeightID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SectionSubjectWeight/" + str(SectionSubjectWeightID), verb = "delete")


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

def getStaffMeetLastScored(StaffMeetLastScoredID, EntityID = 1, returnStaffMeetLastScoredID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentAssignmentIDLastScored = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StaffMeetLastScored/" + str(StaffMeetLastScoredID), verb = "get", return_params_list = return_params)

def modifyStaffMeetLastScored(StaffMeetLastScoredID, EntityID = 1, setStaffMeetLastScoredID = None, setCreatedTime = None, setModifiedTime = None, setStaffMeetID = None, setStudentAssignmentIDLastScored = None, setTimeLastScored = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffMeetLastScoredID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentAssignmentIDLastScored = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StaffMeetLastScored/" + str(StaffMeetLastScoredID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaffMeetLastScored(EntityID = 1, setStaffMeetLastScoredID = None, setCreatedTime = None, setModifiedTime = None, setStaffMeetID = None, setStudentAssignmentIDLastScored = None, setTimeLastScored = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffMeetLastScoredID = False, returnCreatedTime = False, returnModifiedTime = False, returnStaffMeetID = False, returnStudentAssignmentIDLastScored = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StaffMeetLastScored/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaffMeetLastScored(StaffMeetLastScoredID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StaffMeetLastScored/" + str(StaffMeetLastScoredID), verb = "delete")


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

def getStudentAnswer(StudentAnswerID, EntityID = 1, returnStudentAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "get", return_params_list = return_params)

def modifyStudentAnswer(StudentAnswerID, EntityID = 1, setStudentAnswerID = None, setCreatedTime = None, setModifiedTime = None, setQuestionAnswerID = None, setStudentQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnStudentAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAnswer(EntityID = 1, setStudentAnswerID = None, setCreatedTime = None, setModifiedTime = None, setQuestionAnswerID = None, setStudentQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnStudentAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnQuestionAnswerID = False, returnStudentQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAnswer(StudentAnswerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAnswer/" + str(StudentAnswerID), verb = "delete")


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

def getStudentAssignment(StudentAssignmentID, EntityID = 1, returnStudentAssignmentID = False, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "get", return_params_list = return_params)

def modifyStudentAssignment(StudentAssignmentID, EntityID = 1, setStudentAssignmentID = None, setAllQuestionsScored = None, setAnsweredQuestionCount = None, setAnswerKeyIsAvailableAndAssignmentIsScored = None, setAnswerKeyIsAvailableToView = None, setAssignmentDueDateAttendance = None, setAssignmentID = None, setAttemptCount = None, setCalculatedPoints = None, setCannotBeTakenByStudent = None, setComments = None, setCreatedTime = None, setCurrentQuestionNumber = None, setFormattedPointsEarnedPercent = None, setFormattedPointsEarnedPercentCheckDisplay = None, setGradeMarkCode = None, setGradeMarkID = None, setHasAnswers = None, setHasStudentSectionTransaction = None, setIsDropped = None, setIsExpired = None, setIsFutureRetainedScore = None, setIsGraded = None, setIsMissing = None, setIsMissingHasChangedWithinSpecifiedAmountOfTime = None, setIsScored = None, setIsTransferredScore = None, setModifiedTime = None, setNoCount = None, setOnlineAssignmentNotificationSent = None, setOnlineAssignmentReviewNotificationSent = None, setPointsEarned = None, setPointsEarnedPercent = None, setPointsEarnedWithSlash = None, setPointsEarnedWithSlashCheckDisplay = None, setScore = None, setScoreClarifierID = None, setScoreDisplayValue = None, setScoreDisplayValueNoGradeMark = None, setScoreHasChangedWithinSpecifiedAmountOfTime = None, setSectionID = None, setStudentOnlineAssignmentDisplayPointsEarned = None, setStudentOnlineAssignmentDisplayPointsEarnedWithSlash = None, setStudentQuestionCount = None, setStudentSectionID = None, setSubmissionStatus = None, setSubmissionStatusCode = None, setSubmissionStatusCodeToUse = None, setSubmissionStatusToUse = None, setSubmissionTime = None, setTimeLastScored = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAssignmentID = False, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAssignment(EntityID = 1, setStudentAssignmentID = None, setAllQuestionsScored = None, setAnsweredQuestionCount = None, setAnswerKeyIsAvailableAndAssignmentIsScored = None, setAnswerKeyIsAvailableToView = None, setAssignmentDueDateAttendance = None, setAssignmentID = None, setAttemptCount = None, setCalculatedPoints = None, setCannotBeTakenByStudent = None, setComments = None, setCreatedTime = None, setCurrentQuestionNumber = None, setFormattedPointsEarnedPercent = None, setFormattedPointsEarnedPercentCheckDisplay = None, setGradeMarkCode = None, setGradeMarkID = None, setHasAnswers = None, setHasStudentSectionTransaction = None, setIsDropped = None, setIsExpired = None, setIsFutureRetainedScore = None, setIsGraded = None, setIsMissing = None, setIsMissingHasChangedWithinSpecifiedAmountOfTime = None, setIsScored = None, setIsTransferredScore = None, setModifiedTime = None, setNoCount = None, setOnlineAssignmentNotificationSent = None, setOnlineAssignmentReviewNotificationSent = None, setPointsEarned = None, setPointsEarnedPercent = None, setPointsEarnedWithSlash = None, setPointsEarnedWithSlashCheckDisplay = None, setScore = None, setScoreClarifierID = None, setScoreDisplayValue = None, setScoreDisplayValueNoGradeMark = None, setScoreHasChangedWithinSpecifiedAmountOfTime = None, setSectionID = None, setStudentOnlineAssignmentDisplayPointsEarned = None, setStudentOnlineAssignmentDisplayPointsEarnedWithSlash = None, setStudentQuestionCount = None, setStudentSectionID = None, setSubmissionStatus = None, setSubmissionStatusCode = None, setSubmissionStatusCodeToUse = None, setSubmissionStatusToUse = None, setSubmissionTime = None, setTimeLastScored = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAssignmentID = False, returnAllQuestionsScored = False, returnAnsweredQuestionCount = False, returnAnswerKeyIsAvailableAndAssignmentIsScored = False, returnAnswerKeyIsAvailableToView = False, returnAssignmentDueDateAttendance = False, returnAssignmentID = False, returnAttemptCount = False, returnCalculatedPoints = False, returnCannotBeTakenByStudent = False, returnComments = False, returnCreatedTime = False, returnCurrentQuestionNumber = False, returnFormattedPointsEarnedPercent = False, returnFormattedPointsEarnedPercentCheckDisplay = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnHasAnswers = False, returnHasStudentSectionTransaction = False, returnIsDropped = False, returnIsExpired = False, returnIsFutureRetainedScore = False, returnIsGraded = False, returnIsMissing = False, returnIsMissingHasChangedWithinSpecifiedAmountOfTime = False, returnIsScored = False, returnIsTransferredScore = False, returnModifiedTime = False, returnNoCount = False, returnOnlineAssignmentNotificationSent = False, returnOnlineAssignmentReviewNotificationSent = False, returnPointsEarned = False, returnPointsEarnedPercent = False, returnPointsEarnedWithSlash = False, returnPointsEarnedWithSlashCheckDisplay = False, returnScore = False, returnScoreClarifierID = False, returnScoreDisplayValue = False, returnScoreDisplayValueNoGradeMark = False, returnScoreHasChangedWithinSpecifiedAmountOfTime = False, returnSectionID = False, returnStudentOnlineAssignmentDisplayPointsEarned = False, returnStudentOnlineAssignmentDisplayPointsEarnedWithSlash = False, returnStudentQuestionCount = False, returnStudentSectionID = False, returnSubmissionStatus = False, returnSubmissionStatusCode = False, returnSubmissionStatusCodeToUse = False, returnSubmissionStatusToUse = False, returnSubmissionTime = False, returnTimeLastScored = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAssignment(StudentAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignment/" + str(StudentAssignmentID), verb = "delete")


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

def getStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1, returnStudentAssignmentAttemptID = False, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "get", return_params_list = return_params)

def modifyStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1, setStudentAssignmentAttemptID = None, setComments = None, setCreatedTime = None, setDateAttempted = None, setGradeMarkID = None, setIsUsed = None, setModifiedTime = None, setScore = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAssignmentAttemptID = False, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentAssignmentAttempt(EntityID = 1, setStudentAssignmentAttemptID = None, setComments = None, setCreatedTime = None, setDateAttempted = None, setGradeMarkID = None, setIsUsed = None, setModifiedTime = None, setScore = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentAssignmentAttemptID = False, returnComments = False, returnCreatedTime = False, returnDateAttempted = False, returnGradeMarkID = False, returnIsUsed = False, returnModifiedTime = False, returnScore = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentAssignmentAttempt(StudentAssignmentAttemptID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentAssignmentAttempt/" + str(StudentAssignmentAttemptID), verb = "delete")


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

def getStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1, returnStudentGradeBucketAcademicStandardID = False, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "get", return_params_list = return_params)

def modifyStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1, setStudentGradeBucketAcademicStandardID = None, setAcademicStandardID = None, setCalculatedPoints = None, setCreatedTime = None, setEarnedPoints = None, setGradeMarkExists = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setModifiedTime = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentFormatted = None, setPercentWithAdjustment = None, setPercentWithAdjustmentFormatted = None, setPercentWithAdjustmentWithGradeMarkToUse = None, setPercentWithGradeMark = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradeBucketAcademicStandardID = False, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGradeBucketAcademicStandard(EntityID = 1, setStudentGradeBucketAcademicStandardID = None, setAcademicStandardID = None, setCalculatedPoints = None, setCreatedTime = None, setEarnedPoints = None, setGradeMarkExists = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setModifiedTime = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentFormatted = None, setPercentWithAdjustment = None, setPercentWithAdjustmentFormatted = None, setPercentWithAdjustmentWithGradeMarkToUse = None, setPercentWithGradeMark = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradeBucketAcademicStandardID = False, returnAcademicStandardID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGradeBucketAcademicStandard(StudentGradeBucketAcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketAcademicStandard/" + str(StudentGradeBucketAcademicStandardID), verb = "delete")


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

def getStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1, returnStudentGradeBucketSubjectID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "get", return_params_list = return_params)

def modifyStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1, setStudentGradeBucketSubjectID = None, setCalculatedPoints = None, setCreatedTime = None, setEarnedPoints = None, setGradeMarkExists = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setModifiedTime = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentFormatted = None, setPercentWithAdjustment = None, setPercentWithAdjustmentFormatted = None, setPercentWithAdjustmentWithGradeMarkToUse = None, setPercentWithGradeMark = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradeBucketSubjectID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGradeBucketSubject(EntityID = 1, setStudentGradeBucketSubjectID = None, setCalculatedPoints = None, setCreatedTime = None, setEarnedPoints = None, setGradeMarkExists = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setIsAdminOverride = None, setIsUsingPointsBasedScale = None, setModifiedTime = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentFormatted = None, setPercentWithAdjustment = None, setPercentWithAdjustmentFormatted = None, setPercentWithAdjustmentWithGradeMarkToUse = None, setPercentWithGradeMark = None, setPossiblePoints = None, setSectionID = None, setStudentGradeBucketID = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradeBucketSubjectID = False, returnCalculatedPoints = False, returnCreatedTime = False, returnEarnedPoints = False, returnGradeMarkExists = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnIsAdminOverride = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentFormatted = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithGradeMark = False, returnPossiblePoints = False, returnSectionID = False, returnStudentGradeBucketID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGradeBucketSubject(StudentGradeBucketSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradeBucketSubject/" + str(StudentGradeBucketSubjectID), verb = "delete")


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

def getStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1, returnStudentGradingScaleGroupID = False, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "get", return_params_list = return_params)

def modifyStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1, setStudentGradingScaleGroupID = None, setAllowTeachersToModify = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setGradingScaleGroupID = None, setHasAttachedStudentSections = None, setIsAHistoricRecord = None, setModifiedTime = None, setSchoolYearID = None, setStudentGradingScaleGroupIDClonedFrom = None, setStudentGradingScaleGroupStudentSectionCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradingScaleGroupID = False, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGradingScaleGroup(EntityID = 1, setStudentGradingScaleGroupID = None, setAllowTeachersToModify = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setGradingScaleGroupID = None, setHasAttachedStudentSections = None, setIsAHistoricRecord = None, setModifiedTime = None, setSchoolYearID = None, setStudentGradingScaleGroupIDClonedFrom = None, setStudentGradingScaleGroupStudentSectionCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradingScaleGroupID = False, returnAllowTeachersToModify = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnGradingScaleGroupID = False, returnHasAttachedStudentSections = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGradingScaleGroupIDClonedFrom = False, returnStudentGradingScaleGroupStudentSectionCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGradingScaleGroup(StudentGradingScaleGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroup/" + str(StudentGradingScaleGroupID), verb = "delete")


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

def getStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1, returnStudentGradingScaleGroupStudentSectionID = False, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "get", return_params_list = return_params)

def modifyStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1, setStudentGradingScaleGroupStudentSectionID = None, setCreatedTime = None, setGradeBuckets = None, setIsAHistoricRecord = None, setModifiedTime = None, setStudentGradingScaleGroupID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradingScaleGroupStudentSectionID = False, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGradingScaleGroupStudentSection(EntityID = 1, setStudentGradingScaleGroupStudentSectionID = None, setCreatedTime = None, setGradeBuckets = None, setIsAHistoricRecord = None, setModifiedTime = None, setStudentGradingScaleGroupID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGradingScaleGroupStudentSectionID = False, returnCreatedTime = False, returnGradeBuckets = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnStudentGradingScaleGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGradingScaleGroupStudentSection(StudentGradingScaleGroupStudentSectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGradingScaleGroupStudentSection/" + str(StudentGradingScaleGroupStudentSectionID), verb = "delete")


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

def getStudentGroup(StudentGroupID, EntityID = 1, returnStudentGroupID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "get", return_params_list = return_params)

def modifyStudentGroup(StudentGroupID, EntityID = 1, setStudentGroupID = None, setAssignmentCount = None, setCanBeDeleted = None, setCreatedTime = None, setEndDate = None, setIsActive = None, setIsAHistoricRecord = None, setModifiedTime = None, setName = None, setSectionID = None, setStartDate = None, setStudentCount = None, setStudentGroupSyncKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGroup(EntityID = 1, setStudentGroupID = None, setAssignmentCount = None, setCanBeDeleted = None, setCreatedTime = None, setEndDate = None, setIsActive = None, setIsAHistoricRecord = None, setModifiedTime = None, setName = None, setSectionID = None, setStartDate = None, setStudentCount = None, setStudentGroupSyncKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnName = False, returnSectionID = False, returnStartDate = False, returnStudentCount = False, returnStudentGroupSyncKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGroup(StudentGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroup/" + str(StudentGroupID), verb = "delete")


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

def getStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1, returnStudentGroupAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "get", return_params_list = return_params)

def modifyStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1, setStudentGroupAssignmentID = None, setAssignmentID = None, setCreatedTime = None, setDeleteErrorMessage = None, setModifiedTime = None, setStudentGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGroupAssignment(EntityID = 1, setStudentGroupAssignmentID = None, setAssignmentID = None, setCreatedTime = None, setDeleteErrorMessage = None, setModifiedTime = None, setStudentGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnDeleteErrorMessage = False, returnModifiedTime = False, returnStudentGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGroupAssignment(StudentGroupAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupAssignment/" + str(StudentGroupAssignmentID), verb = "delete")


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

def getStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1, returnStudentGroupStudentSectionID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "get", return_params_list = return_params)

def modifyStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1, setStudentGroupStudentSectionID = None, setAssignmentCount = None, setCanBeDeleted = None, setCreatedTime = None, setEndDate = None, setIsActive = None, setModifiedTime = None, setScoredAssignmentCount = None, setStartDate = None, setStudentGroupID = None, setStudentSectionID = None, setUnableToDeleteMessage = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupStudentSectionID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGroupStudentSection(EntityID = 1, setStudentGroupStudentSectionID = None, setAssignmentCount = None, setCanBeDeleted = None, setCreatedTime = None, setEndDate = None, setIsActive = None, setModifiedTime = None, setScoredAssignmentCount = None, setStartDate = None, setStudentGroupID = None, setStudentSectionID = None, setUnableToDeleteMessage = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupStudentSectionID = False, returnAssignmentCount = False, returnCanBeDeleted = False, returnCreatedTime = False, returnEndDate = False, returnIsActive = False, returnModifiedTime = False, returnScoredAssignmentCount = False, returnStartDate = False, returnStudentGroupID = False, returnStudentSectionID = False, returnUnableToDeleteMessage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGroupStudentSection(StudentGroupStudentSectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupStudentSection/" + str(StudentGroupStudentSectionID), verb = "delete")


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

def getStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1, returnStudentGroupTeacherSectionSettingID = False, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "get", return_params_list = return_params)

def modifyStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1, setStudentGroupTeacherSectionSettingID = None, setColor = None, setCreatedTime = None, setDisplay = None, setModifiedTime = None, setStudentGroupID = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupTeacherSectionSettingID = False, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentGroupTeacherSectionSetting(EntityID = 1, setStudentGroupTeacherSectionSettingID = None, setColor = None, setCreatedTime = None, setDisplay = None, setModifiedTime = None, setStudentGroupID = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentGroupTeacherSectionSettingID = False, returnColor = False, returnCreatedTime = False, returnDisplay = False, returnModifiedTime = False, returnStudentGroupID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentGroupTeacherSectionSetting(StudentGroupTeacherSectionSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentGroupTeacherSectionSetting/" + str(StudentGroupTeacherSectionSettingID), verb = "delete")


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

def getStudentQuestion(StudentQuestionID, EntityID = 1, returnStudentQuestionID = False, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "get", return_params_list = return_params)

def modifyStudentQuestion(StudentQuestionID, EntityID = 1, setStudentQuestionID = None, setAssignmentQuestionID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setModifiedTime = None, setOrder = None, setScore = None, setStatus = None, setStatusCode = None, setStatusStudentDisplay = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentQuestionID = False, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentQuestion(EntityID = 1, setStudentQuestionID = None, setAssignmentQuestionID = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCreatedTime = None, setModifiedTime = None, setOrder = None, setScore = None, setStatus = None, setStatusCode = None, setStatusStudentDisplay = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentQuestionID = False, returnAssignmentQuestionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnScore = False, returnStatus = False, returnStatusCode = False, returnStatusStudentDisplay = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentQuestion(StudentQuestionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentQuestion/" + str(StudentQuestionID), verb = "delete")


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

def getStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1, returnStudentSectionGradingScaleGradeBucketID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "get", return_params_list = return_params)

def modifyStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1, setStudentSectionGradingScaleGradeBucketID = None, setCreatedTime = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setStudentGradingScaleGroupStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSectionGradingScaleGradeBucketID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentSectionGradingScaleGradeBucket(EntityID = 1, setStudentSectionGradingScaleGradeBucketID = None, setCreatedTime = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setStudentGradingScaleGroupStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSectionGradingScaleGradeBucketID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnStudentGradingScaleGroupStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentSectionGradingScaleGradeBucket(StudentSectionGradingScaleGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionGradingScaleGradeBucket/" + str(StudentSectionGradingScaleGradeBucketID), verb = "delete")


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

def getStudentSectionNote(StudentSectionNoteID, EntityID = 1, returnStudentSectionNoteID = False, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "get", return_params_list = return_params)

def modifyStudentSectionNote(StudentSectionNoteID, EntityID = 1, setStudentSectionNoteID = None, setCreatedTime = None, setCurrentUserCanModify = None, setLimitToThisSection = None, setModifiedTime = None, setNote = None, setOtherTeachersHaveAccess = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSectionNoteID = False, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentSectionNote(EntityID = 1, setStudentSectionNoteID = None, setCreatedTime = None, setCurrentUserCanModify = None, setLimitToThisSection = None, setModifiedTime = None, setNote = None, setOtherTeachersHaveAccess = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSectionNoteID = False, returnCreatedTime = False, returnCurrentUserCanModify = False, returnLimitToThisSection = False, returnModifiedTime = False, returnNote = False, returnOtherTeachersHaveAccess = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentSectionNote(StudentSectionNoteID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/StudentSectionNote/" + str(StudentSectionNoteID), verb = "delete")


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

def getSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1, returnSubjectGradingScaleGroupID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "get", return_params_list = return_params)

def modifySubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1, setSubjectGradingScaleGroupID = None, setCalculationGroupID = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setModifiedTime = None, setSubjectCount = None, setSubjectGradingScaleGroupIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectGradingScaleGroupID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubjectGradingScaleGroup(EntityID = 1, setSubjectGradingScaleGroupID = None, setCalculationGroupID = None, setCreatedTime = None, setDescription = None, setEntityGroupKey = None, setGradingScaleGroupID = None, setIsAHistoricRecord = None, setIsDefaultGroup = None, setModifiedTime = None, setSubjectCount = None, setSubjectGradingScaleGroupIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectGradingScaleGroupID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingScaleGroupID = False, returnIsAHistoricRecord = False, returnIsDefaultGroup = False, returnModifiedTime = False, returnSubjectCount = False, returnSubjectGradingScaleGroupIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubjectGradingScaleGroup(SubjectGradingScaleGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroup/" + str(SubjectGradingScaleGroupID), verb = "delete")


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

def getSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1, returnSubjectGradingScaleGroupSubjectID = False, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "get", return_params_list = return_params)

def modifySubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1, setSubjectGradingScaleGroupSubjectID = None, setCalculationGroupSubjectID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setSubjectGradingScaleGroupID = None, setSubjectGradingScaleGroupSubjectIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectGradingScaleGroupSubjectID = False, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubjectGradingScaleGroupSubject(EntityID = 1, setSubjectGradingScaleGroupSubjectID = None, setCalculationGroupSubjectID = None, setCreatedTime = None, setEntityGroupKey = None, setModifiedTime = None, setSubjectGradingScaleGroupID = None, setSubjectGradingScaleGroupSubjectIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectGradingScaleGroupSubjectID = False, returnCalculationGroupSubjectID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnSubjectGradingScaleGroupID = False, returnSubjectGradingScaleGroupSubjectIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubjectGradingScaleGroupSubject(SubjectGradingScaleGroupSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/SubjectGradingScaleGroupSubject/" + str(SubjectGradingScaleGroupSubjectID), verb = "delete")


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

def getTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1, returnTeacherSectionAcademicStandardGradeBucketSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1, setTeacherSectionAcademicStandardGradeBucketSettingID = None, setAcademicStandardID = None, setCreatedTime = None, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionAcademicStandardGradeBucketSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionAcademicStandardGradeBucketSetting(EntityID = 1, setTeacherSectionAcademicStandardGradeBucketSettingID = None, setAcademicStandardID = None, setCreatedTime = None, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionAcademicStandardGradeBucketSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionAcademicStandardGradeBucketSetting(TeacherSectionAcademicStandardGradeBucketSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionAcademicStandardGradeBucketSetting/" + str(TeacherSectionAcademicStandardGradeBucketSettingID), verb = "delete")


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

def getTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1, returnTeacherSectionCategoryAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1, setTeacherSectionCategoryAnalyticsSettingID = None, setAnalysisType = None, setAnalysisTypeCode = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionCategoryAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionCategoryAnalyticsSetting(EntityID = 1, setTeacherSectionCategoryAnalyticsSettingID = None, setAnalysisType = None, setAnalysisTypeCode = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionCategoryAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionCategoryAnalyticsSetting(TeacherSectionCategoryAnalyticsSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionCategoryAnalyticsSetting/" + str(TeacherSectionCategoryAnalyticsSettingID), verb = "delete")


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

def getTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1, returnTeacherSectionGradeBucketAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1, setTeacherSectionGradeBucketAnalyticsSettingID = None, setAnalysisType = None, setAnalysisTypeCode = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionGradeBucketAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionGradeBucketAnalyticsSetting(EntityID = 1, setTeacherSectionGradeBucketAnalyticsSettingID = None, setAnalysisType = None, setAnalysisTypeCode = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionGradeBucketAnalyticsSettingID = False, returnAnalysisType = False, returnAnalysisTypeCode = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionGradeBucketAnalyticsSetting(TeacherSectionGradeBucketAnalyticsSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketAnalyticsSetting/" + str(TeacherSectionGradeBucketAnalyticsSettingID), verb = "delete")


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

def getTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1, returnTeacherSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1, setTeacherSectionGradeBucketSettingID = None, setCreatedTime = None, setGradeBucketDisplayType = None, setGradeBucketDisplayTypeCode = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionGradeBucketSetting(EntityID = 1, setTeacherSectionGradeBucketSettingID = None, setCreatedTime = None, setGradeBucketDisplayType = None, setGradeBucketDisplayTypeCode = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setModifiedTime = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionGradeBucketSettingID = False, returnCreatedTime = False, returnGradeBucketDisplayType = False, returnGradeBucketDisplayTypeCode = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionGradeBucketSetting(TeacherSectionGradeBucketSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradeBucketSetting/" + str(TeacherSectionGradeBucketSettingID), verb = "delete")


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

def getTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1, returnTeacherSectionGradingPeriodSettingID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1, setTeacherSectionGradingPeriodSettingID = None, setCreatedTime = None, setGradingPeriodID = None, setIncludeMissingAssignments = None, setModifiedTime = None, setShowAssessments = None, setShowAssignments = None, setShowGradeBuckets = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionGradingPeriodSettingID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionGradingPeriodSetting(EntityID = 1, setTeacherSectionGradingPeriodSettingID = None, setCreatedTime = None, setGradingPeriodID = None, setIncludeMissingAssignments = None, setModifiedTime = None, setShowAssessments = None, setShowAssignments = None, setShowGradeBuckets = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionGradingPeriodSettingID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnIncludeMissingAssignments = False, returnModifiedTime = False, returnShowAssessments = False, returnShowAssignments = False, returnShowGradeBuckets = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionGradingPeriodSetting(TeacherSectionGradingPeriodSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionGradingPeriodSetting/" + str(TeacherSectionGradingPeriodSettingID), verb = "delete")


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

def getTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1, returnTeacherSectionSettingID = False, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1, setTeacherSectionSettingID = None, setBrowseViewID = None, setCalculationGroupGradeBucketIDLocked = None, setClassGroupID = None, setCreatedTime = None, setDisplayAssignmentAttendanceIndicator = None, setDisplayAssignmentStudentGroupColors = None, setDisplayAttendance = None, setDisplayGradebookAverages = None, setDisplayMissingAssignment = None, setDisplayStudentGradeLevel = None, setDisplayStudentGradingPeriodCommentIndicator = None, setDisplayStudentGroupColors = None, setDisplayStudentGroups = None, setDisplayStudentNumber = None, setDisplayUnscoredPastDueAssignments = None, setHasCustomClassRosterSort = None, setHideAssignmentCategoryColors = None, setHideLockedColumns = None, setIsAHistoricRecord = None, setManualDateEntryEndDate = None, setManualDateEntryStartDate = None, setModifiedTime = None, setSectionID = None, setShowGradebookLockedColumnButton = None, setStudentNameDisplayType = None, setStudentNameDisplayTypeCode = None, setStudentsToDisplay = None, setStudentsToDisplayCode = None, setUseCustomClassRosterSort = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnTeacherSectionSettingID = False, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionSetting(EntityID = 1, setTeacherSectionSettingID = None, setBrowseViewID = None, setCalculationGroupGradeBucketIDLocked = None, setClassGroupID = None, setCreatedTime = None, setDisplayAssignmentAttendanceIndicator = None, setDisplayAssignmentStudentGroupColors = None, setDisplayAttendance = None, setDisplayGradebookAverages = None, setDisplayMissingAssignment = None, setDisplayStudentGradeLevel = None, setDisplayStudentGradingPeriodCommentIndicator = None, setDisplayStudentGroupColors = None, setDisplayStudentGroups = None, setDisplayStudentNumber = None, setDisplayUnscoredPastDueAssignments = None, setHasCustomClassRosterSort = None, setHideAssignmentCategoryColors = None, setHideLockedColumns = None, setIsAHistoricRecord = None, setManualDateEntryEndDate = None, setManualDateEntryStartDate = None, setModifiedTime = None, setSectionID = None, setShowGradebookLockedColumnButton = None, setStudentNameDisplayType = None, setStudentNameDisplayTypeCode = None, setStudentsToDisplay = None, setStudentsToDisplayCode = None, setUseCustomClassRosterSort = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnTeacherSectionSettingID = False, returnBrowseViewID = False, returnCalculationGroupGradeBucketIDLocked = False, returnClassGroupID = False, returnCreatedTime = False, returnDisplayAssignmentAttendanceIndicator = False, returnDisplayAssignmentStudentGroupColors = False, returnDisplayAttendance = False, returnDisplayGradebookAverages = False, returnDisplayMissingAssignment = False, returnDisplayStudentGradeLevel = False, returnDisplayStudentGradingPeriodCommentIndicator = False, returnDisplayStudentGroupColors = False, returnDisplayStudentGroups = False, returnDisplayStudentNumber = False, returnDisplayUnscoredPastDueAssignments = False, returnHasCustomClassRosterSort = False, returnHideAssignmentCategoryColors = False, returnHideLockedColumns = False, returnIsAHistoricRecord = False, returnManualDateEntryEndDate = False, returnManualDateEntryStartDate = False, returnModifiedTime = False, returnSectionID = False, returnShowGradebookLockedColumnButton = False, returnStudentNameDisplayType = False, returnStudentNameDisplayTypeCode = False, returnStudentsToDisplay = False, returnStudentsToDisplayCode = False, returnUseCustomClassRosterSort = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionSetting(TeacherSectionSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSetting/" + str(TeacherSectionSettingID), verb = "delete")


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

def getTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1, setTeacherSectionStandardsDisplayAcademicStandardSettingID = None, setAcademicStandardID = None, setCreatedTime = None, setModifiedTime = None, setTeacherSectionStandardsDisplayGradeBucketSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionStandardsDisplayAcademicStandardSetting(EntityID = 1, setTeacherSectionStandardsDisplayAcademicStandardSettingID = None, setAcademicStandardID = None, setCreatedTime = None, setModifiedTime = None, setTeacherSectionStandardsDisplayGradeBucketSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionStandardsDisplayAcademicStandardSettingID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnModifiedTime = False, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionStandardsDisplayAcademicStandardSetting(TeacherSectionStandardsDisplayAcademicStandardSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayAcademicStandardSetting/" + str(TeacherSectionStandardsDisplayAcademicStandardSettingID), verb = "delete")


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

def getTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1, setTeacherSectionStandardsDisplayGradeBucketSettingID = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setModifiedTime = None, setShowBucket = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionStandardsDisplayGradeBucketSetting(EntityID = 1, setTeacherSectionStandardsDisplayGradeBucketSettingID = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setModifiedTime = None, setShowBucket = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionStandardsDisplayGradeBucketSettingID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnModifiedTime = False, returnShowBucket = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionStandardsDisplayGradeBucketSetting(TeacherSectionStandardsDisplayGradeBucketSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStandardsDisplayGradeBucketSetting/" + str(TeacherSectionStandardsDisplayGradeBucketSettingID), verb = "delete")


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

def getTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1, returnTeacherSectionStudentSectionSettingID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1, setTeacherSectionStudentSectionSettingID = None, setCreatedTime = None, setDisplayOrder = None, setModifiedTime = None, setStudentSectionID = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionStudentSectionSettingID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionStudentSectionSetting(EntityID = 1, setTeacherSectionStudentSectionSettingID = None, setCreatedTime = None, setDisplayOrder = None, setModifiedTime = None, setStudentSectionID = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionStudentSectionSettingID = False, returnCreatedTime = False, returnDisplayOrder = False, returnModifiedTime = False, returnStudentSectionID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionStudentSectionSetting(TeacherSectionStudentSectionSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionStudentSectionSetting/" + str(TeacherSectionStudentSectionSettingID), verb = "delete")


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

def getTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1, returnTeacherSectionSubjectGradeBucketSettingID = False, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "get", return_params_list = return_params)

def modifyTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1, setTeacherSectionSubjectGradeBucketSettingID = None, setAllLinkedAcademicStandardsAreDisplayed = None, setCreatedTime = None, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setModifiedTime = None, setSubjectID = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionSubjectGradeBucketSettingID = False, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherSectionSubjectGradeBucketSetting(EntityID = 1, setTeacherSectionSubjectGradeBucketSettingID = None, setAllLinkedAcademicStandardsAreDisplayed = None, setCreatedTime = None, setDisplay = None, setGradingPeriodGradeBucketID = None, setIsExpanded = None, setModifiedTime = None, setSubjectID = None, setTeacherSectionSettingID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTeacherSectionSubjectGradeBucketSettingID = False, returnAllLinkedAcademicStandardsAreDisplayed = False, returnCreatedTime = False, returnDisplay = False, returnGradingPeriodGradeBucketID = False, returnIsExpanded = False, returnModifiedTime = False, returnSubjectID = False, returnTeacherSectionSettingID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherSectionSubjectGradeBucketSetting(TeacherSectionSubjectGradeBucketSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TeacherSectionSubjectGradeBucketSetting/" + str(TeacherSectionSubjectGradeBucketSettingID), verb = "delete")


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

def getTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1, returnTempAdjustedCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "get", return_params_list = return_params)

def modifyTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1, setTempAdjustedCategoryID = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setTempSectionCategoryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAdjustedCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAdjustedCategory(EntityID = 1, setTempAdjustedCategoryID = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setTempSectionCategoryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAdjustedCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnTempSectionCategoryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAdjustedCategory(TempAdjustedCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAdjustedCategory/" + str(TempAdjustedCategoryID), verb = "delete")


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

def getTempAssignmentError(TempAssignmentErrorID, EntityID = 1, returnTempAssignmentErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "get", return_params_list = return_params)

def modifyTempAssignmentError(TempAssignmentErrorID, EntityID = 1, setTempAssignmentErrorID = None, setCreatedTime = None, setErrorNumber = None, setErrorText = None, setModifiedTime = None, setTempSectionAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAssignmentErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAssignmentError(EntityID = 1, setTempAssignmentErrorID = None, setCreatedTime = None, setErrorNumber = None, setErrorText = None, setModifiedTime = None, setTempSectionAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAssignmentErrorID = False, returnCreatedTime = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnTempSectionAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAssignmentError(TempAssignmentErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempAssignmentError/" + str(TempAssignmentErrorID), verb = "delete")


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

def getTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = False, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "get", return_params_list = return_params)

def modifyTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1, setTempCalcGroupBucketRemoveStandardOrSubjectResultID = None, setCreatedTime = None, setErrorText = None, setIsError = None, setModifiedTime = None, setStandardOrSubjectDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = False, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalcGroupBucketRemoveStandardOrSubjectResult(EntityID = 1, setTempCalcGroupBucketRemoveStandardOrSubjectResultID = None, setCreatedTime = None, setErrorText = None, setIsError = None, setModifiedTime = None, setStandardOrSubjectDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCalcGroupBucketRemoveStandardOrSubjectResultID = False, returnCreatedTime = False, returnErrorText = False, returnIsError = False, returnModifiedTime = False, returnStandardOrSubjectDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalcGroupBucketRemoveStandardOrSubjectResult(TempCalcGroupBucketRemoveStandardOrSubjectResultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalcGroupBucketRemoveStandardOrSubjectResult/" + str(TempCalcGroupBucketRemoveStandardOrSubjectResultID), verb = "delete")


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

def getTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1, returnTempCalculationGroupAcademicStandardWeightingID = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "get", return_params_list = return_params)

def modifyTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1, setTempCalculationGroupAcademicStandardWeightingID = None, setCalculationGroupAcademicStandardGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempCalculationGroupAcademicStandardWeightingID = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalculationGroupAcademicStandardWeighting(EntityID = 1, setTempCalculationGroupAcademicStandardWeightingID = None, setCalculationGroupAcademicStandardGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempCalculationGroupAcademicStandardWeightingID = False, returnCalculationGroupAcademicStandardGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalculationGroupAcademicStandardWeighting(TempCalculationGroupAcademicStandardWeightingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupAcademicStandardWeighting/" + str(TempCalculationGroupAcademicStandardWeightingID), verb = "delete")


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

def getTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1, returnTempCalculationGroupSubjectWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "get", return_params_list = return_params)

def modifyTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1, setTempCalculationGroupSubjectWeightingID = None, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupSubjectGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempCalculationGroupSubjectWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalculationGroupSubjectWeighting(EntityID = 1, setTempCalculationGroupSubjectWeightingID = None, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupSubjectGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempCalculationGroupSubjectWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupSubjectGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalculationGroupSubjectWeighting(TempCalculationGroupSubjectWeightingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupSubjectWeighting/" + str(TempCalculationGroupSubjectWeightingID), verb = "delete")


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

def getTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1, returnTempCalculationGroupWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "get", return_params_list = return_params)

def modifyTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1, setTempCalculationGroupWeightingID = None, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setGradeBucketLabel = None, setGradeBucketOrder = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setSubjectDescription = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempCalculationGroupWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCalculationGroupWeighting(EntityID = 1, setTempCalculationGroupWeightingID = None, setAcademicStandardDescription = None, setAcademicStandardFullKey = None, setAcademicStandardID = None, setCalculationGroupGradeBucketID = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setGradeBucketLabel = None, setGradeBucketOrder = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setSubjectDescription = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempCalculationGroupWeightingID = False, returnAcademicStandardDescription = False, returnAcademicStandardFullKey = False, returnAcademicStandardID = False, returnCalculationGroupGradeBucketID = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnGradeBucketLabel = False, returnGradeBucketOrder = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSubjectDescription = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCalculationGroupWeighting(TempCalculationGroupWeightingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCalculationGroupWeighting/" + str(TempCalculationGroupWeightingID), verb = "delete")


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

def getTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1, returnTempCloneGradebookSectionID = False, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "get", return_params_list = return_params)

def modifyTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1, setTempCloneGradebookSectionID = None, setCanClone = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCloneGradebookSectionID = False, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCloneGradebookSection(EntityID = 1, setTempCloneGradebookSectionID = None, setCanClone = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCloneGradebookSectionID = False, returnCanClone = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCloneGradebookSection(TempCloneGradebookSectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCloneGradebookSection/" + str(TempCloneGradebookSectionID), verb = "delete")


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

def getTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1, returnTempCourseMoveCourseID = False, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "get", return_params_list = return_params)

def modifyTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1, setTempCourseMoveCourseID = None, setCodeDescription = None, setCourseCode = None, setCourseDescription = None, setCourseID = None, setCreatedTime = None, setEntityID = None, setGroupCourseID = None, setIsValidUpdate = None, setModifiedTime = None, setNewCalculationGroupDescription = None, setNewCalculationGroupID = None, setOriginalCalculationGroupDescription = None, setOriginalCalculationGroupID = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCourseMoveCourseID = False, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCourseMoveCourse(EntityID = 1, setTempCourseMoveCourseID = None, setCodeDescription = None, setCourseCode = None, setCourseDescription = None, setCourseID = None, setCreatedTime = None, setEntityID = None, setGroupCourseID = None, setIsValidUpdate = None, setModifiedTime = None, setNewCalculationGroupDescription = None, setNewCalculationGroupID = None, setOriginalCalculationGroupDescription = None, setOriginalCalculationGroupID = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCourseMoveCourseID = False, returnCodeDescription = False, returnCourseCode = False, returnCourseDescription = False, returnCourseID = False, returnCreatedTime = False, returnEntityID = False, returnGroupCourseID = False, returnIsValidUpdate = False, returnModifiedTime = False, returnNewCalculationGroupDescription = False, returnNewCalculationGroupID = False, returnOriginalCalculationGroupDescription = False, returnOriginalCalculationGroupID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCourseMoveCourse(TempCourseMoveCourseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveCourse/" + str(TempCourseMoveCourseID), verb = "delete")


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

def getTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1, returnTempCourseMoveErrorID = False, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "get", return_params_list = return_params)

def modifyTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1, setTempCourseMoveErrorID = None, setBucketLabel = None, setCreatedTime = None, setErrorCode = None, setErrorMessage = None, setErrorType = None, setErrorTypeCode = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCourseMoveErrorID = False, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCourseMoveError(EntityID = 1, setTempCourseMoveErrorID = None, setBucketLabel = None, setCreatedTime = None, setErrorCode = None, setErrorMessage = None, setErrorType = None, setErrorTypeCode = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCourseMoveErrorID = False, returnBucketLabel = False, returnCreatedTime = False, returnErrorCode = False, returnErrorMessage = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCourseMoveError(TempCourseMoveErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveError/" + str(TempCourseMoveErrorID), verb = "delete")


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

def getTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1, returnTempCourseMoveSectionErrorID = False, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "get", return_params_list = return_params)

def modifyTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1, setTempCourseMoveSectionErrorID = None, setCourseID = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setSectionCode = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCourseMoveSectionErrorID = False, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCourseMoveSectionError(EntityID = 1, setTempCourseMoveSectionErrorID = None, setCourseID = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setSectionCode = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCourseMoveSectionErrorID = False, returnCourseID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCourseMoveSectionError(TempCourseMoveSectionErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempCourseMoveSectionError/" + str(TempCourseMoveSectionErrorID), verb = "delete")


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

def getTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1, returnTempDropLowScoreStudentAssignmentID = False, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "get", return_params_list = return_params)

def modifyTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1, setTempDropLowScoreStudentAssignmentID = None, setAssignmentName = None, setComments = None, setCreatedTime = None, setDropActionType = None, setDropActionTypeCode = None, setDropCode = None, setDropLowScore = None, setDueDate = None, setMaxScore = None, setModifiedTime = None, setNewGrade = None, setNoDropReason = None, setOriginalGrade = None, setScore = None, setStudentAssignmentID = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setUndoDropActionType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnTempDropLowScoreStudentAssignmentID = False, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempDropLowScoreStudentAssignment(EntityID = 1, setTempDropLowScoreStudentAssignmentID = None, setAssignmentName = None, setComments = None, setCreatedTime = None, setDropActionType = None, setDropActionTypeCode = None, setDropCode = None, setDropLowScore = None, setDueDate = None, setMaxScore = None, setModifiedTime = None, setNewGrade = None, setNoDropReason = None, setOriginalGrade = None, setScore = None, setStudentAssignmentID = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setUndoDropActionType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnTempDropLowScoreStudentAssignmentID = False, returnAssignmentName = False, returnComments = False, returnCreatedTime = False, returnDropActionType = False, returnDropActionTypeCode = False, returnDropCode = False, returnDropLowScore = False, returnDueDate = False, returnMaxScore = False, returnModifiedTime = False, returnNewGrade = False, returnNoDropReason = False, returnOriginalGrade = False, returnScore = False, returnStudentAssignmentID = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUndoDropActionType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempDropLowScoreStudentAssignment(TempDropLowScoreStudentAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempDropLowScoreStudentAssignment/" + str(TempDropLowScoreStudentAssignmentID), verb = "delete")


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

def getTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1, returnTempGradebookCloneErrorID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "get", return_params_list = return_params)

def modifyTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1, setTempGradebookCloneErrorID = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setField = None, setGradeBucketLabel = None, setMessage = None, setModifiedTime = None, setRecordType = None, setRecordTypeCode = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradebookCloneErrorID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempGradebookCloneError(EntityID = 1, setTempGradebookCloneErrorID = None, setCalculationGroupGradeBucketID = None, setCreatedTime = None, setField = None, setGradeBucketLabel = None, setMessage = None, setModifiedTime = None, setRecordType = None, setRecordTypeCode = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradebookCloneErrorID = False, returnCalculationGroupGradeBucketID = False, returnCreatedTime = False, returnField = False, returnGradeBucketLabel = False, returnMessage = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempGradebookCloneError(TempGradebookCloneErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookCloneError/" + str(TempGradebookCloneErrorID), verb = "delete")


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

def getTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1, returnTempGradebookGroupErrorID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "get", return_params_list = return_params)

def modifyTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1, setTempGradebookGroupErrorID = None, setCalculationGroupID = None, setCreatedTime = None, setDescription = None, setEntityID = None, setErrorText = None, setGradingScaleGroupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradebookGroupErrorID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempGradebookGroupError(EntityID = 1, setTempGradebookGroupErrorID = None, setCalculationGroupID = None, setCreatedTime = None, setDescription = None, setEntityID = None, setErrorText = None, setGradingScaleGroupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradebookGroupErrorID = False, returnCalculationGroupID = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnErrorText = False, returnGradingScaleGroupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempGradebookGroupError(TempGradebookGroupErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradebookGroupError/" + str(TempGradebookGroupErrorID), verb = "delete")


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

def getTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1, returnTempGradeMarkErrorID = False, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "get", return_params_list = return_params)

def modifyTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1, setTempGradeMarkErrorID = None, setCreatedTime = None, setDisplayOrder = None, setGradeMarkCode = None, setGradeMarkID = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradeMarkErrorID = False, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempGradeMarkError(EntityID = 1, setTempGradeMarkErrorID = None, setCreatedTime = None, setDisplayOrder = None, setGradeMarkCode = None, setGradeMarkID = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradeMarkErrorID = False, returnCreatedTime = False, returnDisplayOrder = False, returnGradeMarkCode = False, returnGradeMarkID = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempGradeMarkError(TempGradeMarkErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradeMarkError/" + str(TempGradeMarkErrorID), verb = "delete")


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

def getTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1, returnTempGradingPeriodGradeBucketID = False, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "get", return_params_list = return_params)

def modifyTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1, setTempGradingPeriodGradeBucketID = None, setCreatedTime = None, setEndDate = None, setErrorCount = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradingPeriodGradeBucketID = False, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempGradingPeriodGradeBucket(EntityID = 1, setTempGradingPeriodGradeBucketID = None, setCreatedTime = None, setEndDate = None, setErrorCount = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradingPeriodGradeBucketID = False, returnCreatedTime = False, returnEndDate = False, returnErrorCount = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempGradingPeriodGradeBucket(TempGradingPeriodGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucket/" + str(TempGradingPeriodGradeBucketID), verb = "delete")


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

def getTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1, returnTempGradingPeriodGradeBucketErrorID = False, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "get", return_params_list = return_params)

def modifyTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1, setTempGradingPeriodGradeBucketErrorID = None, setCalculationGroupID = None, setCalculationType = None, setCreatedTime = None, setEndDate = None, setErrorNumber = None, setErrorText = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setSubjectOrStandardDescription = None, setSubjectOrStandardKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradingPeriodGradeBucketErrorID = False, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempGradingPeriodGradeBucketError(EntityID = 1, setTempGradingPeriodGradeBucketErrorID = None, setCalculationGroupID = None, setCalculationType = None, setCreatedTime = None, setEndDate = None, setErrorNumber = None, setErrorText = None, setGradeBucketLabelWithDates = None, setGradingPeriodGradeBucketID = None, setModifiedTime = None, setSectionLengthCodeDescription = None, setStartDate = None, setStatusDisplayWithExtensionDate = None, setSubjectOrStandardDescription = None, setSubjectOrStandardKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradingPeriodGradeBucketErrorID = False, returnCalculationGroupID = False, returnCalculationType = False, returnCreatedTime = False, returnEndDate = False, returnErrorNumber = False, returnErrorText = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSectionLengthCodeDescription = False, returnStartDate = False, returnStatusDisplayWithExtensionDate = False, returnSubjectOrStandardDescription = False, returnSubjectOrStandardKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempGradingPeriodGradeBucketError(TempGradingPeriodGradeBucketErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempGradingPeriodGradeBucketError/" + str(TempGradingPeriodGradeBucketErrorID), verb = "delete")


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

def getTempSectionAssignment(TempSectionAssignmentID, EntityID = 1, returnTempSectionAssignmentID = False, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "get", return_params_list = return_params)

def modifyTempSectionAssignment(TempSectionAssignmentID, EntityID = 1, setTempSectionAssignmentID = None, setAnswerRevealDate = None, setAnswerRevealDateAndTime = None, setAnswerRevealTime = None, setAssignedDate = None, setAssignmentID = None, setAssignmentName = None, setAttachmentCount = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setCurrentPeriod = None, setDueDate = None, setEndDate = None, setEndDateAndTime = None, setEndTime = None, setEntityID = None, setErrorCount = None, setHideScoreUntilDate = None, setHideScoreUntilDateAndTime = None, setHideScoreUntilTime = None, setIsOnlineAssignment = None, setMaxScore = None, setModifiedTime = None, setSchoolYearID = None, setSectionDetails = None, setSectionID = None, setSectionLengthEndDate = None, setSectionLengthStartDate = None, setShowCorrectAnswers = None, setStartDate = None, setStartDateAndTime = None, setStartTime = None, setSync = None, setUseForSpecificGradeBucketType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnTempSectionAssignmentID = False, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSectionAssignment(EntityID = 1, setTempSectionAssignmentID = None, setAnswerRevealDate = None, setAnswerRevealDateAndTime = None, setAnswerRevealTime = None, setAssignedDate = None, setAssignmentID = None, setAssignmentName = None, setAttachmentCount = None, setCategoryDescription = None, setCategoryID = None, setCreatedTime = None, setCurrentPeriod = None, setDueDate = None, setEndDate = None, setEndDateAndTime = None, setEndTime = None, setEntityID = None, setErrorCount = None, setHideScoreUntilDate = None, setHideScoreUntilDateAndTime = None, setHideScoreUntilTime = None, setIsOnlineAssignment = None, setMaxScore = None, setModifiedTime = None, setSchoolYearID = None, setSectionDetails = None, setSectionID = None, setSectionLengthEndDate = None, setSectionLengthStartDate = None, setShowCorrectAnswers = None, setStartDate = None, setStartDateAndTime = None, setStartTime = None, setSync = None, setUseForSpecificGradeBucketType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnTempSectionAssignmentID = False, returnAnswerRevealDate = False, returnAnswerRevealDateAndTime = False, returnAnswerRevealTime = False, returnAssignedDate = False, returnAssignmentID = False, returnAssignmentName = False, returnAttachmentCount = False, returnCategoryDescription = False, returnCategoryID = False, returnCreatedTime = False, returnCurrentPeriod = False, returnDueDate = False, returnEndDate = False, returnEndDateAndTime = False, returnEndTime = False, returnEntityID = False, returnErrorCount = False, returnHideScoreUntilDate = False, returnHideScoreUntilDateAndTime = False, returnHideScoreUntilTime = False, returnIsOnlineAssignment = False, returnMaxScore = False, returnModifiedTime = False, returnSchoolYearID = False, returnSectionDetails = False, returnSectionID = False, returnSectionLengthEndDate = False, returnSectionLengthStartDate = False, returnShowCorrectAnswers = False, returnStartDate = False, returnStartDateAndTime = False, returnStartTime = False, returnSync = False, returnUseForSpecificGradeBucketType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSectionAssignment(TempSectionAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionAssignment/" + str(TempSectionAssignmentID), verb = "delete")


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

def getTempSectionCategory(TempSectionCategoryID, EntityID = 1, returnTempSectionCategoryID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "get", return_params_list = return_params)

def modifyTempSectionCategory(TempSectionCategoryID, EntityID = 1, setTempSectionCategoryID = None, setCalculationGroupGradeBucketID = None, setCalculationGroupID = None, setCanClone = None, setCategoryCode = None, setCategoryID = None, setCategoryIDIsInvalid = None, setCreatedTime = None, setErrorMessages = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempSectionCategoryID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSectionCategory(EntityID = 1, setTempSectionCategoryID = None, setCalculationGroupGradeBucketID = None, setCalculationGroupID = None, setCanClone = None, setCategoryCode = None, setCategoryID = None, setCategoryIDIsInvalid = None, setCreatedTime = None, setErrorMessages = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempSectionCategoryID = False, returnCalculationGroupGradeBucketID = False, returnCalculationGroupID = False, returnCanClone = False, returnCategoryCode = False, returnCategoryID = False, returnCategoryIDIsInvalid = False, returnCreatedTime = False, returnErrorMessages = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSectionCategory(TempSectionCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionCategory/" + str(TempSectionCategoryID), verb = "delete")


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

def getTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1, returnTempSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "get", return_params_list = return_params)

def modifyTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1, setTempSectionGradeBucketID = None, setCalculationGroupGradeBucketID = None, setCanClone = None, setChildRecords = None, setCreatedTime = None, setCurrentAllowCategoryOverride = None, setCurrentCalculationType = None, setCurrentCalculationTypeCode = None, setEndDate = None, setErrorMessages = None, setExclude = None, setGradeBucketLabel = None, setGradeBucketTypeID = None, setHasLeftOverPercentage = None, setIsCalculationTypeOverridden = None, setIsSpecificGradeBucket = None, setModifiedTime = None, setNewCalculationType = None, setNewCalculationTypeCode = None, setOrder = None, setSectionGradeBucketID = None, setSectionID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSectionGradeBucket(EntityID = 1, setTempSectionGradeBucketID = None, setCalculationGroupGradeBucketID = None, setCanClone = None, setChildRecords = None, setCreatedTime = None, setCurrentAllowCategoryOverride = None, setCurrentCalculationType = None, setCurrentCalculationTypeCode = None, setEndDate = None, setErrorMessages = None, setExclude = None, setGradeBucketLabel = None, setGradeBucketTypeID = None, setHasLeftOverPercentage = None, setIsCalculationTypeOverridden = None, setIsSpecificGradeBucket = None, setModifiedTime = None, setNewCalculationType = None, setNewCalculationTypeCode = None, setOrder = None, setSectionGradeBucketID = None, setSectionID = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSectionGradeBucketID = False, returnCalculationGroupGradeBucketID = False, returnCanClone = False, returnChildRecords = False, returnCreatedTime = False, returnCurrentAllowCategoryOverride = False, returnCurrentCalculationType = False, returnCurrentCalculationTypeCode = False, returnEndDate = False, returnErrorMessages = False, returnExclude = False, returnGradeBucketLabel = False, returnGradeBucketTypeID = False, returnHasLeftOverPercentage = False, returnIsCalculationTypeOverridden = False, returnIsSpecificGradeBucket = False, returnModifiedTime = False, returnNewCalculationType = False, returnNewCalculationTypeCode = False, returnOrder = False, returnSectionGradeBucketID = False, returnSectionID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSectionGradeBucket(TempSectionGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucket/" + str(TempSectionGradeBucketID), verb = "delete")


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

def getTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1, returnTempSectionGradeBucketWeightID = False, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "get", return_params_list = return_params)

def modifyTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1, setTempSectionGradeBucketWeightID = None, setAcademicStandardIDToWeight = None, setCalculationGroupGradeBucketIDComposite = None, setCalculationGroupGradeBucketIDFeeder = None, setCanClone = None, setCreatedTime = None, setModifiedTime = None, setSectionID = None, setSubjectIDToWeight = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempSectionGradeBucketWeightID = False, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSectionGradeBucketWeight(EntityID = 1, setTempSectionGradeBucketWeightID = None, setAcademicStandardIDToWeight = None, setCalculationGroupGradeBucketIDComposite = None, setCalculationGroupGradeBucketIDFeeder = None, setCanClone = None, setCreatedTime = None, setModifiedTime = None, setSectionID = None, setSubjectIDToWeight = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeightPercent = None, returnTempSectionGradeBucketWeightID = False, returnAcademicStandardIDToWeight = False, returnCalculationGroupGradeBucketIDComposite = False, returnCalculationGroupGradeBucketIDFeeder = False, returnCanClone = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionID = False, returnSubjectIDToWeight = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercent = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSectionGradeBucketWeight(TempSectionGradeBucketWeightID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradeBucketWeight/" + str(TempSectionGradeBucketWeightID), verb = "delete")


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

def getTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1, returnTempSectionGradingScaleID = False, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "get", return_params_list = return_params)

def modifyTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1, setTempSectionGradingScaleID = None, setCanClone = None, setChildGradeBuckets = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSectionGradingScaleID = False, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSectionGradingScale(EntityID = 1, setTempSectionGradingScaleID = None, setCanClone = None, setChildGradeBuckets = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSectionGradingScaleID = False, returnCanClone = False, returnChildGradeBuckets = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSectionGradingScale(TempSectionGradingScaleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScale/" + str(TempSectionGradingScaleID), verb = "delete")


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

def getTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1, returnTempSectionGradingScaleGroupToCreateID = False, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "get", return_params_list = return_params)

def modifyTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1, setTempSectionGradingScaleGroupToCreateID = None, setCourseCode = None, setCourseDescriptionCodeSectionCode = None, setCourseGradingScaleGroupCourseID = None, setCourseGradingScaleGroupID = None, setCourseID = None, setCreatedTime = None, setDescription = None, setGradingPeriodGradeBucketsToRetainJson = None, setInvalidGradeMarks = None, setIsValidInNewGroup = None, setModifiedTime = None, setNewCourseGradingScaleGroupDescription = None, setNewCourseGradingScaleGroupID = None, setReason = None, setRequiresSectionGradingScaleGroups = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSectionGradingScaleGroupToCreateID = False, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSectionGradingScaleGroupToCreate(EntityID = 1, setTempSectionGradingScaleGroupToCreateID = None, setCourseCode = None, setCourseDescriptionCodeSectionCode = None, setCourseGradingScaleGroupCourseID = None, setCourseGradingScaleGroupID = None, setCourseID = None, setCreatedTime = None, setDescription = None, setGradingPeriodGradeBucketsToRetainJson = None, setInvalidGradeMarks = None, setIsValidInNewGroup = None, setModifiedTime = None, setNewCourseGradingScaleGroupDescription = None, setNewCourseGradingScaleGroupID = None, setReason = None, setRequiresSectionGradingScaleGroups = None, setSectionCode = None, setSectionID = None, setSectionLengthCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSectionGradingScaleGroupToCreateID = False, returnCourseCode = False, returnCourseDescriptionCodeSectionCode = False, returnCourseGradingScaleGroupCourseID = False, returnCourseGradingScaleGroupID = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnGradingPeriodGradeBucketsToRetainJson = False, returnInvalidGradeMarks = False, returnIsValidInNewGroup = False, returnModifiedTime = False, returnNewCourseGradingScaleGroupDescription = False, returnNewCourseGradingScaleGroupID = False, returnReason = False, returnRequiresSectionGradingScaleGroups = False, returnSectionCode = False, returnSectionID = False, returnSectionLengthCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSectionGradingScaleGroupToCreate(TempSectionGradingScaleGroupToCreateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempSectionGradingScaleGroupToCreate/" + str(TempSectionGradingScaleGroupToCreateID), verb = "delete")


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

def getTempStudentAssignment(TempStudentAssignmentID, EntityID = 1, returnTempStudentAssignmentID = False, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "get", return_params_list = return_params)

def modifyTempStudentAssignment(TempStudentAssignmentID, EntityID = 1, setTempStudentAssignmentID = None, setAssignmentDescription = None, setAssignmentID = None, setAssignmentName = None, setCreatedTime = None, setDueDate = None, setDueDateIsInGivenDateRange = None, setInclude = None, setIsMissing = None, setMaxScore = None, setModifiedTime = None, setNoCount = None, setScore = None, setScoreClarifierCode = None, setScoreClarifierID = None, setSectionID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnTempStudentAssignmentID = False, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentAssignment(EntityID = 1, setTempStudentAssignmentID = None, setAssignmentDescription = None, setAssignmentID = None, setAssignmentName = None, setCreatedTime = None, setDueDate = None, setDueDateIsInGivenDateRange = None, setInclude = None, setIsMissing = None, setMaxScore = None, setModifiedTime = None, setNoCount = None, setScore = None, setScoreClarifierCode = None, setScoreClarifierID = None, setSectionID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWeight = None, returnTempStudentAssignmentID = False, returnAssignmentDescription = False, returnAssignmentID = False, returnAssignmentName = False, returnCreatedTime = False, returnDueDate = False, returnDueDateIsInGivenDateRange = False, returnInclude = False, returnIsMissing = False, returnMaxScore = False, returnModifiedTime = False, returnNoCount = False, returnScore = False, returnScoreClarifierCode = False, returnScoreClarifierID = False, returnSectionID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeight = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentAssignment(TempStudentAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentAssignment/" + str(TempStudentAssignmentID), verb = "delete")


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

def getTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1, returnTempStudentGradingScaleGroupStudentSectionID = False, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "get", return_params_list = return_params)

def modifyTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1, setTempStudentGradingScaleGroupStudentSectionID = None, setCourseDescriptionCodeSectionCode = None, setCreatedTime = None, setErrorText = None, setGradingPeriodGradeBuckets = None, setHasError = None, setModifiedTime = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthID = None, setStudentFullNameLFM = None, setStudentGradingScaleGroupStudentSectionID = None, setStudentID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentGradingScaleGroupStudentSectionID = False, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentGradingScaleGroupStudentSection(EntityID = 1, setTempStudentGradingScaleGroupStudentSectionID = None, setCourseDescriptionCodeSectionCode = None, setCreatedTime = None, setErrorText = None, setGradingPeriodGradeBuckets = None, setHasError = None, setModifiedTime = None, setSectionID = None, setSectionLengthCode = None, setSectionLengthID = None, setStudentFullNameLFM = None, setStudentGradingScaleGroupStudentSectionID = None, setStudentID = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentGradingScaleGroupStudentSectionID = False, returnCourseDescriptionCodeSectionCode = False, returnCreatedTime = False, returnErrorText = False, returnGradingPeriodGradeBuckets = False, returnHasError = False, returnModifiedTime = False, returnSectionID = False, returnSectionLengthCode = False, returnSectionLengthID = False, returnStudentFullNameLFM = False, returnStudentGradingScaleGroupStudentSectionID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentGradingScaleGroupStudentSection(TempStudentGradingScaleGroupStudentSectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempStudentGradingScaleGroupStudentSection/" + str(TempStudentGradingScaleGroupStudentSectionID), verb = "delete")


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

def getTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1, returnTempUnDropLowScoreStudentSectionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "get", return_params_list = return_params)

def modifyTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1, setTempUnDropLowScoreStudentSectionID = None, setCreatedTime = None, setModifiedTime = None, setNewGrade = None, setOriginalGrade = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUnDropLowScoreStudentSectionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempUnDropLowScoreStudentSection(EntityID = 1, setTempUnDropLowScoreStudentSectionID = None, setCreatedTime = None, setModifiedTime = None, setNewGrade = None, setOriginalGrade = None, setStudentDisplaySortCode = None, setStudentName = None, setStudentSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUnDropLowScoreStudentSectionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNewGrade = False, returnOriginalGrade = False, returnStudentDisplaySortCode = False, returnStudentName = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempUnDropLowScoreStudentSection(TempUnDropLowScoreStudentSectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/TempUnDropLowScoreStudentSection/" + str(TempUnDropLowScoreStudentSectionID), verb = "delete")


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

def getUnenteredStudentGradeBucket(StudentGradeBucketID, EntityID = 1, returnStudentGradeBucketID = False, returnCourseDescription = False, returnDisplayPeriodID = False, returnEntityCode = False, returnEntityID = False, returnGradeBucketID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnGradeMarkIDToApply = False, returnGradingPeriodEndDate = False, returnGradingPeriodStartDate = False, returnIsAdminOverride = False, returnPercent = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStudentGradeBucketFlag = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionEndDate = False, returnStudentSectionTransactionStartDate = False, returnUseServiceIDOverride = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/UnenteredStudentGradeBucket/" + str(StudentGradeBucketID), verb = "get", return_params_list = return_params)

def modifyUnenteredStudentGradeBucket(StudentGradeBucketID, EntityID = 1, setStudentGradeBucketID = None, setCourseDescription = None, setDisplayPeriodID = None, setEntityCode = None, setEntityID = None, setGradeBucketID = None, setGradeBucketLabel = None, setGradeMarkCode = None, setGradeMarkIDToApply = None, setGradingPeriodEndDate = None, setGradingPeriodStartDate = None, setIsAdminOverride = None, setPercent = None, setSchoolYearID = None, setSectionID = None, setStaffID = None, setStudentGradeBucketFlag = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionEndDate = None, setStudentSectionTransactionStartDate = None, setUseServiceIDOverride = None, returnStudentGradeBucketID = False, returnCourseDescription = False, returnDisplayPeriodID = False, returnEntityCode = False, returnEntityID = False, returnGradeBucketID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnGradeMarkIDToApply = False, returnGradingPeriodEndDate = False, returnGradingPeriodStartDate = False, returnIsAdminOverride = False, returnPercent = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStudentGradeBucketFlag = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionEndDate = False, returnStudentSectionTransactionStartDate = False, returnUseServiceIDOverride = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/UnenteredStudentGradeBucket/" + str(StudentGradeBucketID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUnenteredStudentGradeBucket(EntityID = 1, setStudentGradeBucketID = None, setCourseDescription = None, setDisplayPeriodID = None, setEntityCode = None, setEntityID = None, setGradeBucketID = None, setGradeBucketLabel = None, setGradeMarkCode = None, setGradeMarkIDToApply = None, setGradingPeriodEndDate = None, setGradingPeriodStartDate = None, setIsAdminOverride = None, setPercent = None, setSchoolYearID = None, setSectionID = None, setStaffID = None, setStudentGradeBucketFlag = None, setStudentID = None, setStudentSectionID = None, setStudentSectionTransactionEndDate = None, setStudentSectionTransactionStartDate = None, setUseServiceIDOverride = None, returnStudentGradeBucketID = False, returnCourseDescription = False, returnDisplayPeriodID = False, returnEntityCode = False, returnEntityID = False, returnGradeBucketID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnGradeMarkIDToApply = False, returnGradingPeriodEndDate = False, returnGradingPeriodStartDate = False, returnIsAdminOverride = False, returnPercent = False, returnSchoolYearID = False, returnSectionID = False, returnStaffID = False, returnStudentGradeBucketFlag = False, returnStudentID = False, returnStudentSectionID = False, returnStudentSectionTransactionEndDate = False, returnStudentSectionTransactionStartDate = False, returnUseServiceIDOverride = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/UnenteredStudentGradeBucket/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUnenteredStudentGradeBucket(StudentGradeBucketID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/UnenteredStudentGradeBucket/" + str(StudentGradeBucketID), verb = "delete")


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

def getVendorAssignment(VendorAssignmentID, EntityID = 1, returnVendorAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "get", return_params_list = return_params)

def modifyVendorAssignment(VendorAssignmentID, EntityID = 1, setVendorAssignmentID = None, setAssignmentID = None, setCreatedTime = None, setModifiedTime = None, setOneRosterVendorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorSourceID = None, returnVendorAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createVendorAssignment(EntityID = 1, setVendorAssignmentID = None, setAssignmentID = None, setCreatedTime = None, setModifiedTime = None, setOneRosterVendorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorSourceID = None, returnVendorAssignmentID = False, returnAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteVendorAssignment(VendorAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorAssignment/" + str(VendorAssignmentID), verb = "delete")


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

def getVendorCategory(VendorCategoryID, EntityID = 1, returnVendorCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "get", return_params_list = return_params)

def modifyVendorCategory(VendorCategoryID, EntityID = 1, setVendorCategoryID = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setOneRosterVendorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorSourceID = None, returnVendorCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createVendorCategory(EntityID = 1, setVendorCategoryID = None, setCategoryID = None, setCreatedTime = None, setModifiedTime = None, setOneRosterVendorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorSourceID = None, returnVendorCategoryID = False, returnCategoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteVendorCategory(VendorCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorCategory/" + str(VendorCategoryID), verb = "delete")


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

def getVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1, returnVendorStudentAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "get", return_params_list = return_params)

def modifyVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1, setVendorStudentAssignmentID = None, setCreatedTime = None, setModifiedTime = None, setOneRosterVendorID = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorSourceID = None, returnVendorStudentAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createVendorStudentAssignment(EntityID = 1, setVendorStudentAssignmentID = None, setCreatedTime = None, setModifiedTime = None, setOneRosterVendorID = None, setStudentAssignmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorSourceID = None, returnVendorStudentAssignmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnOneRosterVendorID = False, returnStudentAssignmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteVendorStudentAssignment(VendorStudentAssignmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Gradebook/VendorStudentAssignment/" + str(VendorStudentAssignmentID), verb = "delete")