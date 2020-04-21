# This module contains GraduationRequirements functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryArea(searchConditions = [], EntityID = 1, returnAreaID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Area in the district.

	This function returns a dataframe of every Area in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCareerPlanDeclarationTimePeriod(searchConditions = [], EntityID = 1, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CareerPlanDeclarationTimePeriod in the district.

	This function returns a dataframe of every CareerPlanDeclarationTimePeriod in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCareerPlanDeclarationTimePeriodGradeReference(searchConditions = [], EntityID = 1, returnCareerPlanDeclarationTimePeriodGradeReferenceID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CareerPlanDeclarationTimePeriodGradeReference in the district.

	This function returns a dataframe of every CareerPlanDeclarationTimePeriodGradeReference in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCareerPlanDeclarationTimePeriodStudentEntityYear(searchConditions = [], EntityID = 1, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CareerPlanDeclarationTimePeriodStudentEntityYear in the district.

	This function returns a dataframe of every CareerPlanDeclarationTimePeriodStudentEntityYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCareerPlanGradeLevel(searchConditions = [], EntityID = 1, returnCareerPlanGradeLevelID = False, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CareerPlanGradeLevel in the district.

	This function returns a dataframe of every CareerPlanGradeLevel in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumCluster(searchConditions = [], EntityID = 1, returnCurriculumClusterID = False, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumCluster in the district.

	This function returns a dataframe of every CurriculumCluster in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumClusterCurriculum(searchConditions = [], EntityID = 1, returnCurriculumClusterCurriculumID = False, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumClusterCurriculum in the district.

	This function returns a dataframe of every CurriculumClusterCurriculum in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumClusterDefault(searchConditions = [], EntityID = 1, returnCurriculumClusterDefaultID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumClusterDefault in the district.

	This function returns a dataframe of every CurriculumClusterDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCurriculumSubArea(searchConditions = [], EntityID = 1, returnCurriculumSubAreaID = False, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CurriculumSubArea in the district.

	This function returns a dataframe of every CurriculumSubArea in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsement(searchConditions = [], EntityID = 1, returnEndorsementID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsDistrictDefined = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Endorsement in the district.

	This function returns a dataframe of every Endorsement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementDeclarationTimePeriod(searchConditions = [], EntityID = 1, returnEndorsementDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementDeclarationTimePeriod in the district.

	This function returns a dataframe of every EndorsementDeclarationTimePeriod in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementDeclarationTimePeriodGradeReference(searchConditions = [], EntityID = 1, returnEndorsementDeclarationTimePeriodGradeReferenceID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementDeclarationTimePeriodGradeReference in the district.

	This function returns a dataframe of every EndorsementDeclarationTimePeriodGradeReference in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementDeclarationTimePeriodStudentEntityYear(searchConditions = [], EntityID = 1, returnEndorsementDeclarationTimePeriodStudentEntityYearID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementDeclarationTimePeriodStudentEntityYear in the district.

	This function returns a dataframe of every EndorsementDeclarationTimePeriodStudentEntityYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementDefault(searchConditions = [], EntityID = 1, returnEndorsementDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementDefault in the district.

	This function returns a dataframe of every EndorsementDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementOption(searchConditions = [], EntityID = 1, returnEndorsementOptionID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementOption in the district.

	This function returns a dataframe of every EndorsementOption in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementOptionDefault(searchConditions = [], EntityID = 1, returnEndorsementOptionDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementOptionDefault in the district.

	This function returns a dataframe of every EndorsementOptionDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirement(searchConditions = [], EntityID = 1, returnEndorsementRequirementID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirement in the district.

	This function returns a dataframe of every EndorsementRequirement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementAssessment(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementAssessment in the district.

	This function returns a dataframe of every EndorsementRequirementAssessment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementAssessmentCluster(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentClusterID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementAssessmentCluster in the district.

	This function returns a dataframe of every EndorsementRequirementAssessmentCluster in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementAssessmentClusterDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementAssessmentClusterDefault in the district.

	This function returns a dataframe of every EndorsementRequirementAssessmentClusterDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementAssessmentDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentDefaultID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementAssessmentDefault in the district.

	This function returns a dataframe of every EndorsementRequirementAssessmentDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementAssessmentScore(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentScoreID = False, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementAssessmentScore in the district.

	This function returns a dataframe of every EndorsementRequirementAssessmentScore in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementAssessmentScoreDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementAssessmentScoreDefault in the district.

	This function returns a dataframe of every EndorsementRequirementAssessmentScoreDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementCurriculum(searchConditions = [], EntityID = 1, returnEndorsementRequirementCurriculumID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementCurriculum in the district.

	This function returns a dataframe of every EndorsementRequirementCurriculum in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementCurriculumDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementCurriculumDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementCurriculumDefault in the district.

	This function returns a dataframe of every EndorsementRequirementCurriculumDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEndorsementRequirementDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EndorsementRequirementDefault in the district.

	This function returns a dataframe of every EndorsementRequirementDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlan(searchConditions = [], EntityID = 1, returnPlanID = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEarnedCreditsMethodIDDefaultOverride = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Plan in the district.

	This function returns a dataframe of every Plan in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanDefault(searchConditions = [], EntityID = 1, returnPlanDefaultID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanDefault in the district.

	This function returns a dataframe of every PlanDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanEntity(searchConditions = [], EntityID = 1, returnPlanEntityID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanEntity in the district.

	This function returns a dataframe of every PlanEntity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQueuedGraduationPlanRecalcTrigger(searchConditions = [], EntityID = 1, returnQueuedGraduationPlanRecalcTriggerID = False, returnCreatedTime = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QueuedGraduationPlanRecalcTrigger in the district.

	This function returns a dataframe of every QueuedGraduationPlanRecalcTrigger in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQueuedStudentEndorsementCalculation(searchConditions = [], EntityID = 1, returnQueuedStudentEndorsementCalculationID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QueuedStudentEndorsementCalculation in the district.

	This function returns a dataframe of every QueuedStudentEndorsementCalculation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryQueuedStudentPlanCourseworkApplication(searchConditions = [], EntityID = 1, returnQueuedStudentPlanCourseworkApplicationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every QueuedStudentPlanCourseworkApplication in the district.

	This function returns a dataframe of every QueuedStudentPlanCourseworkApplication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentArea(searchConditions = [], EntityID = 1, returnStudentAreaID = False, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentArea in the district.

	This function returns a dataframe of every StudentArea in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentCareerPlan(searchConditions = [], EntityID = 1, returnStudentCareerPlanID = False, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentCareerPlan in the district.

	This function returns a dataframe of every StudentCareerPlan in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEndorsement(searchConditions = [], EntityID = 1, returnStudentEndorsementID = False, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEndorsement in the district.

	This function returns a dataframe of every StudentEndorsement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEndorsementOption(searchConditions = [], EntityID = 1, returnStudentEndorsementOptionID = False, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEndorsementOption in the district.

	This function returns a dataframe of every StudentEndorsementOption in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEndorsementRequirement(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEndorsementRequirement in the district.

	This function returns a dataframe of every StudentEndorsementRequirement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEndorsementRequirementAssessment(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementAssessmentID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEndorsementRequirementAssessment in the district.

	This function returns a dataframe of every StudentEndorsementRequirementAssessment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEndorsementRequirementAssessmentScore(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementAssessmentScoreID = False, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEndorsementRequirementAssessmentScore in the district.

	This function returns a dataframe of every StudentEndorsementRequirementAssessmentScore in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEndorsementRequirementCourseRequest(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementCourseRequestID = False, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEndorsementRequirementCourseRequest in the district.

	This function returns a dataframe of every StudentEndorsementRequirementCourseRequest in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentEndorsementRequirementCurriculum(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementCurriculumID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentEndorsementRequirementCurriculum in the district.

	This function returns a dataframe of every StudentEndorsementRequirementCurriculum in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentPlan(searchConditions = [], EntityID = 1, returnStudentPlanID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentPlan in the district.

	This function returns a dataframe of every StudentPlan in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentPlanThreadLock(searchConditions = [], EntityID = 1, returnStudentPlanThreadLockID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentPlanThreadLock in the district.

	This function returns a dataframe of every StudentPlanThreadLock in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSubArea(searchConditions = [], EntityID = 1, returnStudentSubAreaID = False, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSubArea in the district.

	This function returns a dataframe of every StudentSubArea in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSubAreaCurriculumSubArea(searchConditions = [], EntityID = 1, returnStudentSubAreaCurriculumSubAreaID = False, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSubAreaCurriculumSubArea in the district.

	This function returns a dataframe of every StudentSubAreaCurriculumSubArea in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentSubAreaWaiver(searchConditions = [], EntityID = 1, returnStudentSubAreaWaiverID = False, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentSubAreaWaiver in the district.

	This function returns a dataframe of every StudentSubAreaWaiver in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubArea(searchConditions = [], EntityID = 1, returnSubAreaID = False, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubArea in the district.

	This function returns a dataframe of every SubArea in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubAreaLimitGroup(searchConditions = [], EntityID = 1, returnSubAreaLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubAreaLimitGroup in the district.

	This function returns a dataframe of every SubAreaLimitGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySubAreaLimitGroupCurriculumSubArea(searchConditions = [], EntityID = 1, returnSubAreaLimitGroupCurriculumSubAreaID = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SubAreaLimitGroupCurriculumSubArea in the district.

	This function returns a dataframe of every SubAreaLimitGroupCurriculumSubArea in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempEndorsementDefault(searchConditions = [], EntityID = 1, returnTempEndorsementDefaultID = False, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempEndorsementDefault in the district.

	This function returns a dataframe of every TempEndorsementDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempEndorsementImportError(searchConditions = [], EntityID = 1, returnTempEndorsementImportErrorID = False, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempEndorsementImportError in the district.

	This function returns a dataframe of every TempEndorsementImportError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStudentSubAreaCurriculumSubArea(searchConditions = [], EntityID = 1, returnTempFailedStudentSubAreaCurriculumSubAreaID = False, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStudentSubAreaCurriculumSubArea in the district.

	This function returns a dataframe of every TempFailedStudentSubAreaCurriculumSubArea in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempFailedStudentSubAreaWaiver(searchConditions = [], EntityID = 1, returnTempFailedStudentSubAreaWaiverID = False, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempFailedStudentSubAreaWaiver in the district.

	This function returns a dataframe of every TempFailedStudentSubAreaWaiver in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)