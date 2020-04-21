# This module contains Health functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAdministerNameMedication(searchConditions = [], EntityID = 1, returnAdministerNameMedicationID = False, returnAdministerDate = False, returnAdministerDateOnly = False, returnAdministrationTime = False, returnCreatedTime = False, returnDosesAdministered = False, returnIsVoid = False, returnLocationID = False, returnModifiedTime = False, returnNameMedicationID = False, returnNameMedicationScheduleID = False, returnNameOfficeVisitID = False, returnNote = False, returnNotPerformedReasonID = False, returnStaffIDAdministeredBy = False, returnTotalDosesToday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AdministerNameMedication in the district.

	This function returns a dataframe of every AdministerNameMedication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/AdministerNameMedication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/AdministerNameMedication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBodyMassIndexPercentile(searchConditions = [], EntityID = 1, returnBodyMassIndexPercentileID = False, returnAgeInMonths = False, returnCoefficientOfVariation = False, returnCreatedTime = False, returnEightyFifthPercentile = False, returnFifthPercentile = False, returnFiftiethPercentile = False, returnGender = False, returnGenderCode = False, returnMedian = False, returnModifiedTime = False, returnNinetyFifthPercentile = False, returnNinetySeventhPercentile = False, returnPower = False, returnSeventyFifthPercentile = False, returnSkywardHash = False, returnSkywardID = False, returnTenthPercentile = False, returnThirdPercentile = False, returnTwentyFifthPercentile = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BodyMassIndexPercentile in the district.

	This function returns a dataframe of every BodyMassIndexPercentile in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyMassIndexPercentile/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyMassIndexPercentile/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBodyPart(searchConditions = [], EntityID = 1, returnBodyPartID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BodyPart in the district.

	This function returns a dataframe of every BodyPart in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyPart/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/BodyPart/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChildhoodIllness(searchConditions = [], EntityID = 1, returnChildhoodIllnessID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChildhoodIllness in the district.

	This function returns a dataframe of every ChildhoodIllness in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChildhoodIllnessComment(searchConditions = [], EntityID = 1, returnChildhoodIllnessCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChildhoodIllnessComment in the district.

	This function returns a dataframe of every ChildhoodIllnessComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChildhoodIllnessGuardianNotification(searchConditions = [], EntityID = 1, returnChildhoodIllnessGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChildhoodIllnessGuardianNotification in the district.

	This function returns a dataframe of every ChildhoodIllnessGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChildhoodIllnessGuardianResponse(searchConditions = [], EntityID = 1, returnChildhoodIllnessGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChildhoodIllnessGuardianResponse in the district.

	This function returns a dataframe of every ChildhoodIllnessGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChildhoodIllnessObservation(searchConditions = [], EntityID = 1, returnChildhoodIllnessObservationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChildhoodIllnessObservation in the district.

	This function returns a dataframe of every ChildhoodIllnessObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChildhoodIllnessReferralReason(searchConditions = [], EntityID = 1, returnChildhoodIllnessReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChildhoodIllnessReferralReason in the district.

	This function returns a dataframe of every ChildhoodIllnessReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryChildhoodIllnessReferralResult(searchConditions = [], EntityID = 1, returnChildhoodIllnessReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ChildhoodIllnessReferralResult in the district.

	This function returns a dataframe of every ChildhoodIllnessReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ChildhoodIllnessReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryComplianceSchedule(searchConditions = [], EntityID = 1, returnComplianceScheduleID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ComplianceSchedule in the district.

	This function returns a dataframe of every ComplianceSchedule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryComplianceScheduleDetail(searchConditions = [], EntityID = 1, returnComplianceScheduleDetailID = False, returnAgeGradeType = False, returnAgeGradeTypeCode = False, returnAgeGradeValue = False, returnAgeUnit = False, returnAgeUnitCode = False, returnComplianceScheduleDetailIDClonedFrom = False, returnCreatedTime = False, returnDoseCount = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ComplianceScheduleDetail in the district.

	This function returns a dataframe of every ComplianceScheduleDetail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryComplianceScheduleDetailBooster(searchConditions = [], EntityID = 1, returnComplianceScheduleDetailBoosterID = False, returnComplianceScheduleDetailBoosterIDClonedFrom = False, returnComplianceScheduleDetailID = False, returnCreatedTime = False, returnIntervalTime = False, returnIntervalTimeUnit = False, returnIntervalTimeUnitCode = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ComplianceScheduleDetailBooster in the district.

	This function returns a dataframe of every ComplianceScheduleDetailBooster in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetailBooster/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleDetailBooster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryComplianceScheduleRule(searchConditions = [], EntityID = 1, returnComplianceScheduleRuleID = False, returnCode = False, returnCodeDescription = False, returnComplianceScheduleID = False, returnCreatedTime = False, returnDescription = False, returnGracePeriodDays = False, returnModifiedTime = False, returnRule = False, returnRuleDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ComplianceScheduleRule in the district.

	This function returns a dataframe of every ComplianceScheduleRule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleRule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ComplianceScheduleRule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictGroup(searchConditions = [], EntityID = 1, returnConfigDistrictGroupID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUseNationalChartForBodyMassIndexPercentile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrictYear(searchConditions = [], EntityID = 1, returnConfigDistrictYearID = False, returnAgeEffectiveDate = False, returnComplianceYearStart = False, returnComplianceYearStartCode = False, returnConditionalIndicator = False, returnCreatedTime = False, returnDisplayLotNumber = False, returnDistrictID = False, returnInComplianceIndicator = False, returnLiveVaccineSameMakeupGraceDays = False, returnModifiedTime = False, returnOutOfComplianceIndicator = False, returnProvisionalCalculationType = False, returnProvisionalCalculationTypeCode = False, returnProvisionalDays = False, returnProvisionalIndicator = False, returnSchoolYearID = False, returnUseComplianceDate = False, returnUseLiveVaccineInterval = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationComplianceIsProcessing = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntity(searchConditions = [], EntityID = 1, returnConfigEntityID = False, returnCreatedTime = False, returnEntityID = False, returnLocationIDMedicationQuickEntryDefault = False, returnModifiedTime = False, returnStaffIDMedicationQuickEntryDefault = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ConfigEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalComment(searchConditions = [], EntityID = 1, returnDentalCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalComment in the district.

	This function returns a dataframe of every DentalComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalGuardianNotification(searchConditions = [], EntityID = 1, returnDentalGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalGuardianNotification in the district.

	This function returns a dataframe of every DentalGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalGuardianResponse(searchConditions = [], EntityID = 1, returnDentalGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalGuardianResponse in the district.

	This function returns a dataframe of every DentalGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalReferralReason(searchConditions = [], EntityID = 1, returnDentalReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalReferralReason in the district.

	This function returns a dataframe of every DentalReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalReferralResult(searchConditions = [], EntityID = 1, returnDentalReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalReferralResult in the district.

	This function returns a dataframe of every DentalReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalScreening(searchConditions = [], EntityID = 1, returnDentalScreeningID = False, returnCreatedTime = False, returnDentalScreeningResultID = False, returnDentalTreatmentID = False, returnDistrictID = False, returnEntityIDEnrolledIn = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalScreening in the district.

	This function returns a dataframe of every DentalScreening in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreening/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreening/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalScreeningComment(searchConditions = [], EntityID = 1, returnDentalScreeningCommentID = False, returnCreatedTime = False, returnDentalCommentID = False, returnDentalScreeningID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalScreeningComment in the district.

	This function returns a dataframe of every DentalScreeningComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalScreeningNote(searchConditions = [], EntityID = 1, returnDentalScreeningNoteID = False, returnCreatedTime = False, returnDentalScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalScreeningNote in the district.

	This function returns a dataframe of every DentalScreeningNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalScreeningReferral(searchConditions = [], EntityID = 1, returnDentalScreeningReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnDentalGuardianNotificationID = False, returnDentalGuardianResponseID = False, returnDentalReferralReasonID = False, returnDentalReferralResultID = False, returnDentalScreeningID = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnIsVoid = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalScreeningReferral in the district.

	This function returns a dataframe of every DentalScreeningReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalScreeningResult(searchConditions = [], EntityID = 1, returnDentalScreeningResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalScreeningResult in the district.

	This function returns a dataframe of every DentalScreeningResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalScreeningSecuredNote(searchConditions = [], EntityID = 1, returnDentalScreeningSecuredNoteID = False, returnCreatedTime = False, returnDentalScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalScreeningSecuredNote in the district.

	This function returns a dataframe of every DentalScreeningSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDentalTreatment(searchConditions = [], EntityID = 1, returnDentalTreatmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DentalTreatment in the district.

	This function returns a dataframe of every DentalTreatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalTreatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DentalTreatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesCareLog(searchConditions = [], EntityID = 1, returnDiabetesCareLogID = False, returnBloodGlucose = False, returnBloodGlucoseInsulin = False, returnBloodGlucoseNotChecked = False, returnBodyPartID = False, returnCarbIntake = False, returnCreatedTime = False, returnDiabetesKetoneResultID = False, returnDistrictID = False, returnFoodInsulin = False, returnInsulinDeliveryType = False, returnInsulinDeliveryTypeCode = False, returnInsulinDose = False, returnInsulinOnBoard = False, returnIsVoid = False, returnMedicationDosageUnitID = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnNotificationMethodID = False, returnParentNotified = False, returnRecheckBloodGlucose = False, returnRecheckTime = False, returnSchoolYearID = False, returnScreeningTime = False, returnScreeningTimeDate = False, returnScreeningTimeTime = False, returnTreatmentDescriptionsListDisplay = False, returnTreatments = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesCareLog in the district.

	This function returns a dataframe of every DiabetesCareLog in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesCareLogNote(searchConditions = [], EntityID = 1, returnDiabetesCareLogNoteID = False, returnCreatedTime = False, returnDiabetesCareLogID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesCareLogNote in the district.

	This function returns a dataframe of every DiabetesCareLogNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesCareLogReferral(searchConditions = [], EntityID = 1, returnDiabetesCareLogReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnDiabetesCareLogID = False, returnDiabetesGuardianNotificationID = False, returnDiabetesGuardianResponseID = False, returnDiabetesReferralReasonID = False, returnDiabetesReferralResultID = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnIsVoid = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesCareLogReferral in the district.

	This function returns a dataframe of every DiabetesCareLogReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesCareLogSecuredNote(searchConditions = [], EntityID = 1, returnDiabetesCareLogSecuredNoteID = False, returnCreatedTime = False, returnDiabetesCareLogID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesCareLogSecuredNote in the district.

	This function returns a dataframe of every DiabetesCareLogSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesCareLogTreatment(searchConditions = [], EntityID = 1, returnDiabetesCareLogTreatmentID = False, returnCreatedTime = False, returnDiabetesCareLogID = False, returnDiabetesTreatmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesCareLogTreatment in the district.

	This function returns a dataframe of every DiabetesCareLogTreatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogTreatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesCareLogTreatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesGuardianNotification(searchConditions = [], EntityID = 1, returnDiabetesGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesGuardianNotification in the district.

	This function returns a dataframe of every DiabetesGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesGuardianResponse(searchConditions = [], EntityID = 1, returnDiabetesGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesGuardianResponse in the district.

	This function returns a dataframe of every DiabetesGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesKetoneResult(searchConditions = [], EntityID = 1, returnDiabetesKetoneResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesKetoneResult in the district.

	This function returns a dataframe of every DiabetesKetoneResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesKetoneResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesKetoneResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesReferralReason(searchConditions = [], EntityID = 1, returnDiabetesReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesReferralReason in the district.

	This function returns a dataframe of every DiabetesReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesReferralResult(searchConditions = [], EntityID = 1, returnDiabetesReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesReferralResult in the district.

	This function returns a dataframe of every DiabetesReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDiabetesTreatment(searchConditions = [], EntityID = 1, returnDiabetesTreatmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DiabetesTreatment in the district.

	This function returns a dataframe of every DiabetesTreatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesTreatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DiabetesTreatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDoseInterval(searchConditions = [], EntityID = 1, returnDoseIntervalID = False, returnAgeHighMonths = False, returnAgeLowMonths = False, returnComplianceScheduleDetailID = False, returnCreatedTime = False, returnDoseHigh = False, returnDoseIntervalIDClonedFrom = False, returnDoseLow = False, returnGracePeriodDays = False, returnIntervalType = False, returnIntervalTypeCode = False, returnIntervalValue = False, returnIsConditionalInterval = False, returnIsDistrictDefined = False, returnIsRequired = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineDateHigh = False, returnVaccineDateLow = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DoseInterval in the district.

	This function returns a dataframe of every DoseInterval in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseInterval/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseInterval/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDoseMinimumAge(searchConditions = [], EntityID = 1, returnDoseMinimumAgeID = False, returnAge = False, returnAgeUnitType = False, returnAgeUnitTypeCode = False, returnComplianceScheduleDetailID = False, returnCreatedTime = False, returnDoseMinimumAgeIDClonedFrom = False, returnDoseNumber = False, returnGracePeriodType = False, returnGracePeriodTypeCode = False, returnGraceValue = False, returnIsDistrictDefined = False, returnIsRequired = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineDateHigh = False, returnVaccineDateLow = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DoseMinimumAge in the district.

	This function returns a dataframe of every DoseMinimumAge in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseMinimumAge/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/DoseMinimumAge/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHealthAttachment(searchConditions = [], EntityID = 1, returnHealthAttachmentID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HealthAttachment in the district.

	This function returns a dataframe of every HealthAttachment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthAttachment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthAttachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHealthCondition(searchConditions = [], EntityID = 1, returnHealthConditionID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnIsSecuredIndicator = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationGroupContraindication = False, returnVaccinationGroupContraindicationCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HealthCondition in the district.

	This function returns a dataframe of every HealthCondition in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthCondition/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthCondition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHealthConditionComment(searchConditions = [], EntityID = 1, returnHealthConditionCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HealthConditionComment in the district.

	This function returns a dataframe of every HealthConditionComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHealthConditionTreatment(searchConditions = [], EntityID = 1, returnHealthConditionTreatmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HealthConditionTreatment in the district.

	This function returns a dataframe of every HealthConditionTreatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionTreatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthConditionTreatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHealthProfessional(searchConditions = [], EntityID = 1, returnHealthProfessionalID = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnHealthProfessionalTypeID = False, returnIsActive = False, returnIsDentist = False, returnIsPrimaryPhysician = False, returnModifiedTime = False, returnNameEmailIDDisplayEmail = False, returnNameID = False, returnNamePhoneIDDisplayPhone = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HealthProfessional in the district.

	This function returns a dataframe of every HealthProfessional in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessional/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessional/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHealthProfessionalType(searchConditions = [], EntityID = 1, returnHealthProfessionalTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HealthProfessionalType in the district.

	This function returns a dataframe of every HealthProfessionalType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessionalType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HealthProfessionalType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingComment(searchConditions = [], EntityID = 1, returnHearingCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingComment in the district.

	This function returns a dataframe of every HearingComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingDecibelLevel(searchConditions = [], EntityID = 1, returnHearingDecibelLevelID = False, returnCode = False, returnCreatedTime = False, returnDecibelLevel = False, returnDescription = False, returnDistrictID = False, returnHearingDecibelLevelDefaultID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingDecibelLevel in the district.

	This function returns a dataframe of every HearingDecibelLevel in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingDecibelLevelDefault(searchConditions = [], EntityID = 1, returnHearingDecibelLevelDefaultID = False, returnCode = False, returnCreatedTime = False, returnDecibelLevel = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingDecibelLevelDefault in the district.

	This function returns a dataframe of every HearingDecibelLevelDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevelDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingDecibelLevelDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingGuardianNotification(searchConditions = [], EntityID = 1, returnHearingGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingGuardianNotification in the district.

	This function returns a dataframe of every HearingGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingGuardianResponse(searchConditions = [], EntityID = 1, returnHearingGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingGuardianResponse in the district.

	This function returns a dataframe of every HearingGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingHertzLevel(searchConditions = [], EntityID = 1, returnHearingHertzLevelID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnHearingHertzLevelDefaultID = False, returnHertzLevel = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingHertzLevel in the district.

	This function returns a dataframe of every HearingHertzLevel in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingHertzLevelDefault(searchConditions = [], EntityID = 1, returnHearingHertzLevelDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnHertzLevel = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingHertzLevelDefault in the district.

	This function returns a dataframe of every HearingHertzLevelDefault in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevelDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingHertzLevelDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingObservation(searchConditions = [], EntityID = 1, returnHearingObservationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingObservation in the district.

	This function returns a dataframe of every HearingObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingReferralReason(searchConditions = [], EntityID = 1, returnHearingReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingReferralReason in the district.

	This function returns a dataframe of every HearingReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingReferralResult(searchConditions = [], EntityID = 1, returnHearingReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingReferralResult in the district.

	This function returns a dataframe of every HearingReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingScreening(searchConditions = [], EntityID = 1, returnHearingScreeningID = False, returnCombinedResult = False, returnCombinedResultCode = False, returnCreatedTime = False, returnDistrictID = False, returnEntityIDEnrolledIn = False, returnGroupPercentLossLeftEar = False, returnGroupPercentLossRightEar = False, returnHealthProfessionalIDExaminedBy = False, returnIndividualPercentLossLeftEar = False, returnIndividualPercentLossRightEar = False, returnIsKnownCase = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnObservationDescriptionsListDisplay = False, returnReScreen = False, returnResultLeftEar = False, returnResultLeftEarCode = False, returnResultMiddleEar = False, returnResultMiddleEarCode = False, returnResultRightEar = False, returnResultRightEarCode = False, returnSchoolYearID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingScreening in the district.

	This function returns a dataframe of every HearingScreening in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreening/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreening/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingScreeningComment(searchConditions = [], EntityID = 1, returnHearingScreeningCommentID = False, returnCreatedTime = False, returnHearingCommentID = False, returnHearingScreeningID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingScreeningComment in the district.

	This function returns a dataframe of every HearingScreeningComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingScreeningNote(searchConditions = [], EntityID = 1, returnHearingScreeningNoteID = False, returnCreatedTime = False, returnHearingScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingScreeningNote in the district.

	This function returns a dataframe of every HearingScreeningNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingScreeningObservation(searchConditions = [], EntityID = 1, returnHearingScreeningObservationID = False, returnCreatedTime = False, returnHearingObservationID = False, returnHearingScreeningID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingScreeningObservation in the district.

	This function returns a dataframe of every HearingScreeningObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingScreeningReferral(searchConditions = [], EntityID = 1, returnHearingScreeningReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnHearingGuardianNotificationID = False, returnHearingGuardianResponseID = False, returnHearingReferralReasonID = False, returnHearingReferralResultID = False, returnHearingScreeningID = False, returnIsVoid = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingScreeningReferral in the district.

	This function returns a dataframe of every HearingScreeningReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingScreeningSecuredNote(searchConditions = [], EntityID = 1, returnHearingScreeningSecuredNoteID = False, returnCreatedTime = False, returnHearingScreeningID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingScreeningSecuredNote in the district.

	This function returns a dataframe of every HearingScreeningSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryHearingScreeningThreshold(searchConditions = [], EntityID = 1, returnHearingScreeningThresholdID = False, returnCreatedTime = False, returnHearingDecibelLevelIDLeftEar = False, returnHearingDecibelLevelIDRightEar = False, returnHearingHertzLevelID = False, returnHearingScreeningID = False, returnLeftEarPassed = False, returnModifiedTime = False, returnRightEarPassed = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every HearingScreeningThreshold in the district.

	This function returns a dataframe of every HearingScreeningThreshold in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningThreshold/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/HearingScreeningThreshold/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjury(searchConditions = [], EntityID = 1, returnInjuryID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Injury in the district.

	This function returns a dataframe of every Injury in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Injury/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Injury/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrence(searchConditions = [], EntityID = 1, returnInjuryOccurrenceID = False, returnBodyParts = False, returnCreatedTime = False, returnDaysMissed = False, returnDistrictID = False, returnHealthProfessionalID = False, returnInjuryDateTime = False, returnInjuryDateTimeDate = False, returnInjuryDateTimeTime = False, returnIsImmediateCareRequired = False, returnIsVoid = False, returnLocationID = False, returnModifiedTime = False, returnNameID = False, returnNameIDReportedBy = False, returnNameIDRespondedBy = False, returnReportFileDate = False, returnSchoolID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrence in the district.

	This function returns a dataframe of every InjuryOccurrence in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrence/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrence/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceBodyPart(searchConditions = [], EntityID = 1, returnInjuryOccurrenceBodyPartID = False, returnBodyPartID = False, returnCreatedTime = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceBodyPart in the district.

	This function returns a dataframe of every InjuryOccurrenceBodyPart in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPart/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPart/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceBodyPartInjury(searchConditions = [], EntityID = 1, returnInjuryOccurrenceBodyPartInjuryID = False, returnCreatedTime = False, returnInjuryID = False, returnInjuryOccurrenceBodyPartID = False, returnModifiedTime = False, returnTreatments = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceBodyPartInjury in the district.

	This function returns a dataframe of every InjuryOccurrenceBodyPartInjury in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjury/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjury/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceBodyPartInjuryTreatment(searchConditions = [], EntityID = 1, returnInjuryOccurrenceBodyPartInjuryTreatmentID = False, returnCreatedTime = False, returnInjuryOccurrenceBodyPartInjuryID = False, returnModifiedTime = False, returnTreatmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceBodyPartInjuryTreatment in the district.

	This function returns a dataframe of every InjuryOccurrenceBodyPartInjuryTreatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjuryTreatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceBodyPartInjuryTreatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceComment(searchConditions = [], EntityID = 1, returnInjuryOccurrenceCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceComment in the district.

	This function returns a dataframe of every InjuryOccurrenceComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceGuardianNotification(searchConditions = [], EntityID = 1, returnInjuryOccurrenceGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceGuardianNotification in the district.

	This function returns a dataframe of every InjuryOccurrenceGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceGuardianResponse(searchConditions = [], EntityID = 1, returnInjuryOccurrenceGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceGuardianResponse in the district.

	This function returns a dataframe of every InjuryOccurrenceGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceInjuryOccurrenceComment(searchConditions = [], EntityID = 1, returnInjuryOccurrenceInjuryOccurrenceCommentID = False, returnCreatedTime = False, returnInjuryOccurrenceCommentID = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceInjuryOccurrenceComment in the district.

	This function returns a dataframe of every InjuryOccurrenceInjuryOccurrenceComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceInjuryOccurrenceComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceInjuryOccurrenceComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceNote(searchConditions = [], EntityID = 1, returnInjuryOccurrenceNoteID = False, returnCreatedTime = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceNote in the district.

	This function returns a dataframe of every InjuryOccurrenceNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceReferral(searchConditions = [], EntityID = 1, returnInjuryOccurrenceReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnInjuryOccurrenceGuardianNotificationID = False, returnInjuryOccurrenceGuardianResponseID = False, returnInjuryOccurrenceID = False, returnInjuryOccurrenceReferralReasonID = False, returnInjuryOccurrenceReferralResultID = False, returnIsVoid = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceReferral in the district.

	This function returns a dataframe of every InjuryOccurrenceReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceReferralReason(searchConditions = [], EntityID = 1, returnInjuryOccurrenceReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceReferralReason in the district.

	This function returns a dataframe of every InjuryOccurrenceReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceReferralResult(searchConditions = [], EntityID = 1, returnInjuryOccurrenceReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceReferralResult in the district.

	This function returns a dataframe of every InjuryOccurrenceReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryInjuryOccurrenceSecuredNote(searchConditions = [], EntityID = 1, returnInjuryOccurrenceSecuredNoteID = False, returnCreatedTime = False, returnInjuryOccurrenceID = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every InjuryOccurrenceSecuredNote in the district.

	This function returns a dataframe of every InjuryOccurrenceSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/InjuryOccurrenceSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryLocation(searchConditions = [], EntityID = 1, returnLocationID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Location in the district.

	This function returns a dataframe of every Location in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Location/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Location/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMedication(searchConditions = [], EntityID = 1, returnMedicationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Medication in the district.

	This function returns a dataframe of every Medication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Medication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Medication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMedicationClassification(searchConditions = [], EntityID = 1, returnMedicationClassificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MedicationClassification in the district.

	This function returns a dataframe of every MedicationClassification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMedicationClassificationMedication(searchConditions = [], EntityID = 1, returnMedicationClassificationMedicationID = False, returnCreatedTime = False, returnMedicationClassificationID = False, returnMedicationID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MedicationClassificationMedication in the district.

	This function returns a dataframe of every MedicationClassificationMedication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassificationMedication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationClassificationMedication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMedicationComment(searchConditions = [], EntityID = 1, returnMedicationCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MedicationComment in the district.

	This function returns a dataframe of every MedicationComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMedicationDosageUnit(searchConditions = [], EntityID = 1, returnMedicationDosageUnitID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MedicationDosageUnit in the district.

	This function returns a dataframe of every MedicationDosageUnit in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationDosageUnit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationDosageUnit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMedicationRoute(searchConditions = [], EntityID = 1, returnMedicationRouteID = False, returnCreatedTime = False, returnDescription = False, returnFDACode = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnNCIConceptCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MedicationRoute in the district.

	This function returns a dataframe of every MedicationRoute in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationRoute/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/MedicationRoute/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameMedication(searchConditions = [], EntityID = 1, returnNameMedicationID = False, returnAdministrationInstruction = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDistributionType = False, returnDistributionTypeCode = False, returnEndDate = False, returnEndStatus = False, returnEndStatusCode = False, returnHealthProfessionalIDPrescribedBy = False, returnIsVoid = False, returnMaxDosesPerDay = False, returnMedicationDosageUnitID = False, returnMedicationID = False, returnMedicationRouteID = False, returnModifiedTime = False, returnNameID = False, returnOriginalEndDate = False, returnReceivedDoctorForm = False, returnReceivedParentReleaseForm = False, returnReceivedVerbalParentPermission = False, returnStartDate = False, returnUnitsPerDoseHigh = False, returnUnitsPerDoseLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameMedication in the district.

	This function returns a dataframe of every NameMedication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameMedicationComment(searchConditions = [], EntityID = 1, returnNameMedicationCommentID = False, returnCreatedTime = False, returnMedicationCommentID = False, returnModifiedTime = False, returnNameMedicationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameMedicationComment in the district.

	This function returns a dataframe of every NameMedicationComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameMedicationNote(searchConditions = [], EntityID = 1, returnNameMedicationNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameMedicationID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameMedicationNote in the district.

	This function returns a dataframe of every NameMedicationNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameMedicationPrescription(searchConditions = [], EntityID = 1, returnNameMedicationPrescriptionID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsVoid = False, returnModifiedTime = False, returnNameIDPharmacy = False, returnNameMedicationID = False, returnPrescriptionNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameMedicationPrescription in the district.

	This function returns a dataframe of every NameMedicationPrescription in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationPrescription/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationPrescription/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameMedicationSchedule(searchConditions = [], EntityID = 1, returnNameMedicationScheduleID = False, returnCreatedTime = False, returnEndDate = False, returnFriday = False, returnIsAdministrableAsOfSpecifiedDate = False, returnIsAdministrableAsOfToday = False, returnIsVoid = False, returnModifiedTime = False, returnMonday = False, returnNameMedicationID = False, returnSaturday = False, returnScheduledAdministrationTime = False, returnScheduledAdministrationTimeTime = False, returnStartDate = False, returnSunday = False, returnThursday = False, returnTuesday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnWednesday = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameMedicationSchedule in the district.

	This function returns a dataframe of every NameMedicationSchedule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameMedicationSecuredNote(searchConditions = [], EntityID = 1, returnNameMedicationSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameMedicationID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameMedicationSecuredNote in the district.

	This function returns a dataframe of every NameMedicationSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameMedicationSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisit(searchConditions = [], EntityID = 1, returnNameOfficeVisitID = False, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnHealthProfessionalIDExaminedBy = False, returnIsNameOfficeVisitToday = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitDispositionsListDisplay = False, returnNameOfficeVisitReasonsListDisplay = False, returnNameOfficeVisitTreatmentsListDisplay = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisit in the district.

	This function returns a dataframe of every NameOfficeVisit in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitDisposition(searchConditions = [], EntityID = 1, returnNameOfficeVisitDispositionID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnOfficeVisitDispositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitDisposition in the district.

	This function returns a dataframe of every NameOfficeVisitDisposition in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitDisposition/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitDisposition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitNote(searchConditions = [], EntityID = 1, returnNameOfficeVisitNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitNote in the district.

	This function returns a dataframe of every NameOfficeVisitNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitNotification(searchConditions = [], EntityID = 1, returnNameOfficeVisitNotificationID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitNotification in the district.

	This function returns a dataframe of every NameOfficeVisitNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitReason(searchConditions = [], EntityID = 1, returnNameOfficeVisitReasonID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnOfficeVisitReasonID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitReason in the district.

	This function returns a dataframe of every NameOfficeVisitReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitReferral(searchConditions = [], EntityID = 1, returnNameOfficeVisitReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnIsVoid = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnOfficeVisitGuardianResponseID = False, returnOfficeVisitReferralReasonID = False, returnOfficeVisitReferralResultID = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitReferral in the district.

	This function returns a dataframe of every NameOfficeVisitReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitSecuredNote(searchConditions = [], EntityID = 1, returnNameOfficeVisitSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitSecuredNote in the district.

	This function returns a dataframe of every NameOfficeVisitSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitTimeTransaction(searchConditions = [], EntityID = 1, returnNameOfficeVisitTimeTransactionID = False, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitTimeTransaction in the district.

	This function returns a dataframe of every NameOfficeVisitTimeTransaction in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameOfficeVisitTreatment(searchConditions = [], EntityID = 1, returnNameOfficeVisitTreatmentID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnTreatmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameOfficeVisitTreatment in the district.

	This function returns a dataframe of every NameOfficeVisitTreatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTreatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameOfficeVisitTreatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameProcedure(searchConditions = [], EntityID = 1, returnNameProcedureID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCanCreateOccurrenceAsOfDate = False, returnCanCreateScheduleAsOfDate = False, returnCreatedTime = False, returnDistributionType = False, returnDistributionTypeCode = False, returnEndDate = False, returnGreatestProcedureOccurrenceDate = False, returnGreatestProcedureScheduleEndDate = False, returnIsActiveAsOfDate = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnProcedureID = False, returnProcedureInstruction = False, returnReceivedParentReleaseForm = False, returnReceivedPhysicianDocumentation = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameProcedure in the district.

	This function returns a dataframe of every NameProcedure in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedure/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedure/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameProcedureNote(searchConditions = [], EntityID = 1, returnNameProcedureNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameProcedureID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameProcedureNote in the district.

	This function returns a dataframe of every NameProcedureNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameProcedureOccurrence(searchConditions = [], EntityID = 1, returnNameProcedureOccurrenceID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFromOfficeVisit = False, returnIsVoid = False, returnModifiedTime = False, returnNameIDPerformedByOverride = False, returnNameOfficeVisitID = False, returnNameProcedureID = False, returnNameProcedureScheduleDayID = False, returnNote = False, returnNotPerformedReasonID = False, returnOccurrenceDate = False, returnOccurrenceType = False, returnOccurrenceTypeCode = False, returnProcedureInstructionDisplay = False, returnScheduledStartTimeOverride = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameProcedureOccurrence in the district.

	This function returns a dataframe of every NameProcedureOccurrence in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureOccurrence/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureOccurrence/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameProcedureSchedule(searchConditions = [], EntityID = 1, returnNameProcedureScheduleID = False, returnCalendarID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasEndedAsOfDate = False, returnIncludePartialDays = False, returnIsVoid = False, returnLastCompletedOccurrenceDate = False, returnModifiedTime = False, returnNameIDPerformedBy = False, returnNameProcedureID = False, returnProcedureInstructionOverride = False, returnRepeatsBiWeekly = False, returnScheduledStartTime = False, returnStartDate = False, returnUseProcedureInstructionOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameProcedureSchedule in the district.

	This function returns a dataframe of every NameProcedureSchedule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameProcedureScheduleDay(searchConditions = [], EntityID = 1, returnNameProcedureScheduleDayID = False, returnCreatedTime = False, returnDay = False, returnDayOfTheWeek = False, returnIsActive = False, returnModifiedTime = False, returnNameIDPerformedByOverride = False, returnNameProcedureScheduleID = False, returnScheduledStartTimeOverride = False, returnStartTime = False, returnUsePerformedByNameOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseScheduledStartTimeOverride = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameProcedureScheduleDay in the district.

	This function returns a dataframe of every NameProcedureScheduleDay in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureScheduleDay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureScheduleDay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNameProcedureSecuredNote(searchConditions = [], EntityID = 1, returnNameProcedureSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameProcedureID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NameProcedureSecuredNote in the district.

	This function returns a dataframe of every NameProcedureSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NameProcedureSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotificationMethod(searchConditions = [], EntityID = 1, returnNotificationMethodID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotificationMethod in the district.

	This function returns a dataframe of every NotificationMethod in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNotPerformedReason(searchConditions = [], EntityID = 1, returnNotPerformedReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NotPerformedReason in the district.

	This function returns a dataframe of every NotPerformedReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotPerformedReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/NotPerformedReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitComment(searchConditions = [], EntityID = 1, returnOfficeVisitCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitComment in the district.

	This function returns a dataframe of every OfficeVisitComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitDisposition(searchConditions = [], EntityID = 1, returnOfficeVisitDispositionID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitDisposition in the district.

	This function returns a dataframe of every OfficeVisitDisposition in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitDisposition/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitDisposition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitGuardianResponse(searchConditions = [], EntityID = 1, returnOfficeVisitGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitGuardianResponse in the district.

	This function returns a dataframe of every OfficeVisitGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitReason(searchConditions = [], EntityID = 1, returnOfficeVisitReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitReason in the district.

	This function returns a dataframe of every OfficeVisitReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitReferralReason(searchConditions = [], EntityID = 1, returnOfficeVisitReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitReferralReason in the district.

	This function returns a dataframe of every OfficeVisitReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOfficeVisitReferralResult(searchConditions = [], EntityID = 1, returnOfficeVisitReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OfficeVisitReferralResult in the district.

	This function returns a dataframe of every OfficeVisitReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/OfficeVisitReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalComment(searchConditions = [], EntityID = 1, returnPhysicalCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalComment in the district.

	This function returns a dataframe of every PhysicalComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalGuardianNotification(searchConditions = [], EntityID = 1, returnPhysicalGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalGuardianNotification in the district.

	This function returns a dataframe of every PhysicalGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalGuardianResponse(searchConditions = [], EntityID = 1, returnPhysicalGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalGuardianResponse in the district.

	This function returns a dataframe of every PhysicalGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalObservation(searchConditions = [], EntityID = 1, returnPhysicalObservationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalObservation in the district.

	This function returns a dataframe of every PhysicalObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalReferralReason(searchConditions = [], EntityID = 1, returnPhysicalReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalReferralReason in the district.

	This function returns a dataframe of every PhysicalReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalReferralResult(searchConditions = [], EntityID = 1, returnPhysicalReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalReferralResult in the district.

	This function returns a dataframe of every PhysicalReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalScreening(searchConditions = [], EntityID = 1, returnPhysicalScreeningID = False, returnAtRiskForDiabetes = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnBodyMassIndex = False, returnBodyMassIndexPercentile = False, returnCreatedTime = False, returnDiabetesScreened = False, returnDisplayHeight = False, returnDistrictID = False, returnEntityIDEnrolledIn = False, returnFirstBloodPressureReading = False, returnHealthProfessionalIDExaminedBy = False, returnHeight = False, returnHeightFeet = False, returnHeightInches = False, returnIsVoid = False, returnModifiedTime = False, returnNameID = False, returnNameOfficeVisitID = False, returnSchoolYearID = False, returnScreeningDate = False, returnSecondBloodPressureReading = False, returnSportsPhysical = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, returnWeight = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalScreening in the district.

	This function returns a dataframe of every PhysicalScreening in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreening/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreening/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalScreeningComment(searchConditions = [], EntityID = 1, returnPhysicalScreeningCommentID = False, returnCreatedTime = False, returnModifiedTime = False, returnPhysicalCommentID = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalScreeningComment in the district.

	This function returns a dataframe of every PhysicalScreeningComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalScreeningNote(searchConditions = [], EntityID = 1, returnPhysicalScreeningNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalScreeningNote in the district.

	This function returns a dataframe of every PhysicalScreeningNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalScreeningObservation(searchConditions = [], EntityID = 1, returnPhysicalScreeningObservationID = False, returnCreatedTime = False, returnModifiedTime = False, returnPhysicalObservationID = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalScreeningObservation in the district.

	This function returns a dataframe of every PhysicalScreeningObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalScreeningReferral(searchConditions = [], EntityID = 1, returnPhysicalScreeningReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnIsVoid = False, returnModifiedTime = False, returnPhysicalGuardianNotificationID = False, returnPhysicalGuardianResponseID = False, returnPhysicalReferralReasonID = False, returnPhysicalReferralResultID = False, returnPhysicalScreeningID = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalScreeningReferral in the district.

	This function returns a dataframe of every PhysicalScreeningReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPhysicalScreeningSecuredNote(searchConditions = [], EntityID = 1, returnPhysicalScreeningSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnPhysicalScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PhysicalScreeningSecuredNote in the district.

	This function returns a dataframe of every PhysicalScreeningSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/PhysicalScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryProcedure(searchConditions = [], EntityID = 1, returnProcedureID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnTreatmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Procedure in the district.

	This function returns a dataframe of every Procedure in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Procedure/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Procedure/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisComment(searchConditions = [], EntityID = 1, returnScoliosisCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisComment in the district.

	This function returns a dataframe of every ScoliosisComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisGuardianNotification(searchConditions = [], EntityID = 1, returnScoliosisGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisGuardianNotification in the district.

	This function returns a dataframe of every ScoliosisGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisGuardianResponse(searchConditions = [], EntityID = 1, returnScoliosisGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisGuardianResponse in the district.

	This function returns a dataframe of every ScoliosisGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisObservation(searchConditions = [], EntityID = 1, returnScoliosisObservationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisObservation in the district.

	This function returns a dataframe of every ScoliosisObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisReferralReason(searchConditions = [], EntityID = 1, returnScoliosisReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisReferralReason in the district.

	This function returns a dataframe of every ScoliosisReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisReferralResult(searchConditions = [], EntityID = 1, returnScoliosisReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisReferralResult in the district.

	This function returns a dataframe of every ScoliosisReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisResult(searchConditions = [], EntityID = 1, returnScoliosisResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisResult in the district.

	This function returns a dataframe of every ScoliosisResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisScreening(searchConditions = [], EntityID = 1, returnScoliosisScreeningID = False, returnCreatedTime = False, returnDistrictID = False, returnEntityIDEnrolledIn = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnLatestScoliosisScreeningReferral = False, returnModifiedTime = False, returnNameID = False, returnObservationDescriptionsListDisplay = False, returnRescreen = False, returnSchoolYearID = False, returnScoliosisResultID = False, returnScoliosisTreatmentID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisScreening in the district.

	This function returns a dataframe of every ScoliosisScreening in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreening/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreening/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisScreeningComment(searchConditions = [], EntityID = 1, returnScoliosisScreeningCommentID = False, returnCreatedTime = False, returnModifiedTime = False, returnScoliosisCommentID = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisScreeningComment in the district.

	This function returns a dataframe of every ScoliosisScreeningComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisScreeningNote(searchConditions = [], EntityID = 1, returnScoliosisScreeningNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisScreeningNote in the district.

	This function returns a dataframe of every ScoliosisScreeningNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisScreeningObservation(searchConditions = [], EntityID = 1, returnScoliosisScreeningObservationID = False, returnCreatedTime = False, returnModifiedTime = False, returnScoliosisObservationID = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisScreeningObservation in the district.

	This function returns a dataframe of every ScoliosisScreeningObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisScreeningReferral(searchConditions = [], EntityID = 1, returnScoliosisScreeningReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnIsVoid = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnScoliosisGuardianNotificationID = False, returnScoliosisGuardianResponseID = False, returnScoliosisReferralReasonID = False, returnScoliosisReferralResultID = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisScreeningReferral in the district.

	This function returns a dataframe of every ScoliosisScreeningReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisScreeningSecuredNote(searchConditions = [], EntityID = 1, returnScoliosisScreeningSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnScoliosisScreeningID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisScreeningSecuredNote in the district.

	This function returns a dataframe of every ScoliosisScreeningSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryScoliosisTreatment(searchConditions = [], EntityID = 1, returnScoliosisTreatmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ScoliosisTreatment in the district.

	This function returns a dataframe of every ScoliosisTreatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisTreatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/ScoliosisTreatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentChildhoodIllness(searchConditions = [], EntityID = 1, returnStudentChildhoodIllnessID = False, returnAgeDiagnosed = False, returnChildhoodIllnessID = False, returnCreatedTime = False, returnDistrictID = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnModifiedTime = False, returnObservationDescriptionsListDisplay = False, returnSchoolYearID = False, returnScreeningDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentChildhoodIllness in the district.

	This function returns a dataframe of every StudentChildhoodIllness in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentChildhoodIllnessComment(searchConditions = [], EntityID = 1, returnStudentChildhoodIllnessCommentID = False, returnChildhoodIllnessCommentID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentChildhoodIllnessComment in the district.

	This function returns a dataframe of every StudentChildhoodIllnessComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentChildhoodIllnessNote(searchConditions = [], EntityID = 1, returnStudentChildhoodIllnessNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentChildhoodIllnessNote in the district.

	This function returns a dataframe of every StudentChildhoodIllnessNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentChildhoodIllnessObservation(searchConditions = [], EntityID = 1, returnStudentChildhoodIllnessObservationID = False, returnChildhoodIllnessObservationID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentChildhoodIllnessObservation in the district.

	This function returns a dataframe of every StudentChildhoodIllnessObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentChildhoodIllnessReferral(searchConditions = [], EntityID = 1, returnStudentChildhoodIllnessReferralID = False, returnChildhoodIllnessGuardianNotificationID = False, returnChildhoodIllnessGuardianResponseID = False, returnChildhoodIllnessReferralReasonID = False, returnChildhoodIllnessReferralResultID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnIsVoid = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentChildhoodIllnessReferral in the district.

	This function returns a dataframe of every StudentChildhoodIllnessReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentChildhoodIllnessSecuredNote(searchConditions = [], EntityID = 1, returnStudentChildhoodIllnessSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentChildhoodIllnessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentChildhoodIllnessSecuredNote in the district.

	This function returns a dataframe of every StudentChildhoodIllnessSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentChildhoodIllnessSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentHealthCondition(searchConditions = [], EntityID = 1, returnStudentHealthConditionID = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnHealthConditionID = False, returnHealthConditionTreatmentID = False, returnHealthProfessionalIDExaminedBy = False, returnIsActive = False, returnIsVoid = False, returnModifiedTime = False, returnOriginalEndDate = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentHealthCondition in the district.

	This function returns a dataframe of every StudentHealthCondition in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthCondition/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthCondition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentHealthConditionComment(searchConditions = [], EntityID = 1, returnStudentHealthConditionCommentID = False, returnCreatedTime = False, returnHealthConditionCommentID = False, returnModifiedTime = False, returnStudentHealthConditionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentHealthConditionComment in the district.

	This function returns a dataframe of every StudentHealthConditionComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentHealthConditionNote(searchConditions = [], EntityID = 1, returnStudentHealthConditionNoteID = False, returnCreatedTime = False, returnIsNoteEnteredByGuardian = False, returnModifiedTime = False, returnNote = False, returnNoteEnteredByType = False, returnNoteEnteredByTypeCode = False, returnNoteEnteredByTypeLabel = False, returnStudentHealthConditionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentHealthConditionNote in the district.

	This function returns a dataframe of every StudentHealthConditionNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentHealthConditionSecuredNote(searchConditions = [], EntityID = 1, returnStudentHealthConditionSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentHealthConditionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentHealthConditionSecuredNote in the district.

	This function returns a dataframe of every StudentHealthConditionSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentHealthConditionSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentIHP(searchConditions = [], EntityID = 1, returnStudentIHPID = False, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCreatedTime = False, returnEndDate = False, returnFormDescription = False, returnIsActive = False, returnIsVoid = False, returnModifiedTime = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentIHP in the district.

	This function returns a dataframe of every StudentIHP in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentIHP/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentIHP/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentVaccinationWaiver(searchConditions = [], EntityID = 1, returnStudentVaccinationWaiverID = False, returnClaimDate = False, returnCreatedTime = False, returnExpirationDate = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationWaiverID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentVaccinationWaiver in the district.

	This function returns a dataframe of every StudentVaccinationWaiver in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationWaiver/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentVaccinationYear(searchConditions = [], EntityID = 1, returnStudentVaccinationYearID = False, returnCalculatedGradeCode = False, returnCalculatedGradeNumeric = False, returnCreatedTime = False, returnEffectiveDate = False, returnModifiedTime = False, returnStudentID = False, returnStudentVaccineCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentVaccinationYear in the district.

	This function returns a dataframe of every StudentVaccinationYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentVaccinationYearStatus(searchConditions = [], EntityID = 1, returnStudentVaccinationYearStatusID = False, returnAllDoseDates = False, returnComplianceScheduleDetailID = False, returnComplianceStatus = False, returnCreatedTime = False, returnEndDate = False, returnInvalidDoseDates = False, returnIsConditional = False, returnIsInComplianceByVaccines = False, returnIsOutOfCompliance = False, returnIsOutOfComplianceConditionalDisplay = False, returnIsProvisional = False, returnModifiedTime = False, returnReasonConditional = False, returnReasonOutOfCompliance = False, returnStartDate = False, returnStudentChildhoodIllnessID = False, returnStudentID = False, returnStudentVaccinationWaiverID = False, returnStudentVaccinationYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleID = False, returnValidDoseDates = False, returnValidDoses = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentVaccinationYearStatus in the district.

	This function returns a dataframe of every StudentVaccinationYearStatus in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentVaccinationYearStatusStudentVaccine(searchConditions = [], EntityID = 1, returnStudentVaccinationYearStatusStudentVaccineID = False, returnCreatedTime = False, returnInvalidDoseReason = False, returnIsValidDose = False, returnModifiedTime = False, returnStudentVaccinationYearStatusID = False, returnStudentVaccineID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentVaccinationYearStatusStudentVaccine in the district.

	This function returns a dataframe of every StudentVaccinationYearStatusStudentVaccine in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatusStudentVaccine/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccinationYearStatusStudentVaccine/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentVaccine(searchConditions = [], EntityID = 1, returnStudentVaccineID = False, returnCreatedTime = False, returnDate = False, returnLotNumber = False, returnModifiedTime = False, returnStudentID = False, returnStudentVaccineDates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentVaccine in the district.

	This function returns a dataframe of every StudentVaccine in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccine/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccine/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentVaccineMaintenance(searchConditions = [], EntityID = 1, returnVaccineID = False, returnDate1 = False, returnDate2 = False, returnDate3 = False, returnDate4 = False, returnDate5 = False, returnDate6 = False, returnDate7 = False, returnHasExistingStudentVaccines = False, returnLotNumber1 = False, returnLotNumber2 = False, returnLotNumber3 = False, returnLotNumber4 = False, returnLotNumber5 = False, returnLotNumber6 = False, returnLotNumber7 = False, returnStudentID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentVaccineMaintenance in the district.

	This function returns a dataframe of every StudentVaccineMaintenance in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccineMaintenance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/StudentVaccineMaintenance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempAdministerNameMedication(searchConditions = [], EntityID = 1, returnTempAdministerNameMedicationID = False, returnAdministerNameMedicationID = False, returnAdministrationTime = False, returnCreatedTime = False, returnDosesAdministered = False, returnErrorMessage = False, returnMedicationCode = False, returnModifiedTime = False, returnName = False, returnNewDosesAdministered = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempAdministerNameMedication in the district.

	This function returns a dataframe of every TempAdministerNameMedication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempAdministerNameMedication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempAdministerNameMedication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameMedication(searchConditions = [], EntityID = 1, returnTempNameMedicationID = False, returnAdministrationInstruction = False, returnCode = False, returnCreatedTime = False, returnDistributionType = False, returnDistributionTypeCode = False, returnEndDate = False, returnEndStatusCode = False, returnErrorCount = False, returnFullNameLFM = False, returnHasErrors = False, returnHealthProfessionalIDPrescribedBy = False, returnMaxDosesPerDay = False, returnMedicationCode = False, returnMedicationCommentID = False, returnMedicationDosageUnitID = False, returnMedicationID = False, returnMedicationRouteID = False, returnModifiedTime = False, returnNameID = False, returnNameMedicationID = False, returnNewCode = False, returnNewMaxDosesPerDay = False, returnNewMedicationDosageUnitID = False, returnNewMedicationRouteID = False, returnNewRouteName = False, returnNewUnitsPerDoseHigh = False, returnNewUnitsPerDoseLow = False, returnNote = False, returnOrderType = False, returnOrderTypeCode = False, returnReceivedDoctorForm = False, returnReceivedParentReleaseForm = False, returnReceivedVerbalParentPermission = False, returnRouteName = False, returnStartDate = False, returnUnitsPerDoseHigh = False, returnUnitsPerDoseLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameMedication in the district.

	This function returns a dataframe of every TempNameMedication in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameMedication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameMedication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameMedicationErrorDetail(searchConditions = [], EntityID = 1, returnTempNameMedicationErrorDetailID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempNameMedicationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameMedicationErrorDetail in the district.

	This function returns a dataframe of every TempNameMedicationErrorDetail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameMedicationErrorDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameMedicationErrorDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameProcedureOccurrence(searchConditions = [], EntityID = 1, returnTempNameProcedureOccurrenceID = False, returnCreatedTime = False, returnDayOfTheWeek = False, returnErrorCount = False, returnHasErrors = False, returnModifiedTime = False, returnNameIDPerformedBy = False, returnNameProcedureOccurrenceID = False, returnNameScheduled = False, returnOccurrenceDate = False, returnOldNameIDPerformedBy = False, returnOldNameScheduled = False, returnOldStartTime = False, returnPendingStatus = False, returnSchedulingErrorMessage = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameProcedureOccurrence in the district.

	This function returns a dataframe of every TempNameProcedureOccurrence in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureOccurrence/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureOccurrence/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameProcedureOccurrenceErrorDetail(searchConditions = [], EntityID = 1, returnTempNameProcedureOccurrenceErrorDetailID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempNameProcedureOccurrenceID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameProcedureOccurrenceErrorDetail in the district.

	This function returns a dataframe of every TempNameProcedureOccurrenceErrorDetail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureOccurrenceErrorDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureOccurrenceErrorDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameProcedureScheduleDay(searchConditions = [], EntityID = 1, returnTempNameProcedureScheduleDayID = False, returnCreatedTime = False, returnDay = False, returnDayOfTheWeek = False, returnErrorCount = False, returnExistingIsActive = False, returnExistingNameIDPerformedByOverride = False, returnExistingScheduledStartTimeOverride = False, returnHasErrors = False, returnIsActive = False, returnModifiedTime = False, returnNameIDPerformedByOverride = False, returnNameProcedureScheduleDayID = False, returnScheduledStartTimeOverride = False, returnUseNamePerformedByOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseScheduledStartTimeOverride = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameProcedureScheduleDay in the district.

	This function returns a dataframe of every TempNameProcedureScheduleDay in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleDay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleDay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameProcedureScheduleDayErrorDetail(searchConditions = [], EntityID = 1, returnTempNameProcedureScheduleDayErrorDetailID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempNameProcedureScheduleDayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameProcedureScheduleDayErrorDetail in the district.

	This function returns a dataframe of every TempNameProcedureScheduleDayErrorDetail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleDayErrorDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleDayErrorDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameProcedureScheduleError(searchConditions = [], EntityID = 1, returnTempNameProcedureScheduleErrorID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnErrorCount = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameProcedureScheduleError in the district.

	This function returns a dataframe of every TempNameProcedureScheduleError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNameProcedureScheduleErrorDetail(searchConditions = [], EntityID = 1, returnTempNameProcedureScheduleErrorDetailID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempNameProcedureScheduleErrorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNameProcedureScheduleErrorDetail in the district.

	This function returns a dataframe of every TempNameProcedureScheduleErrorDetail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleErrorDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempNameProcedureScheduleErrorDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentChildhoodIllness(searchConditions = [], EntityID = 1, returnTempStudentChildhoodIllnessID = False, returnAgeDiagnosed = False, returnChildhoodIllnessCode = False, returnChildhoodIllnessDescription = False, returnCreatedTime = False, returnIsVoid = False, returnModifiedTime = False, returnNewChildhoodIllnessCode = False, returnNewChildhoodIllnessDescription = False, returnNewChildhoodIllnessID = False, returnSchoolYear = False, returnScreeningDate = False, returnStudentChildhoodIllnessID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentChildhoodIllness in the district.

	This function returns a dataframe of every TempStudentChildhoodIllness in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentVaccine(searchConditions = [], EntityID = 1, returnTempStudentVaccineID = False, returnCreatedTime = False, returnCVXCode = False, returnDate = False, returnIsDuplicate = False, returnModifiedTime = False, returnNewCVXCode = False, returnNewVaccineCode = False, returnNewVaccineID = False, returnStudentName = False, returnStudentVaccineID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccineCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentVaccine in the district.

	This function returns a dataframe of every TempStudentVaccine in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentVaccine/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/TempStudentVaccine/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTreatment(searchConditions = [], EntityID = 1, returnTreatmentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Treatment in the district.

	This function returns a dataframe of every Treatment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Treatment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Treatment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccination(searchConditions = [], EntityID = 1, returnVaccinationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedByDistrict = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationWaiverCountsForCompliance = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Vaccination in the district.

	This function returns a dataframe of every Vaccination in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccinationChildhoodIllness(searchConditions = [], EntityID = 1, returnVaccinationChildhoodIllnessID = False, returnChildhoodIllnessID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VaccinationChildhoodIllness in the district.

	This function returns a dataframe of every VaccinationChildhoodIllness in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationChildhoodIllness/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccinationWaiver(searchConditions = [], EntityID = 1, returnVaccinationWaiverID = False, returnCountsForCompliance = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, returnWaiverID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VaccinationWaiver in the district.

	This function returns a dataframe of every VaccinationWaiver in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationWaiver/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccinationYear(searchConditions = [], EntityID = 1, returnVaccinationYearID = False, returnCreatedTime = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnProcessByType = False, returnProcessByTypeCode = False, returnRequiredAgeHigh = False, returnRequiredAgeHighDescription = False, returnRequiredAgeHighUnitType = False, returnRequiredAgeHighUnitTypeCode = False, returnRequiredAgeLow = False, returnRequiredAgeLowDescription = False, returnRequiredAgeLowUnitType = False, returnRequiredAgeLowUnitTypeCode = False, returnSchoolYearID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, returnVaccinationYearIDClonedFrom = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VaccinationYear in the district.

	This function returns a dataframe of every VaccinationYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccinationYearComplianceSchedule(searchConditions = [], EntityID = 1, returnVaccinationYearComplianceScheduleID = False, returnComplianceScheduleID = False, returnCreatedTime = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnRank = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleIDClonedFrom = False, returnVaccinationYearID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VaccinationYearComplianceSchedule in the district.

	This function returns a dataframe of every VaccinationYearComplianceSchedule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceSchedule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccinationYearComplianceScheduleRule(searchConditions = [], EntityID = 1, returnVaccinationYearComplianceScheduleRuleID = False, returnComplianceScheduleRuleID = False, returnCreatedTime = False, returnDoseIntervalID = False, returnModifiedTime = False, returnRuleType = False, returnRuleTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationYearComplianceScheduleID = False, returnVaccinationYearComplianceScheduleRuleIDClonedFrom = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VaccinationYearComplianceScheduleRule in the district.

	This function returns a dataframe of every VaccinationYearComplianceScheduleRule in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceScheduleRule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccinationYearComplianceScheduleRule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccine(searchConditions = [], EntityID = 1, returnVaccineID = False, returnCode = False, returnCPTCode = False, returnCPTCodeDescription = False, returnCPTDescription = False, returnCreatedTime = False, returnCVXCode = False, returnCVXFullName = False, returnCVXName = False, returnDescription = False, returnDisplayCode = False, returnDisplayDescription = False, returnDisplayOrder = False, returnIsLiveVaccine = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUsedByDistrict = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Vaccine in the district.

	This function returns a dataframe of every Vaccine in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccine/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Vaccine/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVaccineContent(searchConditions = [], EntityID = 1, returnVaccineContentID = False, returnCreatedTime = False, returnHighDate = False, returnIsDistrictDefined = False, returnLowDate = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVaccinationID = False, returnVaccineID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VaccineContent in the district.

	This function returns a dataframe of every VaccineContent in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccineContent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VaccineContent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionComment(searchConditions = [], EntityID = 1, returnVisionCommentID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionComment in the district.

	This function returns a dataframe of every VisionComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionCorrectiveLens(searchConditions = [], EntityID = 1, returnVisionCorrectiveLensID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionCorrectiveLens in the district.

	This function returns a dataframe of every VisionCorrectiveLens in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionCorrectiveLens/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionCorrectiveLens/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionGuardianNotification(searchConditions = [], EntityID = 1, returnVisionGuardianNotificationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionGuardianNotification in the district.

	This function returns a dataframe of every VisionGuardianNotification in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionGuardianResponse(searchConditions = [], EntityID = 1, returnVisionGuardianResponseID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionGuardianResponse in the district.

	This function returns a dataframe of every VisionGuardianResponse in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionObservation(searchConditions = [], EntityID = 1, returnVisionObservationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionObservation in the district.

	This function returns a dataframe of every VisionObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionReferralReason(searchConditions = [], EntityID = 1, returnVisionReferralReasonID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionReferralReason in the district.

	This function returns a dataframe of every VisionReferralReason in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralReason/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionReferralResult(searchConditions = [], EntityID = 1, returnVisionReferralResultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionReferralResult in the district.

	This function returns a dataframe of every VisionReferralResult in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionReferralResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionScreening(searchConditions = [], EntityID = 1, returnVisionScreeningID = False, returnColorBlindnessTestResult = False, returnColorBlindnessTestResultCode = False, returnCreatedTime = False, returnDistrictID = False, returnEntityIDEnrolledIn = False, returnFarVisionCorrectedLeftEye = False, returnFarVisionCorrectedRightEye = False, returnFarVisionScreeningDistance = False, returnFarVisionScreeningResult = False, returnFarVisionScreeningResultCode = False, returnFarVisionUncorrectedLeftEye = False, returnFarVisionUncorrectedRightEye = False, returnFittingDate = False, returnHealthProfessionalIDExaminedBy = False, returnIsVoid = False, returnModifiedTime = False, returnMuscleBalanceTestResult = False, returnMuscleBalanceTestResultCode = False, returnNameID = False, returnNameOfficeVisitID = False, returnNearVisionCorrectedLeftEye = False, returnNearVisionCorrectedRightEye = False, returnNearVisionScreeningDistance = False, returnNearVisionScreeningResult = False, returnNearVisionScreeningResultCode = False, returnNearVisionUncorrectedLeftEye = False, returnNearVisionUncorrectedRightEye = False, returnOverallScreeningResult = False, returnOverallScreeningResultCode = False, returnReScreen = False, returnSchoolYearID = False, returnScreeningDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVisionCorrectedPriorToExam = False, returnVisionCorrectiveLensID = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionScreening in the district.

	This function returns a dataframe of every VisionScreening in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreening/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreening/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionScreeningComment(searchConditions = [], EntityID = 1, returnVisionScreeningCommentID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionCommentID = False, returnVisionScreeningID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionScreeningComment in the district.

	This function returns a dataframe of every VisionScreeningComment in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningComment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionScreeningNote(searchConditions = [], EntityID = 1, returnVisionScreeningNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionScreeningID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionScreeningNote in the district.

	This function returns a dataframe of every VisionScreeningNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionScreeningObservation(searchConditions = [], EntityID = 1, returnVisionScreeningObservationID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionObservationID = False, returnVisionScreeningID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionScreeningObservation in the district.

	This function returns a dataframe of every VisionScreeningObservation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningObservation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionScreeningReferral(searchConditions = [], EntityID = 1, returnVisionScreeningReferralID = False, returnCompletionDate = False, returnCreatedTime = False, returnHealthProfessionalIDReferredBy = False, returnHealthProfessionalIDReferredTo = False, returnIsVoid = False, returnModifiedTime = False, returnReferralCompleted = False, returnReferralDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDVoidedBy = False, returnVisionGuardianNotificationID = False, returnVisionGuardianResponseID = False, returnVisionReferralReasonID = False, returnVisionReferralResultID = False, returnVisionScreeningID = False, returnVoidedTime = False, returnVoidNote = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionScreeningReferral in the district.

	This function returns a dataframe of every VisionScreeningReferral in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningReferral/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVisionScreeningSecuredNote(searchConditions = [], EntityID = 1, returnVisionScreeningSecuredNoteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVisionScreeningID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VisionScreeningSecuredNote in the district.

	This function returns a dataframe of every VisionScreeningSecuredNote in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VisionScreeningSecuredNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryVitalSign(searchConditions = [], EntityID = 1, returnVitalSignID = False, returnBloodPressureDiastolic = False, returnBloodPressureSystolic = False, returnCreatedTime = False, returnModifiedTime = False, returnNameOfficeVisitID = False, returnPhysicalScreeningID = False, returnPulseRate = False, returnRespiration = False, returnSaturationOfPeripheralOxygen = False, returnTemperature = False, returnTimeTaken = False, returnTimeTakenDate = False, returnTimeTakenTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every VitalSign in the district.

	This function returns a dataframe of every VitalSign in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VitalSign/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/VitalSign/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryWaiver(searchConditions = [], EntityID = 1, returnWaiverID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnExpirationType = False, returnExpirationTypeCode = False, returnExpireUnit = False, returnExpireUnitCode = False, returnExpireValue = False, returnIsActive = False, returnModifiedTime = False, returnRestrictVaccinations = False, returnUseInStateReporting = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaiverType = False, returnWaiverTypeCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Waiver in the district.

	This function returns a dataframe of every Waiver in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Waiver/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Health/Waiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)