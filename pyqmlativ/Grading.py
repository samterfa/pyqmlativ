# This module contains Grading functions.

from .Utilities import make_request

import pandas as pd

def getEveryCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnCommentBucketID = True, returnCommentBucketIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnGradingPeriodID = False, returnIsLimitedByCourse = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCommentBucket(CommentBucketID, EntityID = 1, returnreturnCommentBucketID = False, returnreturnCommentBucketIDClonedFrom = False, returnreturnCommentSetID = False, returnreturnCreatedTime = False, returnreturnDisplayOrder = False, returnreturnEntityGroupKey = False, returnreturnGradingPeriodID = False, returnreturnIsLimitedByCourse = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(CommentBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentBucket(CommentBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(CommentBucketID), verb = "delete")

	return(response)

def getEveryCommentBucketCourse(EntityID = 1, page = 1, pageSize = 100, returnCommentBucketCourseID = True, returnCommentBucketID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCommentBucketCourse(CommentBucketCourseID, EntityID = 1, returnreturnCommentBucketCourseID = False, returnreturnCommentBucketID = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(CommentBucketCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentBucketCourse(CommentBucketCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(CommentBucketCourseID), verb = "delete")

	return(response)

def getEveryCommentCode(EntityID = 1, page = 1, pageSize = 100, returnCommentCodeID = True, returnCode = False, returnCodeDescription = False, returnCommentCodeIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCommentCode(CommentCodeID, EntityID = 1, returnreturnCommentCodeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCommentCodeIDClonedFrom = False, returnreturnCommentSetID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(CommentCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentCode(CommentCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(CommentCodeID), verb = "delete")

	return(response)

def getEveryCommentSet(EntityID = 1, page = 1, pageSize = 100, returnCommentSetID = True, returnCode = False, returnCodeDescription = False, returnCommentSetIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCommentSet(CommentSetID, EntityID = 1, returnreturnCommentSetID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCommentSetIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(CommentSetID), verb = "get", params_list = params_list)

	return(response)

def deleteCommentSet(CommentSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(CommentSetID), verb = "delete")

	return(response)

def getEveryConfigDistrictGroup(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictGroupID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCreditsRoundingDecimals = False, returnFinalGPADecimalSetting = False, returnFinalGPADecimalSettingCode = False, returnFinalGPARoundingDecimals = False, returnGPACalculationDecimalSetting = False, returnGPACalculationDecimalSettingCode = False, returnGPACalculationRoundingDecimals = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1, returnreturnConfigDistrictGroupID = False, returnreturnCreatedTime = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnEarnedCreditsRoundingDecimals = False, returnreturnFinalGPADecimalSetting = False, returnreturnFinalGPADecimalSettingCode = False, returnreturnFinalGPARoundingDecimals = False, returnreturnGPACalculationDecimalSetting = False, returnreturnGPACalculationDecimalSettingCode = False, returnreturnGPACalculationRoundingDecimals = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "delete")

	return(response)

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentSectionLinkOption = False, returnStudentSectionLinkOptionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinkCourseType = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnreturnConfigDistrictYearID = False, returnreturnConfigDistrictYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStudentSectionLinkOption = False, returnreturnStudentSectionLinkOptionCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUseStudentSectionLinkCourseType = False, returnreturnUseStudentSectionLinking = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnCurrentCalculation = False, returnCurrentCalculationCode = False, returnEntityGroupKey = False, returnEntityID = False, returnFreeFormCommentMaxLength = False, returnGradebookLockMessage = False, returnGradeLevelIDCohort = False, returnLockGradebookAssignmentsAfterDate = False, returnLockGradebookCalculation = False, returnLockGradebookStartTime = False, returnLockGradeBuckets = False, returnModifiedTime = False, returnRetainGradesNumberOfDays = False, returnSchoolYearID = False, returnUseAddOnGPA = False, returnUseFactorBasedAddOn = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnreturnConfigEntityGroupYearID = False, returnreturnConfigEntityGroupYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnCurrentCalculation = False, returnreturnCurrentCalculationCode = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnFreeFormCommentMaxLength = False, returnreturnGradebookLockMessage = False, returnreturnGradeLevelIDCohort = False, returnreturnLockGradebookAssignmentsAfterDate = False, returnreturnLockGradebookCalculation = False, returnreturnLockGradebookStartTime = False, returnreturnLockGradeBuckets = False, returnreturnModifiedTime = False, returnreturnRetainGradesNumberOfDays = False, returnreturnSchoolYearID = False, returnreturnUseAddOnGPA = False, returnreturnUseFactorBasedAddOn = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getEveryConfigEntityYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnElectronicSignatureIDReportCard = False, returnElectronicSignatureIDTranscript = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTranscriptTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnreturnConfigEntityYearID = False, returnreturnConfigEntityYearIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnElectronicSignatureIDReportCard = False, returnreturnElectronicSignatureIDTranscript = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnTranscriptTitle = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "delete")

	return(response)

def getEveryCourseGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnCourseGPAMethodID = True, returnCourseGPAMethodIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPACredit = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCourseGPAMethod(CourseGPAMethodID, EntityID = 1, returnreturnCourseGPAMethodID = False, returnreturnCourseGPAMethodIDClonedFrom = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGPACredit = False, returnreturnGPACredits = False, returnreturnGPAMethodEntityID = False, returnreturnModifiedTime = False, returnreturnPointSetEntityID = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(CourseGPAMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteCourseGPAMethod(CourseGPAMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(CourseGPAMethodID), verb = "delete")

	return(response)

def getEveryCourseGPAMethodGradeReferenceOverride(EntityID = 1, page = 1, pageSize = 100, returnCourseGPAMethodGradeReferenceOverrideID = True, returnCourseGPAMethodID = False, returnCreatedTime = False, returnGPACredits = False, returnGradeReferenceID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCourseGPAMethodGradeReferenceOverride(CourseGPAMethodGradeReferenceOverrideID, EntityID = 1, returnreturnCourseGPAMethodGradeReferenceOverrideID = False, returnreturnCourseGPAMethodID = False, returnreturnCreatedTime = False, returnreturnGPACredits = False, returnreturnGradeReferenceID = False, returnreturnModifiedTime = False, returnreturnPointSetEntityID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(CourseGPAMethodGradeReferenceOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteCourseGPAMethodGradeReferenceOverride(CourseGPAMethodGradeReferenceOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(CourseGPAMethodGradeReferenceOverrideID), verb = "delete")

	return(response)

def getEveryEarnedCreditsBucketGroup(EntityID = 1, page = 1, pageSize = 100, returnEarnedCreditsBucketGroupID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupIDClonedFrom = False, returnEntityGroupKey = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEarnedCreditsBucketGroup(EarnedCreditsBucketGroupID, EntityID = 1, returnreturnEarnedCreditsBucketGroupID = False, returnreturnCreatedTime = False, returnreturnEarnedCreditsBucketGroupIDClonedFrom = False, returnreturnEntityGroupKey = False, returnreturnGradingPeriodSetID = False, returnreturnModifiedTime = False, returnreturnSectionLengthID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(EarnedCreditsBucketGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteEarnedCreditsBucketGroup(EarnedCreditsBucketGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(EarnedCreditsBucketGroupID), verb = "delete")

	return(response)

def getEveryEarnedCreditsBucketGroupGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnEarnedCreditsBucketGroupGradeBucketID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketIDClonedFrom = False, returnEarnedCreditsBucketGroupID = False, returnEntityGroupKey = False, returnGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEarnedCreditsBucketGroupGradeBucket(EarnedCreditsBucketGroupGradeBucketID, EntityID = 1, returnreturnEarnedCreditsBucketGroupGradeBucketID = False, returnreturnCreatedTime = False, returnreturnEarnedCreditsBucketGroupGradeBucketIDClonedFrom = False, returnreturnEarnedCreditsBucketGroupID = False, returnreturnEntityGroupKey = False, returnreturnGradeBucketID = False, returnreturnModifiedTime = False, returnreturnPercent = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(EarnedCreditsBucketGroupGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteEarnedCreditsBucketGroupGradeBucket(EarnedCreditsBucketGroupGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(EarnedCreditsBucketGroupGradeBucketID), verb = "delete")

	return(response)

def getEveryEarnedCreditsBucketGroupGradeBucketStudentOverride(EntityID = 1, page = 1, pageSize = 100, returnEarnedCreditsBucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEarnedCreditsBucketGroupGradeBucketStudentOverride(EarnedCreditsBucketGroupGradeBucketStudentOverrideID, EntityID = 1, returnreturnEarnedCreditsBucketGroupGradeBucketStudentOverrideID = False, returnreturnCreatedTime = False, returnreturnEarnedCreditsBucketGroupGradeBucketID = False, returnreturnModifiedTime = False, returnreturnPercent = False, returnreturnStudentSectionID = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(EarnedCreditsBucketGroupGradeBucketStudentOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteEarnedCreditsBucketGroupGradeBucketStudentOverride(EarnedCreditsBucketGroupGradeBucketStudentOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(EarnedCreditsBucketGroupGradeBucketStudentOverrideID), verb = "delete")

	return(response)

def getEveryFactorBasedAddOn(EntityID = 1, page = 1, pageSize = 100, returnFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnFactorBasedAddOnIDClonedFrom = False, returnGPABucketEntityID = False, returnGradeReferenceID = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getFactorBasedAddOn(FactorBasedAddOnID, EntityID = 1, returnreturnFactorBasedAddOnID = False, returnreturnCreatedTime = False, returnreturnFactor = False, returnreturnFactorBasedAddOnIDClonedFrom = False, returnreturnGPABucketEntityID = False, returnreturnGradeReferenceID = False, returnreturnGradingEndDateCutoffForCumulative = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(FactorBasedAddOnID), verb = "get", params_list = params_list)

	return(response)

def deleteFactorBasedAddOn(FactorBasedAddOnID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(FactorBasedAddOnID), verb = "delete")

	return(response)

def getEveryGPABucket(EntityID = 1, page = 1, pageSize = 100, returnGPABucketID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnGPABucketTypeID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucket(GPABucketID, EntityID = 1, returnreturnGPABucketID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnGPABucketTypeID = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNameDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(GPABucketID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucket(GPABucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(GPABucketID), verb = "delete")

	return(response)

def getEveryGPABucketEntity(EntityID = 1, page = 1, pageSize = 100, returnGPABucketEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPABucketEntityIDClonedFrom = False, returnGPABucketID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucketEntity(GPABucketEntityID, EntityID = 1, returnreturnGPABucketEntityID = False, returnreturnCreatedTime = False, returnreturnDisplayOrder = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnFamilyAccessDisplayGradYearHigh = False, returnreturnFamilyAccessDisplayGradYearLow = False, returnreturnGPABucketEntityIDClonedFrom = False, returnreturnGPABucketID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUseForFamilyAccess = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(GPABucketEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucketEntity(GPABucketEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(GPABucketEntityID), verb = "delete")

	return(response)

def getEveryGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupIDClonedFrom = False, returnGPABucketGroupSummaryID = False, returnGPABucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucketGroup(GPABucketGroupID, EntityID = 1, returnreturnGPABucketGroupID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGPABucketGroupIDClonedFrom = False, returnreturnGPABucketGroupSummaryID = False, returnreturnGPABucketID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(GPABucketGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucketGroup(GPABucketGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(GPABucketGroupID), verb = "delete")

	return(response)

def getEveryGPABucketGroupGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupGradeBucketIDClonedFrom = False, returnGPABucketGroupID = False, returnGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnIsUpToDate = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucketGroupGradeBucket(GPABucketGroupGradeBucketID, EntityID = 1, returnreturnGPABucketGroupGradeBucketID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGPABucketGroupGradeBucketIDClonedFrom = False, returnreturnGPABucketGroupID = False, returnreturnGradeBucketID = False, returnreturnGradeRequiredForGPABucket = False, returnreturnIsUpToDate = False, returnreturnModifiedTime = False, returnreturnPercent = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(GPABucketGroupGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucketGroupGradeBucket(GPABucketGroupGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(GPABucketGroupGradeBucketID), verb = "delete")

	return(response)

def getEveryGPABucketGroupGradeBucketStudentOverride(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnGPABucketGroupGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucketGroupGradeBucketStudentOverride(GPABucketGroupGradeBucketStudentOverrideID, EntityID = 1, returnreturnGPABucketGroupGradeBucketStudentOverrideID = False, returnreturnCreatedTime = False, returnreturnGPABucketGroupGradeBucketID = False, returnreturnGradeRequiredForGPABucket = False, returnreturnModifiedTime = False, returnreturnPercent = False, returnreturnStudentSectionID = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(GPABucketGroupGradeBucketStudentOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucketGroupGradeBucketStudentOverride(GPABucketGroupGradeBucketStudentOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(GPABucketGroupGradeBucketStudentOverrideID), verb = "delete")

	return(response)

def getEveryGPABucketGroupSummary(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupSummaryID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupSummaryIDClonedFrom = False, returnGPABucketSetID = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucketGroupSummary(GPABucketGroupSummaryID, EntityID = 1, returnreturnGPABucketGroupSummaryID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGPABucketGroupSummaryIDClonedFrom = False, returnreturnGPABucketSetID = False, returnreturnGradingPeriodSetID = False, returnreturnModifiedTime = False, returnreturnSectionLengthID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(GPABucketGroupSummaryID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucketGroupSummary(GPABucketGroupSummaryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(GPABucketGroupSummaryID), verb = "delete")

	return(response)

def getEveryGPABucketSet(EntityID = 1, page = 1, pageSize = 100, returnGPABucketSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucketSet(GPABucketSetID, EntityID = 1, returnreturnGPABucketSetID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNameDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(GPABucketSetID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucketSet(GPABucketSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(GPABucketSetID), verb = "delete")

	return(response)

def getEveryGPABucketType(EntityID = 1, page = 1, pageSize = 100, returnGPABucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPABucketType(GPABucketTypeID, EntityID = 1, returnreturnGPABucketTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnIsCumulative = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(GPABucketTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteGPABucketType(GPABucketTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(GPABucketTypeID), verb = "delete")

	return(response)

def getEveryGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodID = True, returnAllowFurtherAttemptsOfNonHighSchoolCourses = False, returnCancelSubAreaCreditFromMiddleSchoolCredit = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnExcludeTermTwoFinalYearGrade = False, returnGPABucketSetID = False, returnGradReqRankGPARequiredCourseRule = False, returnGradReqRankGPARequiredCourseRuleCode = False, returnLockGradeMarkPoints = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnSortNumber = False, returnTotalElectiveCreditsPossible = False, returnUseGradReqRankGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTotalElectiveCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPAMethod(GPAMethodID, EntityID = 1, returnreturnGPAMethodID = False, returnreturnAllowFurtherAttemptsOfNonHighSchoolCourses = False, returnreturnCancelSubAreaCreditFromMiddleSchoolCredit = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnExcludeTermTwoFinalYearGrade = False, returnreturnGPABucketSetID = False, returnreturnGradReqRankGPARequiredCourseRule = False, returnreturnGradReqRankGPARequiredCourseRuleCode = False, returnreturnLockGradeMarkPoints = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNameDescription = False, returnreturnSortNumber = False, returnreturnTotalElectiveCreditsPossible = False, returnreturnUseGradReqRankGPA = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUseTotalElectiveCredits = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(GPAMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteGPAMethod(GPAMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(GPAMethodID), verb = "delete")

	return(response)

def getEveryGPAMethodCourseGroup(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPAMethodCourseGroup(GPAMethodCourseGroupID, EntityID = 1, returnreturnGPAMethodCourseGroupID = False, returnreturnCourseGroupID = False, returnreturnCreatedTime = False, returnreturnGPAMethodID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(GPAMethodCourseGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteGPAMethodCourseGroup(GPAMethodCourseGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(GPAMethodCourseGroupID), verb = "delete")

	return(response)

def getEveryGPAMethodEntity(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPAMethodEntityIDClonedFrom = False, returnGPAMethodID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatus = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPAMethodEntity(GPAMethodEntityID, EntityID = 1, returnreturnGPAMethodEntityID = False, returnreturnCreatedTime = False, returnreturnDisplayOrder = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnFamilyAccessDisplayGradYearHigh = False, returnreturnFamilyAccessDisplayGradYearLow = False, returnreturnGPAMethodEntityIDClonedFrom = False, returnreturnGPAMethodID = False, returnreturnIsUpToDate = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStatus = False, returnreturnUseForFamilyAccess = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(GPAMethodEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteGPAMethodEntity(GPAMethodEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(GPAMethodEntityID), verb = "delete")

	return(response)

def getEveryGPAMethodGradeBucketFlagGPAPointsOverride(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodGradeBucketFlagGPAPointsOverrideID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGPAMethodGradeBucketFlagGPAPointsOverride(GPAMethodGradeBucketFlagGPAPointsOverrideID, EntityID = 1, returnreturnGPAMethodGradeBucketFlagGPAPointsOverrideID = False, returnreturnCreatedTime = False, returnreturnGPAMethodID = False, returnreturnGPAPoints = False, returnreturnGPAPointsOverrideOption = False, returnreturnGPAPointsOverrideOptionCode = False, returnreturnGradeBucketFlagID = False, returnreturnModifiedTime = False, returnreturnRank = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(GPAMethodGradeBucketFlagGPAPointsOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteGPAMethodGradeBucketFlagGPAPointsOverride(GPAMethodGradeBucketFlagGPAPointsOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(GPAMethodGradeBucketFlagGPAPointsOverrideID), verb = "delete")

	return(response)

def getEveryGradebookLockGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradebookLockGradeBucketID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradebookLockGradeBucket(GradebookLockGradeBucketID, EntityID = 1, returnreturnGradebookLockGradeBucketID = False, returnreturnConfigEntityGroupYearID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(GradebookLockGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteGradebookLockGradeBucket(GradebookLockGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(GradebookLockGradeBucketID), verb = "delete")

	return(response)

def getEveryGradebookLockGradeReference(EntityID = 1, page = 1, pageSize = 100, returnGradebookLockGradeReferenceID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradebookLockGradeReference(GradebookLockGradeReferenceID, EntityID = 1, returnreturnGradebookLockGradeReferenceID = False, returnreturnConfigEntityGroupYearID = False, returnreturnCreatedTime = False, returnreturnGradeReferenceID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(GradebookLockGradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteGradebookLockGradeReference(GradebookLockGradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(GradebookLockGradeReferenceID), verb = "delete")

	return(response)

def getEveryGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketID = True, returnCreatedTime = False, returnDescription = False, returnEdFiGradingPeriodDescriptorID = False, returnEdFiGradingPeriodID = False, returnEntityGroupKey = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGradeBucketIDClonedFrom = False, returnGradeBucketTypeID = False, returnLabel = False, returnLabelDescription = False, returnModifiedTime = False, returnNumber = False, returnOrder = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeBucket(GradeBucketID, EntityID = 1, returnreturnGradeBucketID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEdFiGradingPeriodDescriptorID = False, returnreturnEdFiGradingPeriodID = False, returnreturnEntityGroupKey = False, returnreturnFamilyAccessDisplayGradYearHigh = False, returnreturnFamilyAccessDisplayGradYearLow = False, returnreturnGradeBucketIDClonedFrom = False, returnreturnGradeBucketTypeID = False, returnreturnLabel = False, returnreturnLabelDescription = False, returnreturnModifiedTime = False, returnreturnNumber = False, returnreturnOrder = False, returnreturnUseForFamilyAccess = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(GradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeBucket(GradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(GradeBucketID), verb = "delete")

	return(response)

def getEveryGradeBucketFlag(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketFlagID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeBucketFlag(GradeBucketFlagID, EntityID = 1, returnreturnGradeBucketFlagID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayOrder = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(GradeBucketFlagID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeBucketFlag(GradeBucketFlagID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(GradeBucketFlagID), verb = "delete")

	return(response)

def getEveryGradeBucketFlagDetail(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketFlagDetailID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketFlagDetailIDClonedFrom = False, returnGradeBucketFlagID = False, returnIsActive = False, returnModifiedTime = False, returnPrintWithGradeMark = False, returnSchoolYearID = False, returnUseEarnedOverride = False, returnUseGPAOverride = False, returnUseGPAPointsOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeBucketFlagDetail(GradeBucketFlagDetailID, EntityID = 1, returnreturnGradeBucketFlagDetailID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGradeBucketFlagDetailIDClonedFrom = False, returnreturnGradeBucketFlagID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnPrintWithGradeMark = False, returnreturnSchoolYearID = False, returnreturnUseEarnedOverride = False, returnreturnUseGPAOverride = False, returnreturnUseGPAPointsOverride = False, returnreturnUseInEarned = False, returnreturnUseInFailed = False, returnreturnUseInGPA = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(GradeBucketFlagDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeBucketFlagDetail(GradeBucketFlagDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(GradeBucketFlagDetailID), verb = "delete")

	return(response)

def getEveryGradeBucketFlagDetailGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagDetailID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeBucketFlagDetailGPAMethod(GradeBucketFlagDetailGPAMethodID, EntityID = 1, returnreturnGradeBucketFlagDetailGPAMethodID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGPAMethodEntityID = False, returnreturnGPAPoints = False, returnreturnGPAPointsOverrideOption = False, returnreturnGPAPointsOverrideOptionCode = False, returnreturnGradeBucketFlagDetailID = False, returnreturnModifiedTime = False, returnreturnPointSetEntityID = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(GradeBucketFlagDetailGPAMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeBucketFlagDetailGPAMethod(GradeBucketFlagDetailGPAMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(GradeBucketFlagDetailGPAMethodID), verb = "delete")

	return(response)

def getEveryGradeBucketType(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEdFiGradeTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketTypeIDClonedFrom = False, returnHasSpecificCategories = False, returnMinimumPercent = False, returnModifiedTime = False, returnSchoolYearID = False, returnSnapshotGradeExtensionDays = False, returnSpecificCategoryGradeBucketTypeCount = False, returnUseAllCategories = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSnapshotGrade = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeBucketType(GradeBucketTypeID, EntityID = 1, returnreturnGradeBucketTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayOrder = False, returnreturnEdFiGradeTypeID = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGradeBucketTypeIDClonedFrom = False, returnreturnHasSpecificCategories = False, returnreturnMinimumPercent = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnSnapshotGradeExtensionDays = False, returnreturnSpecificCategoryGradeBucketTypeCount = False, returnreturnUseAllCategories = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUseSnapshotGrade = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(GradeBucketTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeBucketType(GradeBucketTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(GradeBucketTypeID), verb = "delete")

	return(response)

def getEveryGradeMark(EntityID = 1, page = 1, pageSize = 100, returnGradeMarkID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkExistsInSpecifcEntity = False, returnGradeMarkIDClonedFrom = False, returnGradeMarkIDReverse = False, returnGradeMarkMNID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnReportCardDisplayValue = False, returnSchoolYearID = False, returnStateGradeMarkMNID = False, returnTranscriptDisplayValue = False, returnUseAsTeacherOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeMark(GradeMarkID, EntityID = 1, returnreturnGradeMarkID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayOrder = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGradeMarkExistsInSpecifcEntity = False, returnreturnGradeMarkIDClonedFrom = False, returnreturnGradeMarkIDReverse = False, returnreturnGradeMarkMNID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnIsAHistoricRecord = False, returnreturnModifiedTime = False, returnreturnReportCardDisplayValue = False, returnreturnSchoolYearID = False, returnreturnStateGradeMarkMNID = False, returnreturnTranscriptDisplayValue = False, returnreturnUseAsTeacherOverride = False, returnreturnUseInEarned = False, returnreturnUseInFailed = False, returnreturnUseInGPA = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(GradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeMark(GradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(GradeMarkID), verb = "delete")

	return(response)

def getEveryGradeMarkPointSet(EntityID = 1, page = 1, pageSize = 100, returnGradeMarkPointSetID = True, returnAddOnPoints = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGradeMarkID = False, returnGradeMarkPointSetIDClonedFrom = False, returnModifiedTime = False, returnPointSetEntityID = False, returnRegularPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeMarkPointSet(GradeMarkPointSetID, EntityID = 1, returnreturnGradeMarkPointSetID = False, returnreturnAddOnPoints = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGPAMethodEntityID = False, returnreturnGradeMarkID = False, returnreturnGradeMarkPointSetIDClonedFrom = False, returnreturnModifiedTime = False, returnreturnPointSetEntityID = False, returnreturnRegularPoints = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(GradeMarkPointSetID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeMarkPointSet(GradeMarkPointSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(GradeMarkPointSetID), verb = "delete")

	return(response)

def getEveryGradeReportAcademicSession(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionID = True, returnCreatedTime = False, returnEarnedCredit = False, returnEarnedCreditAttempted = False, returnEarnedCreditsValue = False, returnEntryDate = False, returnGPAValue = False, returnGradeLevelCode = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportStudentID = False, returnHeaderDescription = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportAcademicSession(GradeReportAcademicSessionID, EntityID = 1, returnreturnGradeReportAcademicSessionID = False, returnreturnCreatedTime = False, returnreturnEarnedCredit = False, returnreturnEarnedCreditAttempted = False, returnreturnEarnedCreditsValue = False, returnreturnEntryDate = False, returnreturnGPAValue = False, returnreturnGradeLevelCode = False, returnreturnGradeReportAcademicSessionTemplateGroupID = False, returnreturnGradeReportStudentID = False, returnreturnHeaderDescription = False, returnreturnModifiedTime = False, returnreturnSchoolYearDescription = False, returnreturnSchoolYearID = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithdrawalDate = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(GradeReportAcademicSessionID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportAcademicSession(GradeReportAcademicSessionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(GradeReportAcademicSessionID), verb = "delete")

	return(response)

def getEveryGradeReportAcademicSessionTemplate(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateID = True, returnBreakBySchoolYear = False, returnCourseFilter = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnHeaderDescription = False, returnIncludeNonCreditEarningCourses = False, returnModifiedTime = False, returnSearchConditionFilter = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchoolYearDescending = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportAcademicSessionTemplate(GradeReportAcademicSessionTemplateID, EntityID = 1, returnreturnGradeReportAcademicSessionTemplateID = False, returnreturnBreakBySchoolYear = False, returnreturnCourseFilter = False, returnreturnCreatedTime = False, returnreturnGradeReportAcademicSessionTemplateGroupID = False, returnreturnHeaderDescription = False, returnreturnIncludeNonCreditEarningCourses = False, returnreturnModifiedTime = False, returnreturnSearchConditionFilter = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUseSchoolYearDescending = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(GradeReportAcademicSessionTemplateID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportAcademicSessionTemplate(GradeReportAcademicSessionTemplateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(GradeReportAcademicSessionTemplateID), verb = "delete")

	return(response)

def getEveryGradeReportAcademicSessionTemplateCourse(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateCourseID = True, returnCourseID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateCourseIDClonedFrom = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportAcademicSessionTemplateCourse(GradeReportAcademicSessionTemplateCourseID, EntityID = 1, returnreturnGradeReportAcademicSessionTemplateCourseID = False, returnreturnCourseID = False, returnreturnCreatedTime = False, returnreturnGradeReportAcademicSessionTemplateCourseIDClonedFrom = False, returnreturnGradeReportAcademicSessionTemplateID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(GradeReportAcademicSessionTemplateCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportAcademicSessionTemplateCourse(GradeReportAcademicSessionTemplateCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(GradeReportAcademicSessionTemplateCourseID), verb = "delete")

	return(response)

def getEveryGradeReportAcademicSessionTemplateCourseGroup(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportAcademicSessionTemplateCourseGroup(GradeReportAcademicSessionTemplateCourseGroupID, EntityID = 1, returnreturnGradeReportAcademicSessionTemplateCourseGroupID = False, returnreturnCourseGroupID = False, returnreturnCreatedTime = False, returnreturnGradeReportAcademicSessionTemplateID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(GradeReportAcademicSessionTemplateCourseGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportAcademicSessionTemplateCourseGroup(GradeReportAcademicSessionTemplateCourseGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(GradeReportAcademicSessionTemplateCourseGroupID), verb = "delete")

	return(response)

def getEveryGradeReportAcademicSessionTemplateGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateGradeLevelID = True, returnCreatedTime = False, returnGradeLevelID = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportAcademicSessionTemplateGradeLevel(GradeReportAcademicSessionTemplateGradeLevelID, EntityID = 1, returnreturnGradeReportAcademicSessionTemplateGradeLevelID = False, returnreturnCreatedTime = False, returnreturnGradeLevelID = False, returnreturnGradeReportAcademicSessionTemplateID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(GradeReportAcademicSessionTemplateGradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportAcademicSessionTemplateGradeLevel(GradeReportAcademicSessionTemplateGradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(GradeReportAcademicSessionTemplateGradeLevelID), verb = "delete")

	return(response)

def getEveryGradeReportAcademicSessionTemplateGroup(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateGroupID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnGPABucketID = False, returnGPAField = False, returnGPAFieldCode = False, returnGPALabel1 = False, returnGPAMethodID = False, returnIncludeEarnedCredits = False, returnIncludeGPA = False, returnIncludeSchoolYearDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportAcademicSessionTemplateGroup(GradeReportAcademicSessionTemplateGroupID, EntityID = 1, returnreturnGradeReportAcademicSessionTemplateGroupID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnGPABucketID = False, returnreturnGPAField = False, returnreturnGPAFieldCode = False, returnreturnGPALabel1 = False, returnreturnGPAMethodID = False, returnreturnIncludeEarnedCredits = False, returnreturnIncludeGPA = False, returnreturnIncludeSchoolYearDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(GradeReportAcademicSessionTemplateGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportAcademicSessionTemplateGroup(GradeReportAcademicSessionTemplateGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(GradeReportAcademicSessionTemplateGroupID), verb = "delete")

	return(response)

def getEveryGradeReportColumnAttendanceCategory(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnAttendanceCategoryID = True, returnCategory = False, returnCategoryCode = False, returnCreatedTime = False, returnGradeReportColumnAttendanceCategoryIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportColumnAttendanceCategory(GradeReportColumnAttendanceCategoryID, EntityID = 1, returnreturnGradeReportColumnAttendanceCategoryID = False, returnreturnCategory = False, returnreturnCategoryCode = False, returnreturnCreatedTime = False, returnreturnGradeReportColumnAttendanceCategoryIDClonedFrom = False, returnreturnGradeReportColumnGroupColumnID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(GradeReportColumnAttendanceCategoryID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportColumnAttendanceCategory(GradeReportColumnAttendanceCategoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(GradeReportColumnAttendanceCategoryID), verb = "delete")

	return(response)

def getEveryGradeReportColumnAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnAttendanceTermID = True, returnAttendanceTermID = False, returnCreatedTime = False, returnGradeReportColumnAttendanceTermIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportColumnAttendanceTerm(GradeReportColumnAttendanceTermID, EntityID = 1, returnreturnGradeReportColumnAttendanceTermID = False, returnreturnAttendanceTermID = False, returnreturnCreatedTime = False, returnreturnGradeReportColumnAttendanceTermIDClonedFrom = False, returnreturnGradeReportColumnGroupColumnID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(GradeReportColumnAttendanceTermID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportColumnAttendanceTerm(GradeReportColumnAttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(GradeReportColumnAttendanceTermID), verb = "delete")

	return(response)

def getEveryGradeReportColumnGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnGradeBucketID = True, returnCreatedTime = False, returnGradeReportColumnGradeBucketIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportColumnGradeBucket(GradeReportColumnGradeBucketID, EntityID = 1, returnreturnGradeReportColumnGradeBucketID = False, returnreturnCreatedTime = False, returnreturnGradeReportColumnGradeBucketIDClonedFrom = False, returnreturnGradeReportColumnGroupColumnID = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(GradeReportColumnGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportColumnGradeBucket(GradeReportColumnGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(GradeReportColumnGradeBucketID), verb = "delete")

	return(response)

def getEveryGradeReportColumnGroup(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnGroupID = True, returnAlwaysDisplayGradingColumns = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDescription = False, returnGradeReportColumnGroupIDClonedFrom = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportColumnGroup(GradeReportColumnGroupID, EntityID = 1, returnreturnGradeReportColumnGroupID = False, returnreturnAlwaysDisplayGradingColumns = False, returnreturnConfigDistrictYearID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnGradeReportColumnGroupIDClonedFrom = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(GradeReportColumnGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportColumnGroup(GradeReportColumnGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(GradeReportColumnGroupID), verb = "delete")

	return(response)

def getEveryGradeReportColumnGroupColumn(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnGroupColumnID = True, returnAttendanceOption = False, returnAttendanceOptionCode = False, returnColumnHeader = False, returnColumnType = False, returnColumnTypeCode = False, returnContinueIfBlank = False, returnCreatedTime = False, returnGradeReportColumnGroupColumnIDClonedFrom = False, returnGradeReportColumnGroupID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportColumnGroupColumn(GradeReportColumnGroupColumnID, EntityID = 1, returnreturnGradeReportColumnGroupColumnID = False, returnreturnAttendanceOption = False, returnreturnAttendanceOptionCode = False, returnreturnColumnHeader = False, returnreturnColumnType = False, returnreturnColumnTypeCode = False, returnreturnContinueIfBlank = False, returnreturnCreatedTime = False, returnreturnGradeReportColumnGroupColumnIDClonedFrom = False, returnreturnGradeReportColumnGroupID = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(GradeReportColumnGroupColumnID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportColumnGroupColumn(GradeReportColumnGroupColumnID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(GradeReportColumnGroupColumnID), verb = "delete")

	return(response)

def getEveryGradeReportEndorsementRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportEndorsementRowID = True, returnCreatedTime = False, returnDescription = False, returnGradeReportStudentID = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSort1 = False, returnSort2 = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportEndorsementRow(GradeReportEndorsementRowID, EntityID = 1, returnreturnGradeReportEndorsementRowID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnGradeReportStudentID = False, returnreturnIsDistrictDefined = False, returnreturnModifiedTime = False, returnreturnSort1 = False, returnreturnSort2 = False, returnreturnStatus = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(GradeReportEndorsementRowID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportEndorsementRow(GradeReportEndorsementRowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(GradeReportEndorsementRowID), verb = "delete")

	return(response)

def getEveryGradeReportGPARow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportGPARowID = True, returnCreatedTime = False, returnDataColumn1 = False, returnDataColumn2 = False, returnDataColumn3 = False, returnDataColumn4 = False, returnDataColumn5 = False, returnDataColumn6 = False, returnDataColumn7 = False, returnGPABucketDescription = False, returnGPABucketID = False, returnGPAMethodDescription = False, returnGPAMethodID = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportGPARow(GradeReportGPARowID, EntityID = 1, returnreturnGradeReportGPARowID = False, returnreturnCreatedTime = False, returnreturnDataColumn1 = False, returnreturnDataColumn2 = False, returnreturnDataColumn3 = False, returnreturnDataColumn4 = False, returnreturnDataColumn5 = False, returnreturnDataColumn6 = False, returnreturnDataColumn7 = False, returnreturnGPABucketDescription = False, returnreturnGPABucketID = False, returnreturnGPAMethodDescription = False, returnreturnGPAMethodID = False, returnreturnGradeReportAcademicSessionID = False, returnreturnGradeReportAcademicSessionSortNumber = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(GradeReportGPARowID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportGPARow(GradeReportGPARowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(GradeReportGPARowID), verb = "delete")

	return(response)

def getEveryGradeReportGradingScale(EntityID = 1, page = 1, pageSize = 100, returnGradeReportGradingScaleID = True, returnCreatedTime = False, returnDisplayType = False, returnDisplayTypeCode = False, returnFreeformText = False, returnGradeMarkCode = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnRangeHigh = False, returnRangeLow = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportGradingScale(GradeReportGradingScaleID, EntityID = 1, returnreturnGradeReportGradingScaleID = False, returnreturnCreatedTime = False, returnreturnDisplayType = False, returnreturnDisplayTypeCode = False, returnreturnFreeformText = False, returnreturnGradeMarkCode = False, returnreturnGradeReportStudentID = False, returnreturnModifiedTime = False, returnreturnRangeHigh = False, returnreturnRangeLow = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(GradeReportGradingScaleID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportGradingScale(GradeReportGradingScaleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(GradeReportGradingScaleID), verb = "delete")

	return(response)

def getEveryGradeReportRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRowID = True, returnAttemptedCredit = False, returnClassPeriod = False, returnCourseSubjectDescription = False, returnCourseTypeCode = False, returnCourseTypeDescription = False, returnCreatedTime = False, returnDepartment = False, returnDescription = False, returnEarnedCredit = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnGradeReportRowIDParent = False, returnModifiedTime = False, returnRowType = False, returnRowTypeCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnSortNumber = False, returnStaffName = False, returnStudentSectionID = False, returnTotalPossibleCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportRow(GradeReportRowID, EntityID = 1, returnreturnGradeReportRowID = False, returnreturnAttemptedCredit = False, returnreturnClassPeriod = False, returnreturnCourseSubjectDescription = False, returnreturnCourseTypeCode = False, returnreturnCourseTypeDescription = False, returnreturnCreatedTime = False, returnreturnDepartment = False, returnreturnDescription = False, returnreturnEarnedCredit = False, returnreturnGradeReportAcademicSessionID = False, returnreturnGradeReportAcademicSessionSortNumber = False, returnreturnGradeReportRowIDParent = False, returnreturnModifiedTime = False, returnreturnRowType = False, returnreturnRowTypeCode = False, returnreturnSectionLengthSubsetCode = False, returnreturnSectionLengthSubsetDescription = False, returnreturnSort1 = False, returnreturnSort2 = False, returnreturnSort3 = False, returnreturnSort4 = False, returnreturnSortNumber = False, returnreturnStaffName = False, returnreturnStudentSectionID = False, returnreturnTotalPossibleCredit = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(GradeReportRowID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportRow(GradeReportRowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(GradeReportRowID), verb = "delete")

	return(response)

def getEveryGradeReportRowColumn(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRowColumnID = True, returnCreatedTime = False, returnDisplayValue = False, returnGradeMarkID = False, returnGradeReportColumnGroupColumnID = False, returnGradeReportRowID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportRowColumn(GradeReportRowColumnID, EntityID = 1, returnreturnGradeReportRowColumnID = False, returnreturnCreatedTime = False, returnreturnDisplayValue = False, returnreturnGradeMarkID = False, returnreturnGradeReportColumnGroupColumnID = False, returnreturnGradeReportRowID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(GradeReportRowColumnID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportRowColumn(GradeReportRowColumnID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(GradeReportRowColumnID), verb = "delete")

	return(response)

def getEveryGradeReportRowDetail(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRowDetailID = True, returnCreatedTime = False, returnDetailData = False, returnGradeReportRowID = False, returnGradingPeriodLabel = False, returnGradingPeriodSortNumber = False, returnLabel = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportRowDetail(GradeReportRowDetailID, EntityID = 1, returnreturnGradeReportRowDetailID = False, returnreturnCreatedTime = False, returnreturnDetailData = False, returnreturnGradeReportRowID = False, returnreturnGradingPeriodLabel = False, returnreturnGradingPeriodSortNumber = False, returnreturnLabel = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(GradeReportRowDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportRowDetail(GradeReportRowDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(GradeReportRowDetailID), verb = "delete")

	return(response)

def getEveryGradeReportRunHistory(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRunHistoryID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnCEEBACT = False, returnCity = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFaxNumber = False, returnFooterMessage = False, returnFormattedFullAddress = False, returnGradeReportTemplateID = False, returnIsTexasTranscript = False, returnModifiedTime = False, returnName = False, returnOverwriteExistingReportCard = False, returnParameterDescription = False, returnPhoneNumber = False, returnPostalCode = False, returnPostReportCardToFASA = False, returnPrintCompletedGradingPeriodComments = False, returnReportCardFileName = False, returnRequireFamilyAccessElectronicSignature = False, returnStateProvince = False, returnStatusType = False, returnStatusTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportRunHistory(GradeReportRunHistoryID, EntityID = 1, returnreturnGradeReportRunHistoryID = False, returnreturnAddressLine1 = False, returnreturnAddressLine2 = False, returnreturnCEEBACT = False, returnreturnCity = False, returnreturnCode = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnFamilyPrintType = False, returnreturnFamilyPrintTypeCode = False, returnreturnFaxNumber = False, returnreturnFooterMessage = False, returnreturnFormattedFullAddress = False, returnreturnGradeReportTemplateID = False, returnreturnIsTexasTranscript = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnOverwriteExistingReportCard = False, returnreturnParameterDescription = False, returnreturnPhoneNumber = False, returnreturnPostalCode = False, returnreturnPostReportCardToFASA = False, returnreturnPrintCompletedGradingPeriodComments = False, returnreturnReportCardFileName = False, returnreturnRequireFamilyAccessElectronicSignature = False, returnreturnStateProvince = False, returnreturnStatusType = False, returnreturnStatusTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(GradeReportRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportRunHistory(GradeReportRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(GradeReportRunHistoryID), verb = "delete")

	return(response)

def getEveryGradeReportRunHistoryAttachment(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRunHistoryAttachmentID = True, returnAttachmentCanBeViewedByStudentFamilyFamilyAccess = False, returnAttachmentID = False, returnCreatedTime = False, returnGradeReportRunHistoryID = False, returnGuardianSignedTime = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnSignedByGuardian = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportRunHistoryAttachment(GradeReportRunHistoryAttachmentID, EntityID = 1, returnreturnGradeReportRunHistoryAttachmentID = False, returnreturnAttachmentCanBeViewedByStudentFamilyFamilyAccess = False, returnreturnAttachmentID = False, returnreturnCreatedTime = False, returnreturnGradeReportRunHistoryID = False, returnreturnGuardianSignedTime = False, returnreturnModifiedTime = False, returnreturnNameIDGuardianSignedBy = False, returnreturnSignedByGuardian = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(GradeReportRunHistoryAttachmentID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportRunHistoryAttachment(GradeReportRunHistoryAttachmentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(GradeReportRunHistoryAttachmentID), verb = "delete")

	return(response)

def getEveryGradeReportStudent(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnAdvisorName = False, returnBirthDate = False, returnCity = False, returnCreatedTime = False, returnDoubleColumnHeaderField1 = False, returnDoubleColumnHeaderField10 = False, returnDoubleColumnHeaderField2 = False, returnDoubleColumnHeaderField3 = False, returnDoubleColumnHeaderField4 = False, returnDoubleColumnHeaderField5 = False, returnDoubleColumnHeaderField6 = False, returnDoubleColumnHeaderField7 = False, returnDoubleColumnHeaderField8 = False, returnDoubleColumnHeaderField9 = False, returnEmailAddress = False, returnEthnicityAndRace = False, returnFirstName = False, returnFormattedFullAddress = False, returnFormattedName = False, returnGender = False, returnGenderCode = False, returnGradeReportRunHistoryID = False, returnGraduationDate = False, returnHomeroom = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameIDPrimaryGuardian = False, returnNameSuffix = False, returnNameTitle = False, returnPostalCode = False, returnPrimaryGuardianEmailAddress = False, returnPrimaryGuardianFirstName = False, returnPrimaryGuardianFormattedName = False, returnPrimaryGuardianLastName = False, returnPrimaryGuardianMiddleName = False, returnPrimaryGuardianNameSuffix = False, returnPrimaryGuardianNameTitle = False, returnPrimaryGuardianPhoneNumber = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnSingleColumnHeaderField1 = False, returnSingleColumnHeaderField2 = False, returnSingleColumnHeaderField3 = False, returnSingleColumnHeaderField4 = False, returnSingleColumnHeaderField5 = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnStateProvince = False, returnStudentFamilyID = False, returnStudentFamilyRank = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportStudent(GradeReportStudentID, EntityID = 1, returnreturnGradeReportStudentID = False, returnreturnAddressLine1 = False, returnreturnAddressLine2 = False, returnreturnAdvisorName = False, returnreturnBirthDate = False, returnreturnCity = False, returnreturnCreatedTime = False, returnreturnDoubleColumnHeaderField1 = False, returnreturnDoubleColumnHeaderField10 = False, returnreturnDoubleColumnHeaderField2 = False, returnreturnDoubleColumnHeaderField3 = False, returnreturnDoubleColumnHeaderField4 = False, returnreturnDoubleColumnHeaderField5 = False, returnreturnDoubleColumnHeaderField6 = False, returnreturnDoubleColumnHeaderField7 = False, returnreturnDoubleColumnHeaderField8 = False, returnreturnDoubleColumnHeaderField9 = False, returnreturnEmailAddress = False, returnreturnEthnicityAndRace = False, returnreturnFirstName = False, returnreturnFormattedFullAddress = False, returnreturnFormattedName = False, returnreturnGender = False, returnreturnGenderCode = False, returnreturnGradeReportRunHistoryID = False, returnreturnGraduationDate = False, returnreturnHomeroom = False, returnreturnLastName = False, returnreturnMiddleName = False, returnreturnModifiedTime = False, returnreturnNameIDPrimaryGuardian = False, returnreturnNameSuffix = False, returnreturnNameTitle = False, returnreturnPostalCode = False, returnreturnPrimaryGuardianEmailAddress = False, returnreturnPrimaryGuardianFirstName = False, returnreturnPrimaryGuardianFormattedName = False, returnreturnPrimaryGuardianLastName = False, returnreturnPrimaryGuardianMiddleName = False, returnreturnPrimaryGuardianNameSuffix = False, returnreturnPrimaryGuardianNameTitle = False, returnreturnPrimaryGuardianPhoneNumber = False, returnreturnPromotionStatus = False, returnreturnPromotionStatusCode = False, returnreturnSingleColumnHeaderField1 = False, returnreturnSingleColumnHeaderField2 = False, returnreturnSingleColumnHeaderField3 = False, returnreturnSingleColumnHeaderField4 = False, returnreturnSingleColumnHeaderField5 = False, returnreturnSort1 = False, returnreturnSort2 = False, returnreturnSort3 = False, returnreturnSort4 = False, returnreturnStateProvince = False, returnreturnStudentFamilyID = False, returnreturnStudentFamilyRank = False, returnreturnStudentID = False, returnreturnStudentNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(GradeReportStudentID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportStudent(GradeReportStudentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(GradeReportStudentID), verb = "delete")

	return(response)

def getEveryGradeReportStudentAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentAttendanceTermID = True, returnAttendanceTermCode = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysTardy = False, returnDaysUnexcused = False, returnGradeReportAcademicSessionID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportStudentAttendanceTerm(GradeReportStudentAttendanceTermID, EntityID = 1, returnreturnGradeReportStudentAttendanceTermID = False, returnreturnAttendanceTermCode = False, returnreturnCreatedTime = False, returnreturnDaysAbsent = False, returnreturnDaysExcused = False, returnreturnDaysOther = False, returnreturnDaysTardy = False, returnreturnDaysUnexcused = False, returnreturnGradeReportAcademicSessionID = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(GradeReportStudentAttendanceTermID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportStudentAttendanceTerm(GradeReportStudentAttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(GradeReportStudentAttendanceTermID), verb = "delete")

	return(response)

def getEveryGradeReportStudentTestRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentTestRowID = True, returnCreatedTime = False, returnDateTaken = False, returnGradeReportStudentTestTypeID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumn1 = False, returnTestColumn10 = False, returnTestColumn2 = False, returnTestColumn3 = False, returnTestColumn4 = False, returnTestColumn5 = False, returnTestColumn6 = False, returnTestColumn7 = False, returnTestColumn8 = False, returnTestColumn9 = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportStudentTestRow(GradeReportStudentTestRowID, EntityID = 1, returnreturnGradeReportStudentTestRowID = False, returnreturnCreatedTime = False, returnreturnDateTaken = False, returnreturnGradeReportStudentTestTypeID = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnTestColumn1 = False, returnreturnTestColumn10 = False, returnreturnTestColumn2 = False, returnreturnTestColumn3 = False, returnreturnTestColumn4 = False, returnreturnTestColumn5 = False, returnreturnTestColumn6 = False, returnreturnTestColumn7 = False, returnreturnTestColumn8 = False, returnreturnTestColumn9 = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(GradeReportStudentTestRowID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportStudentTestRow(GradeReportStudentTestRowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(GradeReportStudentTestRowID), verb = "delete")

	return(response)

def getEveryGradeReportStudentTestType(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentTestTypeID = True, returnCreatedTime = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumnHeader1 = False, returnTestColumnHeader10 = False, returnTestColumnHeader2 = False, returnTestColumnHeader3 = False, returnTestColumnHeader4 = False, returnTestColumnHeader5 = False, returnTestColumnHeader6 = False, returnTestColumnHeader7 = False, returnTestColumnHeader8 = False, returnTestColumnHeader9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportStudentTestType(GradeReportStudentTestTypeID, EntityID = 1, returnreturnGradeReportStudentTestTypeID = False, returnreturnCreatedTime = False, returnreturnGradeReportStudentID = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnTestColumnHeader1 = False, returnreturnTestColumnHeader10 = False, returnreturnTestColumnHeader2 = False, returnreturnTestColumnHeader3 = False, returnreturnTestColumnHeader4 = False, returnreturnTestColumnHeader5 = False, returnreturnTestColumnHeader6 = False, returnreturnTestColumnHeader7 = False, returnreturnTestColumnHeader8 = False, returnreturnTestColumnHeader9 = False, returnreturnTestType = False, returnreturnTestTypeCode = False, returnreturnTestVersion = False, returnreturnTestVersionCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(GradeReportStudentTestTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportStudentTestType(GradeReportStudentTestTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(GradeReportStudentTestTypeID), verb = "delete")

	return(response)

def getEveryGradeReportTemplate(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateID = True, returnAcademicSessionType = False, returnAcademicSessionTypeCode = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBlankSignatureLabel = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCommentPrintType = False, returnCommentPrintTypeCode = False, returnConfigEntityYearID = False, returnCourseDescriptionFormat = False, returnCourseDescriptionFormatCode = False, returnCourseFilter = False, returnCourseFilterCode = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodCodeSort1 = False, returnDisplayPeriodCodeSort2 = False, returnDisplayPeriodCodeSort3 = False, returnDisplayPeriodCodeSort4 = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFreeFormGradingLegend = False, returnGPAField1 = False, returnGPAField1Code = False, returnGPAField2 = False, returnGPAField2Code = False, returnGPAField3 = False, returnGPAField3Code = False, returnGPAField4 = False, returnGPAField4Code = False, returnGPAField5 = False, returnGPAField5Code = False, returnGPAField6 = False, returnGPAField6Code = False, returnGPAField7 = False, returnGPAField7Code = False, returnGPALabel1 = False, returnGPALabel2 = False, returnGPALabel3 = False, returnGPALabel4 = False, returnGPALabel5 = False, returnGPALabel6 = False, returnGPALabel7 = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportColumnGroupIDSecondary = False, returnGradeReportTemplateIDClonedFrom = False, returnGradingSort = False, returnGradingSortCode = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHideSignatureSection = False, returnIncludeCurrentYearClasses = False, returnIncludeInProgressGrades = False, returnIncludePhoneInEntityAddress = False, returnIncludePhoneInGuardianAddress = False, returnIncludeTranscriptNotes = False, returnIncludeTransferCourses = False, returnMediaIDLogo = False, returnModifiedTime = False, returnNoReceivingFamily = False, returnOfficialSignatureLabel = False, returnPrintAllCourseRowHeaders = False, returnPrintAttendanceTotals = False, returnPrintBlankSignatureLine = False, returnPrintComments = False, returnPrintElectronicSignature = False, returnPrintEndorsements = False, returnPrintFreeFormComments = False, returnPrintGPA = False, returnPrintGradeScaleAtTop = False, returnPrintHighFrequencyWords = False, returnPrintIndividualAttendanceTerms = False, returnPrintLettersAndSounds = False, returnPrintYearToDateTotals = False, returnReceivesForms = False, returnReportRunInfoID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnStudentSort1 = False, returnStudentSort1Code = False, returnStudentSort2 = False, returnStudentSort2Code = False, returnStudentSort3 = False, returnStudentSort3Code = False, returnStudentSort4 = False, returnStudentSort4Code = False, returnTeacherNameFormat = False, returnTeacherNameFormatCode = False, returnTemplateType = False, returnTemplateTypeCode = False, returnUseFreeFormGradingLegend = False, returnUseFullGPASection = False, returnUseFullGradesSection = False, returnUseGradeMarkDescriptionGradingLegend = False, returnUseGradeMarkRangeGradingLegend = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplate(GradeReportTemplateID, EntityID = 1, returnreturnGradeReportTemplateID = False, returnreturnAcademicSessionType = False, returnreturnAcademicSessionTypeCode = False, returnreturnAdvisorNameFormat = False, returnreturnAdvisorNameFormatCode = False, returnreturnBlankSignatureLabel = False, returnreturnColumnHeaderLabel1 = False, returnreturnColumnHeaderLabel10 = False, returnreturnColumnHeaderLabel2 = False, returnreturnColumnHeaderLabel3 = False, returnreturnColumnHeaderLabel4 = False, returnreturnColumnHeaderLabel5 = False, returnreturnColumnHeaderLabel6 = False, returnreturnColumnHeaderLabel7 = False, returnreturnColumnHeaderLabel8 = False, returnreturnColumnHeaderLabel9 = False, returnreturnCommentPrintType = False, returnreturnCommentPrintTypeCode = False, returnreturnConfigEntityYearID = False, returnreturnCourseDescriptionFormat = False, returnreturnCourseDescriptionFormatCode = False, returnreturnCourseFilter = False, returnreturnCourseFilterCode = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDisplayPeriodCodeSort1 = False, returnreturnDisplayPeriodCodeSort2 = False, returnreturnDisplayPeriodCodeSort3 = False, returnreturnDisplayPeriodCodeSort4 = False, returnreturnFamilyPrintType = False, returnreturnFamilyPrintTypeCode = False, returnreturnFreeFormGradingLegend = False, returnreturnGPAField1 = False, returnreturnGPAField1Code = False, returnreturnGPAField2 = False, returnreturnGPAField2Code = False, returnreturnGPAField3 = False, returnreturnGPAField3Code = False, returnreturnGPAField4 = False, returnreturnGPAField4Code = False, returnreturnGPAField5 = False, returnreturnGPAField5Code = False, returnreturnGPAField6 = False, returnreturnGPAField6Code = False, returnreturnGPAField7 = False, returnreturnGPAField7Code = False, returnreturnGPALabel1 = False, returnreturnGPALabel2 = False, returnreturnGPALabel3 = False, returnreturnGPALabel4 = False, returnreturnGPALabel5 = False, returnreturnGPALabel6 = False, returnreturnGPALabel7 = False, returnreturnGradeReportAcademicSessionTemplateGroupID = False, returnreturnGradeReportColumnGroupIDSecondary = False, returnreturnGradeReportTemplateIDClonedFrom = False, returnreturnGradingSort = False, returnreturnGradingSortCode = False, returnreturnGuardianNameFormat = False, returnreturnGuardianNameFormatCode = False, returnreturnHasLogo = False, returnreturnHideSignatureSection = False, returnreturnIncludeCurrentYearClasses = False, returnreturnIncludeInProgressGrades = False, returnreturnIncludePhoneInEntityAddress = False, returnreturnIncludePhoneInGuardianAddress = False, returnreturnIncludeTranscriptNotes = False, returnreturnIncludeTransferCourses = False, returnreturnMediaIDLogo = False, returnreturnModifiedTime = False, returnreturnNoReceivingFamily = False, returnreturnOfficialSignatureLabel = False, returnreturnPrintAllCourseRowHeaders = False, returnreturnPrintAttendanceTotals = False, returnreturnPrintBlankSignatureLine = False, returnreturnPrintComments = False, returnreturnPrintElectronicSignature = False, returnreturnPrintEndorsements = False, returnreturnPrintFreeFormComments = False, returnreturnPrintGPA = False, returnreturnPrintGradeScaleAtTop = False, returnreturnPrintHighFrequencyWords = False, returnreturnPrintIndividualAttendanceTerms = False, returnreturnPrintLettersAndSounds = False, returnreturnPrintYearToDateTotals = False, returnreturnReceivesForms = False, returnreturnReportRunInfoID = False, returnreturnStudentNameFormat = False, returnreturnStudentNameFormatCode = False, returnreturnStudentSort1 = False, returnreturnStudentSort1Code = False, returnreturnStudentSort2 = False, returnreturnStudentSort2Code = False, returnreturnStudentSort3 = False, returnreturnStudentSort3Code = False, returnreturnStudentSort4 = False, returnreturnStudentSort4Code = False, returnreturnTeacherNameFormat = False, returnreturnTeacherNameFormatCode = False, returnreturnTemplateType = False, returnreturnTemplateTypeCode = False, returnreturnUseFreeFormGradingLegend = False, returnreturnUseFullGPASection = False, returnreturnUseFullGradesSection = False, returnreturnUseGradeMarkDescriptionGradingLegend = False, returnreturnUseGradeMarkRangeGradingLegend = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUseStudentSectionLinking = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(GradeReportTemplateID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplate(GradeReportTemplateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(GradeReportTemplateID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateCommentSet(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateCommentSetID = True, returnCommentSetID = False, returnCreatedTime = False, returnGradeReportTemplateCommentSetIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateCommentSet(GradeReportTemplateCommentSetID, EntityID = 1, returnreturnGradeReportTemplateCommentSetID = False, returnreturnCommentSetID = False, returnreturnCreatedTime = False, returnreturnGradeReportTemplateCommentSetIDClonedFrom = False, returnreturnGradeReportTemplateID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(GradeReportTemplateCommentSetID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateCommentSet(GradeReportTemplateCommentSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(GradeReportTemplateCommentSetID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateEndorsement(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateEndorsementID = True, returnCreatedTime = False, returnEndorsementID = False, returnGradeReportTemplateID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateEndorsement(GradeReportTemplateEndorsementID, EntityID = 1, returnreturnGradeReportTemplateEndorsementID = False, returnreturnCreatedTime = False, returnreturnEndorsementID = False, returnreturnGradeReportTemplateID = False, returnreturnGradYearHigh = False, returnreturnGradYearLow = False, returnreturnModifiedTime = False, returnreturnOrderNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(GradeReportTemplateEndorsementID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateEndorsement(GradeReportTemplateEndorsementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(GradeReportTemplateEndorsementID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateGPABucket(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateGPABucketID = True, returnCreatedTime = False, returnGPABucketID = False, returnGradeReportTemplateGPABucketIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateGPABucket(GradeReportTemplateGPABucketID, EntityID = 1, returnreturnGradeReportTemplateGPABucketID = False, returnreturnCreatedTime = False, returnreturnGPABucketID = False, returnreturnGradeReportTemplateGPABucketIDClonedFrom = False, returnreturnGradeReportTemplateID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(GradeReportTemplateGPABucketID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateGPABucket(GradeReportTemplateGPABucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(GradeReportTemplateGPABucketID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateGPAMethodID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeReportTemplateGPAMethodIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateGPAMethod(GradeReportTemplateGPAMethodID, EntityID = 1, returnreturnGradeReportTemplateGPAMethodID = False, returnreturnCreatedTime = False, returnreturnGPAMethodID = False, returnreturnGradeReportTemplateGPAMethodIDClonedFrom = False, returnreturnGradeReportTemplateID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(GradeReportTemplateGPAMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateGPAMethod(GradeReportTemplateGPAMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(GradeReportTemplateGPAMethodID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateGradeMark(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnGradeReportTemplateGradeMarkIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateGradeMark(GradeReportTemplateGradeMarkID, EntityID = 1, returnreturnGradeReportTemplateGradeMarkID = False, returnreturnCreatedTime = False, returnreturnGradeMarkID = False, returnreturnGradeReportTemplateGradeMarkIDClonedFrom = False, returnreturnGradeReportTemplateID = False, returnreturnModifiedTime = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(GradeReportTemplateGradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateGradeMark(GradeReportTemplateGradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(GradeReportTemplateGradeMarkID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateHeaderColumn(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateHeaderColumnID = True, returnCreatedTime = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnGPABucketID = False, returnGPAMethodID = False, returnGradeReportTemplateHeaderColumnIDClonedFrom = False, returnGradeReportTemplateHeaderRowID = False, returnLabelOverride = False, returnModifiedTime = False, returnRankMethodID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateHeaderColumn(GradeReportTemplateHeaderColumnID, EntityID = 1, returnreturnGradeReportTemplateHeaderColumnID = False, returnreturnCreatedTime = False, returnreturnFieldType = False, returnreturnFieldTypeCode = False, returnreturnFreeformText = False, returnreturnGPABucketID = False, returnreturnGPAMethodID = False, returnreturnGradeReportTemplateHeaderColumnIDClonedFrom = False, returnreturnGradeReportTemplateHeaderRowID = False, returnreturnLabelOverride = False, returnreturnModifiedTime = False, returnreturnRankMethodID = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(GradeReportTemplateHeaderColumnID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateHeaderColumn(GradeReportTemplateHeaderColumnID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(GradeReportTemplateHeaderColumnID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateHeaderRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnGradeReportTemplateHeaderRowIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateHeaderRow(GradeReportTemplateHeaderRowID, EntityID = 1, returnreturnGradeReportTemplateHeaderRowID = False, returnreturnColumnCount = False, returnreturnCreatedTime = False, returnreturnGradeReportTemplateHeaderRowIDClonedFrom = False, returnreturnGradeReportTemplateID = False, returnreturnModifiedTime = False, returnreturnSortNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(GradeReportTemplateHeaderRowID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateHeaderRow(GradeReportTemplateHeaderRowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(GradeReportTemplateHeaderRowID), verb = "delete")

	return(response)

def getEveryGradeReportTemplateTestType(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateTestTypeID = True, returnCreatedTime = False, returnFieldGUIDTestColumn1 = False, returnFieldGUIDTestColumn10 = False, returnFieldGUIDTestColumn2 = False, returnFieldGUIDTestColumn3 = False, returnFieldGUIDTestColumn4 = False, returnFieldGUIDTestColumn5 = False, returnFieldGUIDTestColumn6 = False, returnFieldGUIDTestColumn7 = False, returnFieldGUIDTestColumn8 = False, returnFieldGUIDTestColumn9 = False, returnGradeReportTemplateID = False, returnGradeReportTemplateTestTypeIDClonedFrom = False, returnModifiedTime = False, returnPrintHighestScoreOnly = False, returnSortNumber = False, returnTestColumnHeaderOverride1 = False, returnTestColumnHeaderOverride10 = False, returnTestColumnHeaderOverride2 = False, returnTestColumnHeaderOverride3 = False, returnTestColumnHeaderOverride4 = False, returnTestColumnHeaderOverride5 = False, returnTestColumnHeaderOverride6 = False, returnTestColumnHeaderOverride7 = False, returnTestColumnHeaderOverride8 = False, returnTestColumnHeaderOverride9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradeReportTemplateTestType(GradeReportTemplateTestTypeID, EntityID = 1, returnreturnGradeReportTemplateTestTypeID = False, returnreturnCreatedTime = False, returnreturnFieldGUIDTestColumn1 = False, returnreturnFieldGUIDTestColumn10 = False, returnreturnFieldGUIDTestColumn2 = False, returnreturnFieldGUIDTestColumn3 = False, returnreturnFieldGUIDTestColumn4 = False, returnreturnFieldGUIDTestColumn5 = False, returnreturnFieldGUIDTestColumn6 = False, returnreturnFieldGUIDTestColumn7 = False, returnreturnFieldGUIDTestColumn8 = False, returnreturnFieldGUIDTestColumn9 = False, returnreturnGradeReportTemplateID = False, returnreturnGradeReportTemplateTestTypeIDClonedFrom = False, returnreturnModifiedTime = False, returnreturnPrintHighestScoreOnly = False, returnreturnSortNumber = False, returnreturnTestColumnHeaderOverride1 = False, returnreturnTestColumnHeaderOverride10 = False, returnreturnTestColumnHeaderOverride2 = False, returnreturnTestColumnHeaderOverride3 = False, returnreturnTestColumnHeaderOverride4 = False, returnreturnTestColumnHeaderOverride5 = False, returnreturnTestColumnHeaderOverride6 = False, returnreturnTestColumnHeaderOverride7 = False, returnreturnTestColumnHeaderOverride8 = False, returnreturnTestColumnHeaderOverride9 = False, returnreturnTestType = False, returnreturnTestTypeCode = False, returnreturnTestVersion = False, returnreturnTestVersionCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(GradeReportTemplateTestTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReportTemplateTestType(GradeReportTemplateTestTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(GradeReportTemplateTestTypeID), verb = "delete")

	return(response)

def getEveryGradingPeriod(EntityID = 1, page = 1, pageSize = 100, returnGradingPeriodID = True, returnAfterSectionLengthEndLastGradingPeriod = False, returnBeforeSectionLengthStartFirstGradingPeriod = False, returnCalculatedEndDateWithExtension = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeIDForNotReviewedRequests = False, returnCompletedFieldText = False, returnCompletedText = False, returnCreatedTime = False, returnCurrentActiveStatus = False, returnDateOverrideTeacherGracePeriod = False, returnDateOverrideTeacherGracePeriodDisplay = False, returnDescription = False, returnDisplayAssignments = False, returnDisplayGradeBuckets = False, returnEndDate = False, returnEndDateCopy = False, returnEntityGroupKey = False, returnExtendedEndDateGreaterThanToday = False, returnExtensionDays = False, returnExtensionEndTime = False, returnGradeBucketLabels = False, returnGradingPeriodIDClonedFrom = False, returnGradingPeriodIDClonedTo = False, returnGradingPeriodSetID = False, returnIncludeMissingAssignments = False, returnIncludeMissingAssignmentsOrIsCurrentGradingPeriod = False, returnIsActiveOrExtended = False, returnIsCompleted = False, returnModifiedTime = False, returnNumber = False, returnNumberDescription = False, returnOptionsHeaderText = False, returnProgressReportGradingPeriodNumberDateDisplay = False, returnSectionIDForActiveStatus = False, returnSectionLengthID = False, returnStartDate = False, returnStartDateCopy = False, returnStatusDisplay = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinGradingPeriod = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradingPeriod(GradingPeriodID, EntityID = 1, returnreturnGradingPeriodID = False, returnreturnAfterSectionLengthEndLastGradingPeriod = False, returnreturnBeforeSectionLengthStartFirstGradingPeriod = False, returnreturnCalculatedEndDateWithExtension = False, returnreturnClosedGradingPeriodGradeChangeID = False, returnreturnClosedGradingPeriodGradeChangeIDForNotReviewedRequests = False, returnreturnCompletedFieldText = False, returnreturnCompletedText = False, returnreturnCreatedTime = False, returnreturnCurrentActiveStatus = False, returnreturnDateOverrideTeacherGracePeriod = False, returnreturnDateOverrideTeacherGracePeriodDisplay = False, returnreturnDescription = False, returnreturnDisplayAssignments = False, returnreturnDisplayGradeBuckets = False, returnreturnEndDate = False, returnreturnEndDateCopy = False, returnreturnEntityGroupKey = False, returnreturnExtendedEndDateGreaterThanToday = False, returnreturnExtensionDays = False, returnreturnExtensionEndTime = False, returnreturnGradeBucketLabels = False, returnreturnGradingPeriodIDClonedFrom = False, returnreturnGradingPeriodIDClonedTo = False, returnreturnGradingPeriodSetID = False, returnreturnIncludeMissingAssignments = False, returnreturnIncludeMissingAssignmentsOrIsCurrentGradingPeriod = False, returnreturnIsActiveOrExtended = False, returnreturnIsCompleted = False, returnreturnModifiedTime = False, returnreturnNumber = False, returnreturnNumberDescription = False, returnreturnOptionsHeaderText = False, returnreturnProgressReportGradingPeriodNumberDateDisplay = False, returnreturnSectionIDForActiveStatus = False, returnreturnSectionLengthID = False, returnreturnStartDate = False, returnreturnStartDateCopy = False, returnreturnStatusDisplay = False, returnreturnStatusDisplayWithExtensionDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithinGradingPeriod = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(GradingPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteGradingPeriod(GradingPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(GradingPeriodID), verb = "delete")

	return(response)

def getEveryGradingPeriodGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnFactorBasedGPACountAs = False, returnGradeBucketID = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodEndDateAddSnapshotGraceDays = False, returnGradingPeriodGradeBucketExistsInSpecifcEntity = False, returnGradingPeriodGradeBucketIDClonedFrom = False, returnGradingPeriodIDEnd = False, returnGradingPeriodIDStart = False, returnHasGradeBucketTypeCategories = False, returnIsAHistoricRecord = False, returnIsUpToDate = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnNumberOfGradeBucketsToWeight = False, returnStatus = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradingPeriodGradeBucket(GradingPeriodGradeBucketID, EntityID = 1, returnreturnGradingPeriodGradeBucketID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnFactorBasedGPACountAs = False, returnreturnGradeBucketID = False, returnreturnGradeBucketLabelWithDates = False, returnreturnGradingPeriodEndDateAddSnapshotGraceDays = False, returnreturnGradingPeriodGradeBucketExistsInSpecifcEntity = False, returnreturnGradingPeriodGradeBucketIDClonedFrom = False, returnreturnGradingPeriodIDEnd = False, returnreturnGradingPeriodIDStart = False, returnreturnHasGradeBucketTypeCategories = False, returnreturnIsAHistoricRecord = False, returnreturnIsUpToDate = False, returnreturnMaxExtraCredit = False, returnreturnModifiedTime = False, returnreturnNumberOfGradeBucketsToWeight = False, returnreturnStatus = False, returnreturnUseMaxExtraCredit = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(GradingPeriodGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteGradingPeriodGradeBucket(GradingPeriodGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(GradingPeriodGradeBucketID), verb = "delete")

	return(response)

def getEveryGradingPeriodSet(EntityID = 1, page = 1, pageSize = 100, returnGradingPeriodSetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingPeriodSetIDClonedFrom = False, returnGradingPeriodSetIDClonedTo = False, returnIsDefault = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradingPeriodSet(GradingPeriodSetID, EntityID = 1, returnreturnGradingPeriodSetID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCourseLengthID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEntityGroupKey = False, returnreturnGradingPeriodSetIDClonedFrom = False, returnreturnGradingPeriodSetIDClonedTo = False, returnreturnIsDefault = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(GradingPeriodSetID), verb = "get", params_list = params_list)

	return(response)

def deleteGradingPeriodSet(GradingPeriodSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(GradingPeriodSetID), verb = "delete")

	return(response)

def getEveryGradReqRankGPACourseType(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankGPACourseTypeID = True, returnCourseTypeID = False, returnCreatedTime = False, returnGradReqRankGPAMethodEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradReqRankGPACourseType(GradReqRankGPACourseTypeID, EntityID = 1, returnreturnGradReqRankGPACourseTypeID = False, returnreturnCourseTypeID = False, returnreturnCreatedTime = False, returnreturnGradReqRankGPAMethodEntityID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(GradReqRankGPACourseTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteGradReqRankGPACourseType(GradReqRankGPACourseTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(GradReqRankGPACourseTypeID), verb = "delete")

	return(response)

def getEveryGradReqRankGPAMethodEntity(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankGPAMethodEntityID = True, returnCreatedTime = False, returnGPAMethodEntityID = False, returnGradeBucketFlagIDLocalCredit = False, returnGradeBucketIDTermOne = False, returnGradeBucketIDTermTwo = False, returnGradPlanSetting = False, returnGradPlanSettingCode = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradReqRankGPAMethodEntity(GradReqRankGPAMethodEntityID, EntityID = 1, returnreturnGradReqRankGPAMethodEntityID = False, returnreturnCreatedTime = False, returnreturnGPAMethodEntityID = False, returnreturnGradeBucketFlagIDLocalCredit = False, returnreturnGradeBucketIDTermOne = False, returnreturnGradeBucketIDTermTwo = False, returnreturnGradPlanSetting = False, returnreturnGradPlanSettingCode = False, returnreturnModifiedTime = False, returnreturnPlanID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(GradReqRankGPAMethodEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteGradReqRankGPAMethodEntity(GradReqRankGPAMethodEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(GradReqRankGPAMethodEntityID), verb = "delete")

	return(response)

def getEveryGradReqRankHighSchoolGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankHighSchoolGradeLevelID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradReqRankHighSchoolGradeLevel(GradReqRankHighSchoolGradeLevelID, EntityID = 1, returnreturnGradReqRankHighSchoolGradeLevelID = False, returnreturnCreatedTime = False, returnreturnGPAMethodID = False, returnreturnGradeLevelID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(GradReqRankHighSchoolGradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteGradReqRankHighSchoolGradeLevel(GradReqRankHighSchoolGradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(GradReqRankHighSchoolGradeLevelID), verb = "delete")

	return(response)

def getEveryGradReqRankSchoolYearIncludeLocalCredit(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankSchoolYearIncludeLocalCreditID = True, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradReqRankSchoolYearIncludeLocalCredit(GradReqRankSchoolYearIncludeLocalCreditID, EntityID = 1, returnreturnGradReqRankSchoolYearIncludeLocalCreditID = False, returnreturnCreatedTime = False, returnreturnGPAMethodID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(GradReqRankSchoolYearIncludeLocalCreditID), verb = "get", params_list = params_list)

	return(response)

def deleteGradReqRankSchoolYearIncludeLocalCredit(GradReqRankSchoolYearIncludeLocalCreditID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(GradReqRankSchoolYearIncludeLocalCreditID), verb = "delete")

	return(response)

def getEveryGradReqSubjectType(EntityID = 1, page = 1, pageSize = 100, returnGradReqSubjectTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getGradReqSubjectType(GradReqSubjectTypeID, EntityID = 1, returnreturnGradReqSubjectTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(GradReqSubjectTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteGradReqSubjectType(GradReqSubjectTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(GradReqSubjectTypeID), verb = "delete")

	return(response)

def getEveryHonorRollRuleGPA(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGPAID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnHonorRollRuleGPAIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnMaximumGPA = False, returnMinimumGPA = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRuleGPA(HonorRollRuleGPAID, EntityID = 1, returnreturnHonorRollRuleGPAID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGPABucketID = False, returnreturnGPAMethodID = False, returnreturnGPAType = False, returnreturnGPATypeCode = False, returnreturnHonorRollRuleGPAIDClonedFrom = False, returnreturnHonorRollRunLevelRuleID = False, returnreturnMaximumGPA = False, returnreturnMinimumGPA = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(HonorRollRuleGPAID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRuleGPA(HonorRollRuleGPAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(HonorRollRuleGPAID), verb = "delete")

	return(response)

def getEveryHonorRollRuleGradeMark(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGradeMarkID = True, returnAllowException = False, returnCourseStandardFilterXML = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnExclusionThreshold = False, returnHonorRollRuleGradeMarkIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnInclusionType = False, returnInclusionTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRuleGradeMark(HonorRollRuleGradeMarkID, EntityID = 1, returnreturnHonorRollRuleGradeMarkID = False, returnreturnAllowException = False, returnreturnCourseStandardFilterXML = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnExclusionThreshold = False, returnreturnHonorRollRuleGradeMarkIDClonedFrom = False, returnreturnHonorRollRunLevelRuleID = False, returnreturnInclusionType = False, returnreturnInclusionTypeCode = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnTotalAllowableExceptions = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(HonorRollRuleGradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRuleGradeMark(HonorRollRuleGradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(HonorRollRuleGradeMarkID), verb = "delete")

	return(response)

def getEveryHonorRollRuleGradeMarkGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGradeMarkGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketID = False, returnHonorRollRuleGradeMarkGradeBucketIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRuleGradeMarkGradeBucket(HonorRollRuleGradeMarkGradeBucketID, EntityID = 1, returnreturnHonorRollRuleGradeMarkGradeBucketID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGradeBucketID = False, returnreturnHonorRollRuleGradeMarkGradeBucketIDClonedFrom = False, returnreturnHonorRollRuleGradeMarkID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(HonorRollRuleGradeMarkGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRuleGradeMarkGradeBucket(HonorRollRuleGradeMarkGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(HonorRollRuleGradeMarkGradeBucketID), verb = "delete")

	return(response)

def getEveryHonorRollRuleGradeMarkGradeMark(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGradeMarkGradeMarkID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkID = False, returnHonorRollRuleGradeMarkGradeMarkIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnIsException = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRuleGradeMarkGradeMark(HonorRollRuleGradeMarkGradeMarkID, EntityID = 1, returnreturnHonorRollRuleGradeMarkGradeMarkID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGradeMarkID = False, returnreturnHonorRollRuleGradeMarkGradeMarkIDClonedFrom = False, returnreturnHonorRollRuleGradeMarkID = False, returnreturnIsException = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(HonorRollRuleGradeMarkGradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRuleGradeMarkGradeMark(HonorRollRuleGradeMarkGradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(HonorRollRuleGradeMarkGradeMarkID), verb = "delete")

	return(response)

def getEveryHonorRollRulePriorHonorRoll(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRulePriorHonorRollID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollLevelTotal = False, returnHonorRollRulePriorHonorRollIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRulePriorHonorRoll(HonorRollRulePriorHonorRollID, EntityID = 1, returnreturnHonorRollRulePriorHonorRollID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnHonorRollLevelTotal = False, returnreturnHonorRollRulePriorHonorRollIDClonedFrom = False, returnreturnHonorRollRunLevelRuleID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(HonorRollRulePriorHonorRollID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRulePriorHonorRoll(HonorRollRulePriorHonorRollID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(HonorRollRulePriorHonorRollID), verb = "delete")

	return(response)

def getEveryHonorRollRulePriorHonorRollLevel(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRulePriorHonorRollLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRulePriorHonorRollID = False, returnHonorRollRulePriorHonorRollLevelIDClonedFrom = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRulePriorHonorRollLevel(HonorRollRulePriorHonorRollLevelID, EntityID = 1, returnreturnHonorRollRulePriorHonorRollLevelID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnHonorRollRulePriorHonorRollID = False, returnreturnHonorRollRulePriorHonorRollLevelIDClonedFrom = False, returnreturnHonorRollRunLevelHistoryID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(HonorRollRulePriorHonorRollLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRulePriorHonorRollLevel(HonorRollRulePriorHonorRollLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(HonorRollRulePriorHonorRollLevelID), verb = "delete")

	return(response)

def getEveryHonorRollRun(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunID = True, returnAllowMultipleHonorRollLevels = False, returnContainsGPARule = False, returnCreatedTime = False, returnDisplayGPAForHonorRoll = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketIDToDisplay = False, returnGPAMethodIDToDisplay = False, returnGPATypeToDisplay = False, returnGPATypeToDisplayCode = False, returnHonorRollRunIDClonedFrom = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRun(HonorRollRunID, EntityID = 1, returnreturnHonorRollRunID = False, returnreturnAllowMultipleHonorRollLevels = False, returnreturnContainsGPARule = False, returnreturnCreatedTime = False, returnreturnDisplayGPAForHonorRoll = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnGPABucketIDToDisplay = False, returnreturnGPAMethodIDToDisplay = False, returnreturnGPATypeToDisplay = False, returnreturnGPATypeToDisplayCode = False, returnreturnHonorRollRunIDClonedFrom = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(HonorRollRunID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRun(HonorRollRunID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(HonorRollRunID), verb = "delete")

	return(response)

def getEveryHonorRollRunHistory(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnGPAAsOfDate = False, returnHonorRollRunID = False, returnModifiedTime = False, returnNameDescription = False, returnStudentFilterParameter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRunHistory(HonorRollRunHistoryID, EntityID = 1, returnreturnHonorRollRunHistoryID = False, returnreturnCalculation = False, returnreturnCalculationCode = False, returnreturnCreatedTime = False, returnreturnDate = False, returnreturnDescription = False, returnreturnGPAAsOfDate = False, returnreturnHonorRollRunID = False, returnreturnModifiedTime = False, returnreturnNameDescription = False, returnreturnStudentFilterParameter = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(HonorRollRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRunHistory(HonorRollRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(HonorRollRunHistoryID), verb = "delete")

	return(response)

def getEveryHonorRollRunLevel(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunID = False, returnHonorRollRunLevelIDClonedFrom = False, returnHonorRollRunNameName = False, returnModifiedTime = False, returnName = False, returnOrder = False, returnRulesParameterDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRunLevel(HonorRollRunLevelID, EntityID = 1, returnreturnHonorRollRunLevelID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnHonorRollRunID = False, returnreturnHonorRollRunLevelIDClonedFrom = False, returnreturnHonorRollRunNameName = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnOrder = False, returnreturnRulesParameterDescription = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(HonorRollRunLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRunLevel(HonorRollRunLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(HonorRollRunLevelID), verb = "delete")

	return(response)

def getEveryHonorRollRunLevelHistory(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunLevelHistoryID = True, returnCreatedTime = False, returnEntitySchoolYearHonorRollRunLevelName = False, returnHonorRollRunHistoryID = False, returnHonorRollRunLevelID = False, returnModifiedTime = False, returnParameterDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRunLevelHistory(HonorRollRunLevelHistoryID, EntityID = 1, returnreturnHonorRollRunLevelHistoryID = False, returnreturnCreatedTime = False, returnreturnEntitySchoolYearHonorRollRunLevelName = False, returnreturnHonorRollRunHistoryID = False, returnreturnHonorRollRunLevelID = False, returnreturnModifiedTime = False, returnreturnParameterDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(HonorRollRunLevelHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRunLevelHistory(HonorRollRunLevelHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(HonorRollRunLevelHistoryID), verb = "delete")

	return(response)

def getEveryHonorRollRunLevelRule(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunLevelRuleID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelRuleIDClonedFrom = False, returnModifiedTime = False, returnParameterDescription = False, returnRuleType = False, returnRuleTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getHonorRollRunLevelRule(HonorRollRunLevelRuleID, EntityID = 1, returnreturnHonorRollRunLevelRuleID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnHonorRollRunLevelID = False, returnreturnHonorRollRunLevelRuleIDClonedFrom = False, returnreturnModifiedTime = False, returnreturnParameterDescription = False, returnreturnRuleType = False, returnreturnRuleTypeCode = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(HonorRollRunLevelRuleID), verb = "get", params_list = params_list)

	return(response)

def deleteHonorRollRunLevelRule(HonorRollRunLevelRuleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(HonorRollRunLevelRuleID), verb = "delete")

	return(response)

def getEveryPointSet(EntityID = 1, page = 1, pageSize = 100, returnPointSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPointSet(PointSetID, EntityID = 1, returnreturnPointSetID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictGroupKey = False, returnreturnDistrictID = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnNameDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(PointSetID), verb = "get", params_list = params_list)

	return(response)

def deletePointSet(PointSetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(PointSetID), verb = "delete")

	return(response)

def getEveryPointSetEntity(EntityID = 1, page = 1, pageSize = 100, returnPointSetEntityID = True, returnApplyFactorBasedAddOn = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnPointSetEntityIDClonedFrom = False, returnPointSetID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPointSetEntity(PointSetEntityID, EntityID = 1, returnreturnPointSetEntityID = False, returnreturnApplyFactorBasedAddOn = False, returnreturnCreatedTime = False, returnreturnDisplayOrder = False, returnreturnEntityGroupKey = False, returnreturnEntityID = False, returnreturnIsDefault = False, returnreturnModifiedTime = False, returnreturnPointSetEntityIDClonedFrom = False, returnreturnPointSetID = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(PointSetEntityID), verb = "get", params_list = params_list)

	return(response)

def deletePointSetEntity(PointSetEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(PointSetEntityID), verb = "delete")

	return(response)

def getEveryQueuedGPACalculation(EntityID = 1, page = 1, pageSize = 100, returnQueuedGPACalculationID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSchoolYearID = False, returnSkipCredits = False, returnSourcePrimaryKey = False, returnSourceType = False, returnSourceTypeCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getQueuedGPACalculation(QueuedGPACalculationID, EntityID = 1, returnreturnQueuedGPACalculationID = False, returnreturnCreatedTime = False, returnreturnEndTime = False, returnreturnEntityID = False, returnreturnHostName = False, returnreturnModifiedTime = False, returnreturnProcessID = False, returnreturnSchoolYearID = False, returnreturnSkipCredits = False, returnreturnSourcePrimaryKey = False, returnreturnSourceType = False, returnreturnSourceTypeCode = False, returnreturnStartTime = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnThreadName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDImpersonator = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(QueuedGPACalculationID), verb = "get", params_list = params_list)

	return(response)

def deleteQueuedGPACalculation(QueuedGPACalculationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(QueuedGPACalculationID), verb = "delete")

	return(response)

def getEveryRankMethod(EntityID = 1, page = 1, pageSize = 100, returnRankMethodID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnIncludeNonRankedStudents = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueRangeHigh = False, returnValueRangeLow = False, returnValueRangeType = False, returnValueRangeTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRankMethod(RankMethodID, EntityID = 1, returnreturnRankMethodID = False, returnreturnCreatedTime = False, returnreturnDistrictGroupKey = False, returnreturnGPABucketID = False, returnreturnGPAMethodID = False, returnreturnGPAType = False, returnreturnGPATypeCode = False, returnreturnIncludeNonRankedStudents = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValueRangeHigh = False, returnreturnValueRangeLow = False, returnreturnValueRangeType = False, returnreturnValueRangeTypeCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(RankMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteRankMethod(RankMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(RankMethodID), verb = "delete")

	return(response)

def getEveryRankMethodStudentRangeSetup(EntityID = 1, page = 1, pageSize = 100, returnRankMethodStudentRangeSetupID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethodStudentRangeSetup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRankMethodStudentRangeSetup(RankMethodStudentRangeSetupID, EntityID = 1, returnreturnRankMethodStudentRangeSetupID = False, returnreturnConfigEntityGroupYearID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnRankMethodID = False, returnreturnStudentRangeID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethodStudentRangeSetup/" + str(RankMethodStudentRangeSetupID), verb = "get", params_list = params_list)

	return(response)

def deleteRankMethodStudentRangeSetup(RankMethodStudentRangeSetupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethodStudentRangeSetup/" + str(RankMethodStudentRangeSetupID), verb = "delete")

	return(response)

def getEveryRankRunHistory(EntityID = 1, page = 1, pageSize = 100, returnRankRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnFullGroupingDescription = False, returnGPAAsOfDate = False, returnGradeLevelIDCohort = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentGroup = False, returnStudentGroupCode = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRankRunHistory(RankRunHistoryID, EntityID = 1, returnreturnRankRunHistoryID = False, returnreturnCalculation = False, returnreturnCalculationCode = False, returnreturnCreatedTime = False, returnreturnDate = False, returnreturnDescription = False, returnreturnFullGroupingDescription = False, returnreturnGPAAsOfDate = False, returnreturnGradeLevelIDCohort = False, returnreturnModifiedTime = False, returnreturnRankMethodID = False, returnreturnStudentGroup = False, returnreturnStudentGroupCode = False, returnreturnStudentRangeID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(RankRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteRankRunHistory(RankRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(RankRunHistoryID), verb = "delete")

	return(response)

def getEverySectionLengthGPABucket(EntityID = 1, page = 1, pageSize = 100, returnSectionLengthGPABucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketEntityID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSectionLengthGPABucketIDClonedFrom = False, returnSectionLengthID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSectionLengthGPABucket(SectionLengthGPABucketID, EntityID = 1, returnreturnSectionLengthGPABucketID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnGPABucketEntityID = False, returnreturnIsUpToDate = False, returnreturnModifiedTime = False, returnreturnSectionLengthGPABucketIDClonedFrom = False, returnreturnSectionLengthID = False, returnreturnStatus = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(SectionLengthGPABucketID), verb = "get", params_list = params_list)

	return(response)

def deleteSectionLengthGPABucket(SectionLengthGPABucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(SectionLengthGPABucketID), verb = "delete")

	return(response)

def getEveryStudentCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentCodeID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentCommentBucket(StudentCommentBucketID, EntityID = 1, returnreturnStudentCommentBucketID = False, returnreturnCommentBucketID = False, returnreturnCommentCodeID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodID = False, returnreturnModifiedTime = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(StudentCommentBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentCommentBucket(StudentCommentBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(StudentCommentBucketID), verb = "delete")

	return(response)

def getEveryStudentFreeFormCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentFreeFormCommentBucketID = True, returnComment = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentFreeFormCommentBucket(StudentFreeFormCommentBucketID, EntityID = 1, returnreturnStudentFreeFormCommentBucketID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnGradingPeriodID = False, returnreturnModifiedTime = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(StudentFreeFormCommentBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentFreeFormCommentBucket(StudentFreeFormCommentBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(StudentFreeFormCommentBucketID), verb = "delete")

	return(response)

def getEveryStudentGPABucket(EntityID = 1, page = 1, pageSize = 100, returnStudentGPABucketID = True, returnBonusGPAPoints = False, returnCreatedTime = False, returnDisplayGPACredits = False, returnDisplayGPAPoints = False, returnEntityID = False, returnGPACredits = False, returnGPAPoints = False, returnGPAWithBonus = False, returnGradReqRankGPAStatus = False, returnGradReqRankGPAStatusCode = False, returnHasAllGradesRequiredForGPACalculation = False, returnModifiedTime = False, returnPointsAndCreditsMultiplier = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnStudentSectionGPABucketGroupID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGPABucket(StudentGPABucketID, EntityID = 1, returnreturnStudentGPABucketID = False, returnreturnBonusGPAPoints = False, returnreturnCreatedTime = False, returnreturnDisplayGPACredits = False, returnreturnDisplayGPAPoints = False, returnreturnEntityID = False, returnreturnGPACredits = False, returnreturnGPAPoints = False, returnreturnGPAWithBonus = False, returnreturnGradReqRankGPAStatus = False, returnreturnGradReqRankGPAStatusCode = False, returnreturnHasAllGradesRequiredForGPACalculation = False, returnreturnModifiedTime = False, returnreturnPointsAndCreditsMultiplier = False, returnreturnSchoolYearID = False, returnreturnStudentGradeBucketID = False, returnreturnStudentSectionGPABucketGroupID = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(StudentGPABucketID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGPABucket(StudentGPABucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(StudentGPABucketID), verb = "delete")

	return(response)

def getEveryStudentGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentGPABucketGroupID = True, returnBonusGPA = False, returnBonusGPAWithoutRounding = False, returnCreatedTime = False, returnCurrentDefaultDistrictID = False, returnEarnedCredits = False, returnElectiveBonusGPA = False, returnElectiveFactor = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnFactorBonusGPA = False, returnFactorBonusGPAWithoutRounding = False, returnFailedCredits = False, returnFinalGPARoundingDecimals = False, returnGPA = False, returnGPABucketID = False, returnGPACalculationRoundingDecimals = False, returnGPACredits = False, returnGPACreditsWithoutRounding = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsWithoutRounding = False, returnGPAWithBonus = False, returnGPAWithFactorBonus = False, returnGradReqRankGPABreakdown = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGPABucketGroup(StudentGPABucketGroupID, EntityID = 1, returnreturnStudentGPABucketGroupID = False, returnreturnBonusGPA = False, returnreturnBonusGPAWithoutRounding = False, returnreturnCreatedTime = False, returnreturnCurrentDefaultDistrictID = False, returnreturnEarnedCredits = False, returnreturnElectiveBonusGPA = False, returnreturnElectiveFactor = False, returnreturnElectiveGPACredits = False, returnreturnElectiveGPAPoints = False, returnreturnFactorBonusGPA = False, returnreturnFactorBonusGPAWithoutRounding = False, returnreturnFailedCredits = False, returnreturnFinalGPARoundingDecimals = False, returnreturnGPA = False, returnreturnGPABucketID = False, returnreturnGPACalculationRoundingDecimals = False, returnreturnGPACredits = False, returnreturnGPACreditsWithoutRounding = False, returnreturnGPAMethodID = False, returnreturnGPAPoints = False, returnreturnGPAPointsWithoutRounding = False, returnreturnGPAWithBonus = False, returnreturnGPAWithFactorBonus = False, returnreturnGradReqRankGPABreakdown = False, returnreturnModifiedTime = False, returnreturnRequiredBonusGPA = False, returnreturnRequiredGPACredits = False, returnreturnRequiredGPAPoints = False, returnreturnSchoolYearID = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(StudentGPABucketGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGPABucketGroup(StudentGPABucketGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(StudentGPABucketGroupID), verb = "delete")

	return(response)

def getEveryStudentGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketID = True, returnAbsentCount = False, returnCalculatedCalculationTypeCode = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnCalculatedClosedGradingPeriodGradeChangeStatusCode = False, returnCalculatedPoints = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCompleteByTeacher = False, returnCompleteByTeacherCode = False, returnCompletionDate = False, returnCompletionDateOverride = False, returnConfigEarnedCredits = False, returnConfigFailedCredits = False, returnCreatedTime = False, returnDoNotPost = False, returnEarnedCreditAttempted = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEarnedPoints = False, returnEntityID = False, returnExcusedCount = False, returnFailedCredits = False, returnGradeMarkID = False, returnGradeMarkIDOutOfDistrictTransferWithdraw = False, returnGradeMarkIDOverride = False, returnGradeMarkIDToApply = False, returnGradeMarkIDToUse = False, returnGradeMarkIDToUseIgnoreDoNotPost = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnGradeMarkToUseExists = False, returnGradeMarkToUseIgnoreDoNotPost = False, returnGradingPeriodEndDateHasPassed = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandardGrades = False, returnHasAssignments = False, returnHasStudentSectionGradingScaleGradeBucket = False, returnHasStudentSectionLinkConflict = False, returnHasSubjectGrades = False, returnHasUnscoredRequiredFeederBucket = False, returnIsAdminOverride = False, returnIsComplete = False, returnIsTransferBucket = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnNoGradebookOrAdminOverride = False, returnNoGradebookOverride = False, returnOtherCount = False, returnOverrideComment = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentHasChangedWithinSpecifiedAmountOfTime = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentIgnoreMinimum = False, returnPercentWithAdjustmentNoCap = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithAdjustmentWithGradeMarkToUseIgnoreDoNotPost = False, returnPercentWithAdjustmentWithGradeMarkToUseNoCap = False, returnPercentWithGradeMarkIgnoreDoNotPost = False, returnPossiblePoints = False, returnReportCardGradeMarkToUse = False, returnSchoolYearID = False, returnSectionID = False, returnStartingPercent = False, returnStudentCommentBucketCount = False, returnStudentFreeFormCommentBucketCount = False, returnStudentGradeBucketFlag = False, returnStudentGradeBucketStatus = False, returnStudentSectionID = False, returnTardyCount = False, returnUnexcusedCount = False, returnUseCompletionDateOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentForGradeBucket = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGradeBucket(StudentGradeBucketID, EntityID = 1, returnreturnStudentGradeBucketID = False, returnreturnAbsentCount = False, returnreturnCalculatedCalculationTypeCode = False, returnreturnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnreturnCalculatedClosedGradingPeriodGradeChangeStatusCode = False, returnreturnCalculatedPoints = False, returnreturnClosedGradingPeriodGradeChangeStatus = False, returnreturnClosedGradingPeriodGradeChangeStatusCode = False, returnreturnCompleteByTeacher = False, returnreturnCompleteByTeacherCode = False, returnreturnCompletionDate = False, returnreturnCompletionDateOverride = False, returnreturnConfigEarnedCredits = False, returnreturnConfigFailedCredits = False, returnreturnCreatedTime = False, returnreturnDoNotPost = False, returnreturnEarnedCreditAttempted = False, returnreturnEarnedCredits = False, returnreturnEarnedCreditsPossible = False, returnreturnEarnedPoints = False, returnreturnEntityID = False, returnreturnExcusedCount = False, returnreturnFailedCredits = False, returnreturnGradeMarkID = False, returnreturnGradeMarkIDOutOfDistrictTransferWithdraw = False, returnreturnGradeMarkIDOverride = False, returnreturnGradeMarkIDToApply = False, returnreturnGradeMarkIDToUse = False, returnreturnGradeMarkIDToUseIgnoreDoNotPost = False, returnreturnGradeMarkOverrideComment = False, returnreturnGradeMarkToUse = False, returnreturnGradeMarkToUseExists = False, returnreturnGradeMarkToUseIgnoreDoNotPost = False, returnreturnGradingPeriodEndDateHasPassed = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnHasAcademicStandardGrades = False, returnreturnHasAssignments = False, returnreturnHasStudentSectionGradingScaleGradeBucket = False, returnreturnHasStudentSectionLinkConflict = False, returnreturnHasSubjectGrades = False, returnreturnHasUnscoredRequiredFeederBucket = False, returnreturnIsAdminOverride = False, returnreturnIsComplete = False, returnreturnIsTransferBucket = False, returnreturnIsUsingPointsBasedScale = False, returnreturnModifiedTime = False, returnreturnNoGradebookOrAdminOverride = False, returnreturnNoGradebookOverride = False, returnreturnOtherCount = False, returnreturnOverrideComment = False, returnreturnPercent = False, returnreturnPercentAdjustment = False, returnreturnPercentAdjustmentComment = False, returnreturnPercentHasChangedWithinSpecifiedAmountOfTime = False, returnreturnPercentWithAdjustment = False, returnreturnPercentWithAdjustmentFormatted = False, returnreturnPercentWithAdjustmentIgnoreMinimum = False, returnreturnPercentWithAdjustmentNoCap = False, returnreturnPercentWithAdjustmentWithGradeMarkToUse = False, returnreturnPercentWithAdjustmentWithGradeMarkToUseIgnoreDoNotPost = False, returnreturnPercentWithAdjustmentWithGradeMarkToUseNoCap = False, returnreturnPercentWithGradeMarkIgnoreDoNotPost = False, returnreturnPossiblePoints = False, returnreturnReportCardGradeMarkToUse = False, returnreturnSchoolYearID = False, returnreturnSectionID = False, returnreturnStartingPercent = False, returnreturnStudentCommentBucketCount = False, returnreturnStudentFreeFormCommentBucketCount = False, returnreturnStudentGradeBucketFlag = False, returnreturnStudentGradeBucketStatus = False, returnreturnStudentSectionID = False, returnreturnTardyCount = False, returnreturnUnexcusedCount = False, returnreturnUseCompletionDateOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWeightPercentForGradeBucket = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(StudentGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradeBucket(StudentGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(StudentGradeBucketID), verb = "delete")

	return(response)

def getEveryStudentGradeBucketFlag(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketFlagID = True, returnCreatedTime = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False, returnAPIOptionFlags = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentGradeBucketFlag(StudentGradeBucketFlagID, EntityID = 1, returnreturnStudentGradeBucketFlagID = False, returnreturnCreatedTime = False, returnreturnGradeBucketFlagID = False, returnreturnModifiedTime = False, returnreturnStudentGradeBucketID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False, returnreturnAPIOptionFlags = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(StudentGradeBucketFlagID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentGradeBucketFlag(StudentGradeBucketFlagID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(StudentGradeBucketFlagID), verb = "delete")

	return(response)

def getEveryStudentHonorRollRunLevel(EntityID = 1, page = 1, pageSize = 100, returnStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentHonorRollRunLevel(StudentHonorRollRunLevelID, EntityID = 1, returnreturnStudentHonorRollRunLevelID = False, returnreturnCreatedTime = False, returnreturnGPAValue = False, returnreturnHonorRollRunLevelHistoryID = False, returnreturnModifiedTime = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(StudentHonorRollRunLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentHonorRollRunLevel(StudentHonorRollRunLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(StudentHonorRollRunLevelID), verb = "delete")

	return(response)

def getEveryStudentRange(EntityID = 1, page = 1, pageSize = 100, returnStudentRangeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnFilter = False, returnIsActive = False, returnModifiedTime = False, returnRank = False, returnSchoolID = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnStatus = False, returnStatusCode = False, returnStudentTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRange/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentRange(StudentRangeID, EntityID = 1, returnreturnStudentRangeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnEntityID = False, returnreturnFilter = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnRank = False, returnreturnSchoolID = False, returnreturnSchoolYearID = False, returnreturnSearchConditionFilter = False, returnreturnStatus = False, returnreturnStatusCode = False, returnreturnStudentTypeID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRange/" + str(StudentRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentRange(StudentRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRange/" + str(StudentRangeID), verb = "delete")

	return(response)

def getEveryStudentRank(EntityID = 1, page = 1, pageSize = 100, returnStudentRankID = True, returnCreatedTime = False, returnDisplayRank = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNumberInRank = False, returnNumberOutOf = False, returnRankRunHistoryID = False, returnSchoolYearIDCohort = False, returnStudentID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentRank(StudentRankID, EntityID = 1, returnreturnStudentRankID = False, returnreturnCreatedTime = False, returnreturnDisplayRank = False, returnreturnIsManualRank = False, returnreturnIsProspectiveRank = False, returnreturnModifiedTime = False, returnreturnNumberInRank = False, returnreturnNumberOutOf = False, returnreturnRankRunHistoryID = False, returnreturnSchoolYearIDCohort = False, returnreturnStudentID = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValue = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(StudentRankID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentRank(StudentRankID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(StudentRankID), verb = "delete")

	return(response)

def getEveryStudentSectionGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionGPABucketGroupID = True, returnBonusGPA = False, returnCreatedTime = False, returnElectiveBonusGPA = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnEntityID = False, returnFactorBasedGPACountTotal = False, returnGPACredits = False, returnGPAPoints = False, returnIsGPAElective = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentSectionID = False, returnTotalAddOnPoints = False, returnTotalGPACredits = False, returnTotalGPAPoints = False, returnUseGPATotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentSectionGPABucketGroup(StudentSectionGPABucketGroupID, EntityID = 1, returnreturnStudentSectionGPABucketGroupID = False, returnreturnBonusGPA = False, returnreturnCreatedTime = False, returnreturnElectiveBonusGPA = False, returnreturnElectiveGPACredits = False, returnreturnElectiveGPAPoints = False, returnreturnEntityID = False, returnreturnFactorBasedGPACountTotal = False, returnreturnGPACredits = False, returnreturnGPAPoints = False, returnreturnIsGPAElective = False, returnreturnModifiedTime = False, returnreturnRequiredBonusGPA = False, returnreturnRequiredGPACredits = False, returnreturnRequiredGPAPoints = False, returnreturnSchoolYearID = False, returnreturnStudentGPABucketGroupID = False, returnreturnStudentSectionID = False, returnreturnTotalAddOnPoints = False, returnreturnTotalGPACredits = False, returnreturnTotalGPAPoints = False, returnreturnUseGPATotalOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(StudentSectionGPABucketGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSectionGPABucketGroup(StudentSectionGPABucketGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(StudentSectionGPABucketGroupID), verb = "delete")

	return(response)

def getEveryStudentSectionGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionGPAMethodID = True, returnCreatedTime = False, returnCumulativeGPACredits = False, returnCumulativeGPAPoints = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentSectionGPAMethod(StudentSectionGPAMethodID, EntityID = 1, returnreturnStudentSectionGPAMethodID = False, returnreturnCreatedTime = False, returnreturnCumulativeGPACredits = False, returnreturnCumulativeGPAPoints = False, returnreturnGPACredits = False, returnreturnGPAMethodEntityID = False, returnreturnModifiedTime = False, returnreturnPointSetEntityID = False, returnreturnStudentSectionID = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(StudentSectionGPAMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentSectionGPAMethod(StudentSectionGPAMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(StudentSectionGPAMethodID), verb = "delete")

	return(response)

def getEveryTempFactorBasedAddOn(EntityID = 1, page = 1, pageSize = 100, returnTempFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnGPABucketEntityDisplayName = False, returnGradeReferenceDisplayName = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnOriginalGradingEndDateCutoffForCumulative = False, returnTempFactorBasedAddOnClonedFromID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempFactorBasedAddOn(TempFactorBasedAddOnID, EntityID = 1, returnreturnTempFactorBasedAddOnID = False, returnreturnCreatedTime = False, returnreturnFactor = False, returnreturnGPABucketEntityDisplayName = False, returnreturnGradeReferenceDisplayName = False, returnreturnGradingEndDateCutoffForCumulative = False, returnreturnModifiedTime = False, returnreturnOriginalGradingEndDateCutoffForCumulative = False, returnreturnTempFactorBasedAddOnClonedFromID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(TempFactorBasedAddOnID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFactorBasedAddOn(TempFactorBasedAddOnID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(TempFactorBasedAddOnID), verb = "delete")

	return(response)

def getEveryTempFailedGradingPeriod(EntityID = 1, page = 1, pageSize = 100, returnTempFailedGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNote = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnTempGradingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempFailedGradingPeriod(TempFailedGradingPeriodID, EntityID = 1, returnreturnTempFailedGradingPeriodID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndDate = False, returnreturnGradingPeriodID = False, returnreturnGradingPeriodSetCode = False, returnreturnGradingPeriodSetCodeDescription = False, returnreturnGradingPeriodSetID = False, returnreturnIsUpdated = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnNumber = False, returnreturnOriginalEndDate = False, returnreturnOriginalStartDate = False, returnreturnProcessAction = False, returnreturnProcessActionCode = False, returnreturnSectionLengthCode = False, returnreturnSectionLengthCodeDescription = False, returnreturnSectionLengthID = False, returnreturnStartDate = False, returnreturnTempGradingPeriodID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(TempFailedGradingPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteTempFailedGradingPeriod(TempFailedGradingPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(TempFailedGradingPeriodID), verb = "delete")

	return(response)

def getEveryTempGradeBucketFlagDetailGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnTempGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnGPAMethodDescription = False, returnGradeBucketFlagCodeName = False, returnModifiedTime = False, returnPointSetDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeBucketFlagDetailGPAMethod(TempGradeBucketFlagDetailGPAMethodID, EntityID = 1, returnreturnTempGradeBucketFlagDetailGPAMethodID = False, returnreturnCreatedTime = False, returnreturnGPAMethodDescription = False, returnreturnGradeBucketFlagCodeName = False, returnreturnModifiedTime = False, returnreturnPointSetDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(TempGradeBucketFlagDetailGPAMethodID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeBucketFlagDetailGPAMethod(TempGradeBucketFlagDetailGPAMethodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(TempGradeBucketFlagDetailGPAMethodID), verb = "delete")

	return(response)

def getEveryTempGradeMarkPointSetError(EntityID = 1, page = 1, pageSize = 100, returnTempGradeMarkPointSetErrorID = True, returnCreatedTime = False, returnErrorString = False, returnGPAMethodName = False, returnGradeMarkCode = False, returnModifiedTime = False, returnPointSetName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeMarkPointSetError(TempGradeMarkPointSetErrorID, EntityID = 1, returnreturnTempGradeMarkPointSetErrorID = False, returnreturnCreatedTime = False, returnreturnErrorString = False, returnreturnGPAMethodName = False, returnreturnGradeMarkCode = False, returnreturnModifiedTime = False, returnreturnPointSetName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(TempGradeMarkPointSetErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeMarkPointSetError(TempGradeMarkPointSetErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(TempGradeMarkPointSetErrorID), verb = "delete")

	return(response)

def getEveryTempGradeReportAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarDescription = False, returnCreatedTime = False, returnEndDate = False, returnEntityName = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeReportAttendanceTerm(TempGradeReportAttendanceTermID, EntityID = 1, returnreturnTempGradeReportAttendanceTermID = False, returnreturnAttendanceTermCode = False, returnreturnAttendanceTermID = False, returnreturnCalendarDescription = False, returnreturnCreatedTime = False, returnreturnEndDate = False, returnreturnEntityName = False, returnreturnModifiedTime = False, returnreturnSchoolYearDescription = False, returnreturnStartDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(TempGradeReportAttendanceTermID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeReportAttendanceTerm(TempGradeReportAttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(TempGradeReportAttendanceTermID), verb = "delete")

	return(response)

def getEveryTempGradeReportGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportGradeBucketID = True, returnCreatedTime = False, returnEntityName = False, returnGradeBucketLabel = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSectionLengthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeReportGradeBucket(TempGradeReportGradeBucketID, EntityID = 1, returnreturnTempGradeReportGradeBucketID = False, returnreturnCreatedTime = False, returnreturnEntityName = False, returnreturnGradeBucketLabel = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnSchoolYearDescription = False, returnreturnSectionLengthDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(TempGradeReportGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeReportGradeBucket(TempGradeReportGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(TempGradeReportGradeBucketID), verb = "delete")

	return(response)

def getEveryTempGradeReportTemplate(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportTemplateID = True, returnCreatedTime = False, returnEntityCodeNameClonedFrom = False, returnEntityCodeNameClonedTo = False, returnEntityID = False, returnErrorCount = False, returnHasErrors = False, returnModifiedTime = False, returnNewGradeReportTemplateDescription = False, returnOriginalGradeReportTemplateDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeReportTemplate(TempGradeReportTemplateID, EntityID = 1, returnreturnTempGradeReportTemplateID = False, returnreturnCreatedTime = False, returnreturnEntityCodeNameClonedFrom = False, returnreturnEntityCodeNameClonedTo = False, returnreturnEntityID = False, returnreturnErrorCount = False, returnreturnHasErrors = False, returnreturnModifiedTime = False, returnreturnNewGradeReportTemplateDescription = False, returnreturnOriginalGradeReportTemplateDescription = False, returnreturnSchoolYearID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(TempGradeReportTemplateID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeReportTemplate(TempGradeReportTemplateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(TempGradeReportTemplateID), verb = "delete")

	return(response)

def getEveryTempGradeReportTemplateError(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportTemplateErrorID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempGradeReportTemplateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradeReportTemplateError(TempGradeReportTemplateErrorID, EntityID = 1, returnreturnTempGradeReportTemplateErrorID = False, returnreturnCreatedTime = False, returnreturnError = False, returnreturnErrorDetail = False, returnreturnModifiedTime = False, returnreturnTempGradeReportTemplateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(TempGradeReportTemplateErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradeReportTemplateError(TempGradeReportTemplateErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(TempGradeReportTemplateErrorID), verb = "delete")

	return(response)

def getEveryTempGradingPeriod(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradingPeriod(TempGradingPeriodID, EntityID = 1, returnreturnTempGradingPeriodID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEndDate = False, returnreturnGradingPeriodID = False, returnreturnGradingPeriodSetCode = False, returnreturnGradingPeriodSetCodeDescription = False, returnreturnGradingPeriodSetID = False, returnreturnIsUpdated = False, returnreturnModifiedTime = False, returnreturnNumber = False, returnreturnOriginalEndDate = False, returnreturnOriginalStartDate = False, returnreturnProcessAction = False, returnreturnProcessActionCode = False, returnreturnSectionLengthCode = False, returnreturnSectionLengthCodeDescription = False, returnreturnSectionLengthID = False, returnreturnStartDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(TempGradingPeriodID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingPeriod(TempGradingPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(TempGradingPeriodID), verb = "delete")

	return(response)

def getEveryTempGradingPeriodError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodErrorID = True, returnAcademicStandard = False, returnAssignmentName = False, returnCategory = False, returnCourseDescription = False, returnCreatedTime = False, returnDueDate = False, returnError = False, returnModifiedTime = False, returnSectionNumber = False, returnSubject = False, returnTeacherName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradingPeriodError(TempGradingPeriodErrorID, EntityID = 1, returnreturnTempGradingPeriodErrorID = False, returnreturnAcademicStandard = False, returnreturnAssignmentName = False, returnreturnCategory = False, returnreturnCourseDescription = False, returnreturnCreatedTime = False, returnreturnDueDate = False, returnreturnError = False, returnreturnModifiedTime = False, returnreturnSectionNumber = False, returnreturnSubject = False, returnreturnTeacherName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(TempGradingPeriodErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingPeriodError(TempGradingPeriodErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(TempGradingPeriodErrorID), verb = "delete")

	return(response)

def getEveryTempGradingPeriodUpdateProcessError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodUpdateProcessErrorID = True, returnCreatedTime = False, returnErrorDetail = False, returnModifiedTime = False, returnProcessName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodUpdateProcessError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradingPeriodUpdateProcessError(TempGradingPeriodUpdateProcessErrorID, EntityID = 1, returnreturnTempGradingPeriodUpdateProcessErrorID = False, returnreturnCreatedTime = False, returnreturnErrorDetail = False, returnreturnModifiedTime = False, returnreturnProcessName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodUpdateProcessError/" + str(TempGradingPeriodUpdateProcessErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingPeriodUpdateProcessError(TempGradingPeriodUpdateProcessErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodUpdateProcessError/" + str(TempGradingPeriodUpdateProcessErrorID), verb = "delete")

	return(response)

def getEveryTempGradingUtilityError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingUtilityErrorID = True, returnCreatedTime = False, returnError = False, returnGrade = False, returnHonorRollName = False, returnModifiedTime = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempGradingUtilityError(TempGradingUtilityErrorID, EntityID = 1, returnreturnTempGradingUtilityErrorID = False, returnreturnCreatedTime = False, returnreturnError = False, returnreturnGrade = False, returnreturnHonorRollName = False, returnreturnModifiedTime = False, returnreturnStudentName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValue = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(TempGradingUtilityErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempGradingUtilityError(TempGradingUtilityErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(TempGradingUtilityErrorID), verb = "delete")

	return(response)

def getEveryTempHonorRollGradeMarkMethodRange(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeID = True, returnCreatedTime = False, returnHonorRollGradeMarkMethodID = False, returnHonorRollGradeMarkMethodRangeID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnPriorityOrder = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHonorRollGradeMarkMethodRange(TempHonorRollGradeMarkMethodRangeID, EntityID = 1, returnreturnTempHonorRollGradeMarkMethodRangeID = False, returnreturnCreatedTime = False, returnreturnHonorRollGradeMarkMethodID = False, returnreturnHonorRollGradeMarkMethodRangeID = False, returnreturnIsActive = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnPriorityOrder = False, returnreturnTotalAllowableExceptions = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(TempHonorRollGradeMarkMethodRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHonorRollGradeMarkMethodRange(TempHonorRollGradeMarkMethodRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(TempHonorRollGradeMarkMethodRangeID), verb = "delete")

	return(response)

def getEveryTempHonorRollGradeMarkMethodRangeCourseGroup(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnHonorRollGradeMarkMethodRangeCourseGroupID = False, returnHonorRollGradeMarkMethodRangeID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHonorRollGradeMarkMethodRangeCourseGroup(TempHonorRollGradeMarkMethodRangeCourseGroupID, EntityID = 1, returnreturnTempHonorRollGradeMarkMethodRangeCourseGroupID = False, returnreturnCourseGroupID = False, returnreturnCreatedTime = False, returnreturnHonorRollGradeMarkMethodRangeCourseGroupID = False, returnreturnHonorRollGradeMarkMethodRangeID = False, returnreturnModifiedTime = False, returnreturnTempHonorRollGradeMarkMethodRangeID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(TempHonorRollGradeMarkMethodRangeCourseGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHonorRollGradeMarkMethodRangeCourseGroup(TempHonorRollGradeMarkMethodRangeCourseGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(TempHonorRollGradeMarkMethodRangeCourseGroupID), verb = "delete")

	return(response)

def getEveryTempHonorRollGradeMarkMethodRangeGradeMark(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnHonorRollGradeMarkMethodRangeGradeMarkID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHonorRollGradeMarkMethodRangeGradeMark(TempHonorRollGradeMarkMethodRangeGradeMarkID, EntityID = 1, returnreturnTempHonorRollGradeMarkMethodRangeGradeMarkID = False, returnreturnCreatedTime = False, returnreturnGradeMarkID = False, returnreturnHonorRollGradeMarkMethodRangeGradeMarkID = False, returnreturnModifiedTime = False, returnreturnTempHonorRollGradeMarkMethodRangeID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(TempHonorRollGradeMarkMethodRangeGradeMarkID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHonorRollGradeMarkMethodRangeGradeMark(TempHonorRollGradeMarkMethodRangeGradeMarkID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(TempHonorRollGradeMarkMethodRangeGradeMarkID), verb = "delete")

	return(response)

def getEveryTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID, EntityID = 1, returnreturnTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnreturnCreatedTime = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnreturnModifiedTime = False, returnreturnTempHonorRollGradeMarkMethodRangeID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID), verb = "delete")

	return(response)

def getEveryTempHonorRollMethodRange(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollMethodRangeID = True, returnCreatedTime = False, returnGPAHigh = False, returnGPALow = False, returnHonorRollMethodRangeID = False, returnIsUsed = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempHonorRollMethodRange(TempHonorRollMethodRangeID, EntityID = 1, returnreturnTempHonorRollMethodRangeID = False, returnreturnCreatedTime = False, returnreturnGPAHigh = False, returnreturnGPALow = False, returnreturnHonorRollMethodRangeID = False, returnreturnIsUsed = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(TempHonorRollMethodRangeID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHonorRollMethodRange(TempHonorRollMethodRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(TempHonorRollMethodRangeID), verb = "delete")

	return(response)

def getEveryTempMassChangeSystemDatesError(EntityID = 1, page = 1, pageSize = 100, returnTempMassChangeSystemDatesErrorID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnIsParent = False, returnModifiedTime = False, returnOriginalPrimaryKey = False, returnParentPrimaryKey = False, returnSortOrder = False, returnTableType = False, returnTableTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempMassChangeSystemDatesError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempMassChangeSystemDatesError(TempMassChangeSystemDatesErrorID, EntityID = 1, returnreturnTempMassChangeSystemDatesErrorID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnError = False, returnreturnIsParent = False, returnreturnModifiedTime = False, returnreturnOriginalPrimaryKey = False, returnreturnParentPrimaryKey = False, returnreturnSortOrder = False, returnreturnTableType = False, returnreturnTableTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempMassChangeSystemDatesError/" + str(TempMassChangeSystemDatesErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempMassChangeSystemDatesError(TempMassChangeSystemDatesErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempMassChangeSystemDatesError/" + str(TempMassChangeSystemDatesErrorID), verb = "delete")

	return(response)

def getEveryTempStudentCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnTempStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentBucketName = False, returnCreatedTime = False, returnCurrentCommentCode = False, returnDisplayOrder = False, returnGradingPeriodDescription = False, returnGradingPeriodID = False, returnModifiedTime = False, returnNewCommentCode = False, returnNewCommentCodeID = False, returnSectionLengthCode = False, returnStudentCommentBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentCommentBucket(TempStudentCommentBucketID, EntityID = 1, returnreturnTempStudentCommentBucketID = False, returnreturnCommentBucketID = False, returnreturnCommentBucketName = False, returnreturnCreatedTime = False, returnreturnCurrentCommentCode = False, returnreturnDisplayOrder = False, returnreturnGradingPeriodDescription = False, returnreturnGradingPeriodID = False, returnreturnModifiedTime = False, returnreturnNewCommentCode = False, returnreturnNewCommentCodeID = False, returnreturnSectionLengthCode = False, returnreturnStudentCommentBucketID = False, returnreturnStudentName = False, returnreturnStudentSectionDescription = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWorkflowAction = False, returnreturnWorkflowActionCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(TempStudentCommentBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentCommentBucket(TempStudentCommentBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(TempStudentCommentBucketID), verb = "delete")

	return(response)

def getEveryTempStudentGPABucket(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGPABucketID = True, returnCorrectBonusGPAPoints = False, returnCorrectGPACredits = False, returnCorrectGPAPoints = False, returnCourseName = False, returnCreatedTime = False, returnCurrentBonusGPAPoints = False, returnCurrentGPACredits = False, returnCurrentGPAPoints = False, returnEntityID = False, returnGPABucketCodeDescription = False, returnGPABucketID = False, returnGPAMethodCodeDescription = False, returnGPAMethodID = False, returnGradeBucketCodeDescription = False, returnGradingPeriodGradeBucketID = False, returnIsDelete = False, returnIsGradReqRankGPA = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSchoolYearIDForPostSave = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentGPABucketID = False, returnStudentGradeBucketID = False, returnStudentGradeBucketIsFromTemp = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionGPABucketGroupID = False, returnStudentSectionGPABucketGroupIsFromTemp = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentGPABucket(TempStudentGPABucketID, EntityID = 1, returnreturnTempStudentGPABucketID = False, returnreturnCorrectBonusGPAPoints = False, returnreturnCorrectGPACredits = False, returnreturnCorrectGPAPoints = False, returnreturnCourseName = False, returnreturnCreatedTime = False, returnreturnCurrentBonusGPAPoints = False, returnreturnCurrentGPACredits = False, returnreturnCurrentGPAPoints = False, returnreturnEntityID = False, returnreturnGPABucketCodeDescription = False, returnreturnGPABucketID = False, returnreturnGPAMethodCodeDescription = False, returnreturnGPAMethodID = False, returnreturnGradeBucketCodeDescription = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnIsDelete = False, returnreturnIsGradReqRankGPA = False, returnreturnModifiedTime = False, returnreturnSchoolYearDescription = False, returnreturnSchoolYearID = False, returnreturnSchoolYearIDForPostSave = False, returnreturnStudentGPABucketGroupID = False, returnreturnStudentGPABucketGroupIsFromTemp = False, returnreturnStudentGPABucketID = False, returnreturnStudentGradeBucketID = False, returnreturnStudentGradeBucketIsFromTemp = False, returnreturnStudentID = False, returnreturnStudentNameLFM = False, returnreturnStudentNumber = False, returnreturnStudentSectionGPABucketGroupID = False, returnreturnStudentSectionGPABucketGroupIsFromTemp = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(TempStudentGPABucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentGPABucket(TempStudentGPABucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(TempStudentGPABucketID), verb = "delete")

	return(response)

def getEveryTempStudentGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGPABucketGroupID = True, returnCreatedTime = False, returnGPABucketID = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentGPABucketGroup(TempStudentGPABucketGroupID, EntityID = 1, returnreturnTempStudentGPABucketGroupID = False, returnreturnCreatedTime = False, returnreturnGPABucketID = False, returnreturnGPAMethodID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(TempStudentGPABucketGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentGPABucketGroup(TempStudentGPABucketGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(TempStudentGPABucketGroupID), verb = "delete")

	return(response)

def getEveryTempStudentGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGradeBucketID = True, returnCompleteByTeacherCode = False, returnCreatedTime = False, returnDoNotPost = False, returnEntityID = False, returnGradeBucketCode = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkIDReverse = False, returnGradingPeriodGradeBucketID = False, returnIsTransferBucket = False, returnIsTransferCourse = False, returnModifiedTime = False, returnNewCode = False, returnOldCode = False, returnOverallPercent = False, returnOverallStatus = False, returnPercentWithAdjustment = False, returnSchoolYearID = False, returnSectionID = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionID = False, returnStudentSectionName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentGradeBucket(TempStudentGradeBucketID, EntityID = 1, returnreturnTempStudentGradeBucketID = False, returnreturnCompleteByTeacherCode = False, returnreturnCreatedTime = False, returnreturnDoNotPost = False, returnreturnEntityID = False, returnreturnGradeBucketCode = False, returnreturnGradeMarkID = False, returnreturnGradeMarkIDOverride = False, returnreturnGradeMarkIDReverse = False, returnreturnGradingPeriodGradeBucketID = False, returnreturnIsTransferBucket = False, returnreturnIsTransferCourse = False, returnreturnModifiedTime = False, returnreturnNewCode = False, returnreturnOldCode = False, returnreturnOverallPercent = False, returnreturnOverallStatus = False, returnreturnPercentWithAdjustment = False, returnreturnSchoolYearID = False, returnreturnSectionID = False, returnreturnStudentGradeBucketID = False, returnreturnStudentName = False, returnreturnStudentSectionID = False, returnreturnStudentSectionName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(TempStudentGradeBucketID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentGradeBucket(TempStudentGradeBucketID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(TempStudentGradeBucketID), verb = "delete")

	return(response)

def getEveryTempStudentGradeBucketFlag(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGradeBucketFlagID = True, returnCourseSectionCode = False, returnCreatedTime = False, returnExceptionReason = False, returnGradeBucketFlagCode = False, returnGradeBucketFlagID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnIsException = False, returnModifiedTime = False, returnSectionLengthCode = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentGradeBucketFlag(TempStudentGradeBucketFlagID, EntityID = 1, returnreturnTempStudentGradeBucketFlagID = False, returnreturnCourseSectionCode = False, returnreturnCreatedTime = False, returnreturnExceptionReason = False, returnreturnGradeBucketFlagCode = False, returnreturnGradeBucketFlagID = False, returnreturnGradeBucketLabel = False, returnreturnGradeMarkCode = False, returnreturnIsException = False, returnreturnModifiedTime = False, returnreturnSectionLengthCode = False, returnreturnStudentGradeBucketID = False, returnreturnStudentName = False, returnreturnStudentSectionDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(TempStudentGradeBucketFlagID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentGradeBucketFlag(TempStudentGradeBucketFlagID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(TempStudentGradeBucketFlagID), verb = "delete")

	return(response)

def getEveryTempStudentHonorRollRunLevel(EntityID = 1, page = 1, pageSize = 100, returnTempStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnGrade = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelName = False, returnHonorRollRunLevelOrder = False, returnModifiedTime = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentHonorRollRunLevel(TempStudentHonorRollRunLevelID, EntityID = 1, returnreturnTempStudentHonorRollRunLevelID = False, returnreturnCreatedTime = False, returnreturnGPAValue = False, returnreturnGrade = False, returnreturnHonorRollRunLevelID = False, returnreturnHonorRollRunLevelName = False, returnreturnHonorRollRunLevelOrder = False, returnreturnModifiedTime = False, returnreturnStudentID = False, returnreturnStudentName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(TempStudentHonorRollRunLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentHonorRollRunLevel(TempStudentHonorRollRunLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(TempStudentHonorRollRunLevelID), verb = "delete")

	return(response)

def getEveryTempStudentRank(EntityID = 1, page = 1, pageSize = 100, returnTempStudentRankID = True, returnCohortNumericYear = False, returnCreatedTime = False, returnGPA = False, returnGraduationRequirementYear = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNoRank = False, returnRank = False, returnRankMethodID = False, returnSchoolYearIDCohort = False, returnStudentGrade = False, returnStudentID = False, returnStudentName = False, returnStudentRankID = False, returnStudentRankSort = False, returnTotalStudents = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentRank(TempStudentRankID, EntityID = 1, returnreturnTempStudentRankID = False, returnreturnCohortNumericYear = False, returnreturnCreatedTime = False, returnreturnGPA = False, returnreturnGraduationRequirementYear = False, returnreturnIsManualRank = False, returnreturnIsProspectiveRank = False, returnreturnModifiedTime = False, returnreturnNoRank = False, returnreturnRank = False, returnreturnRankMethodID = False, returnreturnSchoolYearIDCohort = False, returnreturnStudentGrade = False, returnreturnStudentID = False, returnreturnStudentName = False, returnreturnStudentRankID = False, returnreturnStudentRankSort = False, returnreturnTotalStudents = False, returnreturnUseOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(TempStudentRankID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentRank(TempStudentRankID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(TempStudentRankID), verb = "delete")

	return(response)

def getEveryTempStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionCode = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentSection(TempStudentSectionID, EntityID = 1, returnreturnTempStudentSectionID = False, returnreturnCourse = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnSectionCode = False, returnreturnStudentNameLFM = False, returnreturnStudentNumber = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(TempStudentSectionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentSection(TempStudentSectionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(TempStudentSectionID), verb = "delete")

	return(response)

def getEveryTempStudentSectionFailedUpdate(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionFailedUpdateID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnSection = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentSectionFailedUpdate(TempStudentSectionFailedUpdateID, EntityID = 1, returnreturnTempStudentSectionFailedUpdateID = False, returnreturnCourse = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnSection = False, returnreturnStudentNameLFM = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(TempStudentSectionFailedUpdateID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentSectionFailedUpdate(TempStudentSectionFailedUpdateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(TempStudentSectionFailedUpdateID), verb = "delete")

	return(response)

def getEveryTempStudentSectionGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionGPABucketGroupID = True, returnCreatedTime = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnIsCumulative = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentSectionGPABucketGroup(TempStudentSectionGPABucketGroupID, EntityID = 1, returnreturnTempStudentSectionGPABucketGroupID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnGPABucketID = False, returnreturnGPAMethodID = False, returnreturnIsCumulative = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStudentGPABucketGroupID = False, returnreturnStudentGPABucketGroupIsFromTemp = False, returnreturnStudentID = False, returnreturnStudentSectionID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(TempStudentSectionGPABucketGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentSectionGPABucketGroup(TempStudentSectionGPABucketGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(TempStudentSectionGPABucketGroupID), verb = "delete")

	return(response)

def getEveryTempTransferCourse(EntityID = 1, page = 1, pageSize = 100, returnTempTransferCourseID = True, returnCourseCredits = False, returnCourseDescription = False, returnCourseID = False, returnCourseSection = False, returnCreatedTime = False, returnEarnedCreditOverride = False, returnEndDate = False, returnEntityCode = False, returnEntityID = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLinking = False, returnGradedCourse = False, returnGradeReferenceID = False, returnGradingPeriodSetID = False, returnGradYear = False, returnModifiedTime = False, returnSchoolYear = False, returnSchoolYearID = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentID = False, returnTotalEarnedCredits = False, returnTotalFailedCredits = False, returnUseAddOnGPA = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditPercentOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempTransferCourse(TempTransferCourseID, EntityID = 1, returnreturnTempTransferCourseID = False, returnreturnCourseCredits = False, returnreturnCourseDescription = False, returnreturnCourseID = False, returnreturnCourseSection = False, returnreturnCreatedTime = False, returnreturnEarnedCreditOverride = False, returnreturnEndDate = False, returnreturnEntityCode = False, returnreturnEntityID = False, returnreturnExcludeFromReportCardsAndTranscripts = False, returnreturnExcludeFromStudentSectionLinking = False, returnreturnGradedCourse = False, returnreturnGradeReferenceID = False, returnreturnGradingPeriodSetID = False, returnreturnGradYear = False, returnreturnModifiedTime = False, returnreturnSchoolYear = False, returnreturnSchoolYearID = False, returnreturnSectionID = False, returnreturnSectionLengthID = False, returnreturnSectionLengthSubsetID = False, returnreturnStartDate = False, returnreturnStudentID = False, returnreturnTotalEarnedCredits = False, returnreturnTotalFailedCredits = False, returnreturnUseAddOnGPA = False, returnreturnUseEarnedCreditOverride = False, returnreturnUseEarnedCreditPercentOverride = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(TempTransferCourseID), verb = "get", params_list = params_list)

	return(response)

def deleteTempTransferCourse(TempTransferCourseID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(TempTransferCourseID), verb = "delete")

	return(response)

def getEveryTranscriptNote(EntityID = 1, page = 1, pageSize = 100, returnTranscriptNoteID = True, returnCreatedTime = False, returnDateAdded = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTranscriptNote(TranscriptNoteID, EntityID = 1, returnreturnTranscriptNoteID = False, returnreturnCreatedTime = False, returnreturnDateAdded = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(TranscriptNoteID), verb = "get", params_list = params_list)

	return(response)

def deleteTranscriptNote(TranscriptNoteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(TranscriptNoteID), verb = "delete")

	return(response)

def getEveryTranscriptSent(EntityID = 1, page = 1, pageSize = 100, returnTranscriptSentID = True, returnComment = False, returnCreatedTime = False, returnDateSent = False, returnInstitutionID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTranscriptSent(TranscriptSentID, EntityID = 1, returnreturnTranscriptSentID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnDateSent = False, returnreturnInstitutionID = False, returnreturnModifiedTime = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(TranscriptSentID), verb = "get", params_list = params_list)

	return(response)

def deleteTranscriptSent(TranscriptSentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(TranscriptSentID), verb = "delete")

	return(response)