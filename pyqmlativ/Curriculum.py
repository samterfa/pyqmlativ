# This module contains Curriculum functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAcademicStandard(searchConditions = [], EntityID = 1, returnAcademicStandardID = False, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnBackgroundColor = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandard in the district.

	This function returns a dataframe of every AcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardDefault(searchConditions = [], EntityID = 1, returnAcademicStandardDefaultID = False, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardDefault in the district.

	This function returns a dataframe of every AcademicStandardDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardGradeRange(searchConditions = [], EntityID = 1, returnAcademicStandardGradeRangeID = False, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardGradeRange in the district.

	This function returns a dataframe of every AcademicStandardGradeRange in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardGradeRangeDefault(searchConditions = [], EntityID = 1, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardGradeRangeDefault in the district.

	This function returns a dataframe of every AcademicStandardGradeRangeDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardHierarchyDepth(searchConditions = [], EntityID = 1, returnAcademicStandardHierarchyDepthID = False, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardHierarchyDepth in the district.

	This function returns a dataframe of every AcademicStandardHierarchyDepth in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardSet(searchConditions = [], EntityID = 1, returnAcademicStandardSetID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardSet in the district.

	This function returns a dataframe of every AcademicStandardSet in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardSetDefault(searchConditions = [], EntityID = 1, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardSetDefault in the district.

	This function returns a dataframe of every AcademicStandardSetDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardSubject(searchConditions = [], EntityID = 1, returnAcademicStandardSubjectID = False, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardSubject in the district.

	This function returns a dataframe of every AcademicStandardSubject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAcademicStandardSubjectDefault(searchConditions = [], EntityID = 1, returnAcademicStandardSubjectDefaultID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AcademicStandardSubjectDefault in the district.

	This function returns a dataframe of every AcademicStandardSubjectDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryAssessmentToolMN(searchConditions = [], EntityID = 1, returnAssessmentToolMNID = False, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AssessmentToolMN in the district.

	This function returns a dataframe of every AssessmentToolMN in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculum(searchConditions = [], EntityID = 1, returnCurriculumID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Curriculum in the district.

	This function returns a dataframe of every Curriculum in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumAcademicStandard(searchConditions = [], EntityID = 1, returnCurriculumAcademicStandardID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumAcademicStandard in the district.

	This function returns a dataframe of every CurriculumAcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumCustomRequirement(searchConditions = [], EntityID = 1, returnCurriculumCustomRequirementID = False, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumCustomRequirement in the district.

	This function returns a dataframe of every CurriculumCustomRequirement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumGradeLevel(searchConditions = [], EntityID = 1, returnCurriculumGradeLevelID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumGradeLevel in the district.

	This function returns a dataframe of every CurriculumGradeLevel in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumProgramMN(searchConditions = [], EntityID = 1, returnCurriculumProgramMNID = False, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumProgramMN in the district.

	This function returns a dataframe of every CurriculumProgramMN in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumSubject(searchConditions = [], EntityID = 1, returnCurriculumSubjectID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumSubject in the district.

	This function returns a dataframe of every CurriculumSubject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumSubjectAcademicStandard(searchConditions = [], EntityID = 1, returnCurriculumSubjectAcademicStandardID = False, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumSubjectAcademicStandard in the district.

	This function returns a dataframe of every CurriculumSubjectAcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumYear(searchConditions = [], EntityID = 1, returnCurriculumYearID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumYear in the district.

	This function returns a dataframe of every CurriculumYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarlyEducationInstructionalApproachMN(searchConditions = [], EntityID = 1, returnEarlyEducationInstructionalApproachMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarlyEducationInstructionalApproachMN in the district.

	This function returns a dataframe of every EarlyEducationInstructionalApproachMN in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEarlyEducationProgramMN(searchConditions = [], EntityID = 1, returnEarlyEducationProgramMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EarlyEducationProgramMN in the district.

	This function returns a dataframe of every EarlyEducationProgramMN in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHierarchyDepth(searchConditions = [], EntityID = 1, returnHierarchyDepthID = False, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnDynamicRelationshipID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HierarchyDepth in the district.

	This function returns a dataframe of every HierarchyDepth in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPrerequisite(searchConditions = [], EntityID = 1, returnPrerequisiteID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Prerequisite in the district.

	This function returns a dataframe of every Prerequisite in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPrerequisiteCurriculum(searchConditions = [], EntityID = 1, returnPrerequisiteCurriculumID = False, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PrerequisiteCurriculum in the district.

	This function returns a dataframe of every PrerequisiteCurriculum in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySiteBasedInitiativeMN(searchConditions = [], EntityID = 1, returnSiteBasedInitiativeMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SiteBasedInitiativeMN in the district.

	This function returns a dataframe of every SiteBasedInitiativeMN in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStandardPlacementMN(searchConditions = [], EntityID = 1, returnStandardPlacementMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StandardPlacementMN in the district.

	This function returns a dataframe of every StandardPlacementMN in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubject(searchConditions = [], EntityID = 1, returnSubjectID = False, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Subject in the district.

	This function returns a dataframe of every Subject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAcademicStandard(searchConditions = [], EntityID = 1, returnTempAcademicStandardID = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAcademicStandard in the district.

	This function returns a dataframe of every TempAcademicStandard in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAcademicStandardGradeRange(searchConditions = [], EntityID = 1, returnTempAcademicStandardGradeRangeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAcademicStandardGradeRange in the district.

	This function returns a dataframe of every TempAcademicStandardGradeRange in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAcademicStandardSet(searchConditions = [], EntityID = 1, returnTempAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAcademicStandardSet in the district.

	This function returns a dataframe of every TempAcademicStandardSet in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAcademicStandardSubject(searchConditions = [], EntityID = 1, returnTempAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAcademicStandardSubject in the district.

	This function returns a dataframe of every TempAcademicStandardSubject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempGradeRangeCopyResult(searchConditions = [], EntityID = 1, returnTempGradeRangeCopyResultID = False, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempGradeRangeCopyResult in the district.

	This function returns a dataframe of every TempGradeRangeCopyResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempHierarchyDepth(searchConditions = [], EntityID = 1, returnTempHierarchyDepthID = False, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempHierarchyDepth in the district.

	This function returns a dataframe of every TempHierarchyDepth in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)