# This module contains Attendance functions.

#from .Utilities import make_request

import pandas as pd

def getEveryAttendancePeriod(EntityID = 1, page = 1, pageSize = 100, returnAttendancePeriodID = True, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAttendancePeriod(AttendancePeriodID, EntityID = 1, returnAttendancePeriodID = True, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyAttendancePeriod(AttendancePeriodID, EntityID = 1, setAttendancePeriodIDClonedFrom = None, setCode = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setUseTeacherEntryCutOffTime = None, setRelationships = None, returnAttendancePeriodID = True, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createAttendancePeriod(EntityID = 1, setAttendancePeriodIDClonedFrom = None, setCode = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setUseTeacherEntryCutOffTime = None, setRelationships = None, returnAttendancePeriodID = True, returnAttendancePeriodIDClonedFrom = False, returnAttendancePeriodIDClonedTo = False, returnCode = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTeacherEntryCutOffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteAttendancePeriod(AttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

	return(response)