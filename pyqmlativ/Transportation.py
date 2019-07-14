# This module contains Transportation functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryBus(EntityID = 1, page = 1, pageSize = 100, returnBusID = True, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBus(BusID, EntityID = 1, returnBusID = True, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(BusID), verb = "get", return_params_list = return_params_list)

def modifyBus(BusID, EntityID = 1, setCapacity = None, setCode = None, setDescription = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnBusID = True, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(BusID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBus(EntityID = 1, setCapacity = None, setCode = None, setDescription = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnBusID = True, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBus(BusID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryBusRoute(EntityID = 1, page = 1, pageSize = 100, returnBusRouteID = True, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBusRoute(BusRouteID, EntityID = 1, returnBusRouteID = True, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(BusRouteID), verb = "get", return_params_list = return_params_list)

def modifyBusRoute(BusRouteID, EntityID = 1, setArrivalTime = None, setBusID = None, setBusRouteIDClonedFrom = None, setDepartureTime = None, setDescription = None, setMileage = None, setNameIDDriver = None, setRouteType = None, setRouteTypeCode = None, setSchoolYearID = None, setRelationships = None, returnBusRouteID = True, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(BusRouteID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBusRoute(EntityID = 1, setArrivalTime = None, setBusID = None, setBusRouteIDClonedFrom = None, setDepartureTime = None, setDescription = None, setMileage = None, setNameIDDriver = None, setRouteType = None, setRouteTypeCode = None, setSchoolYearID = None, setRelationships = None, returnBusRouteID = True, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBusRoute(BusRouteID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryBusStop(EntityID = 1, page = 1, pageSize = 100, returnBusStopID = True, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBusStop(BusStopID, EntityID = 1, returnBusStopID = True, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(BusStopID), verb = "get", return_params_list = return_params_list)

def modifyBusStop(BusStopID, EntityID = 1, setAddressID = None, setArrivalTime = None, setBusRouteID = None, setBusStopIDClonedFrom = None, setDepartureTime = None, setDescription = None, setDistrictID = None, setStopNumber = None, setRelationships = None, returnBusStopID = True, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(BusStopID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBusStop(EntityID = 1, setAddressID = None, setArrivalTime = None, setBusRouteID = None, setBusStopIDClonedFrom = None, setDepartureTime = None, setDescription = None, setDistrictID = None, setStopNumber = None, setRelationships = None, returnBusStopID = True, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBusStop(BusStopID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentBusStop(EntityID = 1, page = 1, pageSize = 100, returnStudentBusStopID = True, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentBusStop(StudentBusStopID, EntityID = 1, returnStudentBusStopID = True, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(StudentBusStopID), verb = "get", return_params_list = return_params_list)

def modifyStudentBusStop(StudentBusStopID, EntityID = 1, setBusStopID = None, setIsFriday = None, setIsMonday = None, setIsSaturday = None, setIsSunday = None, setIsThursday = None, setIsTuesday = None, setIsWednesday = None, setStopType = None, setStopTypeCode = None, setStudentID = None, setRelationships = None, returnStudentBusStopID = True, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(StudentBusStopID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentBusStop(EntityID = 1, setBusStopID = None, setIsFriday = None, setIsMonday = None, setIsSaturday = None, setIsSunday = None, setIsThursday = None, setIsTuesday = None, setIsWednesday = None, setStopType = None, setStopTypeCode = None, setStudentID = None, setRelationships = None, returnStudentBusStopID = True, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentBusStop(StudentBusStopID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentTransportation(EntityID = 1, page = 1, pageSize = 100, returnStudentTransportationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStudentID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentTransportation(StudentTransportationID, EntityID = 1, returnStudentTransportationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStudentID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(StudentTransportationID), verb = "get", return_params_list = return_params_list)

def modifyStudentTransportation(StudentTransportationID, EntityID = 1, setDistrictID = None, setEndDate = None, setMiles = None, setSchoolYearID = None, setStartDate = None, setStudentID = None, setTransportationCategoryID = None, setTransported = None, setRelationships = None, returnStudentTransportationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStudentID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(StudentTransportationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentTransportation(EntityID = 1, setDistrictID = None, setEndDate = None, setMiles = None, setSchoolYearID = None, setStartDate = None, setStudentID = None, setTransportationCategoryID = None, setTransported = None, setRelationships = None, returnStudentTransportationID = True, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStudentID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentTransportation(StudentTransportationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTransportationCategory(EntityID = 1, page = 1, pageSize = 100, returnTransportationCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTransportationCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTransportationCategory(TransportationCategoryID, EntityID = 1, returnTransportationCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTransportationCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(TransportationCategoryID), verb = "get", return_params_list = return_params_list)

def modifyTransportationCategory(TransportationCategoryID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setSchoolYearID = None, setTransportationCategoryIDClonedFrom = None, setRelationships = None, returnTransportationCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTransportationCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(TransportationCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTransportationCategory(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setSchoolYearID = None, setTransportationCategoryIDClonedFrom = None, setRelationships = None, returnTransportationCategoryID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTransportationCategoryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTransportationCategory(TransportationCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")