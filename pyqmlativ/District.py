# This module contains District functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryBuilding(searchConditions = [], EntityID = 1, returnBuildingID = False, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Building in the district.

	This function returns a dataframe of every Building in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryCalendarYear(searchConditions = [], EntityID = 1, returnCalendarYearID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every CalendarYear in the district.

	This function returns a dataframe of every CalendarYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigEntityYear(searchConditions = [], EntityID = 1, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDistrictGroup(searchConditions = [], EntityID = 1, returnDistrictGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DistrictGroup in the district.

	This function returns a dataframe of every DistrictGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDistrict(searchConditions = [], EntityID = 1, returnDistrictID = False, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnIsCurrentlySelected = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every District in the district.

	This function returns a dataframe of every District in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryDistrictSchoolYear(searchConditions = [], EntityID = 1, returnDistrictSchoolYearID = False, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every DistrictSchoolYear in the district.

	This function returns a dataframe of every DistrictSchoolYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityCloneDestination(searchConditions = [], EntityID = 1, returnEntityCloneDestinationID = False, returnCreatedTime = False, returnEntityCloneRunID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityCloneDestination in the district.

	This function returns a dataframe of every EntityCloneDestination in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityCloneError(searchConditions = [], EntityID = 1, returnEntityCloneErrorID = False, returnAttemptedOperation = False, returnAttemptedOperationCode = False, returnCreatedTime = False, returnEntityCloneSelectedObjectID = False, returnEntityIDTarget = False, returnMessage = False, returnModifiedTime = False, returnObjectJSON = False, returnSchoolYearIDTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityCloneError in the district.

	This function returns a dataframe of every EntityCloneError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityCloneRun(searchConditions = [], EntityID = 1, returnEntityCloneRunID = False, returnCreatedTime = False, returnEntityIDSource = False, returnMediaID = False, returnModifiedTime = False, returnSchoolYearIDSource = False, returnStatus = False, returnStatusCode = False, returnTargetEntities = False, returnTargetYears = False, returnTotalRecordsAdded = False, returnTotalRecordsDeleted = False, returnTotalRecordsErrored = False, returnTotalRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityCloneRun in the district.

	This function returns a dataframe of every EntityCloneRun in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityCloneSelectedObject(searchConditions = [], EntityID = 1, returnEntityCloneSelectedObjectID = False, returnCloneOrder = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnNumberOfRecordsAdded = False, returnNumberOfRecordsDeleted = False, returnNumberOfRecordsErrored = False, returnNumberOfRecordsExported = False, returnNumberOfRecordsUpdated = False, returnObjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityCloneSelectedObject in the district.

	This function returns a dataframe of every EntityCloneSelectedObject in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityCloneSelection(searchConditions = [], EntityID = 1, returnEntityCloneSelectionID = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnModuleID = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityCloneSelection in the district.

	This function returns a dataframe of every EntityCloneSelection in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityGroup(searchConditions = [], EntityID = 1, returnEntityGroupID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityGroup in the district.

	This function returns a dataframe of every EntityGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityGroupEntity(searchConditions = [], EntityID = 1, returnEntityGroupEntityID = False, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityGroupEntity in the district.

	This function returns a dataframe of every EntityGroupEntity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityGroupSetup(searchConditions = [], EntityID = 1, returnEntityGroupSetupID = False, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityGroupSetup in the district.

	This function returns a dataframe of every EntityGroupSetup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityGroupSetupEntity(searchConditions = [], EntityID = 1, returnEntityGroupSetupEntityID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityGroupSetupEntity in the district.

	This function returns a dataframe of every EntityGroupSetupEntity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityGroupSetupRun(searchConditions = [], EntityID = 1, returnEntityGroupSetupRunID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityGroupSetupRun in the district.

	This function returns a dataframe of every EntityGroupSetupRun in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntityGroupSetupRunDetail(searchConditions = [], EntityID = 1, returnEntityGroupSetupRunDetailID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every EntityGroupSetupRunDetail in the district.

	This function returns a dataframe of every EntityGroupSetupRunDetail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryEntity(searchConditions = [], EntityID = 1, returnEntityID = False, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIlluminateEndGradeLevel = False, returnIlluminateSiteType = False, returnIlluminateSiteTypeCalculated = False, returnIlluminateSiteTypeOverride = False, returnIlluminateStartGradeLevel = False, returnIsCurrentlySelected = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Entity in the district.

	This function returns a dataframe of every Entity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryFiscalYear(searchConditions = [], EntityID = 1, returnFiscalYearID = False, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDynamicRelationshipID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every FiscalYear in the district.

	This function returns a dataframe of every FiscalYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoom(searchConditions = [], EntityID = 1, returnRoomID = False, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSeatsAvailableForDateRangeAndDisplayPeriods = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Room in the district.

	This function returns a dataframe of every Room in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryRoomType(searchConditions = [], EntityID = 1, returnRoomTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every RoomType in the district.

	This function returns a dataframe of every RoomType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySchoolYear(searchConditions = [], EntityID = 1, returnSchoolYearID = False, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnStudentAwardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SchoolYear in the district.

	This function returns a dataframe of every SchoolYear in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStateDistrictMN(searchConditions = [], EntityID = 1, returnStateDistrictMNID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StateDistrictMN in the district.

	This function returns a dataframe of every StateDistrictMN in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)