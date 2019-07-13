# This module contains Attendance functions.

from .Utilities import make_request

import pandas as pd

import json

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

def getEveryAttendancePeriodConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnAttendancePeriodConfigEntityGroupYearID = True, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1, returnAttendancePeriodConfigEntityGroupYearID = True, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1, setAttendancePeriodConfigEntityGroupYearIDClonedFrom = None, setAttendancePeriodID = None, setConfigEntityGroupYearID = None, setEntityGroupKey = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutoffNumberOfMinutesAfter = None, setTeacherEntryCutoffTime = None, setTeacherEntryCutoffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutoffTime = None, setRelationships = None, returnAttendancePeriodConfigEntityGroupYearID = True, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createAttendancePeriodConfigEntityGroupYear(EntityID = 1, setAttendancePeriodConfigEntityGroupYearIDClonedFrom = None, setAttendancePeriodID = None, setConfigEntityGroupYearID = None, setEntityGroupKey = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutoffNumberOfMinutesAfter = None, setTeacherEntryCutoffTime = None, setTeacherEntryCutoffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutoffTime = None, setRelationships = None, returnAttendancePeriodConfigEntityGroupYearID = True, returnAttendancePeriodConfigEntityGroupYearIDClonedFrom = False, returnAttendancePeriodID = False, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutoffNumberOfMinutesAfter = False, returnTeacherEntryCutoffTime = False, returnTeacherEntryCutoffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutoffTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteAttendancePeriodConfigEntityGroupYear(AttendancePeriodConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriodConfigEntityGroupYear/" + str(AttendancePeriodConfigEntityGroupYearID), verb = "delete")

	return(response)

def getEveryAttendanceReason(EntityID = 1, page = 1, pageSize = 100, returnAttendanceReasonID = True, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAttendanceReason(AttendanceReasonID, EntityID = 1, returnAttendanceReasonID = True, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyAttendanceReason(AttendanceReasonID, EntityID = 1, setAttendanceReasonIDClonedFrom = None, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setTeacherEntryID = None, setRelationships = None, returnAttendanceReasonID = True, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createAttendanceReason(EntityID = 1, setAttendanceReasonIDClonedFrom = None, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setTeacherEntryID = None, setRelationships = None, returnAttendanceReasonID = True, returnAttendanceReasonIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteAttendanceReason(AttendanceReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReason/" + str(AttendanceReasonID), verb = "delete")

	return(response)

def getEveryAttendanceReportRunHistory(EntityID = 1, page = 1, pageSize = 100, returnAttendanceReportRunHistoryID = True, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRunDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1, returnAttendanceReportRunHistoryID = True, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRunDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1, setDate = None, setEntityID = None, setFilterType = None, setFilterTypeCode = None, setGracePeriod = None, setIsActive = None, setRunDescription = None, setSchoolYearID = None, setRelationships = None, returnAttendanceReportRunHistoryID = True, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRunDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createAttendanceReportRunHistory(EntityID = 1, setDate = None, setEntityID = None, setFilterType = None, setFilterTypeCode = None, setGracePeriod = None, setIsActive = None, setRunDescription = None, setSchoolYearID = None, setRelationships = None, returnAttendanceReportRunHistoryID = True, returnCountType = False, returnCreatedTime = False, returnDate = False, returnEntityID = False, returnFilterType = False, returnFilterTypeCode = False, returnGracePeriod = False, returnIsActive = False, returnModifiedTime = False, returnParameterData = False, returnParameterDescription = False, returnRunDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteAttendanceReportRunHistory(AttendanceReportRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistory/" + str(AttendanceReportRunHistoryID), verb = "delete")

	return(response)

def getEveryAttendanceReportRunHistoryThresholdResetRange(EntityID = 1, page = 1, pageSize = 100, returnAttendanceReportRunHistoryThresholdResetRangeID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1, returnAttendanceReportRunHistoryThresholdResetRangeID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1, setAttendanceReportRunHistoryID = None, setThresholdResetRangeID = None, setRelationships = None, returnAttendanceReportRunHistoryThresholdResetRangeID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createAttendanceReportRunHistoryThresholdResetRange(EntityID = 1, setAttendanceReportRunHistoryID = None, setThresholdResetRangeID = None, setRelationships = None, returnAttendanceReportRunHistoryThresholdResetRangeID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteAttendanceReportRunHistoryThresholdResetRange(AttendanceReportRunHistoryThresholdResetRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceReportRunHistoryThresholdResetRange/" + str(AttendanceReportRunHistoryThresholdResetRangeID), verb = "delete")

	return(response)

def getEveryAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnAttendanceTermID = True, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAttendanceTerm(AttendanceTermID, EntityID = 1, returnAttendanceTermID = True, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyAttendanceTerm(AttendanceTermID, EntityID = 1, setAttendanceTermIDClonedFrom = None, setCalendarID = None, setCode = None, setEndDate = None, setStartDate = None, setRelationships = None, returnAttendanceTermID = True, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createAttendanceTerm(EntityID = 1, setAttendanceTermIDClonedFrom = None, setCalendarID = None, setCode = None, setEndDate = None, setStartDate = None, setRelationships = None, returnAttendanceTermID = True, returnAttendanceTermIDClonedFrom = False, returnCalendarID = False, returnCode = False, returnCreatedTime = False, returnDaysInTerm = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteAttendanceTerm(AttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceTerm/" + str(AttendanceTermID), verb = "delete")

	return(response)

def getEveryAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnAttendanceTypeID = True, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAttendanceType(AttendanceTypeID, EntityID = 1, returnAttendanceTypeID = True, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyAttendanceType(AttendanceTypeID, EntityID = 1, setAttendanceTypeIDClonedFrom = None, setCategory = None, setCategoryCode = None, setCategoryDescription = None, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIncludeInClassCounts = None, setIncludeInSpecialClassCounts = None, setIncludeInTotals = None, setIsTruant = None, setSchoolYearID = None, setShowOnGradesheetAssignments = None, setTeacherEntryID = None, setRelationships = None, returnAttendanceTypeID = True, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createAttendanceType(EntityID = 1, setAttendanceTypeIDClonedFrom = None, setCategory = None, setCategoryCode = None, setCategoryDescription = None, setCode = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setIncludeInClassCounts = None, setIncludeInSpecialClassCounts = None, setIncludeInTotals = None, setIsTruant = None, setSchoolYearID = None, setShowOnGradesheetAssignments = None, setTeacherEntryID = None, setRelationships = None, returnAttendanceTypeID = True, returnAttendanceTypeIDClonedFrom = False, returnAttendanceTypeMNID = False, returnCategory = False, returnCategoryCode = False, returnCategoryDescription = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeInClassCounts = False, returnIncludeInSpecialClassCounts = False, returnIncludeInTotals = False, returnIsTruant = False, returnModifiedTime = False, returnSchoolYearID = False, returnShowOnGradesheetAssignments = False, returnTeacherEntryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteAttendanceType(AttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendanceType/" + str(AttendanceTypeID), verb = "delete")

	return(response)

def getEveryBellSchedule(EntityID = 1, page = 1, pageSize = 100, returnBellScheduleID = True, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getBellSchedule(BellScheduleID, EntityID = 1, returnBellScheduleID = True, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyBellSchedule(BellScheduleID, EntityID = 1, setBellScheduleIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setIsDefault = None, setSchoolYearID = None, setRelationships = None, returnBellScheduleID = True, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createBellSchedule(EntityID = 1, setBellScheduleIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setIsDefault = None, setSchoolYearID = None, setRelationships = None, returnBellScheduleID = True, returnBellScheduleIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteBellSchedule(BellScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedule/" + str(BellScheduleID), verb = "delete")

	return(response)

def getEveryBellScheduleGroup(EntityID = 1, page = 1, pageSize = 100, returnBellScheduleGroupID = True, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getBellScheduleGroup(BellScheduleGroupID, EntityID = 1, returnBellScheduleGroupID = True, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyBellScheduleGroup(BellScheduleGroupID, EntityID = 1, setBellScheduleGroupIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setIsDefault = None, setSchoolYearID = None, setRelationships = None, returnBellScheduleGroupID = True, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createBellScheduleGroup(EntityID = 1, setBellScheduleGroupIDClonedFrom = None, setCode = None, setDescription = None, setEntityID = None, setIsDefault = None, setSchoolYearID = None, setRelationships = None, returnBellScheduleGroupID = True, returnAttendancePeriodIDAsOfDate = False, returnBellScheduleGroupIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteBellScheduleGroup(BellScheduleGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroup/" + str(BellScheduleGroupID), verb = "delete")

	return(response)

def getEveryBellScheduleGroupBellSchedule(EntityID = 1, page = 1, pageSize = 100, returnBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1, returnBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1, setBellScheduleGroupID = None, setBellScheduleID = None, setRelationships = None, returnBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createBellScheduleGroupBellSchedule(EntityID = 1, setBellScheduleGroupID = None, setBellScheduleID = None, setRelationships = None, returnBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupID = False, returnBellScheduleID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteBellScheduleGroupBellSchedule(BellScheduleGroupBellScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellScheduleGroupBellSchedule/" + str(BellScheduleGroupBellScheduleID), verb = "delete")

	return(response)

def getEveryBellSchedulingPeriod(EntityID = 1, page = 1, pageSize = 100, returnBellSchedulingPeriodID = True, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1, returnBellSchedulingPeriodID = True, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1, setBellScheduleID = None, setBellSchedulingPeriodIDClonedFrom = None, setEndTime = None, setSchedulingPeriodID = None, setStartTime = None, setRelationships = None, returnBellSchedulingPeriodID = True, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createBellSchedulingPeriod(EntityID = 1, setBellScheduleID = None, setBellSchedulingPeriodIDClonedFrom = None, setEndTime = None, setSchedulingPeriodID = None, setStartTime = None, setRelationships = None, returnBellSchedulingPeriodID = True, returnBellScheduleID = False, returnBellSchedulingPeriodIDClonedFrom = False, returnCreatedTime = False, returnEndTime = False, returnEndTimeWithOverride = False, returnLengthInMinutes = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnStartTimeWithOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteBellSchedulingPeriod(BellSchedulingPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/BellSchedulingPeriod/" + str(BellSchedulingPeriodID), verb = "delete")

	return(response)

def getEveryCalendarDay(EntityID = 1, page = 1, pageSize = 100, returnCalendarDayID = True, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarDay(CalendarDayID, EntityID = 1, returnCalendarDayID = True, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendarDay(CalendarDayID, EntityID = 1, setBellScheduleID = None, setCalendarID = None, setComment = None, setCountAs = None, setDate = None, setDayRotationID = None, setRelationships = None, returnCalendarDayID = True, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendarDay(EntityID = 1, setBellScheduleID = None, setCalendarID = None, setComment = None, setCountAs = None, setDate = None, setDayRotationID = None, setRelationships = None, returnCalendarDayID = True, returnAttendanceTerm = False, returnBellScheduleGroupSummary = False, returnBellScheduleID = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDateWithDayOfWeekAbbreviated = False, returnDayOfTheWeek = False, returnDayOfTheWeekNumber = False, returnDayRotationID = False, returnModifiedTime = False, returnNumberOfCalendarDayEvents = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendarDay(CalendarDayID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDay/" + str(CalendarDayID), verb = "delete")

	return(response)

def getEveryCalendarDayBellScheduleGroupBellSchedule(EntityID = 1, page = 1, pageSize = 100, returnCalendarDayBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1, returnCalendarDayBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupID = None, setCalendarDayID = None, setRelationships = None, returnCalendarDayBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendarDayBellScheduleGroupBellSchedule(EntityID = 1, setBellScheduleGroupBellScheduleID = None, setBellScheduleGroupID = None, setCalendarDayID = None, setRelationships = None, returnCalendarDayBellScheduleGroupBellScheduleID = True, returnBellScheduleGroupBellScheduleID = False, returnBellScheduleGroupID = False, returnCalendarDayID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendarDayBellScheduleGroupBellSchedule(CalendarDayBellScheduleGroupBellScheduleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayBellScheduleGroupBellSchedule/" + str(CalendarDayBellScheduleGroupBellScheduleID), verb = "delete")

	return(response)

def getEveryCalendarDayCalendarEvent(EntityID = 1, page = 1, pageSize = 100, returnCalendarDayCalendarEventID = True, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1, returnCalendarDayCalendarEventID = True, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1, setCalendarDayID = None, setCalendarEventID = None, setRelationships = None, returnCalendarDayCalendarEventID = True, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendarDayCalendarEvent(EntityID = 1, setCalendarDayID = None, setCalendarEventID = None, setRelationships = None, returnCalendarDayCalendarEventID = True, returnCalendarDayID = False, returnCalendarEventID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendarDayCalendarEvent(CalendarDayCalendarEventID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayCalendarEvent/" + str(CalendarDayCalendarEventID), verb = "delete")

	return(response)

def getEveryCalendarDayDisplayPeriodOverride(EntityID = 1, page = 1, pageSize = 100, returnCalendarDayDisplayPeriodOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1, returnCalendarDayDisplayPeriodOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1, setCalendarDayID = None, setDisplayPeriodID = None, setLengthMinutes = None, setRemovePeriod = None, setRelationships = None, returnCalendarDayDisplayPeriodOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendarDayDisplayPeriodOverride(EntityID = 1, setCalendarDayID = None, setDisplayPeriodID = None, setLengthMinutes = None, setRemovePeriod = None, setRelationships = None, returnCalendarDayDisplayPeriodOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnLengthMinutes = False, returnModifiedTime = False, returnRemovePeriod = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendarDayDisplayPeriodOverride(CalendarDayDisplayPeriodOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDayDisplayPeriodOverride/" + str(CalendarDayDisplayPeriodOverrideID), verb = "delete")

	return(response)

def getEveryCalendarDaySchedulingPeriodTimesOverride(EntityID = 1, page = 1, pageSize = 100, returnCalendarDaySchedulingPeriodTimesOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1, returnCalendarDaySchedulingPeriodTimesOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1, setCalendarDayID = None, setEndTime = None, setSchedulingPeriodID = None, setStartTime = None, setRelationships = None, returnCalendarDaySchedulingPeriodTimesOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendarDaySchedulingPeriodTimesOverride(EntityID = 1, setCalendarDayID = None, setEndTime = None, setSchedulingPeriodID = None, setStartTime = None, setRelationships = None, returnCalendarDaySchedulingPeriodTimesOverrideID = True, returnCalendarDayID = False, returnCreatedTime = False, returnDurationInMinutes = False, returnEndTime = False, returnModifiedTime = False, returnSchedulingPeriodID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendarDaySchedulingPeriodTimesOverride(CalendarDaySchedulingPeriodTimesOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDaySchedulingPeriodTimesOverride/" + str(CalendarDaySchedulingPeriodTimesOverrideID), verb = "delete")

	return(response)

def getEveryCalendarDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1, returnCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1, setCalendarDisplayPeriodIDClonedFrom = None, setCalendarID = None, setDisplayPeriodID = None, setIncludeInClassCounts = None, setIncludeInTotalCounts = None, setTakeAttendance = None, setRelationships = None, returnCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendarDisplayPeriod(EntityID = 1, setCalendarDisplayPeriodIDClonedFrom = None, setCalendarID = None, setDisplayPeriodID = None, setIncludeInClassCounts = None, setIncludeInTotalCounts = None, setTakeAttendance = None, setRelationships = None, returnCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDClonedFrom = False, returnCalendarID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnIncludeInClassCounts = False, returnIncludeInTotalCounts = False, returnModifiedTime = False, returnTakeAttendance = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendarDisplayPeriod(CalendarDisplayPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarDisplayPeriod/" + str(CalendarDisplayPeriodID), verb = "delete")

	return(response)

def getEveryCalendarEvent(EntityID = 1, page = 1, pageSize = 100, returnCalendarEventID = True, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendarEvent(CalendarEventID, EntityID = 1, returnCalendarEventID = True, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendarEvent(CalendarEventID, EntityID = 1, setCalendarEventIDClonedFrom = None, setCode = None, setDescription = None, setEdFiCalendarEventID = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCalendarEventID = True, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendarEvent(EntityID = 1, setCalendarEventIDClonedFrom = None, setCode = None, setDescription = None, setEdFiCalendarEventID = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCalendarEventID = True, returnCalendarEventIDClonedFrom = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiCalendarEventID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendarEvent(CalendarEventID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CalendarEvent/" + str(CalendarEventID), verb = "delete")

	return(response)

def getEveryCalendar(EntityID = 1, page = 1, pageSize = 100, returnCalendarID = True, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCalendar(CalendarID, EntityID = 1, returnCalendarID = True, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCalendar(CalendarID, EntityID = 1, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCalendarIDClonedFrom = None, setCode = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setMCCCAcademicYearImportID = None, setMCCCCalendarImportID = None, setSchoolYearID = None, setStartDate = None, setZeroDayHighPeriodCount = None, setRelationships = None, returnCalendarID = True, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCalendar(EntityID = 1, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCalendarIDClonedFrom = None, setCode = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setMCCCAcademicYearImportID = None, setMCCCCalendarImportID = None, setSchoolYearID = None, setStartDate = None, setZeroDayHighPeriodCount = None, setRelationships = None, returnCalendarID = True, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCalendarIDClonedFrom = False, returnCalendarIDClonedTo = False, returnCalendarMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnMCCCAcademicYearImportID = False, returnMCCCCalendarImportID = False, returnModifiedTime = False, returnNorthEastSemesterReportData = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCalendar(CalendarID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/Calendar/" + str(CalendarID), verb = "delete")

	return(response)

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = True, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setAttendanceReasonIDTardyDefault = None, setAttendanceTypeIDTardyDefault = None, setConfigEntityGroupYearIDClonedFrom = None, setEnableInOutTime = None, setEntityGroupKey = None, setEntityID = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setIncludeTardyCountOnLetter = None, setMultiPeriodClassCountMethod = None, setMultiPeriodClassCountMethodCode = None, setPresentBackgroundColor = None, setPresentBackgroundColorHex = None, setPresentBackgroundColorRgba = None, setRestrictTeacherAttendanceUpdates = None, setSchoolYearID = None, setSpecialClassCountsLabel = None, setTardyDefaultComment = None, setTardyKioskTardySlipTitle = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutOffNumberOfMinutesAfter = None, setTeacherEntryCutOffTime = None, setTeacherEntryCutOffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutOffTime = None, setUseInOutTimeForCalculations = None, setUseMarkAllStudentsPresentOnTile = None, setUseSpecialClassCounts = None, setUseTardyCalculator = None, setUseTardyKiosk = None, setUseTeacherPerfectAttendanceConfirmation = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createConfigEntityGroupYear(EntityID = 1, setAttendanceReasonIDTardyDefault = None, setAttendanceTypeIDTardyDefault = None, setConfigEntityGroupYearIDClonedFrom = None, setEnableInOutTime = None, setEntityGroupKey = None, setEntityID = None, setIncludeGradeLevelOnLetter = None, setIncludeParentNameAndOrPhoneNumberOnLetter = None, setIncludeSchoolOrCampusOnLetter = None, setIncludeSignatureLineForOfficeOnLetter = None, setIncludeSignatureLineForParentOnLetter = None, setIncludeSignatureLineForStudentOnLetter = None, setIncludeStudentNameAndOrNumberOnLetter = None, setIncludeTardyCountOnLetter = None, setMultiPeriodClassCountMethod = None, setMultiPeriodClassCountMethodCode = None, setPresentBackgroundColor = None, setPresentBackgroundColorHex = None, setPresentBackgroundColorRgba = None, setRestrictTeacherAttendanceUpdates = None, setSchoolYearID = None, setSpecialClassCountsLabel = None, setTardyDefaultComment = None, setTardyKioskTardySlipTitle = None, setTeacherEntryCutoffDuration = None, setTeacherEntryCutOffNumberOfMinutesAfter = None, setTeacherEntryCutOffTime = None, setTeacherEntryCutOffTimeCode = None, setTeacherEntryCutoffWindowEndTime = None, setTeacherEntryCutoffWindowStartTime = None, setTeacherEntrySpecificCutOffTime = None, setUseInOutTimeForCalculations = None, setUseMarkAllStudentsPresentOnTile = None, setUseSpecialClassCounts = None, setUseTardyCalculator = None, setUseTardyKiosk = None, setUseTeacherPerfectAttendanceConfirmation = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnAttendanceReasonIDTardyDefault = False, returnAttendanceTypeIDTardyDefault = False, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnEnableInOutTime = False, returnEntityGroupKey = False, returnEntityID = False, returnIncludeGradeLevelOnLetter = False, returnIncludeParentNameAndOrPhoneNumberOnLetter = False, returnIncludeSchoolOrCampusOnLetter = False, returnIncludeSignatureLineForOfficeOnLetter = False, returnIncludeSignatureLineForParentOnLetter = False, returnIncludeSignatureLineForStudentOnLetter = False, returnIncludeStudentNameAndOrNumberOnLetter = False, returnIncludeTardyCountOnLetter = False, returnModifiedTime = False, returnMultiPeriodClassCountMethod = False, returnMultiPeriodClassCountMethodCode = False, returnPresentBackgroundColor = False, returnPresentBackgroundColorHex = False, returnPresentBackgroundColorRgba = False, returnRestrictTeacherAttendanceUpdates = False, returnSchoolYearID = False, returnSpecialClassCountsLabel = False, returnTardyDefaultComment = False, returnTardyKioskTardySlipTitle = False, returnTeacherEntryCutoffDuration = False, returnTeacherEntryCutOffNumberOfMinutesAfter = False, returnTeacherEntryCutOffTime = False, returnTeacherEntryCutOffTimeCode = False, returnTeacherEntryCutoffWindowEndTime = False, returnTeacherEntryCutoffWindowStartTime = False, returnTeacherEntrySpecificCutOffTime = False, returnUseInOutTimeForCalculations = False, returnUseMarkAllStudentsPresentOnTile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSpecialClassCounts = False, returnUseTardyCalculator = False, returnUseTardyKiosk = False, returnUseTeacherPerfectAttendanceConfirmation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "delete")

	return(response)

def getEveryCrossEntityAttendanceReason(EntityID = 1, page = 1, pageSize = 100, returnCrossEntityAttendanceReasonID = True, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1, returnCrossEntityAttendanceReasonID = True, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1, setAttendanceReasonIDFrom = None, setAttendanceReasonIDTo = None, setEntityIDTo = None, setSchoolYearID = None, setRelationships = None, returnCrossEntityAttendanceReasonID = True, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCrossEntityAttendanceReason(EntityID = 1, setAttendanceReasonIDFrom = None, setAttendanceReasonIDTo = None, setEntityIDTo = None, setSchoolYearID = None, setRelationships = None, returnCrossEntityAttendanceReasonID = True, returnAttendanceReasonIDFrom = False, returnAttendanceReasonIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCrossEntityAttendanceReason(CrossEntityAttendanceReasonID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceReason/" + str(CrossEntityAttendanceReasonID), verb = "delete")

	return(response)

def getEveryCrossEntityAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnCrossEntityAttendanceTypeID = True, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1, returnCrossEntityAttendanceTypeID = True, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1, setAttendanceTypeIDFrom = None, setAttendanceTypeIDTo = None, setEntityIDTo = None, setSchoolYearID = None, setRelationships = None, returnCrossEntityAttendanceTypeID = True, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCrossEntityAttendanceType(EntityID = 1, setAttendanceTypeIDFrom = None, setAttendanceTypeIDTo = None, setEntityIDTo = None, setSchoolYearID = None, setRelationships = None, returnCrossEntityAttendanceTypeID = True, returnAttendanceTypeIDFrom = False, returnAttendanceTypeIDTo = False, returnCreatedTime = False, returnEntityIDTo = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCrossEntityAttendanceType(CrossEntityAttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityAttendanceType/" + str(CrossEntityAttendanceTypeID), verb = "delete")

	return(response)

def getEveryCrossEntityCalendarDisplayPeriod(EntityID = 1, page = 1, pageSize = 100, returnCrossEntityCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1, returnCrossEntityCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1, setCalendarDisplayPeriodIDFrom = None, setCalendarDisplayPeriodIDTo = None, setIsAutoCreated = None, setRelationships = None, returnCrossEntityCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createCrossEntityCalendarDisplayPeriod(EntityID = 1, setCalendarDisplayPeriodIDFrom = None, setCalendarDisplayPeriodIDTo = None, setIsAutoCreated = None, setRelationships = None, returnCrossEntityCalendarDisplayPeriodID = True, returnCalendarDisplayPeriodIDFrom = False, returnCalendarDisplayPeriodIDTo = False, returnCreatedTime = False, returnIsAutoCreated = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteCrossEntityCalendarDisplayPeriod(CrossEntityCalendarDisplayPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/CrossEntityCalendarDisplayPeriod/" + str(CrossEntityCalendarDisplayPeriodID), verb = "delete")

	return(response)

def getEveryDailySectionAttendance(EntityID = 1, page = 1, pageSize = 100, returnDailySectionAttendanceID = True, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDailySectionAttendance(DailySectionAttendanceID, EntityID = 1, returnDailySectionAttendanceID = True, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyDailySectionAttendance(DailySectionAttendanceID, EntityID = 1, setAttendancePeriodID = None, setCalendarDayID = None, setMeetID = None, setRelationships = None, returnDailySectionAttendanceID = True, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createDailySectionAttendance(EntityID = 1, setAttendancePeriodID = None, setCalendarDayID = None, setMeetID = None, setRelationships = None, returnDailySectionAttendanceID = True, returnAttendancePeriodID = False, returnCalendarDayID = False, returnCreatedTime = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteDailySectionAttendance(DailySectionAttendanceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DailySectionAttendance/" + str(DailySectionAttendanceID), verb = "delete")

	return(response)

def getEveryDayRotationPattern(EntityID = 1, page = 1, pageSize = 100, returnDayRotationPatternID = True, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDayRotationPattern(DayRotationPatternID, EntityID = 1, returnDayRotationPatternID = True, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyDayRotationPattern(DayRotationPatternID, EntityID = 1, setDayNumber = None, setDayRotationID = None, setDayRotationPatternIDClonedFrom = None, setEntityGroupKey = None, setRelationships = None, returnDayRotationPatternID = True, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createDayRotationPattern(EntityID = 1, setDayNumber = None, setDayRotationID = None, setDayRotationPatternIDClonedFrom = None, setEntityGroupKey = None, setRelationships = None, returnDayRotationPatternID = True, returnCreatedTime = False, returnDayNumber = False, returnDayRotationID = False, returnDayRotationPatternIDClonedFrom = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteDayRotationPattern(DayRotationPatternID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DayRotationPattern/" + str(DayRotationPatternID), verb = "delete")

	return(response)

def getEveryDisciplineThreshold(EntityID = 1, page = 1, pageSize = 100, returnDisciplineThresholdID = True, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDisciplineThreshold(DisciplineThresholdID, EntityID = 1, returnDisciplineThresholdID = True, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyDisciplineThreshold(DisciplineThresholdID, EntityID = 1, setActionID = None, setAllowDisciplineOnCurrentDay = None, setAttendanceSlipComment = None, setBuildingIDServing = None, setCreateDisciplineRecord = None, setDisciplineSlipComment = None, setDurationToServe = None, setDurationToServePerDay = None, setFooterComment = None, setGenerateActionDetail = None, setGreeting = None, setIncidentDefaultComment = None, setIncidentDescription = None, setIsRepeatable = None, setLocationIDServing = None, setOffenseID = None, setRoomIDServing = None, setServeOnFriday = None, setServeOnMonday = None, setServeOnSaturday = None, setServeOnSunday = None, setServeOnThursday = None, setServeOnTuesday = None, setServeOnWednesday = None, setServingTime = None, setStaffIDAuthorizedBy = None, setThresholdRangeHigh = None, setThresholdRangeLow = None, setThresholdResetRangeID = None, setRelationships = None, returnDisciplineThresholdID = True, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createDisciplineThreshold(EntityID = 1, setActionID = None, setAllowDisciplineOnCurrentDay = None, setAttendanceSlipComment = None, setBuildingIDServing = None, setCreateDisciplineRecord = None, setDisciplineSlipComment = None, setDurationToServe = None, setDurationToServePerDay = None, setFooterComment = None, setGenerateActionDetail = None, setGreeting = None, setIncidentDefaultComment = None, setIncidentDescription = None, setIsRepeatable = None, setLocationIDServing = None, setOffenseID = None, setRoomIDServing = None, setServeOnFriday = None, setServeOnMonday = None, setServeOnSaturday = None, setServeOnSunday = None, setServeOnThursday = None, setServeOnTuesday = None, setServeOnWednesday = None, setServingTime = None, setStaffIDAuthorizedBy = None, setThresholdRangeHigh = None, setThresholdRangeLow = None, setThresholdResetRangeID = None, setRelationships = None, returnDisciplineThresholdID = True, returnActionID = False, returnAllowDisciplineOnCurrentDay = False, returnAttendanceLettersRan = False, returnAttendanceSlipComment = False, returnBuildingIDServing = False, returnCreateDisciplineRecord = False, returnCreatedTime = False, returnDisciplineSlipComment = False, returnDurationToServe = False, returnDurationToServePerDay = False, returnFooterComment = False, returnGenerateActionDetail = False, returnGreeting = False, returnIncidentDefaultComment = False, returnIncidentDescription = False, returnIsRepeatable = False, returnLocationIDServing = False, returnModifiedTime = False, returnOffenseID = False, returnRangeDisplay = False, returnRoomIDServing = False, returnServeOnFriday = False, returnServeOnMonday = False, returnServeOnSaturday = False, returnServeOnSunday = False, returnServeOnThursday = False, returnServeOnTuesday = False, returnServeOnWednesday = False, returnServingTime = False, returnStaffIDAuthorizedBy = False, returnThresholdRangeHigh = False, returnThresholdRangeLow = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteDisciplineThreshold(DisciplineThresholdID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DisciplineThreshold/" + str(DisciplineThresholdID), verb = "delete")

	return(response)

def getEveryDroppedStudentAttendancePeriod(EntityID = 1, page = 1, pageSize = 100, returnDroppedStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1, returnDroppedStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setCalendarDayID = None, setComment = None, setIncidentOffenseNameActionDetailID = None, setIsGuardianNotified = None, setStudentID = None, setRelationships = None, returnDroppedStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createDroppedStudentAttendancePeriod(EntityID = 1, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setCalendarDayID = None, setComment = None, setIncidentOffenseNameActionDetailID = None, setIsGuardianNotified = None, setStudentID = None, setRelationships = None, returnDroppedStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnIncidentOffenseNameActionDetailID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteDroppedStudentAttendancePeriod(DroppedStudentAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/DroppedStudentAttendancePeriod/" + str(DroppedStudentAttendancePeriodID), verb = "delete")

	return(response)

def getEveryRecordedUnrecordedAttendance(EntityID = 1, page = 1, pageSize = 100, returnMeetDisplayPeriodID = True, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1, returnMeetDisplayPeriodID = True, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1, setRelationships = None, returnMeetDisplayPeriodID = True, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createRecordedUnrecordedAttendance(EntityID = 1, setRelationships = None, returnMeetDisplayPeriodID = True, returnAttendanceTaken = False, returnCountAs = False, returnCreatedTime = False, returnDailySectionAttendanceID = False, returnDate = False, returnDayOfTheWeek = False, returnDisplayPeriodCode = False, returnMeetID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteRecordedUnrecordedAttendance(MeetDisplayPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RecordedUnrecordedAttendance/" + str(MeetDisplayPeriodID), verb = "delete")

	return(response)

def getEveryRoomLayout(EntityID = 1, page = 1, pageSize = 100, returnRoomLayoutID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRoomLayout(RoomLayoutID, EntityID = 1, returnRoomLayoutID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyRoomLayout(RoomLayoutID, EntityID = 1, setDescription = None, setRoomID = None, setRelationships = None, returnRoomLayoutID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createRoomLayout(EntityID = 1, setDescription = None, setRoomID = None, setRelationships = None, returnRoomLayoutID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteRoomLayout(RoomLayoutID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayout/" + str(RoomLayoutID), verb = "delete")

	return(response)

def getEveryRoomLayoutObject(EntityID = 1, page = 1, pageSize = 100, returnRoomLayoutObjectID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRoomLayoutObject(RoomLayoutObjectID, EntityID = 1, returnRoomLayoutObjectID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyRoomLayoutObject(RoomLayoutObjectID, EntityID = 1, setRoomLayoutID = None, setRoomObjectID = None, setRotation = None, setXLocation = None, setYLocation = None, setRelationships = None, returnRoomLayoutObjectID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createRoomLayoutObject(EntityID = 1, setRoomLayoutID = None, setRoomObjectID = None, setRotation = None, setXLocation = None, setYLocation = None, setRelationships = None, returnRoomLayoutObjectID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutID = False, returnRoomObjectID = False, returnRotation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXLocation = False, returnYLocation = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteRoomLayoutObject(RoomLayoutObjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomLayoutObject/" + str(RoomLayoutObjectID), verb = "delete")

	return(response)

def getEveryRoomObject(EntityID = 1, page = 1, pageSize = 100, returnRoomObjectID = True, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRoomObject(RoomObjectID, EntityID = 1, returnRoomObjectID = True, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyRoomObject(RoomObjectID, EntityID = 1, setIsStudentSeat = None, setLabel = None, setParameters = None, setSkywardID = None, setRelationships = None, returnRoomObjectID = True, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createRoomObject(EntityID = 1, setIsStudentSeat = None, setLabel = None, setParameters = None, setSkywardID = None, setRelationships = None, returnRoomObjectID = True, returnCreatedTime = False, returnIsStudentSeat = False, returnLabel = False, returnModifiedTime = False, returnParameters = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteRoomObject(RoomObjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/RoomObject/" + str(RoomObjectID), verb = "delete")

	return(response)

def getEverySeatingChart(EntityID = 1, page = 1, pageSize = 100, returnSeatingChartID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSeatingChart(SeatingChartID, EntityID = 1, returnSeatingChartID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifySeatingChart(SeatingChartID, EntityID = 1, setDescription = None, setRoomLayoutID = None, setRelationships = None, returnSeatingChartID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createSeatingChart(EntityID = 1, setDescription = None, setRoomLayoutID = None, setRelationships = None, returnSeatingChartID = True, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRoomLayoutID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteSeatingChart(SeatingChartID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChart/" + str(SeatingChartID), verb = "delete")

	return(response)

def getEverySeatingChartMeet(EntityID = 1, page = 1, pageSize = 100, returnSeatingChartMeetID = True, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSeatingChartMeet(SeatingChartMeetID, EntityID = 1, returnSeatingChartMeetID = True, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifySeatingChartMeet(SeatingChartMeetID, EntityID = 1, setIsCurrent = None, setMeetID = None, setSeatingChartID = None, setRelationships = None, returnSeatingChartMeetID = True, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createSeatingChartMeet(EntityID = 1, setIsCurrent = None, setMeetID = None, setSeatingChartID = None, setRelationships = None, returnSeatingChartMeetID = True, returnCreatedTime = False, returnIsCurrent = False, returnMeetID = False, returnModifiedTime = False, returnSeatingChartID = False, returnSectionList = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteSeatingChartMeet(SeatingChartMeetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartMeet/" + str(SeatingChartMeetID), verb = "delete")

	return(response)

def getEverySeatingChartSeat(EntityID = 1, page = 1, pageSize = 100, returnSeatingChartSeatID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSeatingChartSeat(SeatingChartSeatID, EntityID = 1, returnSeatingChartSeatID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifySeatingChartSeat(SeatingChartSeatID, EntityID = 1, setRoomLayoutObjectID = None, setSeatingChartID = None, setStudentID = None, setRelationships = None, returnSeatingChartSeatID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createSeatingChartSeat(EntityID = 1, setRoomLayoutObjectID = None, setSeatingChartID = None, setStudentID = None, setRelationships = None, returnSeatingChartSeatID = True, returnCreatedTime = False, returnModifiedTime = False, returnRoomLayoutObjectID = False, returnSeatingChartID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteSeatingChartSeat(SeatingChartSeatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartSeat/" + str(SeatingChartSeatID), verb = "delete")

	return(response)

def getEverySeatingChartUsedLast(EntityID = 1, page = 1, pageSize = 100, returnSeatingChartUsedLastID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1, returnSeatingChartUsedLastID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifySeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1, setDisplayPeriodID = None, setRoomID = None, setSeatingChartID = None, setStaffID = None, setRelationships = None, returnSeatingChartUsedLastID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createSeatingChartUsedLast(EntityID = 1, setDisplayPeriodID = None, setRoomID = None, setSeatingChartID = None, setStaffID = None, setRelationships = None, returnSeatingChartUsedLastID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnModifiedTime = False, returnRoomID = False, returnSeatingChartID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteSeatingChartUsedLast(SeatingChartUsedLastID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/SeatingChartUsedLast/" + str(SeatingChartUsedLastID), verb = "delete")

	return(response)

def getEveryStaffMeetSetting(EntityID = 1, page = 1, pageSize = 100, returnStaffMeetSettingID = True, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnModifiedTime = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStaffMeetSetting(StaffMeetSettingID, EntityID = 1, returnStaffMeetSettingID = True, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnModifiedTime = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStaffMeetSetting(StaffMeetSettingID, EntityID = 1, setDisplayAttendanceTotalsOnDesktop = None, setDisplayAttendanceTotalsOnMobile = None, setDisplayHistoricalAttendanceOnDesktop = None, setDisplayHistoricalAttendanceOnMobile = None, setStaffMeetID = None, setRelationships = None, returnStaffMeetSettingID = True, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnModifiedTime = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStaffMeetSetting(EntityID = 1, setDisplayAttendanceTotalsOnDesktop = None, setDisplayAttendanceTotalsOnMobile = None, setDisplayHistoricalAttendanceOnDesktop = None, setDisplayHistoricalAttendanceOnMobile = None, setStaffMeetID = None, setRelationships = None, returnStaffMeetSettingID = True, returnCreatedTime = False, returnDisplayAttendanceTotalsOnDesktop = False, returnDisplayAttendanceTotalsOnMobile = False, returnDisplayHistoricalAttendanceOnDesktop = False, returnDisplayHistoricalAttendanceOnMobile = False, returnModifiedTime = False, returnStaffMeetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStaffMeetSetting(StaffMeetSettingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StaffMeetSetting/" + str(StaffMeetSettingID), verb = "delete")

	return(response)

def getEveryStudentAttendance(EntityID = 1, page = 1, pageSize = 100, returnStudentAttendanceID = True, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAttendance(StudentAttendanceID, EntityID = 1, returnStudentAttendanceID = True, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStudentAttendance(StudentAttendanceID, EntityID = 1, setCalendarDayID = None, setComment = None, setDaysAbsent = None, setDaysExcused = None, setDaysOther = None, setDaysUnexcused = None, setEntityID = None, setIsGuardianNotified = None, setSchoolYearID = None, setStudentID = None, setTardyCount = None, setRelationships = None, returnStudentAttendanceID = True, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStudentAttendance(EntityID = 1, setCalendarDayID = None, setComment = None, setDaysAbsent = None, setDaysExcused = None, setDaysOther = None, setDaysUnexcused = None, setEntityID = None, setIsGuardianNotified = None, setSchoolYearID = None, setStudentID = None, setTardyCount = None, setRelationships = None, returnStudentAttendanceID = True, returnCalendarDayID = False, returnComment = False, returnCommentsExistForStudentAttendance = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysUnexcused = False, returnEntityID = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnTardyCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStudentAttendance(StudentAttendanceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendance/" + str(StudentAttendanceID), verb = "delete")

	return(response)

def getEveryStudentAttendancePeriod(EntityID = 1, page = 1, pageSize = 100, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setComment = None, setEntityIDAttendancePeriod = None, setEntityIDCourse = None, setIncidentOffenseNameActionDetailID = None, setStudentAttendanceID = None, setStudentSectionID = None, setViewingFromAttendanceEntity = None, setRelationships = None, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStudentAttendancePeriod(EntityID = 1, setAttendancePeriodID = None, setAttendanceReasonID = None, setAttendanceTypeID = None, setComment = None, setEntityIDAttendancePeriod = None, setEntityIDCourse = None, setIncidentOffenseNameActionDetailID = None, setStudentAttendanceID = None, setStudentSectionID = None, setViewingFromAttendanceEntity = None, setRelationships = None, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnAttendanceReasonID = False, returnAttendanceTypeID = False, returnAttendanceTypeWithReason = False, returnComment = False, returnCreatedTime = False, returnCrossWalkedAttendanceTypeWithReason = False, returnEntityIDAttendancePeriod = False, returnEntityIDCourse = False, returnIncidentOffenseNameActionDetailID = False, returnModifiedTime = False, returnStudentAttendanceID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewingFromAttendanceEntity = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStudentAttendancePeriod(StudentAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriod/" + str(StudentAttendancePeriodID), verb = "delete")

	return(response)

def getEveryStudentAttendancePeriodGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1, setRelationships = None, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStudentAttendancePeriodGroup(EntityID = 1, setRelationships = None, returnStudentAttendancePeriodID = True, returnAttendancePeriodID = False, returnEntityID = False, returnSchoolYearID = False, returnStudentAttendanceID = False, returnStudentID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStudentAttendancePeriodGroup(StudentAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendancePeriodGroup/" + str(StudentAttendancePeriodID), verb = "delete")

	return(response)

def getEveryStudentAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnStudentID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentAttendanceTerm(StudentID, EntityID = 1, returnStudentID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStudentAttendanceTerm(StudentID, EntityID = 1, setRelationships = None, returnStudentID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStudentAttendanceTerm(EntityID = 1, setRelationships = None, returnStudentID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnEndDate = False, returnEntityID = False, returnIsDefault = False, returnSchoolYearID = False, returnStartDate = False, returnTotalDaysAbsent = False, returnTotalDaysExcused = False, returnTotalDaysOther = False, returnTotalDaysUnexcused = False, returnTotalTardyCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStudentAttendanceTerm(StudentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentAttendanceTerm/" + str(StudentID), verb = "delete")

	return(response)

def getEveryStudentDisciplineThresholdAttendanceReportRunHistory(EntityID = 1, page = 1, pageSize = 100, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1, setAttendanceReportRunHistoryID = None, setDisciplineThresholdID = None, setIsActive = None, setStudentID = None, setRelationships = None, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStudentDisciplineThresholdAttendanceReportRunHistory(EntityID = 1, setAttendanceReportRunHistoryID = None, setDisciplineThresholdID = None, setIsActive = None, setStudentID = None, setRelationships = None, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = True, returnAttendanceReportRunHistoryID = False, returnCreatedTime = False, returnDisciplineThresholdID = False, returnIsActive = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStudentDisciplineThresholdAttendanceReportRunHistory(StudentDisciplineThresholdAttendanceReportRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentDisciplineThresholdAttendanceReportRunHistory/" + str(StudentDisciplineThresholdAttendanceReportRunHistoryID), verb = "delete")

	return(response)

def getEveryStudentInOutTime(EntityID = 1, page = 1, pageSize = 100, returnStudentInOutTimeID = True, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentInOutTime(StudentInOutTimeID, EntityID = 1, returnStudentInOutTimeID = True, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStudentInOutTime(StudentInOutTimeID, EntityID = 1, setStudentAttendanceID = None, setTimeIn = None, setTimeOut = None, setRelationships = None, returnStudentInOutTimeID = True, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStudentInOutTime(EntityID = 1, setStudentAttendanceID = None, setTimeIn = None, setTimeOut = None, setRelationships = None, returnStudentInOutTimeID = True, returnCreatedTime = False, returnMinutesPresent = False, returnModifiedTime = False, returnPeriodTimes = False, returnStudentAttendanceID = False, returnTimeIn = False, returnTimeOut = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStudentInOutTime(StudentInOutTimeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentInOutTime/" + str(StudentInOutTimeID), verb = "delete")

	return(response)

def getEveryStudentThresholdPeriod(EntityID = 1, page = 1, pageSize = 100, returnStudentThresholdPeriodID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1, returnStudentThresholdPeriodID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setCountsTowardsThreshold = None, setDate = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentDisciplineThresholdAttendanceReportRunHistoryID = None, setStudentSectionID = None, setRelationships = None, returnStudentThresholdPeriodID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createStudentThresholdPeriod(EntityID = 1, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setCountsTowardsThreshold = None, setDate = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentDisciplineThresholdAttendanceReportRunHistoryID = None, setStudentSectionID = None, setRelationships = None, returnStudentThresholdPeriodID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCountsTowardsThreshold = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentDisciplineThresholdAttendanceReportRunHistoryID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteStudentThresholdPeriod(StudentThresholdPeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/StudentThresholdPeriod/" + str(StudentThresholdPeriodID), verb = "delete")

	return(response)

def getEveryTeacherEntry(EntityID = 1, page = 1, pageSize = 100, returnTeacherEntryID = True, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherEntry(TeacherEntryID, EntityID = 1, returnTeacherEntryID = True, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTeacherEntry(TeacherEntryID, EntityID = 1, setBackgroundColor = None, setBackgroundColorHex = None, setBackgroundColorRgba = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setLabel = None, setSchoolYearID = None, setTeacherEntryIDClonedFrom = None, setRelationships = None, returnTeacherEntryID = True, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTeacherEntry(EntityID = 1, setBackgroundColor = None, setBackgroundColorHex = None, setBackgroundColorRgba = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setLabel = None, setSchoolYearID = None, setTeacherEntryIDClonedFrom = None, setRelationships = None, returnTeacherEntryID = True, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnLabel = False, returnModifiedTime = False, returnSchoolYearID = False, returnTeacherEntryIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTeacherEntry(TeacherEntryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TeacherEntry/" + str(TeacherEntryID), verb = "delete")

	return(response)

def getEveryTempAffectedCalendarDayRecord(EntityID = 1, page = 1, pageSize = 100, returnTempAffectedCalendarDayRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1, returnTempAffectedCalendarDayRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setCalendar = None, setCalendarID = None, setComment = None, setCountAs = None, setDate = None, setDayOfTheWeek = None, setEntity = None, setFailureReason = None, setNewBellSchedule = None, setNewCountAs = None, setNewDayRotation = None, setNewDayRotationID = None, setNewFundingPeriod = None, setNewFundingPeriodID = None, setNewInstructionalMinutesOverride = None, setNewOperationalMinutesOverride = None, setNewStateCalendarWaiverEventTypeCodeTX = None, setNewStateCalendarWaiverEventTypeCodeTXID = None, setNewStateSchoolDayEventCodeTX = None, setNewStateSchoolDayEventCodeTXID = None, setNewUseInstructionalMinutesOverride = None, setNewUseOperationalMinutesOverride = None, setNewWaiverMinutes = None, setOldBellSchedule = None, setOldDayRotation = None, setOldDayRotationID = None, setOldFundingPeriod = None, setOldFundingPeriodID = None, setOldInstructionalMinutesOverride = None, setOldOperationalMinutesOverride = None, setOldStateCalendarWaiverEventTypeCodeTX = None, setOldStateCalendarWaiverEventTypeCodeTXID = None, setOldStateSchoolDayEventCodeTX = None, setOldStateSchoolDayEventCodeTXID = None, setOldUseInstructionalMinutesOverride = None, setOldUseOperationalMinutesOverride = None, setOldWaiverMinutes = None, setRelationships = None, returnTempAffectedCalendarDayRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempAffectedCalendarDayRecord(EntityID = 1, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setCalendar = None, setCalendarID = None, setComment = None, setCountAs = None, setDate = None, setDayOfTheWeek = None, setEntity = None, setFailureReason = None, setNewBellSchedule = None, setNewCountAs = None, setNewDayRotation = None, setNewDayRotationID = None, setNewFundingPeriod = None, setNewFundingPeriodID = None, setNewInstructionalMinutesOverride = None, setNewOperationalMinutesOverride = None, setNewStateCalendarWaiverEventTypeCodeTX = None, setNewStateCalendarWaiverEventTypeCodeTXID = None, setNewStateSchoolDayEventCodeTX = None, setNewStateSchoolDayEventCodeTXID = None, setNewUseInstructionalMinutesOverride = None, setNewUseOperationalMinutesOverride = None, setNewWaiverMinutes = None, setOldBellSchedule = None, setOldDayRotation = None, setOldDayRotationID = None, setOldFundingPeriod = None, setOldFundingPeriodID = None, setOldInstructionalMinutesOverride = None, setOldOperationalMinutesOverride = None, setOldStateCalendarWaiverEventTypeCodeTX = None, setOldStateCalendarWaiverEventTypeCodeTXID = None, setOldStateSchoolDayEventCodeTX = None, setOldStateSchoolDayEventCodeTXID = None, setOldUseInstructionalMinutesOverride = None, setOldUseOperationalMinutesOverride = None, setOldWaiverMinutes = None, setRelationships = None, returnTempAffectedCalendarDayRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnCalendar = False, returnCalendarID = False, returnComment = False, returnCountAs = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnEntity = False, returnFailureReason = False, returnModifiedTime = False, returnNewBellSchedule = False, returnNewCountAs = False, returnNewDayRotation = False, returnNewDayRotationID = False, returnNewFundingPeriod = False, returnNewFundingPeriodID = False, returnNewInstructionalMinutesOverride = False, returnNewOperationalMinutesOverride = False, returnNewStateCalendarWaiverEventTypeCodeTX = False, returnNewStateCalendarWaiverEventTypeCodeTXID = False, returnNewStateSchoolDayEventCodeTX = False, returnNewStateSchoolDayEventCodeTXID = False, returnNewUseInstructionalMinutesOverride = False, returnNewUseOperationalMinutesOverride = False, returnNewWaiverMinutes = False, returnOldBellSchedule = False, returnOldDayRotation = False, returnOldDayRotationID = False, returnOldFundingPeriod = False, returnOldFundingPeriodID = False, returnOldInstructionalMinutesOverride = False, returnOldOperationalMinutesOverride = False, returnOldStateCalendarWaiverEventTypeCodeTX = False, returnOldStateCalendarWaiverEventTypeCodeTXID = False, returnOldStateSchoolDayEventCodeTX = False, returnOldStateSchoolDayEventCodeTXID = False, returnOldUseInstructionalMinutesOverride = False, returnOldUseOperationalMinutesOverride = False, returnOldWaiverMinutes = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempAffectedCalendarDayRecord(TempAffectedCalendarDayRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedCalendarDayRecord/" + str(TempAffectedCalendarDayRecordID), verb = "delete")

	return(response)

def getEveryTempAffectedStudentAttendancePeriodRecord(EntityID = 1, page = 1, pageSize = 100, returnTempAffectedStudentAttendancePeriodRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1, returnTempAffectedStudentAttendancePeriodRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setAttendanceCategory = None, setAttendancePeriodID = None, setAttendanceReasonCodeDescription = None, setAttendanceReasonID = None, setAttendanceTypeCodeDescription = None, setAttendanceTypeID = None, setCalendarDayID = None, setCECEAttendancePeriodID = None, setCECEAttendanceReasonID = None, setCECEAttendanceTypeID = None, setComment = None, setDate = None, setDayRotationCode = None, setEntity = None, setFailureReason = None, setFullName = None, setIsForCECEAttendancePeriod = None, setIsGuardianNotified = None, setNewStudentSectionCode = None, setNewStudentSectionID = None, setOldStudentSectionCode = None, setOldStudentSectionID = None, setPeriodCode = None, setProcessFromCECEEntity = None, setStudentAttendanceID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempAffectedStudentAttendancePeriodRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempAffectedStudentAttendancePeriodRecord(EntityID = 1, setAction = None, setActionCode = None, setAffectedPrimaryKey = None, setAttendanceCategory = None, setAttendancePeriodID = None, setAttendanceReasonCodeDescription = None, setAttendanceReasonID = None, setAttendanceTypeCodeDescription = None, setAttendanceTypeID = None, setCalendarDayID = None, setCECEAttendancePeriodID = None, setCECEAttendanceReasonID = None, setCECEAttendanceTypeID = None, setComment = None, setDate = None, setDayRotationCode = None, setEntity = None, setFailureReason = None, setFullName = None, setIsForCECEAttendancePeriod = None, setIsGuardianNotified = None, setNewStudentSectionCode = None, setNewStudentSectionID = None, setOldStudentSectionCode = None, setOldStudentSectionID = None, setPeriodCode = None, setProcessFromCECEEntity = None, setStudentAttendanceID = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempAffectedStudentAttendancePeriodRecordID = True, returnAction = False, returnActionCode = False, returnAffectedPrimaryKey = False, returnAttendanceCategory = False, returnAttendancePeriodID = False, returnAttendanceReasonCodeDescription = False, returnAttendanceReasonID = False, returnAttendanceTypeCodeDescription = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCECEAttendancePeriodID = False, returnCECEAttendanceReasonID = False, returnCECEAttendanceTypeID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnEntity = False, returnFailureReason = False, returnFullName = False, returnIsForCECEAttendancePeriod = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewStudentSectionCode = False, returnNewStudentSectionID = False, returnOldStudentSectionCode = False, returnOldStudentSectionID = False, returnPeriodCode = False, returnProcessFromCECEEntity = False, returnStudentAttendanceID = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempAffectedStudentAttendancePeriodRecord(TempAffectedStudentAttendancePeriodRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendancePeriodRecord/" + str(TempAffectedStudentAttendancePeriodRecordID), verb = "delete")

	return(response)

def getEveryTempAffectedStudentAttendanceRecord(EntityID = 1, page = 1, pageSize = 100, returnTempAffectedStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1, returnTempAffectedStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1, setAffectedPrimaryKey = None, setCalendarDayID = None, setComment = None, setDate = None, setDayRotationCode = None, setFailedStudentAttendancePeriods = None, setFailureReason = None, setFullName = None, setIsGuardianNotified = None, setNewDaysAbsent = None, setNewDaysExcused = None, setNewDaysOther = None, setNewDaysUnexcused = None, setNewGuardianNotified = None, setNewStudentAttendancePeriods = None, setNewTardyCount = None, setOldDaysAbsent = None, setOldDaysExcused = None, setOldDaysOther = None, setOldDaysUnexcused = None, setOldStudentAttendancePeriods = None, setOldTardyCount = None, setPreviousGuardianNotified = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempAffectedStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempAffectedStudentAttendanceRecord(EntityID = 1, setAffectedPrimaryKey = None, setCalendarDayID = None, setComment = None, setDate = None, setDayRotationCode = None, setFailedStudentAttendancePeriods = None, setFailureReason = None, setFullName = None, setIsGuardianNotified = None, setNewDaysAbsent = None, setNewDaysExcused = None, setNewDaysOther = None, setNewDaysUnexcused = None, setNewGuardianNotified = None, setNewStudentAttendancePeriods = None, setNewTardyCount = None, setOldDaysAbsent = None, setOldDaysExcused = None, setOldDaysOther = None, setOldDaysUnexcused = None, setOldStudentAttendancePeriods = None, setOldTardyCount = None, setPreviousGuardianNotified = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnTempAffectedStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnCalendarDayID = False, returnComment = False, returnCreatedTime = False, returnDate = False, returnDayRotationCode = False, returnFailedStudentAttendancePeriods = False, returnFailureReason = False, returnFullName = False, returnIsGuardianNotified = False, returnModifiedTime = False, returnNewDaysAbsent = False, returnNewDaysExcused = False, returnNewDaysOther = False, returnNewDaysUnexcused = False, returnNewGuardianNotified = False, returnNewStudentAttendancePeriods = False, returnNewTardyCount = False, returnOldDaysAbsent = False, returnOldDaysExcused = False, returnOldDaysOther = False, returnOldDaysUnexcused = False, returnOldStudentAttendancePeriods = False, returnOldTardyCount = False, returnPreviousGuardianNotified = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempAffectedStudentAttendanceRecord(TempAffectedStudentAttendanceRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAffectedStudentAttendanceRecord/" + str(TempAffectedStudentAttendanceRecordID), verb = "delete")

	return(response)

def getEveryTempAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnTempAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAttendanceTerm(TempAttendanceTermID, EntityID = 1, returnTempAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempAttendanceTerm(TempAttendanceTermID, EntityID = 1, setAttendanceTermCode = None, setAttendanceTermID = None, setCalendarCode = None, setCalendarID = None, setEndDate = None, setIsUpdated = None, setOriginalEndDate = None, setOriginalStartDate = None, setStartDate = None, setRelationships = None, returnTempAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempAttendanceTerm(EntityID = 1, setAttendanceTermCode = None, setAttendanceTermID = None, setCalendarCode = None, setCalendarID = None, setEndDate = None, setIsUpdated = None, setOriginalEndDate = None, setOriginalStartDate = None, setStartDate = None, setRelationships = None, returnTempAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarCode = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnIsUpdated = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempAttendanceTerm(TempAttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempAttendanceTerm/" + str(TempAttendanceTermID), verb = "delete")

	return(response)

def getEveryTempCalendar(EntityID = 1, page = 1, pageSize = 100, returnTempCalendarID = True, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCalendar(TempCalendarID, EntityID = 1, returnTempCalendarID = True, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempCalendar(TempCalendarID, EntityID = 1, setAffectedPrimaryKey = None, setCalendarID = None, setCode = None, setCodeDescription = None, setNewEndDate = None, setNewStartDate = None, setOldEndDate = None, setOldStartDate = None, setRelationships = None, returnTempCalendarID = True, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempCalendar(EntityID = 1, setAffectedPrimaryKey = None, setCalendarID = None, setCode = None, setCodeDescription = None, setNewEndDate = None, setNewStartDate = None, setOldEndDate = None, setOldStartDate = None, setRelationships = None, returnTempCalendarID = True, returnAffectedPrimaryKey = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnModifiedTime = False, returnNewEndDate = False, returnNewStartDate = False, returnOldEndDate = False, returnOldStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempCalendar(TempCalendarID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendar/" + str(TempCalendarID), verb = "delete")

	return(response)

def getEveryTempCalendarAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnTempCalendarAttendanceTermID = True, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1, returnTempCalendarAttendanceTermID = True, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1, setAttendanceTermID = None, setCalendarID = None, setCode = None, setCodeDescription = None, setEndDate = None, setOriginalEndDate = None, setOriginalStartDate = None, setStartDate = None, setTableType = None, setTableTypeCode = None, setRelationships = None, returnTempCalendarAttendanceTermID = True, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempCalendarAttendanceTerm(EntityID = 1, setAttendanceTermID = None, setCalendarID = None, setCode = None, setCodeDescription = None, setEndDate = None, setOriginalEndDate = None, setOriginalStartDate = None, setStartDate = None, setTableType = None, setTableTypeCode = None, setRelationships = None, returnTempCalendarAttendanceTermID = True, returnAttendanceTermID = False, returnCalendarID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndDate = False, returnModifiedTime = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnStartDate = False, returnTableType = False, returnTableTypeCode = False, returnTableTypeString = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempCalendarAttendanceTerm(TempCalendarAttendanceTermID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarAttendanceTerm/" + str(TempCalendarAttendanceTermID), verb = "delete")

	return(response)

def getEveryTempCalendarDayCalendarEventRecord(EntityID = 1, page = 1, pageSize = 100, returnTempCalendarDayCalendarEventRecordID = True, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1, returnTempCalendarDayCalendarEventRecordID = True, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1, setCalendar = None, setCalendarDayID = None, setCalendarEvent = None, setCalendarEventID = None, setDate = None, setFailureReason = None, setRelationships = None, returnTempCalendarDayCalendarEventRecordID = True, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempCalendarDayCalendarEventRecord(EntityID = 1, setCalendar = None, setCalendarDayID = None, setCalendarEvent = None, setCalendarEventID = None, setDate = None, setFailureReason = None, setRelationships = None, returnTempCalendarDayCalendarEventRecordID = True, returnCalendar = False, returnCalendarDayID = False, returnCalendarEvent = False, returnCalendarEventID = False, returnCreatedTime = False, returnDate = False, returnFailureReason = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempCalendarDayCalendarEventRecord(TempCalendarDayCalendarEventRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCalendarDayCalendarEventRecord/" + str(TempCalendarDayCalendarEventRecordID), verb = "delete")

	return(response)

def getEveryTempCloneCalendarError(EntityID = 1, page = 1, pageSize = 100, returnTempCloneCalendarErrorID = True, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1, returnTempCloneCalendarErrorID = True, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1, setDescription = None, setEntityName = None, setFailureReason = None, setRecordType = None, setRecordTypeCode = None, setRelationships = None, returnTempCloneCalendarErrorID = True, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempCloneCalendarError(EntityID = 1, setDescription = None, setEntityName = None, setFailureReason = None, setRecordType = None, setRecordTypeCode = None, setRelationships = None, returnTempCloneCalendarErrorID = True, returnCreatedTime = False, returnDescription = False, returnEntityName = False, returnFailureReason = False, returnModifiedTime = False, returnRecordType = False, returnRecordTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempCloneCalendarError(TempCloneCalendarErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarError/" + str(TempCloneCalendarErrorID), verb = "delete")

	return(response)

def getEveryTempCloneCalendarRecord(EntityID = 1, page = 1, pageSize = 100, returnTempCloneCalendarRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1, returnTempCloneCalendarRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1, setAffectedPrimaryKey = None, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCode = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntity = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setSchoolYearID = None, setStartDate = None, setZeroDayHighPeriodCount = None, setRelationships = None, returnTempCloneCalendarRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempCloneCalendarRecord(EntityID = 1, setAffectedPrimaryKey = None, setAttendanceCalculationMethod = None, setAttendanceCalculationMethodCode = None, setCode = None, setDefaultDayLengthMinutes = None, setDescription = None, setEndDate = None, setEntity = None, setEntityID = None, setHalfDayHighPeriodCount = None, setIsDefault = None, setSchoolYearID = None, setStartDate = None, setZeroDayHighPeriodCount = None, setRelationships = None, returnTempCloneCalendarRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceCalculationMethod = False, returnAttendanceCalculationMethodCode = False, returnCode = False, returnCreatedTime = False, returnDefaultDayLengthMinutes = False, returnDescription = False, returnEndDate = False, returnEntity = False, returnEntityID = False, returnHalfDayHighPeriodCount = False, returnIsDefault = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZeroDayHighPeriodCount = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempCloneCalendarRecord(TempCloneCalendarRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempCloneCalendarRecord/" + str(TempCloneCalendarRecordID), verb = "delete")

	return(response)

def getEveryTempStudentAttendanceRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1, returnTempStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1, setAffectedPrimaryKey = None, setAttendanceTakenByPeriod = None, setDate = None, setDayOfTheWeek = None, setDayRotation = None, setDayRotationID = None, setGuardianNotified = None, setStudentName = None, setStudentNumber = None, setRelationships = None, returnTempStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempStudentAttendanceRecord(EntityID = 1, setAffectedPrimaryKey = None, setAttendanceTakenByPeriod = None, setDate = None, setDayOfTheWeek = None, setDayRotation = None, setDayRotationID = None, setGuardianNotified = None, setStudentName = None, setStudentNumber = None, setRelationships = None, returnTempStudentAttendanceRecordID = True, returnAffectedPrimaryKey = False, returnAttendanceTakenByPeriod = False, returnCreatedTime = False, returnDate = False, returnDayOfTheWeek = False, returnDayRotation = False, returnDayRotationID = False, returnGuardianNotified = False, returnModifiedTime = False, returnStudentName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempStudentAttendanceRecord(TempStudentAttendanceRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentAttendanceRecord/" + str(TempStudentAttendanceRecordID), verb = "delete")

	return(response)

def getEveryTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = True, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = True, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1, setCountType = None, setCountTypeCode = None, setDateHigh = None, setDateLow = None, setDisciplineThresholdID = None, setResetRangeAttendanceTypes = None, setStudentID = None, setStudentName = None, setThresholdValue = None, setRelationships = None, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = True, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(EntityID = 1, setCountType = None, setCountTypeCode = None, setDateHigh = None, setDateLow = None, setDisciplineThresholdID = None, setResetRangeAttendanceTypes = None, setStudentID = None, setStudentName = None, setThresholdValue = None, setRelationships = None, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = True, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateHigh = False, returnDateLow = False, returnDisciplineThresholdID = False, returnModifiedTime = False, returnResetRangeAttendanceTypes = False, returnStudentID = False, returnStudentName = False, returnThresholdValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempStudentDisciplineThresholdAttendanceReportRunHistoryRecord(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentDisciplineThresholdAttendanceReportRunHistoryRecord/" + str(TempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID), verb = "delete")

	return(response)

def getEveryTempStudentThresholdPeriodRecord(EntityID = 1, page = 1, pageSize = 100, returnTempStudentThresholdPeriodRecordID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1, returnTempStudentThresholdPeriodRecordID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setDate = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentSectionID = None, setTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = None, setRelationships = None, returnTempStudentThresholdPeriodRecordID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createTempStudentThresholdPeriodRecord(EntityID = 1, setAttendancePeriodID = None, setAttendanceTypeID = None, setCalendarDayID = None, setDate = None, setSectionID = None, setStudentAttendancePeriodID = None, setStudentSectionID = None, setTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = None, setRelationships = None, returnTempStudentThresholdPeriodRecordID = True, returnAttendancePeriodID = False, returnAttendanceTypeID = False, returnCalendarDayID = False, returnCreatedTime = False, returnDate = False, returnModifiedTime = False, returnSectionID = False, returnStudentAttendancePeriodID = False, returnStudentSectionID = False, returnTempStudentDisciplineThresholdAttendanceReportRunHistoryRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteTempStudentThresholdPeriodRecord(TempStudentThresholdPeriodRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/TempStudentThresholdPeriodRecord/" + str(TempStudentThresholdPeriodRecordID), verb = "delete")

	return(response)

def getEveryThresholdResetRange(EntityID = 1, page = 1, pageSize = 100, returnThresholdResetRangeID = True, returnAttendanceLettersRan = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnModifiedTime = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getThresholdResetRange(ThresholdResetRangeID, EntityID = 1, returnThresholdResetRangeID = True, returnAttendanceLettersRan = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnModifiedTime = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyThresholdResetRange(ThresholdResetRangeID, EntityID = 1, setCountType = None, setCountTypeCode = None, setDateHigh = None, setDateLow = None, setEntityID = None, setNumberPerDay = None, setSchoolYearID = None, setType = None, setTypeCode = None, setRelationships = None, returnThresholdResetRangeID = True, returnAttendanceLettersRan = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnModifiedTime = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createThresholdResetRange(EntityID = 1, setCountType = None, setCountTypeCode = None, setDateHigh = None, setDateLow = None, setEntityID = None, setNumberPerDay = None, setSchoolYearID = None, setType = None, setTypeCode = None, setRelationships = None, returnThresholdResetRangeID = True, returnAttendanceLettersRan = False, returnCountType = False, returnCountTypeCode = False, returnCreatedTime = False, returnDateDisplay = False, returnDateHigh = False, returnDateLow = False, returnEntityID = False, returnIsForAttendanceLetters = False, returnModifiedTime = False, returnNumberPerDay = False, returnResetRangeAttendanceTypes = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteThresholdResetRange(ThresholdResetRangeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRange/" + str(ThresholdResetRangeID), verb = "delete")

	return(response)

def getEveryThresholdResetRangeAttendancePeriod(EntityID = 1, page = 1, pageSize = 100, returnThresholdResetRangeAttendancePeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1, returnThresholdResetRangeAttendancePeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1, setAttendancePeriodID = None, setThresholdResetRangeID = None, setRelationships = None, returnThresholdResetRangeAttendancePeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createThresholdResetRangeAttendancePeriod(EntityID = 1, setAttendancePeriodID = None, setThresholdResetRangeID = None, setRelationships = None, returnThresholdResetRangeAttendancePeriodID = True, returnAttendancePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteThresholdResetRangeAttendancePeriod(ThresholdResetRangeAttendancePeriodID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendancePeriod/" + str(ThresholdResetRangeAttendancePeriodID), verb = "delete")

	return(response)

def getEveryThresholdResetRangeAttendanceType(EntityID = 1, page = 1, pageSize = 100, returnThresholdResetRangeAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1, returnThresholdResetRangeAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "") for param in return_params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "get", return_params_list = return_params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def modifyThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1, setAttendanceTypeID = None, setThresholdResetRangeID = None, setRelationships = None, returnThresholdResetRangeAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[2:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def createThresholdResetRangeAttendanceType(EntityID = 1, setAttendanceTypeID = None, setThresholdResetRangeID = None, setRelationships = None, returnThresholdResetRangeAttendanceTypeID = True, returnAttendanceTypeID = False, returnCreatedTime = False, returnModifiedTime = False, returnThresholdResetRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = []
	return_params_list.extend(list(params[[(value is True) for value in params.value]].index))
	return_params_list = [ param.replace("return", "", 1) for param in return_params_list ]

	payload_params = params[[(value is not None) for value in params.value]]
	payload_params = payload_params[[("return" not in item) for item in payload_params.index]]
	payload_params.index = [ name.replace("set", "", 1) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params[1:]["value"])})
	payload_params = json.dumps(payload_params)

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(response)

def deleteThresholdResetRangeAttendanceType(ThresholdResetRangeAttendanceTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/ThresholdResetRangeAttendanceType/" + str(ThresholdResetRangeAttendanceTypeID), verb = "delete")

	return(response)