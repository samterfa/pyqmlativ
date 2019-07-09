# This module contains Curriculum functions.

from . import make_request

def getAcademicStandard(AcademicStandardID, EntityID = 1, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandard(AcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "delete")

	return(response)

def getAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "delete")

	return(response)

def getAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "delete")

	return(response)

def getAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "delete")

	return(response)

def getAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "delete")

	return(response)

def getAcademicStandardSet(AcademicStandardSetID, EntityID = 1, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSet(AcademicStandardSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "delete")

	return(response)

def getAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "delete")

	return(response)

def getAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "delete")

	return(response)

def getAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "delete")

	return(response)

def getAssessmentToolMN(AssessmentToolMNID, EntityID = 1, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "get", params_list = params_list)

	return(response)

def deleteAssessmentToolMN(AssessmentToolMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "delete")

	return(response)

def getCurriculum(CurriculumID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculum(CurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "delete")

	return(response)

def getCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "delete")

	return(response)

def getCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "delete")

	return(response)

def getCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "delete")

	return(response)

def getCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "delete")

	return(response)

def getCurriculumSubject(CurriculumSubjectID, EntityID = 1, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumSubject(CurriculumSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "delete")

	return(response)

def getCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "delete")

	return(response)

def getCurriculumYear(CurriculumYearID, EntityID = 1, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumYear(CurriculumYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "delete")

	return(response)

def getEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "get", params_list = params_list)

	return(response)

def deleteEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "delete")

	return(response)

def getEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "get", params_list = params_list)

	return(response)

def deleteEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "delete")

	return(response)

def getHierarchyDepth(HierarchyDepthID, EntityID = 1, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteHierarchyDepth(HierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "delete")

	return(response)

def getPrerequisite(PrerequisiteID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "get", params_list = params_list)

	return(response)

def deletePrerequisite(PrerequisiteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "delete")

	return(response)

def getPrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deletePrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "delete")

	return(response)

def getSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "get", params_list = params_list)

	return(response)

def deleteSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "delete")

	return(response)

def getStandardPlacementMN(StandardPlacementMNID, EntityID = 1, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "get", params_list = params_list)

	return(response)

def deleteStandardPlacementMN(StandardPlacementMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "delete")

	return(response)

def getSubject(SubjectID, EntityID = 1, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteSubject(SubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "delete")

	return(response)

def getTempAcademicStandard(TempAcademicStandardID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandard(TempAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "delete")

	return(response)

def getTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "delete")

	return(response)

def getTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "delete")

	return(response)

def getTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "delete")

	return(response)

def getTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "delete")

	return(response)

def getTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "delete")

	return(response)