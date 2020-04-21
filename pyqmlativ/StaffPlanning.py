# This module contains StaffPlanning functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAssignmentTypePlanPositionDistributionSummary(searchConditions = [], EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every AssignmentTypePlanPositionDistributionSummary in the district.

	This function returns a dataframe of every AssignmentTypePlanPositionDistributionSummary in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBuildingPlanPositionDistributionSummary(searchConditions = [], EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BuildingPlanPositionDistributionSummary in the district.

	This function returns a dataframe of every BuildingPlanPositionDistributionSummary in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlan(searchConditions = [], EntityID = 1, returnPlanID = False, returnBudgetVersionAmount = False, returnBudgetVersionDifference = False, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnIsBudgeted = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanEmployee(searchConditions = [], EntityID = 1, returnPlanEmployeeID = False, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanEmployee in the district.

	This function returns a dataframe of every PlanEmployee in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanGroup(searchConditions = [], EntityID = 1, returnPlanGroupID = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanGroup in the district.

	This function returns a dataframe of every PlanGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanGroupAssignmentType(searchConditions = [], EntityID = 1, returnPlanGroupAssignmentTypeID = False, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanGroupAssignmentType in the district.

	This function returns a dataframe of every PlanGroupAssignmentType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanGroupBuilding(searchConditions = [], EntityID = 1, returnPlanGroupBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanGroupBuilding in the district.

	This function returns a dataframe of every PlanGroupBuilding in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanGroupClearance(searchConditions = [], EntityID = 1, returnPlanGroupClearanceID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanGroupClearance in the district.

	This function returns a dataframe of every PlanGroupClearance in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanGroupPositionType(searchConditions = [], EntityID = 1, returnPlanGroupPositionTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanGroupPositionType in the district.

	This function returns a dataframe of every PlanGroupPositionType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPosition(searchConditions = [], EntityID = 1, returnPlanPositionID = False, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPosition in the district.

	This function returns a dataframe of every PlanPosition in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionBenefit(searchConditions = [], EntityID = 1, returnPlanPositionBenefitID = False, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionBenefit in the district.

	This function returns a dataframe of every PlanPositionBenefit in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionDistribution(searchConditions = [], EntityID = 1, returnPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionDistribution in the district.

	This function returns a dataframe of every PlanPositionDistribution in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionDistributionAccountDistribution(searchConditions = [], EntityID = 1, returnPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionDistributionID = False, returnProratedDistributionPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionDistributionAccountDistribution in the district.

	This function returns a dataframe of every PlanPositionDistributionAccountDistribution in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionPay(searchConditions = [], EntityID = 1, returnPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionPay in the district.

	This function returns a dataframe of every PlanPositionPay in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionPayAccountCalculation(searchConditions = [], EntityID = 1, returnPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionPayAccountCalculation in the district.

	This function returns a dataframe of every PlanPositionPayAccountCalculation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionPayAccountDistribution(searchConditions = [], EntityID = 1, returnPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionPayAccountDistribution in the district.

	This function returns a dataframe of every PlanPositionPayAccountDistribution in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionPayBenefit(searchConditions = [], EntityID = 1, returnPlanPositionPayBenefitID = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionPayBenefit in the district.

	This function returns a dataframe of every PlanPositionPayBenefit in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionPayBenefitAccount(searchConditions = [], EntityID = 1, returnPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionPayBenefitAccount in the district.

	This function returns a dataframe of every PlanPositionPayBenefitAccount in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPlanPositionSupplement(searchConditions = [], EntityID = 1, returnPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PlanPositionSupplement in the district.

	This function returns a dataframe of every PlanPositionSupplement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryPositionTypePlanPositionDistributionSummary(searchConditions = [], EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every PositionTypePlanPositionDistributionSummary in the district.

	This function returns a dataframe of every PositionTypePlanPositionDistributionSummary in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempException(searchConditions = [], EntityID = 1, returnTempExceptionID = False, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempException in the district.

	This function returns a dataframe of every TempException in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionBenefit(searchConditions = [], EntityID = 1, returnTempPlanPositionBenefitID = False, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionBenefit in the district.

	This function returns a dataframe of every TempPlanPositionBenefit in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionDistribution(searchConditions = [], EntityID = 1, returnTempPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionDistribution in the district.

	This function returns a dataframe of every TempPlanPositionDistribution in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionDistributionAccountDistribution(searchConditions = [], EntityID = 1, returnTempPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionDistributionAccountDistribution in the district.

	This function returns a dataframe of every TempPlanPositionDistributionAccountDistribution in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionEmployee(searchConditions = [], EntityID = 1, returnTempPlanPositionEmployeeID = False, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorCount = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCode = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionEmployee in the district.

	This function returns a dataframe of every TempPlanPositionEmployee in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionException(searchConditions = [], EntityID = 1, returnTempPlanPositionExceptionID = False, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionException in the district.

	This function returns a dataframe of every TempPlanPositionException in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionPay(searchConditions = [], EntityID = 1, returnTempPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionPay in the district.

	This function returns a dataframe of every TempPlanPositionPay in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionPayAccountCalculation(searchConditions = [], EntityID = 1, returnTempPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionPayAccountCalculation in the district.

	This function returns a dataframe of every TempPlanPositionPayAccountCalculation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionPayAccountDistribution(searchConditions = [], EntityID = 1, returnTempPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionPayAccountDistribution in the district.

	This function returns a dataframe of every TempPlanPositionPayAccountDistribution in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionPayBenefit(searchConditions = [], EntityID = 1, returnTempPlanPositionPayBenefitID = False, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionPayBenefit in the district.

	This function returns a dataframe of every TempPlanPositionPayBenefit in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionPayBenefitAccount(searchConditions = [], EntityID = 1, returnTempPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionPayBenefitAccount in the district.

	This function returns a dataframe of every TempPlanPositionPayBenefitAccount in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempPlanPositionSupplement(searchConditions = [], EntityID = 1, returnTempPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempPlanPositionSupplement in the district.

	This function returns a dataframe of every TempPlanPositionSupplement in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)