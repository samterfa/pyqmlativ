# This module contains GraduationRequirements functions.

from .Utilities import make_request

import pandas as pd

def getEveryArea(EntityID = 1, page = 1, pageSize = 100, returnAreaID = True, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getArea(AreaID, EntityID = 1, returnreturnAreaID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayOrder = False, returnreturnElectiveSubAreaID = False, returnreturnGradReqRankGPARequiredCourseRuleOverride = False, returnreturnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnreturnIsElective = False, returnreturnIsNotElective = False, returnreturnIsNotSystemArea = False, returnreturnIsSystemArea = False, returnreturnModifiedTime = False, returnreturnNonElectiveCreditTotal = False, returnreturnPlanID = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnTotalCredits = False, returnreturnUseGradReqSubjectType = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "get", params_list = params_list)

	return(response)

def deleteArea(AreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "delete")

	return(response)

def getEveryCareerPlanDeclarationTimePeriod(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1, returnreturnCareerPlanDeclarationTimePeriodID = False, returnreturnCreatedTime = False, returnreturnEndTime = False, returnreturnEntityID = False, returnreturnFilterOption = False, returnreturnFilterOptionCode = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStartTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "delete")

	return(response)

def getEveryCareerPlanDeclarationTimePeriodGradeReference(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanDeclarationTimePeriodGradeReferenceID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnreturnCareerPlanDeclarationTimePeriodGradeReferenceID = False, returnreturnCareerPlanDeclarationTimePeriodID = False, returnreturnCreatedTime = False, returnreturnGradeReferenceID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "delete")

	return(response)

def getEveryCareerPlanDeclarationTimePeriodStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = True, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnreturnCareerPlanDeclarationTimePeriodStudentEntityYearID = False, returnreturnCareerPlanDeclarationTimePeriodID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnStudentEntityYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "delete")

	return(response)

def getEveryCareerPlanGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnCareerPlanGradeLevelID = True, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1, returnreturnCareerPlanGradeLevelID = False, returnreturnConfigDistrictID = False, returnreturnCreatedTime = False, returnreturnDisplayName = False, returnreturnGradeLevelID = False, returnreturnIsPriorLevel = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "delete")

	return(response)

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnreturnConfigDistrictID = False, returnreturnCourseWorkAppliedByType = False, returnreturnCourseWorkAppliedByTypeCode = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnGradingPeriodEndDateLastCheckedDate = False, returnreturnIncludeFutureCredit = False, returnreturnIncludeInProgressCredit = False, returnreturnModifiedTime = False, returnreturnTurnOffAutomaticCalculation = False, returnreturnTurnOffAutomaticEndorsementCalculation = False, returnreturnUsePriorToLastGradeLevel = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getEveryCurriculumCluster(EntityID = 1, page = 1, pageSize = 100, returnCurriculumClusterID = True, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumCluster(CurriculumClusterID, EntityID = 1, returnreturnCurriculumClusterID = False, returnreturnCreatedTime = False, returnreturnCurriculumClusterDefaultID = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumCluster(CurriculumClusterID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "delete")

	return(response)

def getEveryCurriculumClusterCurriculum(EntityID = 1, page = 1, pageSize = 100, returnCurriculumClusterCurriculumID = True, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1, returnreturnCurriculumClusterCurriculumID = False, returnreturnCreatedTime = False, returnreturnCurriculumClusterID = False, returnreturnCurriculumID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnIsAdvancedCredit = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "delete")

	return(response)

def getEveryCurriculumClusterDefault(EntityID = 1, page = 1, pageSize = 100, returnCurriculumClusterDefaultID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1, returnreturnCurriculumClusterDefaultID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "delete")

	return(response)

def getEveryCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnCurriculumSubAreaID = True, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumSubArea(CurriculumSubAreaID, EntityID = 1, returnreturnCurriculumSubAreaID = False, returnreturnAllowReuseOfPreviouslyAppliedCredits = False, returnreturnApplicationOrder = False, returnreturnCreatedTime = False, returnreturnCurriculumID = False, returnreturnIsCustomCurriculumSubAreaWithStudentID = False, returnreturnIsGradReqRankGPAWaiver = False, returnreturnMaximumPercentOfCourseCredit = False, returnreturnModifiedTime = False, returnreturnSchoolYearHigh = False, returnreturnSchoolYearLow = False, returnreturnStudentID = False, returnreturnSubAreaID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumSubArea(CurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "delete")

	return(response)

def getEveryEndorsement(EntityID = 1, page = 1, pageSize = 100, returnEndorsementID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsement(EndorsementID, EntityID = 1, returnreturnEndorsementID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEndorsementDefaultID = False, returnreturnHasEndorsementOptions = False, returnreturnIsActive = False, returnreturnIsDeclarable = False, returnreturnIsPreviouslyLoaded = False, returnreturnModifiedTime = False, returnreturnPrintOnTranscript = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsement(EndorsementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "delete")

	return(response)

def getEveryEndorsementDeclarationTimePeriod(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDeclarationTimePeriodID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1, returnreturnEndorsementDeclarationTimePeriodID = False, returnreturnCreatedTime = False, returnreturnEndTime = False, returnreturnEntityID = False, returnreturnFilterOption = False, returnreturnFilterOptionCode = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStartTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "delete")

	return(response)

def getEveryEndorsementDeclarationTimePeriodGradeReference(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDeclarationTimePeriodGradeReferenceID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnreturnEndorsementDeclarationTimePeriodGradeReferenceID = False, returnreturnCreatedTime = False, returnreturnEndorsementDeclarationTimePeriodID = False, returnreturnGradeReferenceID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "delete")

	return(response)

def getEveryEndorsementDeclarationTimePeriodStudentEntityYear(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDeclarationTimePeriodStudentEntityYearID = True, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnreturnEndorsementDeclarationTimePeriodStudentEntityYearID = False, returnreturnCreatedTime = False, returnreturnEndorsementDeclarationTimePeriodID = False, returnreturnModifiedTime = False, returnreturnStudentEntityYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "delete")

	return(response)

def getEveryEndorsementDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementDefault(EndorsementDefaultID, EntityID = 1, returnreturnEndorsementDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsActive = False, returnreturnIsDeclarable = False, returnreturnModifiedTime = False, returnreturnPrintOnTranscript = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementDefault(EndorsementDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "delete")

	return(response)

def getEveryEndorsementOption(EntityID = 1, page = 1, pageSize = 100, returnEndorsementOptionID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementOption(EndorsementOptionID, EntityID = 1, returnreturnEndorsementOptionID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndorsementID = False, returnreturnEndorsementOptionDefaultID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnModifiedTime = False, returnreturnMustCompleteGradPlan = False, returnreturnOrderNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementOption(EndorsementOptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "delete")

	return(response)

def getEveryEndorsementOptionDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementOptionDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1, returnreturnEndorsementOptionDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndorsementDefaultID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnModifiedTime = False, returnreturnMustCompleteGradPlan = False, returnreturnOrderNumber = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "delete")

	return(response)

def getEveryEndorsementRequirement(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirement(EndorsementRequirementID, EntityID = 1, returnreturnEndorsementRequirementID = False, returnreturnAdvancedCreditsRequired = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndorsementOptionID = False, returnreturnEndorsementRequirementDefaultID = False, returnreturnMaximumClusterLimit = False, returnreturnMinimumClusterLimit = False, returnreturnModifiedTime = False, returnreturnMustFulfillAllCurriculumClusters = False, returnreturnOrderNumber = False, returnreturnOverallCreditsRequired = False, returnreturnRequirementAssessmentType = False, returnreturnRequirementAssessmentTypeCode = False, returnreturnRequirementType = False, returnreturnRequirementTypeCode = False, returnreturnUseMaximumClusterLimit = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirement(EndorsementRequirementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementAssessment(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1, returnreturnEndorsementRequirementAssessmentID = False, returnreturnClusterType = False, returnreturnClusterTypeCode = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementAssessmentDefaultID = False, returnreturnEndorsementRequirementID = False, returnreturnModifiedTime = False, returnreturnTestType = False, returnreturnTestTypeCode = False, returnreturnTestVersion = False, returnreturnTestVersionCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementAssessmentCluster(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentClusterID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1, returnreturnEndorsementRequirementAssessmentClusterID = False, returnreturnClusterScoreType = False, returnreturnClusterScoreTypeCode = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementAssessmentClusterDefaultID = False, returnreturnEndorsementRequirementAssessmentID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementAssessmentClusterDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentClusterDefaultID = True, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1, returnreturnEndorsementRequirementAssessmentClusterDefaultID = False, returnreturnClusterScoreType = False, returnreturnClusterScoreTypeCode = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementAssessmentDefaultID = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementAssessmentDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentDefaultID = True, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1, returnreturnEndorsementRequirementAssessmentDefaultID = False, returnreturnClusterType = False, returnreturnClusterTypeCode = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementDefaultID = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnTestType = False, returnreturnTestTypeCode = False, returnreturnTestVersion = False, returnreturnTestVersionCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementAssessmentScore(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentScoreID = True, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1, returnreturnEndorsementRequirementAssessmentScoreID = False, returnreturnAssessmentScoreColumn = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementAssessmentClusterID = False, returnreturnEndorsementRequirementAssessmentScoreDefaultID = False, returnreturnModifiedTime = False, returnreturnPassingScore = False, returnreturnPassingScoreHigh = False, returnreturnPassingScoreLow = False, returnreturnScoreLocation = False, returnreturnScoreType = False, returnreturnScoreTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementAssessmentScoreDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementAssessmentScoreDefaultID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1, returnreturnEndorsementRequirementAssessmentScoreDefaultID = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementAssessmentClusterDefaultID = False, returnreturnModifiedTime = False, returnreturnPassingScore = False, returnreturnPassingScoreHigh = False, returnreturnPassingScoreLow = False, returnreturnScoreLocation = False, returnreturnScoreType = False, returnreturnScoreTypeCode = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementCurriculum(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementCurriculumID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1, returnreturnEndorsementRequirementCurriculumID = False, returnreturnAdvancedCreditsRequired = False, returnreturnCreatedTime = False, returnreturnCreditsRequired = False, returnreturnCurriculumClusterID = False, returnreturnEndorsementRequirementCurriculumDefaultID = False, returnreturnEndorsementRequirementID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementCurriculumDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementCurriculumDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1, returnreturnEndorsementRequirementCurriculumDefaultID = False, returnreturnAdvancedCreditsRequired = False, returnreturnCreatedTime = False, returnreturnCreditsRequired = False, returnreturnCurriculumClusterDefaultID = False, returnreturnEndorsementRequirementDefaultID = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "delete")

	return(response)

def getEveryEndorsementRequirementDefault(EntityID = 1, page = 1, pageSize = 100, returnEndorsementRequirementDefaultID = True, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1, returnreturnEndorsementRequirementDefaultID = False, returnreturnAdvancedCreditsRequired = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndorsementOptionDefaultID = False, returnreturnMaximumClusterLimit = False, returnreturnMinimumClusterLimit = False, returnreturnModifiedTime = False, returnreturnMustFulfillAllCurriculumClusters = False, returnreturnOrderNumber = False, returnreturnOverallCreditsRequired = False, returnreturnRequirementAssessmentType = False, returnreturnRequirementAssessmentTypeCode = False, returnreturnRequirementType = False, returnreturnRequirementTypeCode = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUseMaximumClusterLimit = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "delete")

	return(response)

def getEveryPlan(EntityID = 1, page = 1, pageSize = 100, returnPlanID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPlan(PlanID, EntityID = 1, returnreturnPlanID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEdFiGraduationPlanID = False, returnreturnGeneralElectiveSubAreaID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnIsNotSystemPlan = False, returnreturnIsSystemPlan = False, returnreturnModifiedTime = False, returnreturnNonElectiveCreditTotal = False, returnreturnNumberOfSubAreasForCurriculum = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnTotalCredits = False, returnreturnTotalYears = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "get", params_list = params_list)

	return(response)

def deletePlan(PlanID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "delete")

	return(response)

def getEveryPlanDefault(EntityID = 1, page = 1, pageSize = 100, returnPlanDefaultID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPlanDefault(PlanDefaultID, EntityID = 1, returnreturnPlanDefaultID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnModifiedTime = False, returnreturnPlanID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "get", params_list = params_list)

	return(response)

def deletePlanDefault(PlanDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "delete")

	return(response)

def getEveryPlanEntity(EntityID = 1, page = 1, pageSize = 100, returnPlanEntityID = True, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPlanEntity(PlanEntityID, EntityID = 1, returnreturnPlanEntityID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnGradYearRange = False, returnreturnModifiedTime = False, returnreturnPlanID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "get", params_list = params_list)

	return(response)

def deletePlanEntity(PlanEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "delete")

	return(response)

def getEveryQueuedGraduationPlanRecalcTrigger(EntityID = 1, page = 1, pageSize = 100, returnQueuedGraduationPlanRecalcTriggerID = True, returnCreatedTime = False, returnModifiedTime = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1, returnreturnQueuedGraduationPlanRecalcTriggerID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnSourceID = False, returnreturnSourceObject = False, returnreturnSourceObjectCode = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "get", params_list = params_list)

	return(response)

def deleteQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "delete")

	return(response)

def getEveryQueuedStudentPlanCourseworkApplication(EntityID = 1, page = 1, pageSize = 100, returnQueuedStudentPlanCourseworkApplicationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1, returnreturnQueuedStudentPlanCourseworkApplicationID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnEndTime = False, returnreturnHostName = False, returnreturnModifiedTime = False, returnreturnProcessID = False, returnreturnRecalculationStatusDetails = False, returnreturnStartTime = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnStudentPlanID = False, returnreturnThreadName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDImpersonator = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "get", params_list = params_list)

	return(response)

def deleteQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "delete")

	return(response)

def getEveryStudentArea(EntityID = 1, page = 1, pageSize = 100, returnStudentAreaID = True, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentArea(StudentAreaID, EntityID = 1, returnreturnStudentAreaID = False, returnreturnAreaID = False, returnreturnAttemptedCredits = False, returnreturnCompletedCredits = False, returnreturnCreatedTime = False, returnreturnFutureCredits = False, returnreturnInProgressCredits = False, returnreturnIsFulfilledInPlan = False, returnreturnModifiedTime = False, returnreturnPlannedCredits = False, returnreturnRemainingCredits = False, returnreturnStudentPlanID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWaivedCredits = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentArea(StudentAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "delete")

	return(response)

def getEveryStudentCareerPlan(EntityID = 1, page = 1, pageSize = 100, returnStudentCareerPlanID = True, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentCareerPlan(StudentCareerPlanID, EntityID = 1, returnreturnStudentCareerPlanID = False, returnreturnCareerPlanGradeLevelID = False, returnreturnCreatedTime = False, returnreturnCredits = False, returnreturnCurriculumID = False, returnreturnGradeListDisplay = False, returnreturnIsStudentPermittedToChangeGradeLevel = False, returnreturnIsStudentPermittedToDelete = False, returnreturnModifiedTime = False, returnreturnStudentCourseRequestID = False, returnreturnStudentID = False, returnreturnStudentSubAreaID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentCareerPlan(StudentCareerPlanID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "delete")

	return(response)

def getEveryStudentEndorsement(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementID = True, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEndorsement(StudentEndorsementID, EntityID = 1, returnreturnStudentEndorsementID = False, returnreturnAttachmentComments = False, returnreturnAttachmentCount = False, returnreturnAttachmentIndicatorColumn = False, returnreturnCompletionMethod = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnEndorsementID = False, returnreturnGuardianSignedTime = False, returnreturnHasDeclaredEndorsementOptions = False, returnreturnHasEndorsementOptions = False, returnreturnHasEndorsementOptionsToAddOrDeclare = False, returnreturnIsAdminAdded = False, returnreturnIsComplete = False, returnreturnIsDeclared = False, returnreturnIsReceived = False, returnreturnIsSignedByGuardian = False, returnreturnIsSignedByStudent = False, returnreturnModifiedTime = False, returnreturnNameIDGuardianSignedBy = False, returnreturnStudentID = False, returnreturnStudentSignedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsement(StudentEndorsementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "delete")

	return(response)

def getEveryStudentEndorsementOption(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementOptionID = True, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1, returnreturnStudentEndorsementOptionID = False, returnreturnAdminAdded = False, returnreturnCreatedTime = False, returnreturnEndorsementOptionID = False, returnreturnGradPlanInProgress = False, returnreturnIsComplete = False, returnreturnIsDeclared = False, returnreturnIsReceived = False, returnreturnModifiedTime = False, returnreturnOverallCreditsRequired = False, returnreturnStudentEndorsementID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "delete")

	return(response)

def getEveryStudentEndorsementRequirement(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1, returnreturnStudentEndorsementRequirementID = False, returnreturnAdvancedCreditsApplied = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementID = False, returnreturnIsComplete = False, returnreturnModifiedTime = False, returnreturnOverallCreditsApplied = False, returnreturnStudentEndorsementOptionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "delete")

	return(response)

def getEveryStudentEndorsementRequirementAssessment(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementAssessmentID = True, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1, returnreturnStudentEndorsementRequirementAssessmentID = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementAssessmentID = False, returnreturnIsComplete = False, returnreturnModifiedTime = False, returnreturnStudentEndorsementRequirementID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "delete")

	return(response)

def getEveryStudentEndorsementRequirementAssessmentScore(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementAssessmentScoreID = True, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1, returnreturnStudentEndorsementRequirementAssessmentScoreID = False, returnreturnAssessmentScore = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementAssessmentScoreID = False, returnreturnIsPassingScore = False, returnreturnModifiedTime = False, returnreturnStudentEndorsementRequirementAssessmentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "delete")

	return(response)

def getEveryStudentEndorsementRequirementCourseRequest(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementCourseRequestID = True, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1, returnreturnStudentEndorsementRequirementCourseRequestID = False, returnreturnAppliedAdvancedCredits = False, returnreturnAppliedOverallCredits = False, returnreturnApplyToType = False, returnreturnApplyToTypeCode = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementCurriculumID = False, returnreturnModifiedTime = False, returnreturnStudentCourseRequestID = False, returnreturnStudentEndorsementRequirementCurriculumID = False, returnreturnStudentEndorsementRequirementID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "delete")

	return(response)

def getEveryStudentEndorsementRequirementCurriculum(EntityID = 1, page = 1, pageSize = 100, returnStudentEndorsementRequirementCurriculumID = True, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1, returnreturnStudentEndorsementRequirementCurriculumID = False, returnreturnAdvancedCreditsApplied = False, returnreturnCreatedTime = False, returnreturnEndorsementRequirementCurriculumID = False, returnreturnIsComplete = False, returnreturnModifiedTime = False, returnreturnOverallCreditsApplied = False, returnreturnStudentEndorsementRequirementID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "delete")

	return(response)

def getEveryStudentPlan(EntityID = 1, page = 1, pageSize = 100, returnStudentPlanID = True, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentPlan(StudentPlanID, EntityID = 1, returnreturnStudentPlanID = False, returnreturnAttemptedCredits = False, returnreturnCompletedCredits = False, returnreturnCreatedTime = False, returnreturnFutureCredits = False, returnreturnInProgressCredits = False, returnreturnIsCurrent = False, returnreturnModifiedTime = False, returnreturnPlanID = False, returnreturnPlannedCredits = False, returnreturnRemainingCredits = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWaivedCredits = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentPlan(StudentPlanID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "delete")

	return(response)

def getEveryStudentPlanThreadLock(EntityID = 1, page = 1, pageSize = 100, returnStudentPlanThreadLockID = True, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1, returnreturnStudentPlanThreadLockID = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnStudentPlanID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "delete")

	return(response)

def getEveryStudentSubArea(EntityID = 1, page = 1, pageSize = 100, returnStudentSubAreaID = True, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentSubArea(StudentSubAreaID, EntityID = 1, returnreturnStudentSubAreaID = False, returnreturnAttemptedCredits = False, returnreturnCanAddManualStudentSubAreaCurriculumSubArea = False, returnreturnCanAddWaiver = False, returnreturnCanHaveWaiver = False, returnreturnCompletedCredits = False, returnreturnCreatedTime = False, returnreturnFutureCredits = False, returnreturnInProgressCredits = False, returnreturnIsFulfilledInPlan = False, returnreturnModifiedTime = False, returnreturnPlannedCredits = False, returnreturnRemainingCredits = False, returnreturnStudentAreaID = False, returnreturnStudentPlanID = False, returnreturnSubAreaID = False, returnreturnTotalManualCredits = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWaivedCredits = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSubArea(StudentSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "delete")

	return(response)

def getEveryStudentSubAreaCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnStudentSubAreaCurriculumSubAreaID = True, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1, returnreturnStudentSubAreaCurriculumSubAreaID = False, returnreturnAppliedOrder = False, returnreturnAttemptedCredits = False, returnreturnCompletedCredits = False, returnreturnCreatedTime = False, returnreturnCurriculumSubAreaID = False, returnreturnEntryMethod = False, returnreturnEntryMethodCode = False, returnreturnFutureCredits = False, returnreturnInProgressCredits = False, returnreturnIsAutomatic = False, returnreturnModifiedTime = False, returnreturnPlannedCredits = False, returnreturnStudentCourseRequestID = False, returnreturnStudentSubAreaID = False, returnreturnTotalCredits = False, returnreturnTotalNonAttemptedCredits = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "delete")

	return(response)

def getEveryStudentSubAreaWaiver(EntityID = 1, page = 1, pageSize = 100, returnStudentSubAreaWaiverID = True, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1, returnreturnStudentSubAreaWaiverID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnCredits = False, returnreturnModifiedTime = False, returnreturnStudentSubAreaID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "delete")

	return(response)

def getEverySubArea(EntityID = 1, page = 1, pageSize = 100, returnSubAreaID = True, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSubArea(SubAreaID, EntityID = 1, returnreturnSubAreaID = False, returnreturnAreaID = False, returnreturnAreaSubAreaDescription = False, returnreturnCreatedTime = False, returnreturnCredits = False, returnreturnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnreturnDescription = False, returnreturnDisplayOrder = False, returnreturnGradReqRankGPARequiredCourseRuleOverride = False, returnreturnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnreturnHasSkywardID = False, returnreturnIsElective = False, returnreturnIsSystemSubArea = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteSubArea(SubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "delete")

	return(response)

def getEverySubAreaLimitGroup(EntityID = 1, page = 1, pageSize = 100, returnSubAreaLimitGroupID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1, returnreturnSubAreaLimitGroupID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnCreditLimit = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnSubAreaID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "delete")

	return(response)

def getEverySubAreaLimitGroupCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnSubAreaLimitGroupCurriculumSubAreaID = True, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1, returnreturnSubAreaLimitGroupCurriculumSubAreaID = False, returnreturnCreatedTime = False, returnreturnCurriculumSubAreaID = False, returnreturnModifiedTime = False, returnreturnSubAreaLimitGroupID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "delete")

	return(response)

def getEveryTempEndorsementDefault(EntityID = 1, page = 1, pageSize = 100, returnTempEndorsementDefaultID = True, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1, returnreturnTempEndorsementDefaultID = False, returnreturnActionType = False, returnreturnActionTypeCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnEndorsementDefaultID = False, returnreturnEndorsementID = False, returnreturnModifiedTime = False, returnreturnPrintOnTranscript = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWaivable = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "delete")

	return(response)

def getEveryTempEndorsementImportError(EntityID = 1, page = 1, pageSize = 100, returnTempEndorsementImportErrorID = True, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1, returnreturnTempEndorsementImportErrorID = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnErrorString = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "delete")

	return(response)

def getEveryTempFailedStudentSubAreaCurriculumSubArea(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentSubAreaCurriculumSubAreaID = True, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1, returnreturnTempFailedStudentSubAreaCurriculumSubAreaID = False, returnreturnActionType = False, returnreturnAppliedOrder = False, returnreturnAreaSubAreaDescription = False, returnreturnAttemptedCredits = False, returnreturnCompletedCredits = False, returnreturnCourseCode = False, returnreturnCourseDescription = False, returnreturnCreatedTime = False, returnreturnCurriculumSubAreaID = False, returnreturnEntityCode = False, returnreturnFutureCredits = False, returnreturnInProgressCredits = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnSchoolYearDescription = False, returnreturnSectionCode = False, returnreturnStudentCourseRequestID = False, returnreturnStudentSubAreaID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "delete")

	return(response)

def getEveryTempFailedStudentSubAreaWaiver(EntityID = 1, page = 1, pageSize = 100, returnTempFailedStudentSubAreaWaiverID = True, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1, returnreturnTempFailedStudentSubAreaWaiverID = False, returnreturnActionType = False, returnreturnAreaSubAreaDescription = False, returnreturnCreatedTime = False, returnreturnCredits = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnStudentSubAreaID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "delete")

	return(response)