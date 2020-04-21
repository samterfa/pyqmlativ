# This module contains Grading functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryCommentBucket(searchConditions = [], EntityID = 1, returnCommentBucketID = False, returnCommentBucketIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnGradingPeriodID = False, returnIsLimitedByCourse = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CommentBucket in the district.

	This function returns a dataframe of every CommentBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCommentBucketCourse(searchConditions = [], EntityID = 1, returnCommentBucketCourseID = False, returnCommentBucketID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CommentBucketCourse in the district.

	This function returns a dataframe of every CommentBucketCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCommentCode(searchConditions = [], EntityID = 1, returnCommentCodeID = False, returnCode = False, returnCodeDescription = False, returnCommentCodeIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CommentCode in the district.

	This function returns a dataframe of every CommentCode in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCommentSet(searchConditions = [], EntityID = 1, returnCommentSetID = False, returnCode = False, returnCodeDescription = False, returnCommentSetIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CommentSet in the district.

	This function returns a dataframe of every CommentSet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictGroup(searchConditions = [], EntityID = 1, returnConfigDistrictGroupID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCreditsRoundingDecimals = False, returnFinalGPADecimalSetting = False, returnFinalGPADecimalSettingCode = False, returnFinalGPARoundingDecimals = False, returnGPACalculationDecimalSetting = False, returnGPACalculationDecimalSettingCode = False, returnGPACalculationRoundingDecimals = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigDistrictGroup in the district.

	This function returns a dataframe of every ConfigDistrictGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentSectionLinkOption = False, returnStudentSectionLinkOptionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinkCourseType = False, returnUseStudentSectionLinking = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityGroupYear(searchConditions = [], EntityID = 1, returnConfigEntityGroupYearID = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnCurrentCalculation = False, returnCurrentCalculationCode = False, returnEarnedCreditsMethodIDDefault = False, returnEntityGroupKey = False, returnEntityID = False, returnFreeFormCommentMaxLength = False, returnGradebookLockMessage = False, returnGradeLevelIDCohort = False, returnLockGradebookAssignmentsAfterDate = False, returnLockGradebookCalculation = False, returnLockGradebookStartTime = False, returnLockGradeBuckets = False, returnModifiedTime = False, returnRetainGradesNumberOfDays = False, returnSchoolYearID = False, returnUseAddOnGPA = False, returnUseFactorBasedAddOn = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityYear(searchConditions = [], EntityID = 1, returnConfigEntityYearID = False, returnAcademicSummaryTypeETranscript = False, returnAcademicSummaryTypeETranscriptCode = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnElectronicSignatureIDReportCard = False, returnElectronicSignatureIDTranscript = False, returnEntityID = False, returnGPAMaximumRangeETranscript = False, returnGPAMethodEntityIDETranscript = False, returnModifiedTime = False, returnRankMethodIDETranscript = False, returnRequiredCreditTypeETranscript = False, returnRequiredCreditTypeETranscriptCode = False, returnSchoolYearID = False, returnTranscriptTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigEntityYear in the district.

	This function returns a dataframe of every ConfigEntityYear in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityYearGraduationRequiredCredit(searchConditions = [], EntityID = 1, returnConfigEntityYearGraduationRequiredCreditID = False, returnConfigEntityYearID = False, returnCreatedTime = False, returnCreditsRequired = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ConfigEntityYearGraduationRequiredCredit in the district.

	This function returns a dataframe of every ConfigEntityYearGraduationRequiredCredit in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYearGraduationRequiredCredit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYearGraduationRequiredCredit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseEarnedCreditsMethod(searchConditions = [], EntityID = 1, returnCourseEarnedCreditsMethodID = False, returnCourseEarnedCreditsMethodIDClonedFrom = False, returnCourseID = False, returnCourseOrOverrideEarnedCredits = False, returnCreatedTime = False, returnEarnedCreditsMethodEntityID = False, returnEarnedCreditsOverride = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseEarnedCreditsMethod in the district.

	This function returns a dataframe of every CourseEarnedCreditsMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseEarnedCreditsMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseEarnedCreditsMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGPAMethod(searchConditions = [], EntityID = 1, returnCourseGPAMethodID = False, returnCourseGPAMethodIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPACredit = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGPAMethod in the district.

	This function returns a dataframe of every CourseGPAMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCourseGPAMethodGradeReferenceOverride(searchConditions = [], EntityID = 1, returnCourseGPAMethodGradeReferenceOverrideID = False, returnCourseGPAMethodID = False, returnCreatedTime = False, returnGPACredits = False, returnGradeReferenceID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CourseGPAMethodGradeReferenceOverride in the district.

	This function returns a dataframe of every CourseGPAMethodGradeReferenceOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDefaultGradingScaleGroupGradeMark(searchConditions = [], EntityID = 1, returnDefaultGradingScaleGroupGradeMarkID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnDefaultCalculationPercent = False, returnDefaultGradingScaleGroupGradeMarkIDClonedFrom = False, returnEntityGroupKey = False, returnGradeMarkID = False, returnModifiedTime = False, returnPercentHigh = False, returnPercentLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DefaultGradingScaleGroupGradeMark in the district.

	This function returns a dataframe of every DefaultGradingScaleGroupGradeMark in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/DefaultGradingScaleGroupGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/DefaultGradingScaleGroupGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarnedCreditsBucketGroup(searchConditions = [], EntityID = 1, returnEarnedCreditsBucketGroupID = False, returnCreatedTime = False, returnEarnedCreditsBucketGroupIDClonedFrom = False, returnEntityGroupKey = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarnedCreditsBucketGroup in the district.

	This function returns a dataframe of every EarnedCreditsBucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarnedCreditsBucketGroupGradeBucket(searchConditions = [], EntityID = 1, returnEarnedCreditsBucketGroupGradeBucketID = False, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketIDClonedFrom = False, returnEarnedCreditsBucketGroupID = False, returnEntityGroupKey = False, returnGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarnedCreditsBucketGroupGradeBucket in the district.

	This function returns a dataframe of every EarnedCreditsBucketGroupGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarnedCreditsBucketGroupGradeBucketStudentOverride(searchConditions = [], EntityID = 1, returnEarnedCreditsBucketGroupGradeBucketStudentOverrideID = False, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarnedCreditsBucketGroupGradeBucketStudentOverride in the district.

	This function returns a dataframe of every EarnedCreditsBucketGroupGradeBucketStudentOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarnedCreditsMethod(searchConditions = [], EntityID = 1, returnEarnedCreditsMethodID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarnedCreditsMethod in the district.

	This function returns a dataframe of every EarnedCreditsMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarnedCreditsMethodEntity(searchConditions = [], EntityID = 1, returnEarnedCreditsMethodEntityID = False, returnCreatedTime = False, returnEarnedCreditsMethodEntityIDClonedFrom = False, returnEarnedCreditsMethodID = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarnedCreditsMethodEntity in the district.

	This function returns a dataframe of every EarnedCreditsMethodEntity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsMethodEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsMethodEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicAwardException(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicAwardExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptAcademicAwardV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicAwardException in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicAwardException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicAwardException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicAwardException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicAwardV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicAwardV1ID = False, returnAcademicAwardDate = False, returnAcademicAwardLevel = False, returnAcademicAwardLevelCode = False, returnAcademicAwardTitle = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnOrganizationName = False, returnSchoolYearID = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicAwardV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicAwardV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicAwardV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicAwardV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicHonorException(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicHonorExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptAcademicHonorV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicHonorException in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicHonorException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicHonorException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicHonorException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicHonorV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicHonorV1ID = False, returnAcademicAwardLevel = False, returnAcademicAwardLevelCode = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnHonorsTitle = False, returnKeyHash = False, returnModifiedTime = False, returnOrganizationName = False, returnSchoolYearID = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicHonorV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicHonorV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicHonorV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicHonorV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicRecordException(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicRecordExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptAcademicRecordV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicRecordException in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicRecordException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicRecordException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicRecordException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicRecordV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicRecordV1ID = False, returnCEEBACT = False, returnCohortGraduationYear = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnHasSchoolOverride = False, returnKeyHash = False, returnModifiedTime = False, returnOrganizationName = False, returnSchoolLevel = False, returnSchoolLevelCode = False, returnSchoolOverride = False, returnSchoolOverrideCode = False, returnSchoolYearID = False, returnStudentID = False, returnStudentLevel = False, returnStudentLevelCode = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicRecordV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicRecordV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicRecordV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicRecordV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicSessionException(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicSessionExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptAcademicSessionV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicSessionException in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicSessionException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSessionException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSessionException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicSessionV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicSessionV1ID = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysPresent = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnEntryWithdrawalID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnOrganizationName = False, returnSchoolYearID = False, returnSectionLengthID = False, returnSessionDesignator = False, returnSessionName = False, returnSessionSchoolYear = False, returnSessionType = False, returnSessionTypeCode = False, returnStudentID = False, returnStudentLevel = False, returnStudentLevelCode = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicSessionV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicSessionV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSessionV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSessionV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicSummaryException(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicSummaryExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptAcademicSummaryV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicSummaryException in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicSummaryException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSummaryException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSummaryException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAcademicSummaryV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptAcademicSummaryV1ID = False, returnAcademicSummaryType = False, returnAcademicSummaryTypeCode = False, returnClassRank = False, returnClassSize = False, returnCreatedTime = False, returnCreditHoursEarned = False, returnCreditHoursForGPA = False, returnCreditHoursRequired = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnEntryDate = False, returnEntryWithdrawalID = False, returnExitDate = False, returnGPARangeMaximum = False, returnGradePointAverage = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnOrganizationName = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentID = False, returnStudentPlanID = False, returnStudentRankID = False, returnTotalQualityPoints = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAcademicSummaryV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptAcademicSummaryV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSummaryV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAcademicSummaryV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAddressException(searchConditions = [], EntityID = 1, returnElectronicTranscriptAddressExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptAddressV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAddressException in the district.

	This function returns a dataframe of every ElectronicTranscriptAddressException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAddressException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAddressException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAddressV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptAddressV1ID = False, returnAddressID = False, returnAddressLine1 = False, returnAddressLine2 = False, returnAddressLine3 = False, returnCity = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnPostalCode = False, returnSchoolYearID = False, returnStateProvinceCode = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAddressV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptAddressV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAddressV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAddressV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAgencyIdentifierException(searchConditions = [], EntityID = 1, returnElectronicTranscriptAgencyIdentifierExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptAgencyIdentifierV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAgencyIdentifierException in the district.

	This function returns a dataframe of every ElectronicTranscriptAgencyIdentifierException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAgencyIdentifierException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAgencyIdentifierException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAgencyIdentifierV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptAgencyIdentifierV1ID = False, returnAgency = False, returnAgencyAssignedID = False, returnAgencyCode = False, returnAgencyName = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAgencyIdentifierV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptAgencyIdentifierV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAgencyIdentifierV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAgencyIdentifierV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptAPITransaction(searchConditions = [], EntityID = 1, returnElectronicTranscriptAPITransactionID = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnIsError = False, returnMessage = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptAPITransaction in the district.

	This function returns a dataframe of every ElectronicTranscriptAPITransaction in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAPITransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptAPITransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptCourseException(searchConditions = [], EntityID = 1, returnElectronicTranscriptCourseExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptCourseV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptCourseException in the district.

	This function returns a dataframe of every ElectronicTranscriptCourseException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptCourseException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptCourseException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptCourseV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptCourseV1ID = False, returnAgencyCourseID = False, returnCourseAcademicGrade = False, returnCourseBeginDate = False, returnCourseCreditBasis = False, returnCourseCreditBasisCode = False, returnCourseCreditEarned = False, returnCourseEndDate = False, returnCourseGPAApplicability = False, returnCourseGPAApplicabilityCode = False, returnCourseLevel = False, returnCourseLevelCode = False, returnCourseNumber = False, returnCourseQualityPointsEarned = False, returnCourseTitle = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnIsInProgress = False, returnKeyHash = False, returnModifiedTime = False, returnNoteMessage = False, returnOrganizationName = False, returnSchoolYearID = False, returnSectionLengthID = False, returnSessionDesignator = False, returnStudentGradeBucketID = False, returnStudentID = False, returnStudentSectionID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptCourseV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptCourseV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptCourseV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptCourseV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptImmunizationException(searchConditions = [], EntityID = 1, returnElectronicTranscriptImmunizationExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptImmunizationV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnStudentVaccineID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptImmunizationException in the district.

	This function returns a dataframe of every ElectronicTranscriptImmunizationException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptImmunizationException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptImmunizationException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptImmunizationV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptImmunizationV1ID = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnImmunizationCode = False, returnImmunizationDate = False, returnImmunizationStatus = False, returnImmunizationStatusCode = False, returnKeyHash = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentChildhoodIllnessID = False, returnStudentID = False, returnStudentVaccinationWaiverID = False, returnStudentVaccineID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptImmunizationV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptImmunizationV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptImmunizationV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptImmunizationV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptLicensureException(searchConditions = [], EntityID = 1, returnElectronicTranscriptLicensureExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptLicensureV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptLicensureException in the district.

	This function returns a dataframe of every ElectronicTranscriptLicensureException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptLicensureNoteException(searchConditions = [], EntityID = 1, returnElectronicTranscriptLicensureNoteExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptLicensureNoteV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptLicensureNoteException in the district.

	This function returns a dataframe of every ElectronicTranscriptLicensureNoteException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureNoteException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureNoteException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptLicensureNoteV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptLicensureNoteV1ID = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnLicensureName = False, returnLicensurePassageDate = False, returnModifiedTime = False, returnNoteMessage = False, returnOrganizationName = False, returnSchoolYearID = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptLicensureNoteV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptLicensureNoteV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureNoteV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureNoteV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptLicensureV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptLicensureV1ID = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnLicensureName = False, returnLicensurePassageDate = False, returnModifiedTime = False, returnOrganizationName = False, returnSchoolYearID = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptLicensureV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptLicensureV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptLicensureV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptPersonException(searchConditions = [], EntityID = 1, returnElectronicTranscriptPersonExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptPersonV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptPersonException in the district.

	This function returns a dataframe of every ElectronicTranscriptPersonException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPersonException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPersonException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptPersonV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptPersonV1ID = False, returnBirthDate = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnGuardianFirstName = False, returnGuardianLastName = False, returnHasErrors = False, returnKeyHash = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameIDGuardian = False, returnNameSuffix = False, returnNameSuffixCode = False, returnSchoolAssignedPersonID = False, returnSchoolYearID = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptPersonV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptPersonV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPersonV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPersonV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptPhoneException(searchConditions = [], EntityID = 1, returnElectronicTranscriptPhoneExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptPhoneV1ID = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptPhoneException in the district.

	This function returns a dataframe of every ElectronicTranscriptPhoneException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPhoneException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPhoneException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptPhoneV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptPhoneV1ID = False, returnAreaCityCode = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnNamePhoneID = False, returnPhoneNumber = False, returnSchoolYearID = False, returnStudentID = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptPhoneV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptPhoneV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPhoneV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptPhoneV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptRunHistory(searchConditions = [], EntityID = 1, returnElectronicTranscriptRunHistoryID = False, returnAPIErrorCount = False, returnAPISuccessCount = False, returnCanAccessMedia = False, returnCreatedTime = False, returnDistrictID = False, returnEndDateTime = False, returnEntityIDExportedFor = False, returnHasAnEntityExport = False, returnHasValidMedia = False, returnIsExport = False, returnIsLocked = False, returnMediaID = False, returnModifiedTime = False, returnRunData = False, returnRunParameters = False, returnSchoolYearID = False, returnScopeAccessAllowed = False, returnStartDateTime = False, returnStatus = False, returnStatusCode = False, returnStudentFilterDisplay = False, returnType = False, returnTypeCode = False, returnUserIDCanceledBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptRunHistory in the district.

	This function returns a dataframe of every ElectronicTranscriptRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptSubtestException(searchConditions = [], EntityID = 1, returnElectronicTranscriptSubtestExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnElectronicTranscriptSubtestV1ID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnStudentTestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptSubtestException in the district.

	This function returns a dataframe of every ElectronicTranscriptSubtestException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptSubtestException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptSubtestException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptSubtestV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptSubtestV1ID = False, returnCreatedTime = False, returnEducationSubtest = False, returnEducationSubtestCode = False, returnEducationTest = False, returnEducationTestCode = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnNoteMessage = False, returnSchoolYearID = False, returnStudentID = False, returnStudentTestID = False, returnSubtestName = False, returnTestDate = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptSubtestV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptSubtestV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptSubtestV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptSubtestV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptTestException(searchConditions = [], EntityID = 1, returnElectronicTranscriptTestExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnElectronicTranscriptTestV1ID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnStudentTestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptTestException in the district.

	This function returns a dataframe of every ElectronicTranscriptTestException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptTestScoreException(searchConditions = [], EntityID = 1, returnElectronicTranscriptTestScoreExceptionID = False, returnCreatedTime = False, returnElectronicTranscriptRunHistoryID = False, returnElectronicTranscriptTestScoreV1ID = False, returnEntityID = False, returnMessage = False, returnMessageType = False, returnMessageTypeCode = False, returnModifiedTime = False, returnProcessType = False, returnProcessTypeCode = False, returnRuleNumber = False, returnSchoolYearID = False, returnStudentID = False, returnStudentTestID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptTestScoreException in the district.

	This function returns a dataframe of every ElectronicTranscriptTestScoreException in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestScoreException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestScoreException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptTestScoreV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptTestScoreV1ID = False, returnCreatedTime = False, returnEducationSubtest = False, returnEducationSubtestCode = False, returnEducationTest = False, returnEducationTestCode = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnNoteMessage = False, returnSchoolYearID = False, returnScoreValue = False, returnStudentID = False, returnStudentTestID = False, returnSubtestName = False, returnTestDate = False, returnTestScoreMethod = False, returnTestScoreMethodCode = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptTestScoreV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptTestScoreV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestScoreV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestScoreV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElectronicTranscriptTestV1(searchConditions = [], EntityID = 1, returnElectronicTranscriptTestV1ID = False, returnCreatedTime = False, returnEducationTest = False, returnEducationTestCode = False, returnElectronicTranscriptRunHistoryID = False, returnEntityID = False, returnHasErrors = False, returnKeyHash = False, returnModifiedTime = False, returnNoteMessage = False, returnSchoolYearID = False, returnStudentID = False, returnStudentTestID = False, returnTestDate = False, returnTestName = False, returnUpdateHash = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElectronicTranscriptTestV1 in the district.

	This function returns a dataframe of every ElectronicTranscriptTestV1 in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestV1/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ElectronicTranscriptTestV1/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFactorBasedAddOn(searchConditions = [], EntityID = 1, returnFactorBasedAddOnID = False, returnCreatedTime = False, returnFactor = False, returnFactorBasedAddOnIDClonedFrom = False, returnGPABucketEntityID = False, returnGradeReferenceID = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FactorBasedAddOn in the district.

	This function returns a dataframe of every FactorBasedAddOn in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucket(searchConditions = [], EntityID = 1, returnGPABucketID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnGPABucketTypeID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucket in the district.

	This function returns a dataframe of every GPABucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucketEntity(searchConditions = [], EntityID = 1, returnGPABucketEntityID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPABucketEntityIDClonedFrom = False, returnGPABucketID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucketEntity in the district.

	This function returns a dataframe of every GPABucketEntity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucketGroup(searchConditions = [], EntityID = 1, returnGPABucketGroupID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupIDClonedFrom = False, returnGPABucketGroupSummaryID = False, returnGPABucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucketGroup in the district.

	This function returns a dataframe of every GPABucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucketGroupGradeBucket(searchConditions = [], EntityID = 1, returnGPABucketGroupGradeBucketID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupGradeBucketIDClonedFrom = False, returnGPABucketGroupID = False, returnGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnIsUpToDate = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucketGroupGradeBucket in the district.

	This function returns a dataframe of every GPABucketGroupGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucketGroupGradeBucketStudentOverride(searchConditions = [], EntityID = 1, returnGPABucketGroupGradeBucketStudentOverrideID = False, returnCreatedTime = False, returnGPABucketGroupGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucketGroupGradeBucketStudentOverride in the district.

	This function returns a dataframe of every GPABucketGroupGradeBucketStudentOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucketGroupSummary(searchConditions = [], EntityID = 1, returnGPABucketGroupSummaryID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupSummaryIDClonedFrom = False, returnGPABucketSetID = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucketGroupSummary in the district.

	This function returns a dataframe of every GPABucketGroupSummary in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucketSet(searchConditions = [], EntityID = 1, returnGPABucketSetID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucketSet in the district.

	This function returns a dataframe of every GPABucketSet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPABucketType(searchConditions = [], EntityID = 1, returnGPABucketTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPABucketType in the district.

	This function returns a dataframe of every GPABucketType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPAMethod(searchConditions = [], EntityID = 1, returnGPAMethodID = False, returnAllowFurtherAttemptsOfNonHighSchoolCourses = False, returnCancelSubAreaCreditFromMiddleSchoolCredit = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnExcludeTermTwoFinalYearGrade = False, returnGPABucketSetID = False, returnGradReqRankGPARequiredCourseRule = False, returnGradReqRankGPARequiredCourseRuleCode = False, returnLockGradeMarkPoints = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnSortNumber = False, returnTotalElectiveCreditsPossible = False, returnUseGradReqRankGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTotalElectiveCredits = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPAMethod in the district.

	This function returns a dataframe of every GPAMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPAMethodCourseGroup(searchConditions = [], EntityID = 1, returnGPAMethodCourseGroupID = False, returnCourseGroupID = False, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPAMethodCourseGroup in the district.

	This function returns a dataframe of every GPAMethodCourseGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPAMethodEntity(searchConditions = [], EntityID = 1, returnGPAMethodEntityID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPAMethodEntityIDClonedFrom = False, returnGPAMethodID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatus = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPAMethodEntity in the district.

	This function returns a dataframe of every GPAMethodEntity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGPAMethodGradeBucketFlagGPAPointsOverride(searchConditions = [], EntityID = 1, returnGPAMethodGradeBucketFlagGPAPointsOverrideID = False, returnCreatedTime = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GPAMethodGradeBucketFlagGPAPointsOverride in the district.

	This function returns a dataframe of every GPAMethodGradeBucketFlagGPAPointsOverride in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradebookLockGradeBucket(searchConditions = [], EntityID = 1, returnGradebookLockGradeBucketID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradebookLockGradeBucket in the district.

	This function returns a dataframe of every GradebookLockGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradebookLockGradeReference(searchConditions = [], EntityID = 1, returnGradebookLockGradeReferenceID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradebookLockGradeReference in the district.

	This function returns a dataframe of every GradebookLockGradeReference in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeBucket(searchConditions = [], EntityID = 1, returnGradeBucketID = False, returnCreatedTime = False, returnDescription = False, returnDynamicRelationshipID = False, returnEdFiGradingPeriodDescriptorID = False, returnEdFiGradingPeriodID = False, returnEntityGroupKey = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGradeBucketIDClonedFrom = False, returnGradeBucketTypeID = False, returnLabel = False, returnLabelDescription = False, returnModifiedTime = False, returnNumber = False, returnOrder = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeBucket in the district.

	This function returns a dataframe of every GradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeBucketFlag(searchConditions = [], EntityID = 1, returnGradeBucketFlagID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeBucketFlag in the district.

	This function returns a dataframe of every GradeBucketFlag in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeBucketFlagDetail(searchConditions = [], EntityID = 1, returnGradeBucketFlagDetailID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketFlagDetailIDClonedFrom = False, returnGradeBucketFlagID = False, returnIsActive = False, returnModifiedTime = False, returnPrintWithGradeMark = False, returnSchoolYearID = False, returnUseEarnedOverride = False, returnUseGPAOverride = False, returnUseGPAPointsOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeBucketFlagDetail in the district.

	This function returns a dataframe of every GradeBucketFlagDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeBucketFlagDetailGPAMethod(searchConditions = [], EntityID = 1, returnGradeBucketFlagDetailGPAMethodID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagDetailID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeBucketFlagDetailGPAMethod in the district.

	This function returns a dataframe of every GradeBucketFlagDetailGPAMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeBucketType(searchConditions = [], EntityID = 1, returnGradeBucketTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEdFiGradeTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketTypeIDClonedFrom = False, returnHasSpecificCategories = False, returnMinimumPercent = False, returnModifiedTime = False, returnSchoolYearID = False, returnSnapshotGradeExtensionDays = False, returnSpecificCategoryGradeBucketTypeCount = False, returnUseAllCategories = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSnapshotGrade = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeBucketType in the district.

	This function returns a dataframe of every GradeBucketType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeMark(searchConditions = [], EntityID = 1, returnGradeMarkID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkExistsInSpecifcEntity = False, returnGradeMarkIDClonedFrom = False, returnGradeMarkIDReverse = False, returnGradeMarkMNID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnReportCardDisplayValue = False, returnSchoolYearID = False, returnStateGradeMarkMNID = False, returnTranscriptDisplayValue = False, returnUseAsTeacherOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeMark in the district.

	This function returns a dataframe of every GradeMark in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeMarkPointSet(searchConditions = [], EntityID = 1, returnGradeMarkPointSetID = False, returnAddOnPoints = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGradeMarkID = False, returnGradeMarkPointSetIDClonedFrom = False, returnModifiedTime = False, returnPointSetEntityID = False, returnRegularPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeMarkPointSet in the district.

	This function returns a dataframe of every GradeMarkPointSet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportAcademicSession(searchConditions = [], EntityID = 1, returnGradeReportAcademicSessionID = False, returnCreatedTime = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysUnexcusedYTD = False, returnEarnedCredit = False, returnEarnedCreditAttempted = False, returnEarnedCreditsValue = False, returnEntryDate = False, returnGPAValue = False, returnGradeLevelCode = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportStudentID = False, returnHeaderDescription = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportAcademicSession in the district.

	This function returns a dataframe of every GradeReportAcademicSession in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportAcademicSessionTemplate(searchConditions = [], EntityID = 1, returnGradeReportAcademicSessionTemplateID = False, returnBreakBySchoolYear = False, returnCourseFilter = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnHeaderDescription = False, returnIncludeNonCreditEarningCourses = False, returnModifiedTime = False, returnSearchConditionFilter = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchoolYearDescending = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportAcademicSessionTemplate in the district.

	This function returns a dataframe of every GradeReportAcademicSessionTemplate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportAcademicSessionTemplateCourse(searchConditions = [], EntityID = 1, returnGradeReportAcademicSessionTemplateCourseID = False, returnCourseID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateCourseIDClonedFrom = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportAcademicSessionTemplateCourse in the district.

	This function returns a dataframe of every GradeReportAcademicSessionTemplateCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportAcademicSessionTemplateCourseGroup(searchConditions = [], EntityID = 1, returnGradeReportAcademicSessionTemplateCourseGroupID = False, returnCourseGroupID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportAcademicSessionTemplateCourseGroup in the district.

	This function returns a dataframe of every GradeReportAcademicSessionTemplateCourseGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportAcademicSessionTemplateGradeLevel(searchConditions = [], EntityID = 1, returnGradeReportAcademicSessionTemplateGradeLevelID = False, returnCreatedTime = False, returnGradeLevelID = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportAcademicSessionTemplateGradeLevel in the district.

	This function returns a dataframe of every GradeReportAcademicSessionTemplateGradeLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportAcademicSessionTemplateGroup(searchConditions = [], EntityID = 1, returnGradeReportAcademicSessionTemplateGroupID = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEarnedCreditsMethodIDDefaultOverride = False, returnGPABucketID = False, returnGPAField = False, returnGPAFieldCode = False, returnGPALabel1 = False, returnGPAMethodID = False, returnIncludeEarnedCredits = False, returnIncludeGPA = False, returnIncludeSchoolYearDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportAcademicSessionTemplateGroup in the district.

	This function returns a dataframe of every GradeReportAcademicSessionTemplateGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportColumnAttendanceCategory(searchConditions = [], EntityID = 1, returnGradeReportColumnAttendanceCategoryID = False, returnCategory = False, returnCategoryCode = False, returnCreatedTime = False, returnGradeReportColumnAttendanceCategoryIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportColumnAttendanceCategory in the district.

	This function returns a dataframe of every GradeReportColumnAttendanceCategory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportColumnAttendanceTerm(searchConditions = [], EntityID = 1, returnGradeReportColumnAttendanceTermID = False, returnAttendanceTermID = False, returnCreatedTime = False, returnGradeReportColumnAttendanceTermIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportColumnAttendanceTerm in the district.

	This function returns a dataframe of every GradeReportColumnAttendanceTerm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportColumnGradeBucket(searchConditions = [], EntityID = 1, returnGradeReportColumnGradeBucketID = False, returnCreatedTime = False, returnGradeReportColumnGradeBucketIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportColumnGradeBucket in the district.

	This function returns a dataframe of every GradeReportColumnGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportColumnGroup(searchConditions = [], EntityID = 1, returnGradeReportColumnGroupID = False, returnAlwaysDisplayGradingColumns = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDescription = False, returnGradeReportColumnGroupIDClonedFrom = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportColumnGroup in the district.

	This function returns a dataframe of every GradeReportColumnGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportColumnGroupColumn(searchConditions = [], EntityID = 1, returnGradeReportColumnGroupColumnID = False, returnAttendanceOption = False, returnAttendanceOptionCode = False, returnColumnHeader = False, returnColumnType = False, returnColumnTypeCode = False, returnContinueIfBlank = False, returnCreatedTime = False, returnDynamicRelationshipID = False, returnGradeReportColumnGroupColumnIDClonedFrom = False, returnGradeReportColumnGroupID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportColumnGroupColumn in the district.

	This function returns a dataframe of every GradeReportColumnGroupColumn in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportEndorsementRow(searchConditions = [], EntityID = 1, returnGradeReportEndorsementRowID = False, returnCreatedTime = False, returnDescription = False, returnGradeReportStudentID = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSort1 = False, returnSort2 = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportEndorsementRow in the district.

	This function returns a dataframe of every GradeReportEndorsementRow in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportGPARow(searchConditions = [], EntityID = 1, returnGradeReportGPARowID = False, returnCreatedTime = False, returnDataColumn1 = False, returnDataColumn2 = False, returnDataColumn3 = False, returnDataColumn4 = False, returnDataColumn5 = False, returnDataColumn6 = False, returnDataColumn7 = False, returnGPABucketDescription = False, returnGPABucketID = False, returnGPAMethodDescription = False, returnGPAMethodID = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportGPARow in the district.

	This function returns a dataframe of every GradeReportGPARow in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportGradingScale(searchConditions = [], EntityID = 1, returnGradeReportGradingScaleID = False, returnCreatedTime = False, returnDisplayType = False, returnDisplayTypeCode = False, returnFreeformText = False, returnGradeMarkCode = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnRangeHigh = False, returnRangeLow = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportGradingScale in the district.

	This function returns a dataframe of every GradeReportGradingScale in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportRow(searchConditions = [], EntityID = 1, returnGradeReportRowID = False, returnAttemptedCredit = False, returnBackgroundColor = False, returnClassPeriod = False, returnCourseSubjectDescription = False, returnCourseTypeCode = False, returnCourseTypeDescription = False, returnCreatedTime = False, returnDepartment = False, returnDescription = False, returnEarnedCredit = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnGradeReportRowIDParent = False, returnModifiedTime = False, returnRowType = False, returnRowTypeCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnSortNumber = False, returnStaffName = False, returnStudentSectionID = False, returnTextColor = False, returnTotalPossibleCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportRow in the district.

	This function returns a dataframe of every GradeReportRow in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportRowColumn(searchConditions = [], EntityID = 1, returnGradeReportRowColumnID = False, returnCreatedTime = False, returnDisplayValue = False, returnGradeMarkID = False, returnGradeReportColumnGroupColumnID = False, returnGradeReportRowID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportRowColumn in the district.

	This function returns a dataframe of every GradeReportRowColumn in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportRowDetail(searchConditions = [], EntityID = 1, returnGradeReportRowDetailID = False, returnCreatedTime = False, returnDetailData = False, returnGradeReportRowID = False, returnGradingPeriodLabel = False, returnGradingPeriodSortNumber = False, returnLabel = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportRowDetail in the district.

	This function returns a dataframe of every GradeReportRowDetail in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportRunHistory(searchConditions = [], EntityID = 1, returnGradeReportRunHistoryID = False, returnAddressLine1 = False, returnAddressLine2 = False, returnCEEBACT = False, returnCity = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFaxNumber = False, returnFooterMessage = False, returnFormattedFullAddress = False, returnGradeReportTemplateID = False, returnIsTexasTranscript = False, returnModifiedTime = False, returnName = False, returnOverwriteExistingReportCard = False, returnParameterDescription = False, returnPhoneNumber = False, returnPostalCode = False, returnPostReportCardToFASA = False, returnPrintCompletedGradingPeriodComments = False, returnReportCardFileName = False, returnRequireFamilyAccessElectronicSignature = False, returnStateProvince = False, returnStatusType = False, returnStatusTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportRunHistory in the district.

	This function returns a dataframe of every GradeReportRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportRunHistoryAttachment(searchConditions = [], EntityID = 1, returnGradeReportRunHistoryAttachmentID = False, returnAttachmentCanBeViewedByStudentFamilyFamilyAccess = False, returnAttachmentID = False, returnCreatedTime = False, returnGradeReportRunHistoryID = False, returnGuardianSignedTime = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnSignedByGuardian = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportRunHistoryAttachment in the district.

	This function returns a dataframe of every GradeReportRunHistoryAttachment in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportStudent(searchConditions = [], EntityID = 1, returnGradeReportStudentID = False, returnAddressLine1 = False, returnAddressLine2 = False, returnAdvisorName = False, returnBirthDate = False, returnCity = False, returnCreatedTime = False, returnDoubleColumnHeaderField1 = False, returnDoubleColumnHeaderField10 = False, returnDoubleColumnHeaderField2 = False, returnDoubleColumnHeaderField3 = False, returnDoubleColumnHeaderField4 = False, returnDoubleColumnHeaderField5 = False, returnDoubleColumnHeaderField6 = False, returnDoubleColumnHeaderField7 = False, returnDoubleColumnHeaderField8 = False, returnDoubleColumnHeaderField9 = False, returnEmailAddress = False, returnEthnicityAndRace = False, returnFirstName = False, returnFormattedFullAddress = False, returnFormattedName = False, returnGender = False, returnGenderCode = False, returnGradeReportRunHistoryID = False, returnGraduationDate = False, returnHomeroom = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameIDPrimaryGuardian = False, returnNameSuffix = False, returnNameTitle = False, returnPostalCode = False, returnPrimaryGuardianEmailAddress = False, returnPrimaryGuardianFirstName = False, returnPrimaryGuardianFormattedName = False, returnPrimaryGuardianLastName = False, returnPrimaryGuardianMiddleName = False, returnPrimaryGuardianNameSuffix = False, returnPrimaryGuardianNameTitle = False, returnPrimaryGuardianPhoneNumber = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnSingleColumnHeaderField1 = False, returnSingleColumnHeaderField2 = False, returnSingleColumnHeaderField3 = False, returnSingleColumnHeaderField4 = False, returnSingleColumnHeaderField5 = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnStateProvince = False, returnStudentFamilyID = False, returnStudentFamilyRank = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportStudent in the district.

	This function returns a dataframe of every GradeReportStudent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportStudentAttendanceTerm(searchConditions = [], EntityID = 1, returnGradeReportStudentAttendanceTermID = False, returnAttendanceTermCode = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysTardy = False, returnDaysUnexcused = False, returnGradeReportAcademicSessionID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportStudentAttendanceTerm in the district.

	This function returns a dataframe of every GradeReportStudentAttendanceTerm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportStudentCTE(searchConditions = [], EntityID = 1, returnGradeReportStudentCTEID = False, returnCreatedTime = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnProgramName = False, returnProgramStatus = False, returnProgramType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportStudentCTE in the district.

	This function returns a dataframe of every GradeReportStudentCTE in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentCTE/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentCTE/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportStudentHighlightIN(searchConditions = [], EntityID = 1, returnGradeReportStudentHighlightINID = False, returnCreatedTime = False, returnGradeReportStudentID = False, returnHighlightType = False, returnHighlightTypeCode = False, returnModifiedTime = False, returnSchoolYear = False, returnTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportStudentHighlightIN in the district.

	This function returns a dataframe of every GradeReportStudentHighlightIN in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentHighlightIN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentHighlightIN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportStudentTestRow(searchConditions = [], EntityID = 1, returnGradeReportStudentTestRowID = False, returnCreatedTime = False, returnDateTaken = False, returnGradeReportStudentTestTypeID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumn1 = False, returnTestColumn10 = False, returnTestColumn2 = False, returnTestColumn3 = False, returnTestColumn4 = False, returnTestColumn5 = False, returnTestColumn6 = False, returnTestColumn7 = False, returnTestColumn8 = False, returnTestColumn9 = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportStudentTestRow in the district.

	This function returns a dataframe of every GradeReportStudentTestRow in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportStudentTestType(searchConditions = [], EntityID = 1, returnGradeReportStudentTestTypeID = False, returnCreatedTime = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnSortNumber = False, returnTestCode = False, returnTestColumnHeader1 = False, returnTestColumnHeader10 = False, returnTestColumnHeader2 = False, returnTestColumnHeader3 = False, returnTestColumnHeader4 = False, returnTestColumnHeader5 = False, returnTestColumnHeader6 = False, returnTestColumnHeader7 = False, returnTestColumnHeader8 = False, returnTestColumnHeader9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportStudentTestType in the district.

	This function returns a dataframe of every GradeReportStudentTestType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportStudentVaccination(searchConditions = [], EntityID = 1, returnGradeReportStudentVaccinationID = False, returnComplianceScheduleCode = False, returnCreatedTime = False, returnDoseDates = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationCodeDescription = False, returnWaiverCodeDescription = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportStudentVaccination in the district.

	This function returns a dataframe of every GradeReportStudentVaccination in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentVaccination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentVaccination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplate(searchConditions = [], EntityID = 1, returnGradeReportTemplateID = False, returnAcademicSessionType = False, returnAcademicSessionTypeCode = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBlankSignatureLabel = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCommentPrintType = False, returnCommentPrintTypeCode = False, returnConfigEntityYearID = False, returnCourseDescriptionFormat = False, returnCourseDescriptionFormatCode = False, returnCourseFilter = False, returnCourseFilterCode = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodCodeSort1 = False, returnDisplayPeriodCodeSort2 = False, returnDisplayPeriodCodeSort3 = False, returnDisplayPeriodCodeSort4 = False, returnEarnedCreditsMethodIDDefaultOverride = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFreeFormGradingLegend = False, returnGPAField1 = False, returnGPAField1Code = False, returnGPAField2 = False, returnGPAField2Code = False, returnGPAField3 = False, returnGPAField3Code = False, returnGPAField4 = False, returnGPAField4Code = False, returnGPAField5 = False, returnGPAField5Code = False, returnGPAField6 = False, returnGPAField6Code = False, returnGPAField7 = False, returnGPAField7Code = False, returnGPALabel1 = False, returnGPALabel2 = False, returnGPALabel3 = False, returnGPALabel4 = False, returnGPALabel5 = False, returnGPALabel6 = False, returnGPALabel7 = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportColumnGroupIDSecondary = False, returnGradeReportTemplateIDClonedFrom = False, returnGradingSort = False, returnGradingSortCode = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHideSignatureSection = False, returnIncludeCurrentYearClasses = False, returnIncludeInProgressGrades = False, returnIncludePhoneInEntityAddress = False, returnIncludePhoneInGuardianAddress = False, returnIncludeTranscriptNotes = False, returnIncludeTransferCourses = False, returnMediaIDLogo = False, returnModifiedTime = False, returnNoReceivingFamily = False, returnOfficialSignatureLabel = False, returnPrintAllCourseRowHeaders = False, returnPrintAttendanceTotals = False, returnPrintBlankSignatureLine = False, returnPrintComments = False, returnPrintCTEPrograms = False, returnPrintElectronicSignature = False, returnPrintEndorsements = False, returnPrintFreeFormComments = False, returnPrintGPA = False, returnPrintGradeScaleAtTop = False, returnPrintHighFrequencyWords = False, returnPrintIndividualAttendanceTerms = False, returnPrintLettersAndSounds = False, returnPrintStudentHighlights = False, returnPrintVaccinations = False, returnPrintYearAttendanceTotals = False, returnPrintYearToDateTotals = False, returnReceivesForms = False, returnReportRunInfoID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnStudentSort1 = False, returnStudentSort1Code = False, returnStudentSort2 = False, returnStudentSort2Code = False, returnStudentSort3 = False, returnStudentSort3Code = False, returnStudentSort4 = False, returnStudentSort4Code = False, returnTeacherNameFormat = False, returnTeacherNameFormatCode = False, returnTemplateType = False, returnTemplateTypeCode = False, returnUseFreeFormGradingLegend = False, returnUseFullGPASection = False, returnUseFullGradesSection = False, returnUseGradeMarkDescriptionGradingLegend = False, returnUseGradeMarkRangeGradingLegend = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsesGPAOrEarnedCredits = False, returnUseStudentSectionLinking = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplate in the district.

	This function returns a dataframe of every GradeReportTemplate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateCommentSet(searchConditions = [], EntityID = 1, returnGradeReportTemplateCommentSetID = False, returnCommentSetID = False, returnCreatedTime = False, returnGradeReportTemplateCommentSetIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateCommentSet in the district.

	This function returns a dataframe of every GradeReportTemplateCommentSet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateEndorsement(searchConditions = [], EntityID = 1, returnGradeReportTemplateEndorsementID = False, returnCreatedTime = False, returnEndorsementID = False, returnGradeReportTemplateID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateEndorsement in the district.

	This function returns a dataframe of every GradeReportTemplateEndorsement in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateGPABucket(searchConditions = [], EntityID = 1, returnGradeReportTemplateGPABucketID = False, returnCreatedTime = False, returnGPABucketID = False, returnGradeReportTemplateGPABucketIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateGPABucket in the district.

	This function returns a dataframe of every GradeReportTemplateGPABucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateGPAMethod(searchConditions = [], EntityID = 1, returnGradeReportTemplateGPAMethodID = False, returnCreatedTime = False, returnGPAMethodID = False, returnGradeReportTemplateGPAMethodIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateGPAMethod in the district.

	This function returns a dataframe of every GradeReportTemplateGPAMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateGradeMark(searchConditions = [], EntityID = 1, returnGradeReportTemplateGradeMarkID = False, returnCreatedTime = False, returnGradeMarkID = False, returnGradeReportTemplateGradeMarkIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateGradeMark in the district.

	This function returns a dataframe of every GradeReportTemplateGradeMark in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateHeaderColumn(searchConditions = [], EntityID = 1, returnGradeReportTemplateHeaderColumnID = False, returnCreatedTime = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnGPABucketID = False, returnGPAMethodID = False, returnGradeReportTemplateHeaderColumnIDClonedFrom = False, returnGradeReportTemplateHeaderRowID = False, returnLabelOverride = False, returnModifiedTime = False, returnRankMethodID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateHeaderColumn in the district.

	This function returns a dataframe of every GradeReportTemplateHeaderColumn in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateHeaderRow(searchConditions = [], EntityID = 1, returnGradeReportTemplateHeaderRowID = False, returnColumnCount = False, returnCreatedTime = False, returnGradeReportTemplateHeaderRowIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateHeaderRow in the district.

	This function returns a dataframe of every GradeReportTemplateHeaderRow in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateHierarchyDepthSetting(searchConditions = [], EntityID = 1, returnGradeReportTemplateHierarchyDepthSettingID = False, returnBackgroundColor = False, returnCreatedTime = False, returnDepthLevel = False, returnGradeReportTemplateHierarchyDepthSettingIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnPrintBackgroundColor = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateHierarchyDepthSetting in the district.

	This function returns a dataframe of every GradeReportTemplateHierarchyDepthSetting in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHierarchyDepthSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHierarchyDepthSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateTestType(searchConditions = [], EntityID = 1, returnGradeReportTemplateTestTypeID = False, returnCreatedTime = False, returnFieldGUIDTestColumn1 = False, returnFieldGUIDTestColumn10 = False, returnFieldGUIDTestColumn2 = False, returnFieldGUIDTestColumn3 = False, returnFieldGUIDTestColumn4 = False, returnFieldGUIDTestColumn5 = False, returnFieldGUIDTestColumn6 = False, returnFieldGUIDTestColumn7 = False, returnFieldGUIDTestColumn8 = False, returnFieldGUIDTestColumn9 = False, returnGradeReportTemplateID = False, returnGradeReportTemplateTestTypeIDClonedFrom = False, returnModifiedTime = False, returnPrintHighestScoreOnly = False, returnSortNumber = False, returnTestCode = False, returnTestColumnHeaderOverride1 = False, returnTestColumnHeaderOverride10 = False, returnTestColumnHeaderOverride2 = False, returnTestColumnHeaderOverride3 = False, returnTestColumnHeaderOverride4 = False, returnTestColumnHeaderOverride5 = False, returnTestColumnHeaderOverride6 = False, returnTestColumnHeaderOverride7 = False, returnTestColumnHeaderOverride8 = False, returnTestColumnHeaderOverride9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateTestType in the district.

	This function returns a dataframe of every GradeReportTemplateTestType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradeReportTemplateVaccination(searchConditions = [], EntityID = 1, returnGradeReportTemplateVaccinationID = False, returnCreatedTime = False, returnGradeReportTemplateID = False, returnGradeReportTemplateVaccinationIDClonedFrom = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradeReportTemplateVaccination in the district.

	This function returns a dataframe of every GradeReportTemplateVaccination in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateVaccination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateVaccination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradingPeriod(searchConditions = [], EntityID = 1, returnGradingPeriodID = False, returnAfterSectionLengthEndLastGradingPeriod = False, returnBeforeSectionLengthStartFirstGradingPeriod = False, returnCalculatedEndDateWithExtension = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeIDForNotReviewedRequests = False, returnCompletedFieldText = False, returnCompletedText = False, returnCreatedTime = False, returnCurrentActiveStatus = False, returnDateOverrideTeacherGracePeriod = False, returnDateOverrideTeacherGracePeriodDisplay = False, returnDescription = False, returnDisplayAssignments = False, returnDisplayGradeBuckets = False, returnEndDate = False, returnEndDateCopy = False, returnEndDateWithRetainGradesNumberOfDays = False, returnEntityGroupKey = False, returnExtendedEndDateGreaterThanToday = False, returnExtensionDays = False, returnExtensionEndTime = False, returnGradeBucketLabels = False, returnGradingPeriodIDClonedFrom = False, returnGradingPeriodIDClonedTo = False, returnGradingPeriodSetID = False, returnIncludeMissingAssignments = False, returnIncludeMissingAssignmentsOrIsCurrentGradingPeriod = False, returnIsActiveOrExtended = False, returnIsCompleted = False, returnModifiedTime = False, returnNumber = False, returnNumberDescription = False, returnOptionsHeaderText = False, returnProgressReportGradingPeriodNumberDateDisplay = False, returnSectionIDForActiveStatus = False, returnSectionLengthID = False, returnStartDate = False, returnStartDateCopy = False, returnStatusDisplay = False, returnStatusDisplayWithExtensionDate = False, returnUniqueCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinGradingPeriod = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradingPeriod in the district.

	This function returns a dataframe of every GradingPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradingPeriodGradeBucket(searchConditions = [], EntityID = 1, returnGradingPeriodGradeBucketID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnFactorBasedGPACountAs = False, returnGradeBucketID = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodEndDateAddSnapshotGraceDays = False, returnGradingPeriodGradeBucketExistsInSpecifcEntity = False, returnGradingPeriodGradeBucketIDClonedFrom = False, returnGradingPeriodIDEnd = False, returnGradingPeriodIDStart = False, returnHasGradeBucketTypeCategories = False, returnIsAHistoricRecord = False, returnIsGradeBucketForETranscript = False, returnIsUpToDate = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnNumberOfGradeBucketsToWeight = False, returnStateETranscriptSessionTypeID = False, returnStatus = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradingPeriodGradeBucket in the district.

	This function returns a dataframe of every GradingPeriodGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradingPeriodSet(searchConditions = [], EntityID = 1, returnGradingPeriodSetID = False, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingPeriodSetIDClonedFrom = False, returnGradingPeriodSetIDClonedTo = False, returnIsDefault = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradingPeriodSet in the district.

	This function returns a dataframe of every GradingPeriodSet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradReqRankGPACourseType(searchConditions = [], EntityID = 1, returnGradReqRankGPACourseTypeID = False, returnCourseTypeID = False, returnCreatedTime = False, returnGradReqRankGPAMethodEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradReqRankGPACourseType in the district.

	This function returns a dataframe of every GradReqRankGPACourseType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradReqRankGPAMethodEntity(searchConditions = [], EntityID = 1, returnGradReqRankGPAMethodEntityID = False, returnCreatedTime = False, returnGPAMethodEntityID = False, returnGradeBucketFlagIDLocalCredit = False, returnGradeBucketIDTermOne = False, returnGradeBucketIDTermTwo = False, returnGradPlanSetting = False, returnGradPlanSettingCode = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradReqRankGPAMethodEntity in the district.

	This function returns a dataframe of every GradReqRankGPAMethodEntity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradReqRankHighSchoolGradeLevel(searchConditions = [], EntityID = 1, returnGradReqRankHighSchoolGradeLevelID = False, returnCreatedTime = False, returnGPAMethodID = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradReqRankHighSchoolGradeLevel in the district.

	This function returns a dataframe of every GradReqRankHighSchoolGradeLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradReqRankSchoolYearIncludeLocalCredit(searchConditions = [], EntityID = 1, returnGradReqRankSchoolYearIncludeLocalCreditID = False, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradReqRankSchoolYearIncludeLocalCredit in the district.

	This function returns a dataframe of every GradReqRankSchoolYearIncludeLocalCredit in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryGradReqSubjectType(searchConditions = [], EntityID = 1, returnGradReqSubjectTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every GradReqSubjectType in the district.

	This function returns a dataframe of every GradReqSubjectType in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRuleGPA(searchConditions = [], EntityID = 1, returnHonorRollRuleGPAID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnHonorRollRuleGPAIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnMaximumGPA = False, returnMinimumGPA = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRuleGPA in the district.

	This function returns a dataframe of every HonorRollRuleGPA in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRuleGradeMark(searchConditions = [], EntityID = 1, returnHonorRollRuleGradeMarkID = False, returnAllowException = False, returnCourseStandardFilterXML = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnExclusionThreshold = False, returnHonorRollRuleGradeMarkIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnInclusionType = False, returnInclusionTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRuleGradeMark in the district.

	This function returns a dataframe of every HonorRollRuleGradeMark in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRuleGradeMarkGradeBucket(searchConditions = [], EntityID = 1, returnHonorRollRuleGradeMarkGradeBucketID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketID = False, returnHonorRollRuleGradeMarkGradeBucketIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRuleGradeMarkGradeBucket in the district.

	This function returns a dataframe of every HonorRollRuleGradeMarkGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRuleGradeMarkGradeMark(searchConditions = [], EntityID = 1, returnHonorRollRuleGradeMarkGradeMarkID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkID = False, returnHonorRollRuleGradeMarkGradeMarkIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnIsException = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRuleGradeMarkGradeMark in the district.

	This function returns a dataframe of every HonorRollRuleGradeMarkGradeMark in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRulePriorHonorRoll(searchConditions = [], EntityID = 1, returnHonorRollRulePriorHonorRollID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollLevelTotal = False, returnHonorRollRulePriorHonorRollIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRulePriorHonorRoll in the district.

	This function returns a dataframe of every HonorRollRulePriorHonorRoll in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRulePriorHonorRollLevel(searchConditions = [], EntityID = 1, returnHonorRollRulePriorHonorRollLevelID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRulePriorHonorRollID = False, returnHonorRollRulePriorHonorRollLevelIDClonedFrom = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRulePriorHonorRollLevel in the district.

	This function returns a dataframe of every HonorRollRulePriorHonorRollLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRun(searchConditions = [], EntityID = 1, returnHonorRollRunID = False, returnAllowMultipleHonorRollLevels = False, returnContainsGPARule = False, returnCreatedTime = False, returnDisplayGPAForHonorRoll = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketIDToDisplay = False, returnGPAMethodIDToDisplay = False, returnGPATypeToDisplay = False, returnGPATypeToDisplayCode = False, returnHonorRollRunIDClonedFrom = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRun in the district.

	This function returns a dataframe of every HonorRollRun in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRunHistory(searchConditions = [], EntityID = 1, returnHonorRollRunHistoryID = False, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnGPAAsOfDate = False, returnHonorRollRunID = False, returnModifiedTime = False, returnNameDescription = False, returnStudentFilterParameter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRunHistory in the district.

	This function returns a dataframe of every HonorRollRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRunLevel(searchConditions = [], EntityID = 1, returnHonorRollRunLevelID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunID = False, returnHonorRollRunLevelIDClonedFrom = False, returnHonorRollRunNameName = False, returnModifiedTime = False, returnName = False, returnOrder = False, returnRulesParameterDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRunLevel in the district.

	This function returns a dataframe of every HonorRollRunLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRunLevelHistory(searchConditions = [], EntityID = 1, returnHonorRollRunLevelHistoryID = False, returnCreatedTime = False, returnEntitySchoolYearHonorRollRunLevelName = False, returnHonorRollRunHistoryID = False, returnHonorRollRunLevelID = False, returnModifiedTime = False, returnParameterDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRunLevelHistory in the district.

	This function returns a dataframe of every HonorRollRunLevelHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHonorRollRunLevelRule(searchConditions = [], EntityID = 1, returnHonorRollRunLevelRuleID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelRuleIDClonedFrom = False, returnModifiedTime = False, returnOrder = False, returnParameterDescription = False, returnRuleType = False, returnRuleTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HonorRollRunLevelRule in the district.

	This function returns a dataframe of every HonorRollRunLevelRule in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPointSet(searchConditions = [], EntityID = 1, returnPointSetID = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PointSet in the district.

	This function returns a dataframe of every PointSet in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPointSetEntity(searchConditions = [], EntityID = 1, returnPointSetEntityID = False, returnApplyFactorBasedAddOn = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnIsDefault = False, returnIsWeighted = False, returnModifiedTime = False, returnPointSetEntityIDClonedFrom = False, returnPointSetID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PointSetEntity in the district.

	This function returns a dataframe of every PointSetEntity in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQueuedGPACalculation(searchConditions = [], EntityID = 1, returnQueuedGPACalculationID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSchoolYearID = False, returnSkipCredits = False, returnSourcePrimaryKey = False, returnSourceType = False, returnSourceTypeCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QueuedGPACalculation in the district.

	This function returns a dataframe of every QueuedGPACalculation in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRankMethod(searchConditions = [], EntityID = 1, returnRankMethodID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnIncludeNonRankedStudents = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueRangeHigh = False, returnValueRangeLow = False, returnValueRangeType = False, returnValueRangeTypeCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RankMethod in the district.

	This function returns a dataframe of every RankMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRankRunHistory(searchConditions = [], EntityID = 1, returnRankRunHistoryID = False, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnEntityID = False, returnFriendlyParameterDescription = False, returnFullGroupingDescription = False, returnGPAAsOfDate = False, returnGradeLevelIDCohort = False, returnModifiedTime = False, returnParameterDescription = False, returnRankMethodID = False, returnSchoolYearID = False, returnStudentGroup = False, returnStudentGroupCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RankRunHistory in the district.

	This function returns a dataframe of every RankRunHistory in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySectionLengthGPABucket(searchConditions = [], EntityID = 1, returnSectionLengthGPABucketID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketEntityID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSectionLengthGPABucketIDClonedFrom = False, returnSectionLengthID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SectionLengthGPABucket in the district.

	This function returns a dataframe of every SectionLengthGPABucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentCommentBucket(searchConditions = [], EntityID = 1, returnStudentCommentBucketID = False, returnCommentBucketID = False, returnCommentCodeID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentCommentBucket in the district.

	This function returns a dataframe of every StudentCommentBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEarnedCreditsBucket(searchConditions = [], EntityID = 1, returnStudentEarnedCreditsBucketID = False, returnCreatedTime = False, returnEarnedCredits = False, returnEarnedCreditsAllEntered = False, returnEarnedCreditsAttempted = False, returnEarnedCreditsAttemptedAllEntered = False, returnEarnedCreditsAttemptedCompleted = False, returnEarnedCreditsAttemptedDefault = False, returnEarnedCreditsCompleted = False, returnEarnedCreditsDefault = False, returnEarnedCreditsMethodID = False, returnEarnedCreditsPossible = False, returnEarnedCreditsPossibleAllEntered = False, returnEarnedCreditsPossibleCompleted = False, returnEarnedCreditsPossibleDefault = False, returnEntityID = False, returnFailedCredits = False, returnFailedCreditsAllEntered = False, returnFailedCreditsCompleted = False, returnFailedCreditsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentEarnedCreditsBucketGroupID = False, returnStudentGradeBucketID = False, returnStudentID = False, returnStudentSectionEarnedCreditsBucketGroupID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEarnedCreditsBucket in the district.

	This function returns a dataframe of every StudentEarnedCreditsBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentEarnedCreditsBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentEarnedCreditsBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEarnedCreditsBucketGroup(searchConditions = [], EntityID = 1, returnStudentEarnedCreditsBucketGroupID = False, returnCreatedTime = False, returnEarnedCreditsAllEntered = False, returnEarnedCreditsAttemptedAllEntered = False, returnEarnedCreditsAttemptedCompleted = False, returnEarnedCreditsAttemptedDefault = False, returnEarnedCreditsCompleted = False, returnEarnedCreditsDefault = False, returnEarnedCreditsMethodID = False, returnEarnedCreditsPossibleAllEntered = False, returnEarnedCreditsPossibleCompleted = False, returnEarnedCreditsPossibleDefault = False, returnFailedCreditsAllEntered = False, returnFailedCreditsCompleted = False, returnFailedCreditsDefault = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEarnedCreditsBucketGroup in the district.

	This function returns a dataframe of every StudentEarnedCreditsBucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentEarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentEarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentFreeFormCommentBucket(searchConditions = [], EntityID = 1, returnStudentFreeFormCommentBucketID = False, returnComment = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentFreeFormCommentBucket in the district.

	This function returns a dataframe of every StudentFreeFormCommentBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGPABucket(searchConditions = [], EntityID = 1, returnStudentGPABucketID = False, returnBonusGPAPoints = False, returnCreatedTime = False, returnDisplayGPACredits = False, returnDisplayGPAPoints = False, returnEntityID = False, returnGPACredits = False, returnGPAPoints = False, returnGPAWithBonus = False, returnGradReqRankGPAStatus = False, returnGradReqRankGPAStatusCode = False, returnHasAllGradesRequiredForGPACalculation = False, returnModifiedTime = False, returnPointsAndCreditsMultiplier = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnStudentSectionGPABucketGroupID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGPABucket in the district.

	This function returns a dataframe of every StudentGPABucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGPABucketGroup(searchConditions = [], EntityID = 1, returnStudentGPABucketGroupID = False, returnBonusGPA = False, returnBonusGPAWithoutRounding = False, returnCreatedTime = False, returnCurrentDefaultDistrictID = False, returnEarnedCredits = False, returnElectiveBonusGPA = False, returnElectiveFactor = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnFactorBonusGPA = False, returnFactorBonusGPAWithoutRounding = False, returnFailedCredits = False, returnFinalGPARoundingDecimals = False, returnGPA = False, returnGPABucketID = False, returnGPACalculationRoundingDecimals = False, returnGPACredits = False, returnGPACreditsWithoutRounding = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsWithoutRounding = False, returnGPAWithBonus = False, returnGPAWithFactorBonus = False, returnGradReqRankGPABreakdown = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGPABucketGroup in the district.

	This function returns a dataframe of every StudentGPABucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGradeBucket(searchConditions = [], EntityID = 1, returnStudentGradeBucketID = False, returnAbsentCount = False, returnCalculatedCalculationTypeCode = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnCalculatedClosedGradingPeriodGradeChangeStatusCode = False, returnCalculatedPoints = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCompleteByTeacher = False, returnCompleteByTeacherCode = False, returnCompletionDate = False, returnCompletionDateOverride = False, returnConfigEarnedCredits = False, returnConfigFailedCredits = False, returnCreatedTime = False, returnDoNotPost = False, returnEarnedCreditAttempted = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEarnedPoints = False, returnEntityID = False, returnExcusedCount = False, returnFailedCredits = False, returnGradeMarkID = False, returnGradeMarkIDOutOfDistrictTransferWithdraw = False, returnGradeMarkIDOverride = False, returnGradeMarkIDToApply = False, returnGradeMarkIDToUse = False, returnGradeMarkIDToUseIgnoreDoNotPost = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnGradeMarkToUseExists = False, returnGradeMarkToUseIgnoreDoNotPost = False, returnGradingPeriodEndDateHasPassed = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandardGrades = False, returnHasAssignments = False, returnHasGrade = False, returnHasStudentSectionGradingScaleGradeBucket = False, returnHasStudentSectionLinkConflict = False, returnHasSubjectGrades = False, returnHasUnscoredRequiredFeederBucket = False, returnIsAdminOverride = False, returnIsComplete = False, returnIsTransferBucket = False, returnIsUnused = False, returnIsUsingPointsBasedScale = False, returnIsWeightedOnByEnrolledInBucket = False, returnModifiedTime = False, returnNoGradebookOrAdminOverride = False, returnNoGradebookOverride = False, returnOtherCount = False, returnOverrideComment = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentHasChangedWithinSpecifiedAmountOfTime = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentIgnoreMinimum = False, returnPercentWithAdjustmentNoCap = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithAdjustmentWithGradeMarkToUseIgnoreDoNotPost = False, returnPercentWithAdjustmentWithGradeMarkToUseNoCap = False, returnPercentWithGradeMarkIgnoreDoNotPost = False, returnPossiblePoints = False, returnReportCardGradeMarkToUse = False, returnSchoolYearID = False, returnSectionID = False, returnStartingPercent = False, returnStudentCommentBucketCount = False, returnStudentFreeFormCommentBucketCount = False, returnStudentGradeBucketFlag = False, returnStudentGradeBucketStatus = False, returnStudentSectionID = False, returnTardyCount = False, returnUnexcusedCount = False, returnUseCompletionDateOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentForGradeBucket = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGradeBucket in the district.

	This function returns a dataframe of every StudentGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentGradeBucketFlag(searchConditions = [], EntityID = 1, returnStudentGradeBucketFlagID = False, returnCreatedTime = False, returnGradeBucketFlagID = False, returnIsManual = False, returnModifiedTime = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnAPIOptionFlags = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentGradeBucketFlag in the district.

	This function returns a dataframe of every StudentGradeBucketFlag in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentHonorRollRunLevel(searchConditions = [], EntityID = 1, returnStudentHonorRollRunLevelID = False, returnCreatedTime = False, returnGPAValue = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentHonorRollRunLevel in the district.

	This function returns a dataframe of every StudentHonorRollRunLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentRank(searchConditions = [], EntityID = 1, returnStudentRankID = False, returnCreatedTime = False, returnDisplayRank = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNumberInRank = False, returnNumberOutOf = False, returnRankRunHistoryID = False, returnSchoolYearIDCohort = False, returnStudentID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentRank in the district.

	This function returns a dataframe of every StudentRank in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionEarnedCreditsBucketGroup(searchConditions = [], EntityID = 1, returnStudentSectionEarnedCreditsBucketGroupID = False, returnCreatedTime = False, returnEarnedCreditsAllEntered = False, returnEarnedCreditsAttemptedAllEntered = False, returnEarnedCreditsAttemptedCompleted = False, returnEarnedCreditsAttemptedDefault = False, returnEarnedCreditsCompleted = False, returnEarnedCreditsDefault = False, returnEarnedCreditsMethodID = False, returnEarnedCreditsPossibleAllEntered = False, returnEarnedCreditsPossibleCompleted = False, returnEarnedCreditsPossibleDefault = False, returnEntityID = False, returnFailedCreditsAllEntered = False, returnFailedCreditsCompleted = False, returnFailedCreditsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentEarnedCreditsBucketGroupID = False, returnStudentID = False, returnStudentSectionID = False, returnTotalEarnedCreditsOverride = False, returnTotalFailedCreditsOverride = False, returnUseEarnedCreditsTotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionEarnedCreditsBucketGroup in the district.

	This function returns a dataframe of every StudentSectionEarnedCreditsBucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionEarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionEarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionEarnedCreditsMethod(searchConditions = [], EntityID = 1, returnStudentSectionEarnedCreditsMethodID = False, returnCreatedTime = False, returnEarnedCreditsMethodEntityID = False, returnEarnedCreditsOverride = False, returnModifiedTime = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionEarnedCreditsMethod in the district.

	This function returns a dataframe of every StudentSectionEarnedCreditsMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionEarnedCreditsMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionEarnedCreditsMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionGPABucketGroup(searchConditions = [], EntityID = 1, returnStudentSectionGPABucketGroupID = False, returnBonusGPA = False, returnCreatedTime = False, returnElectiveBonusGPA = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnEntityID = False, returnFactorBasedGPACountTotal = False, returnGPACredits = False, returnGPAPoints = False, returnIsGPAElective = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentSectionID = False, returnTotalAddOnPoints = False, returnTotalGPACredits = False, returnTotalGPAPoints = False, returnUseGPATotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionGPABucketGroup in the district.

	This function returns a dataframe of every StudentSectionGPABucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSectionGPAMethod(searchConditions = [], EntityID = 1, returnStudentSectionGPAMethodID = False, returnCreatedTime = False, returnCumulativeGPACredits = False, returnCumulativeGPAPoints = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSectionGPAMethod in the district.

	This function returns a dataframe of every StudentSectionGPAMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFactorBasedAddOn(searchConditions = [], EntityID = 1, returnTempFactorBasedAddOnID = False, returnCreatedTime = False, returnFactor = False, returnGPABucketEntityDisplayName = False, returnGradeReferenceDisplayName = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnOriginalGradingEndDateCutoffForCumulative = False, returnTempFactorBasedAddOnClonedFromID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFactorBasedAddOn in the district.

	This function returns a dataframe of every TempFactorBasedAddOn in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedGradingPeriod(searchConditions = [], EntityID = 1, returnTempFailedGradingPeriodID = False, returnCourseLengthCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNote = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStartDate = False, returnTempGradingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedGradingPeriod in the district.

	This function returns a dataframe of every TempFailedGradingPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeBucketFlagDetailGPAMethod(searchConditions = [], EntityID = 1, returnTempGradeBucketFlagDetailGPAMethodID = False, returnCreatedTime = False, returnEntityCode = False, returnGPAMethodDescription = False, returnGPAMethodEntityID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagCodeName = False, returnGradeBucketFlagDetailGPAMethodID = False, returnGradeBucketFlagDetailID = False, returnModifiedTime = False, returnNumericYear = False, returnPointSetDescription = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeBucketFlagDetailGPAMethod in the district.

	This function returns a dataframe of every TempGradeBucketFlagDetailGPAMethod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeBucketFlagDetailGPAMethodError(searchConditions = [], EntityID = 1, returnTempGradeBucketFlagDetailGPAMethodErrorID = False, returnCreatedTime = False, returnErrorString = False, returnGradeBucketFlagDetailGPAMethod = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeBucketFlagDetailGPAMethodError in the district.

	This function returns a dataframe of every TempGradeBucketFlagDetailGPAMethodError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethodError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethodError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeMarkPointSetError(searchConditions = [], EntityID = 1, returnTempGradeMarkPointSetErrorID = False, returnCreatedTime = False, returnErrorString = False, returnGPAMethodName = False, returnGradeMarkCode = False, returnModifiedTime = False, returnPointSetName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeMarkPointSetError in the district.

	This function returns a dataframe of every TempGradeMarkPointSetError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeReportAttendanceTerm(searchConditions = [], EntityID = 1, returnTempGradeReportAttendanceTermID = False, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarDescription = False, returnCreatedTime = False, returnEndDate = False, returnEntityName = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeReportAttendanceTerm in the district.

	This function returns a dataframe of every TempGradeReportAttendanceTerm in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeReportGradeBucket(searchConditions = [], EntityID = 1, returnTempGradeReportGradeBucketID = False, returnCreatedTime = False, returnEntityName = False, returnGradeBucketLabel = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSectionLengthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeReportGradeBucket in the district.

	This function returns a dataframe of every TempGradeReportGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeReportTemplate(searchConditions = [], EntityID = 1, returnTempGradeReportTemplateID = False, returnCreatedTime = False, returnEntityCodeNameClonedFrom = False, returnEntityCodeNameClonedTo = False, returnEntityID = False, returnErrorCount = False, returnHasErrors = False, returnModifiedTime = False, returnNewGradeReportTemplateDescription = False, returnOriginalGradeReportTemplateDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeReportTemplate in the district.

	This function returns a dataframe of every TempGradeReportTemplate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeReportTemplateError(searchConditions = [], EntityID = 1, returnTempGradeReportTemplateErrorID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempGradeReportTemplateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeReportTemplateError in the district.

	This function returns a dataframe of every TempGradeReportTemplateError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradingPeriod(searchConditions = [], EntityID = 1, returnTempGradingPeriodID = False, returnCourseLengthCode = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthEndDate = False, returnSectionLengthID = False, returnSectionLengthStartDate = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradingPeriod in the district.

	This function returns a dataframe of every TempGradingPeriod in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradingPeriodError(searchConditions = [], EntityID = 1, returnTempGradingPeriodErrorID = False, returnAcademicStandard = False, returnAssignmentName = False, returnCategory = False, returnCourseDescription = False, returnCreatedTime = False, returnDueDate = False, returnError = False, returnModifiedTime = False, returnSectionNumber = False, returnSubject = False, returnTeacherName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradingPeriodError in the district.

	This function returns a dataframe of every TempGradingPeriodError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradingUtilityError(searchConditions = [], EntityID = 1, returnTempGradingUtilityErrorID = False, returnCreatedTime = False, returnError = False, returnGrade = False, returnHonorRollName = False, returnModifiedTime = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradingUtilityError in the district.

	This function returns a dataframe of every TempGradingUtilityError in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHonorRollGradeMarkMethodRange(searchConditions = [], EntityID = 1, returnTempHonorRollGradeMarkMethodRangeID = False, returnCreatedTime = False, returnHonorRollGradeMarkMethodID = False, returnHonorRollGradeMarkMethodRangeID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnPriorityOrder = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHonorRollGradeMarkMethodRange in the district.

	This function returns a dataframe of every TempHonorRollGradeMarkMethodRange in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHonorRollGradeMarkMethodRangeCourseGroup(searchConditions = [], EntityID = 1, returnTempHonorRollGradeMarkMethodRangeCourseGroupID = False, returnCourseGroupID = False, returnCreatedTime = False, returnHonorRollGradeMarkMethodRangeCourseGroupID = False, returnHonorRollGradeMarkMethodRangeID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHonorRollGradeMarkMethodRangeCourseGroup in the district.

	This function returns a dataframe of every TempHonorRollGradeMarkMethodRangeCourseGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHonorRollGradeMarkMethodRangeGradeMark(searchConditions = [], EntityID = 1, returnTempHonorRollGradeMarkMethodRangeGradeMarkID = False, returnCreatedTime = False, returnGradeMarkID = False, returnHonorRollGradeMarkMethodRangeGradeMarkID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHonorRollGradeMarkMethodRangeGradeMark in the district.

	This function returns a dataframe of every TempHonorRollGradeMarkMethodRangeGradeMark in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(searchConditions = [], EntityID = 1, returnTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket in the district.

	This function returns a dataframe of every TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHonorRollMethodRange(searchConditions = [], EntityID = 1, returnTempHonorRollMethodRangeID = False, returnCreatedTime = False, returnGPAHigh = False, returnGPALow = False, returnHonorRollMethodRangeID = False, returnIsUsed = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHonorRollMethodRange in the district.

	This function returns a dataframe of every TempHonorRollMethodRange in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentCommentBucket(searchConditions = [], EntityID = 1, returnTempStudentCommentBucketID = False, returnCommentBucketID = False, returnCommentBucketName = False, returnCreatedTime = False, returnCurrentCommentCode = False, returnDisplayOrder = False, returnGradingPeriodDescription = False, returnGradingPeriodID = False, returnModifiedTime = False, returnNewCommentCode = False, returnNewCommentCodeID = False, returnSectionLengthCode = False, returnStudentCommentBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentCommentBucket in the district.

	This function returns a dataframe of every TempStudentCommentBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentGPABucket(searchConditions = [], EntityID = 1, returnTempStudentGPABucketID = False, returnCorrectBonusGPAPoints = False, returnCorrectGPACredits = False, returnCorrectGPAPoints = False, returnCourseName = False, returnCreatedTime = False, returnCurrentBonusGPAPoints = False, returnCurrentGPACredits = False, returnCurrentGPAPoints = False, returnEntityID = False, returnGPABucketCodeDescription = False, returnGPABucketID = False, returnGPAMethodCodeDescription = False, returnGPAMethodID = False, returnGradeBucketCodeDescription = False, returnGradingPeriodGradeBucketID = False, returnIsDelete = False, returnIsGradReqRankGPA = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSchoolYearIDForPostSave = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentGPABucketID = False, returnStudentGradeBucketID = False, returnStudentGradeBucketIsFromTemp = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionGPABucketGroupID = False, returnStudentSectionGPABucketGroupIsFromTemp = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentGPABucket in the district.

	This function returns a dataframe of every TempStudentGPABucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentGPABucketGroup(searchConditions = [], EntityID = 1, returnTempStudentGPABucketGroupID = False, returnCreatedTime = False, returnGPABucketID = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentGPABucketGroup in the district.

	This function returns a dataframe of every TempStudentGPABucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentGradeBucket(searchConditions = [], EntityID = 1, returnTempStudentGradeBucketID = False, returnCompleteByTeacherCode = False, returnCreatedTime = False, returnDoNotPost = False, returnEntityID = False, returnGradeBucketCode = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkIDReverse = False, returnGradingPeriodGradeBucketID = False, returnIsTransferBucket = False, returnIsTransferCourse = False, returnModifiedTime = False, returnNewCode = False, returnOldCode = False, returnOverallPercent = False, returnOverallStatus = False, returnPercentWithAdjustment = False, returnSchoolYearID = False, returnSectionID = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionID = False, returnStudentSectionName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentGradeBucket in the district.

	This function returns a dataframe of every TempStudentGradeBucket in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentGradeBucketFlag(searchConditions = [], EntityID = 1, returnTempStudentGradeBucketFlagID = False, returnCourseSectionCode = False, returnCreatedTime = False, returnExceptionReason = False, returnGradeBucketFlagCode = False, returnGradeBucketFlagID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnIsDelete = False, returnIsError = False, returnIsException = False, returnIsManual = False, returnModifiedTime = False, returnSectionLengthCode = False, returnStudentGradeBucketFlagIDToDelete = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentGradeBucketFlag in the district.

	This function returns a dataframe of every TempStudentGradeBucketFlag in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentHonorRollRunLevel(searchConditions = [], EntityID = 1, returnTempStudentHonorRollRunLevelID = False, returnCreatedTime = False, returnGPAValue = False, returnGrade = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelName = False, returnHonorRollRunLevelOrder = False, returnModifiedTime = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentHonorRollRunLevel in the district.

	This function returns a dataframe of every TempStudentHonorRollRunLevel in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentRank(searchConditions = [], EntityID = 1, returnTempStudentRankID = False, returnCohortNumericYear = False, returnCreatedTime = False, returnGPA = False, returnGraduationRequirementYear = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNoRank = False, returnRank = False, returnRankMethodID = False, returnSchoolYearIDCohort = False, returnStudentGrade = False, returnStudentID = False, returnStudentName = False, returnStudentRankID = False, returnStudentRankSort = False, returnTotalStudents = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentRank in the district.

	This function returns a dataframe of every TempStudentRank in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentSection(searchConditions = [], EntityID = 1, returnTempStudentSectionID = False, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionCode = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentSection in the district.

	This function returns a dataframe of every TempStudentSection in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentSectionFailedUpdate(searchConditions = [], EntityID = 1, returnTempStudentSectionFailedUpdateID = False, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnSection = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentSectionFailedUpdate in the district.

	This function returns a dataframe of every TempStudentSectionFailedUpdate in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentSectionGPABucketGroup(searchConditions = [], EntityID = 1, returnTempStudentSectionGPABucketGroupID = False, returnCreatedTime = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnIsCumulative = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentSectionGPABucketGroup in the district.

	This function returns a dataframe of every TempStudentSectionGPABucketGroup in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempTransferCourse(searchConditions = [], EntityID = 1, returnTempTransferCourseID = False, returnCourseCredits = False, returnCourseDescription = False, returnCourseID = False, returnCourseSection = False, returnCreatedTime = False, returnEarnedCreditOverride = False, returnEndDate = False, returnEntityCode = False, returnEntityID = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLinking = False, returnGradedCourse = False, returnGradeReferenceID = False, returnGradingPeriodSetID = False, returnGradYear = False, returnModifiedTime = False, returnSchoolYear = False, returnSchoolYearID = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentID = False, returnTotalEarnedCredits = False, returnTotalFailedCredits = False, returnUseAddOnGPA = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditPercentOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempTransferCourse in the district.

	This function returns a dataframe of every TempTransferCourse in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTranscriptNote(searchConditions = [], EntityID = 1, returnTranscriptNoteID = False, returnCreatedTime = False, returnDateAdded = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TranscriptNote in the district.

	This function returns a dataframe of every TranscriptNote in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTranscriptSent(searchConditions = [], EntityID = 1, returnTranscriptSentID = False, returnComment = False, returnCreatedTime = False, returnDateSent = False, returnInstitutionID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TranscriptSent in the district.

	This function returns a dataframe of every TranscriptSent in the district filtered by search conditions.

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)