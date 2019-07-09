# This module contains GraduationRequirements functions.

from . import make_request

def getArea(AreaID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "get", params_list = params_list)

	return(response)

def deleteArea(AreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "delete")

	return(response)

def getCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "delete")

	return(response)

def getCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "delete")

	return(response)

def getCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "delete")

	return(response)

def getCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "delete")

	return(response)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getCurriculumCluster(CurriculumClusterID, EntityID = 1, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumCluster(CurriculumClusterID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "delete")

	return(response)

def getCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "delete")

	return(response)

def getCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "delete")

	return(response)

def getCurriculumSubArea(CurriculumSubAreaID, EntityID = 1, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumSubArea(CurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "delete")

	return(response)

def getEndorsement(EndorsementID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsement(EndorsementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "delete")

	return(response)

def getEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "delete")

	return(response)

def getEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "delete")

	return(response)

def getEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "delete")

	return(response)

def getEndorsementDefault(EndorsementDefaultID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDefault(EndorsementDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "delete")

	return(response)

def getEndorsementOption(EndorsementOptionID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementOption(EndorsementOptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "delete")

	return(response)

def getEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "delete")

	return(response)

def getEndorsementRequirement(EndorsementRequirementID, EntityID = 1, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirement(EndorsementRequirementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "delete")

	return(response)

def getEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "delete")

	return(response)

def getEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "delete")

	return(response)

def getEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "delete")

	return(response)

def getEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "delete")

	return(response)

def getEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "delete")

	return(response)

def getEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "delete")

	return(response)

def getEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "delete")

	return(response)

def getEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "delete")

	return(response)

def getEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "delete")

	return(response)

def getPlan(PlanID, EntityID = 1, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "get", params_list = params_list)

	return(response)

def deletePlan(PlanID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "delete")

	return(response)

def getPlanDefault(PlanDefaultID, EntityID = 1, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "get", params_list = params_list)

	return(response)

def deletePlanDefault(PlanDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "delete")

	return(response)

def getPlanEntity(PlanEntityID, EntityID = 1, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "get", params_list = params_list)

	return(response)

def deletePlanEntity(PlanEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "delete")

	return(response)

def getQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "get", params_list = params_list)

	return(response)

def deleteQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "delete")

	return(response)

def getQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "get", params_list = params_list)

	return(response)

def deleteQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "delete")

	return(response)

def getStudentArea(StudentAreaID, EntityID = 1, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentArea(StudentAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "delete")

	return(response)

def getStudentCareerPlan(StudentCareerPlanID, EntityID = 1, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentCareerPlan(StudentCareerPlanID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "delete")

	return(response)

def getStudentEndorsement(StudentEndorsementID, EntityID = 1, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsement(StudentEndorsementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "delete")

	return(response)

def getStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "delete")

	return(response)

def getStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "delete")

	return(response)

def getStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "delete")

	return(response)

def getStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "delete")

	return(response)

def getStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "delete")

	return(response)

def getStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "delete")

	return(response)

def getStudentPlan(StudentPlanID, EntityID = 1, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentPlan(StudentPlanID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "delete")

	return(response)

def getStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "delete")

	return(response)

def getStudentSubArea(StudentSubAreaID, EntityID = 1, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSubArea(StudentSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "delete")

	return(response)

def getStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "delete")

	return(response)

def getStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "delete")

	return(response)

def getSubArea(SubAreaID, EntityID = 1, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteSubArea(SubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "delete")

	return(response)

def getSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "delete")

	return(response)

def getSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "delete")

	return(response)

def getTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "delete")

	return(response)

def getTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "delete")

	return(response)

def getTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "delete")

	return(response)

def getTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "delete")

	return(response)