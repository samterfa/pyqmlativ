# This module contains Transportation functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryBus(searchConditions = [], EntityID = 1, returnBusID = False, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnHasHistoricBusRoutes = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Bus in the district.

	This function returns a dataframe of every Bus in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBusRoute(searchConditions = [], EntityID = 1, returnBusRouteID = False, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BusRoute in the district.

	This function returns a dataframe of every BusRoute in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryBusStop(searchConditions = [], EntityID = 1, returnBusStopID = False, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every BusStop in the district.

	This function returns a dataframe of every BusStop in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnTransportationImportFileLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentBusStop(searchConditions = [], EntityID = 1, returnStudentBusStopID = False, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentBusStop in the district.

	This function returns a dataframe of every StudentBusStop in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStudentTransportation(searchConditions = [], EntityID = 1, returnStudentTransportationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStateDistrictMNID = False, returnStudentID = False, returnStudentTransportationMNID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StudentTransportation in the district.

	This function returns a dataframe of every StudentTransportation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentBusStop(searchConditions = [], EntityID = 1, returnTempStudentBusStopID = False, returnBusStopArrivalTime = False, returnBusStopDescription = False, returnBusStopFullAddress = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStudentBusStopID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentBusStop in the district.

	This function returns a dataframe of every TempStudentBusStop in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentTransportation(searchConditions = [], EntityID = 1, returnTempStudentTransportationID = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStartDate = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentTransportationID = False, returnTransportationCategoryDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentTransportation in the district.

	This function returns a dataframe of every TempStudentTransportation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempTransportation(searchConditions = [], EntityID = 1, returnTempTransportationID = False, returnArrivalTime = False, returnBus = False, returnBusRoute = False, returnBusStop = False, returnBusStopAddress = False, returnCreatedTime = False, returnDays = False, returnDriver = False, returnExceptions = False, returnFirstName = False, returnGradeLevel = False, returnHasExceptions = False, returnLastName = False, returnModifiedTime = False, returnSchool = False, returnStopType = False, returnStudentAddress = False, returnStudentNumber = False, returnTransportationCategory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempTransportation in the district.

	This function returns a dataframe of every TempTransportation in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTransportationCategory(searchConditions = [], EntityID = 1, returnTransportationCategoryID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateTransportationCategoryCodeMNID = False, returnTransportationCategoryIDClonedFrom = False, returnTransportationCategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TransportationCategory in the district.

	This function returns a dataframe of every TransportationCategory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)