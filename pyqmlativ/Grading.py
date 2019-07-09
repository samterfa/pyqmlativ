# This module contains Grading functions.

from . import make_request

def getCommentBucket(CommentBucketID, EntityID = 1, returnCommentBucketIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnGradingPeriodID = False, returnIsLimitedByCourse = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(CommentBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentBucket(CommentBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(CommentBucketID), verb = "delete")

	return(response)

def getCommentBucketCourse(CommentBucketCourseID, EntityID = 1, returnCommentBucketID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(CommentBucketCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentBucketCourse(CommentBucketCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(CommentBucketCourseID), verb = "delete")

	return(response)

def getCommentCode(CommentCodeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCommentCodeIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(CommentCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentCode(CommentCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(CommentCodeID), verb = "delete")

	return(response)

def getCommentSet(CommentSetID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCommentSetIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(CommentSetID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentSet(CommentSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(CommentSetID), verb = "delete")

	return(response)

def getConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCreditsRoundingDecimals = False, returnFinalGPADecimalSetting = False, returnFinalGPADecimalSettingCode = False, returnFinalGPARoundingDecimals = False, returnGPACalculationDecimalSetting = False, returnGPACalculationDecimalSettingCode = False, returnGPACalculationRoundingDecimals = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "delete")

	return(response)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentSectionLinkOption = False, returnStudentSectionLinkOptionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinkCourseType = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnCurrentCalculation = False, returnCurrentCalculationCode = False, returnEntityGroupKey = False, returnEntityID = False, returnFreeFormCommentMaxLength = False, returnGradebookLockMessage = False, returnGradeLevelIDCohort = False, returnLockGradebookAssignmentsAfterDate = False, returnLockGradebookCalculation = False, returnLockGradebookStartTime = False, returnLockGradeBuckets = False, returnModifiedTime = False, returnRetainGradesNumberOfDays = False, returnSchoolYearID = False, returnUseAddOnGPA = False, returnUseFactorBasedAddOn = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnElectronicSignatureIDReportCard = False, returnElectronicSignatureIDTranscript = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTranscriptTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):