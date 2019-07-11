# This module contains Curriculum functions.

from .Utilities import make_request

import pandas as pd

def getEveryAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardID = True, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandard(AcademicStandardID, EntityID = 1, returnreturnAcademicStandardID = False, returnreturnAcademicStandardDefaultID = False, returnreturnAcademicStandardGradeRangeID = False, returnreturnAcademicStandardIDParent = False, returnreturnChildAcademicStandardCount = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDescriptionToUse = False, returnreturnDisplayAs = False, returnreturnDistrictGroupKey = False, returnreturnEnteredByDistrict = False, returnreturnExtendedDescription = False, returnreturnFullKey = False, returnreturnFullKeyPrefix = False, returnreturnGrandChildLevelHierarchyDepthDescription = False, returnreturnGuid = False, returnreturnHierarchyDepthDescription = False, returnreturnIsAttachedToASubject = False, returnreturnIsHighFrequencyWord = False, returnreturnIsLettersAndSounds = False, returnreturnIsPlaceHolder = False, returnreturnKey = False, returnreturnLabel = False, returnreturnLetterAndSoundType = False, returnreturnLetterAndSoundTypeCode = False, returnreturnLetterType = False, returnreturnLetterTypeCode = False, returnreturnLevel = False, returnreturnModifiedTime = False, returnreturnNextLevelHierarchyDepthDescription = False, returnreturnParentGuid = False, returnreturnSequence = False, returnreturnStateNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandard(AcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "delete")

	return(response)

def getEveryAcademicStandardDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardDefaultID = True, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1, returnreturnAcademicStandardDefaultID = False, returnreturnAcademicStandardDefaultIDParent = False, returnreturnAcademicStandardGradeRangeDefaultID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsHighFrequencyWord = False, returnreturnKey = False, returnreturnLetterAndSoundType = False, returnreturnLetterAndSoundTypeCode = False, returnreturnLetterType = False, returnreturnLetterTypeCode = False, returnreturnLevel = False, returnreturnModifiedTime = False, returnreturnParentGuid = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "delete")

	return(response)

def getEveryAcademicStandardGradeRange(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradeRangeID = True, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1, returnreturnAcademicStandardGradeRangeID = False, returnreturnAcademicStandardGradeRangeDefaultID = False, returnreturnAcademicStandardSubjectID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnEnteredByDistrict = False, returnreturnFullKey = False, returnreturnFullKeyPrefix = False, returnreturnGradeRangeHigh = False, returnreturnGradeRangeLow = False, returnreturnGuid = False, returnreturnKey = False, returnreturnModifiedTime = False, returnreturnSequence = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "delete")

	return(response)

def getEveryAcademicStandardGradeRangeDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradeRangeDefaultID = True, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1, returnreturnAcademicStandardGradeRangeDefaultID = False, returnreturnAcademicStandardSubjectDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnKey = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "delete")

	return(response)

def getEveryAcademicStandardHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardHierarchyDepthID = True, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1, returnreturnAcademicStandardHierarchyDepthID = False, returnreturnAcademicStandardID = False, returnreturnAcademicStandardIDAtLevel = False, returnreturnCreatedTime = False, returnreturnDistrictGroupKey = False, returnreturnHierarchyDepthID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "delete")

	return(response)

def getEveryAcademicStandardSet(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSetID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardSet(AcademicStandardSetID, EntityID = 1, returnreturnAcademicStandardSetID = False, returnreturnAcademicStandardSetDefaultID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnEnteredByDistrict = False, returnreturnIsActive = False, returnreturnKey = False, returnreturnModifiedTime = False, returnreturnStateCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSet(AcademicStandardSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "delete")

	return(response)

def getEveryAcademicStandardSetDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSetDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1, returnreturnAcademicStandardSetDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnKey = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "delete")

	return(response)

def getEveryAcademicStandardSubject(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSubjectID = True, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1, returnreturnAcademicStandardSubjectID = False, returnreturnAcademicStandardSetID = False, returnreturnAcademicStandardSubjectDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnEnteredByDistrict = False, returnreturnFullKey = False, returnreturnFullKeyPrefix = False, returnreturnKey = False, returnreturnModifiedTime = False, returnreturnSequence = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnYear = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "delete")

	return(response)

def getEveryAcademicStandardSubjectDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSubjectDefaultID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1, returnreturnAcademicStandardSubjectDefaultID = False, returnreturnAcademicStandardSetDefaultID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnKey = False, returnreturnModifiedTime = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "delete")

	return(response)

def getEveryAssessmentToolMN(EntityID = 1, page = 1, pageSize = 100, returnAssessmentToolMNID = True, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAssessmentToolMN(AssessmentToolMNID, EntityID = 1, returnreturnAssessmentToolMNID = False, returnreturnAssessmentToolMNIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnCurriculumYearID = False, returnreturnModifiedTime = False, returnreturnStateAssessmentToolMNID = False, returnreturnStateImplementationStatusMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "get", params_list = params_list)

	return(response)

def deleteAssessmentToolMN(AssessmentToolMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "delete")

	return(response)

def getEveryCurriculum(EntityID = 1, page = 1, pageSize = 100, returnCurriculumID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculum(CurriculumID, EntityID = 1, returnreturnCurriculumID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnCurriculumSubAreaExistsForStudentAndSubArea = False, returnreturnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnreturnCurriculumSubjectSummary = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnEarnedCredits = False, returnreturnGradeLevelSummary = False, returnreturnGradReqRankGPAIgnoreDuplicateCheck = False, returnreturnGradReqSubjectTypeID = False, returnreturnHasPrerequisiteCurriculums = False, returnreturnHasPrerequisites = False, returnreturnIsActive = False, returnreturnIsAllowedToBeSelectedInCareerPlan = False, returnreturnIsFederalDistanceEducation = False, returnreturnIsFederalDualEnrollment = False, returnreturnModifiedTime = False, returnreturnNumberOfActiveCurrentOrFutureCourses = False, returnreturnNumberOfAttachedSubjects = False, returnreturnPrerequisiteCurriculumExistsForPrerequisite = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculum(CurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "delete")

	return(response)

def getEveryCurriculumAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCurriculumAcademicStandardID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1, returnreturnCurriculumAcademicStandardID = False, returnreturnAcademicStandardID = False, returnreturnCreatedTime = False, returnreturnCurriculumID = False, returnreturnDistrictGroupKey = False, returnreturnIsGraded = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "delete")

	return(response)

def getEveryCurriculumCustomRequirement(EntityID = 1, page = 1, pageSize = 100, returnCurriculumCustomRequirementID = True, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1, returnreturnCurriculumCustomRequirementID = False, returnreturnCreatedTime = False, returnreturnCurriculumID = False, returnreturnCustomRequirementID = False, returnreturnDistrictGroupKey = False, returnreturnModifiedTime = False, returnreturnSchoolYearHigh = False, returnreturnSchoolYearLow = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "delete")

	return(response)

def getEveryCurriculumGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnCurriculumGradeLevelID = True, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1, returnreturnCurriculumGradeLevelID = False, returnreturnCreatedTime = False, returnreturnCurriculumID = False, returnreturnDistrictGroupKey = False, returnreturnGradeLevelID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "delete")

	return(response)

def getEveryCurriculumProgramMN(EntityID = 1, page = 1, pageSize = 100, returnCurriculumProgramMNID = True, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1, returnreturnCurriculumProgramMNID = False, returnreturnCreatedTime = False, returnreturnCurriculumProgramMNIDClonedFrom = False, returnreturnCurriculumYearID = False, returnreturnModifiedTime = False, returnreturnStateCurriculumProgramMNID = False, returnreturnStateImplementationStatusMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "delete")

	return(response)

def getEveryCurriculumSubject(EntityID = 1, page = 1, pageSize = 100, returnCurriculumSubjectID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumSubject(CurriculumSubjectID, EntityID = 1, returnreturnCurriculumSubjectID = False, returnreturnCreatedTime = False, returnreturnCurriculumID = False, returnreturnCurriculumSubjectIDClonedFrom = False, returnreturnCurriculumSubjectIDClonedTo = False, returnreturnDistrictGroupKey = False, returnreturnIsDefault = False, returnreturnModifiedTime = False, returnreturnNumberOfAttachedCurriculumAcademicStandards = False, returnreturnSubjectID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumSubject(CurriculumSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "delete")

	return(response)

def getEveryCurriculumSubjectAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCurriculumSubjectAcademicStandardID = True, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1, returnreturnCurriculumSubjectAcademicStandardID = False, returnreturnCreatedTime = False, returnreturnCurriculumAcademicStandardID = False, returnreturnCurriculumSubjectID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "delete")

	return(response)

def getEveryCurriculumYear(EntityID = 1, page = 1, pageSize = 100, returnCurriculumYearID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCurriculumYear(CurriculumYearID, EntityID = 1, returnreturnCurriculumYearID = False, returnreturnCreatedTime = False, returnreturnCurriculumID = False, returnreturnCurriculumYearIDClonedFrom = False, returnreturnCurriculumYearIDClonedTo = False, returnreturnCurriculumYearMNID = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnFederalAdvancedPlacementCourseTypeID = False, returnreturnFederalSubjectTypeID = False, returnreturnHasCourseLevels = False, returnreturnIsAdultBasicEducation = False, returnreturnIsEndOfCourse = False, returnreturnIsFederalDistanceEducation = False, returnreturnIsFederalDualEnrollment = False, returnreturnIsFederalProgram = False, returnreturnIsGraduationRequirement = False, returnreturnIsStateProgram = False, returnreturnModifiedTime = False, returnreturnReportToFitnessGram = False, returnreturnSchoolYearID = False, returnreturnStateCourseCodeMNID = False, returnreturnStateEarlyEducationLocationMNID = False, returnreturnStateStandardAddressedCodeMNID = False, returnreturnStateSTARAssignmentCodeMNID = False, returnreturnStateSubjectAreaCodeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "get", params_list = params_list)

	return(response)

def deleteCurriculumYear(CurriculumYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "delete")

	return(response)

def getEveryEarlyEducationInstructionalApproachMN(EntityID = 1, page = 1, pageSize = 100, returnEarlyEducationInstructionalApproachMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1, returnreturnEarlyEducationInstructionalApproachMNID = False, returnreturnCreatedTime = False, returnreturnCurriculumYearID = False, returnreturnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnreturnModifiedTime = False, returnreturnStateEarlyEducationInstructionalApproachMNID = False, returnreturnStateImplementationStatusMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "get", params_list = params_list)

	return(response)

def deleteEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "delete")

	return(response)

def getEveryEarlyEducationProgramMN(EntityID = 1, page = 1, pageSize = 100, returnEarlyEducationProgramMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1, returnreturnEarlyEducationProgramMNID = False, returnreturnCreatedTime = False, returnreturnCurriculumYearID = False, returnreturnEarlyEducationProgramMNIDClonedFrom = False, returnreturnModifiedTime = False, returnreturnStateEarlyEducationProgramMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "get", params_list = params_list)

	return(response)

def deleteEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "delete")

	return(response)

def getEveryHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnHierarchyDepthID = True, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHierarchyDepth(HierarchyDepthID, EntityID = 1, returnreturnHierarchyDepthID = False, returnreturnAcademicStandardSetID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDepthLevel = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteHierarchyDepth(HierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "delete")

	return(response)

def getEveryPrerequisite(EntityID = 1, page = 1, pageSize = 100, returnPrerequisiteID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPrerequisite(PrerequisiteID, EntityID = 1, returnreturnPrerequisiteID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnCurriculumID = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnEarnedCredits = False, returnreturnHasPrerequisiteCurriculums = False, returnreturnModifiedTime = False, returnreturnSchoolYearHigh = False, returnreturnSchoolYearLow = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "get", params_list = params_list)

	return(response)

def deletePrerequisite(PrerequisiteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "delete")

	return(response)

def getEveryPrerequisiteCurriculum(EntityID = 1, page = 1, pageSize = 100, returnPrerequisiteCurriculumID = True, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1, returnreturnPrerequisiteCurriculumID = False, returnreturnCreatedTime = False, returnreturnCurriculumIDRequired = False, returnreturnModifiedTime = False, returnreturnPrerequisiteID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "get", params_list = params_list)

	return(response)

def deletePrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "delete")

	return(response)

def getEverySiteBasedInitiativeMN(EntityID = 1, page = 1, pageSize = 100, returnSiteBasedInitiativeMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1, returnreturnSiteBasedInitiativeMNID = False, returnreturnCreatedTime = False, returnreturnCurriculumYearID = False, returnreturnModifiedTime = False, returnreturnSiteBasedInitiativeMNIDClonedFrom = False, returnreturnStateImplementationStatusMNID = False, returnreturnStateSiteBasedInitiativeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "get", params_list = params_list)

	return(response)

def deleteSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "delete")

	return(response)

def getEveryStandardPlacementMN(EntityID = 1, page = 1, pageSize = 100, returnStandardPlacementMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStandardPlacementMN(StandardPlacementMNID, EntityID = 1, returnreturnStandardPlacementMNID = False, returnreturnCreatedTime = False, returnreturnCurriculumYearID = False, returnreturnModifiedTime = False, returnreturnStateStandardCodeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "get", params_list = params_list)

	return(response)

def deleteStandardPlacementMN(StandardPlacementMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "delete")

	return(response)

def getEverySubject(EntityID = 1, page = 1, pageSize = 100, returnSubjectID = True, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSubject(SubjectID, EntityID = 1, returnreturnSubjectID = False, returnreturnBackgroundColor = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsPrimaryForSelectedCurriculum = False, returnreturnModifiedTime = False, returnreturnNumberOfAttachedCurriculums = False, returnreturnSchoolYearID = False, returnreturnSubjectIDClonedFrom = False, returnreturnSubjectIDClonedTo = False, returnreturnTextColor = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteSubject(SubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "delete")

	return(response)

def getEveryTempAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardID = True, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAcademicStandard(TempAcademicStandardID, EntityID = 1, returnreturnTempAcademicStandardID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEnteredByDistrict = False, returnreturnExtendedDescription = False, returnreturnGuid = False, returnreturnImportedFrom = False, returnreturnIsPlaceHolder = False, returnreturnKey = False, returnreturnLabel = False, returnreturnLevel = False, returnreturnModifiedTime = False, returnreturnParentGuid = False, returnreturnSequence = False, returnreturnStateNumber = False, returnreturnTempAcademicStandardGradeRangeID = False, returnreturnTempAcademicStandardIDParent = False, returnreturnTempAcademicStandardSetID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandard(TempAcademicStandardID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "delete")

	return(response)

def getEveryTempAcademicStandardGradeRange(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardGradeRangeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1, returnreturnTempAcademicStandardGradeRangeID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEnteredByDistrict = False, returnreturnGradeRangeHigh = False, returnreturnGradeRangeLow = False, returnreturnGuid = False, returnreturnImportedFrom = False, returnreturnModifiedTime = False, returnreturnSequence = False, returnreturnTempAcademicStandardSubjectID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "delete")

	return(response)

def getEveryTempAcademicStandardSet(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardSetID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1, returnreturnTempAcademicStandardSetID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEnteredByDistrict = False, returnreturnImportedFrom = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnStateCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "delete")

	return(response)

def getEveryTempAcademicStandardSubject(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardSubjectID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1, returnreturnTempAcademicStandardSubjectID = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEnteredByDistrict = False, returnreturnImportedFrom = False, returnreturnModifiedTime = False, returnreturnSequence = False, returnreturnTempAcademicStandardSetID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnYear = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "delete")

	return(response)

def getEveryTempGradeRangeCopyResult(EntityID = 1, page = 1, pageSize = 100, returnTempGradeRangeCopyResultID = True, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1, returnreturnTempGradeRangeCopyResultID = False, returnreturnAcademicStandardSubjectCode = False, returnreturnCreatedTime = False, returnreturnErrorText = False, returnreturnGradeRangeCode = False, returnreturnIsError = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "delete")

	return(response)

def getEveryTempHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnTempHierarchyDepthID = True, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1, returnreturnTempHierarchyDepthID = False, returnreturnAcademicStandardSetCode = False, returnreturnAcademicStandardSetDescription = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnDepthLevel = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "delete")

	return(response)