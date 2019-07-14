# This module contains Guidance functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryNotificationMethod(EntityID = 1, page = 1, pageSize = 100, returnNotificationMethodID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNotificationMethod(NotificationMethodID, EntityID = 1, returnNotificationMethodID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(NotificationMethodID), verb = "get", return_params_list = return_params_list)

def modifyNotificationMethod(NotificationMethodID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnNotificationMethodID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/" + str(NotificationMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNotificationMethod(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnNotificationMethodID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/NotificationMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNotificationMethod(NotificationMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOfficeVisitComment(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOfficeVisitComment(OfficeVisitCommentID, EntityID = 1, returnOfficeVisitCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "get", return_params_list = return_params_list)

def modifyOfficeVisitComment(OfficeVisitCommentID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnOfficeVisitCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/" + str(OfficeVisitCommentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOfficeVisitComment(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnOfficeVisitCommentID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitComment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOfficeVisitComment(OfficeVisitCommentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOfficeVisitGuardianResponse(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1, returnOfficeVisitGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "get", return_params_list = return_params_list)

def modifyOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnOfficeVisitGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/" + str(OfficeVisitGuardianResponseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOfficeVisitGuardianResponse(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnOfficeVisitGuardianResponseID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitGuardianResponse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOfficeVisitGuardianResponse(OfficeVisitGuardianResponseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOfficeVisitReason(EntityID = 1, page = 1, pageSize = 100, returnOfficeVisitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOfficeVisitReason(OfficeVisitReasonID, EntityID = 1, returnOfficeVisitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "get", return_params_list = return_params_list)

def modifyOfficeVisitReason(OfficeVisitReasonID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnOfficeVisitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/" + str(OfficeVisitReasonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOfficeVisitReason(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsActive = None, setRelationships = None, returnOfficeVisitReasonID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/OfficeVisitReason/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOfficeVisitReason(OfficeVisitReasonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentOfficeVisit(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitID = True, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1, returnStudentOfficeVisitID = True, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(StudentOfficeVisitID), verb = "get", return_params_list = return_params_list)

def modifyStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1, setDocumentationIsComplete = None, setEntityID = None, setHasBeenReleased = None, setIsStudentOfficeVisitToday = None, setOfficeVisitCommentID = None, setSchoolID = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnStudentOfficeVisitID = True, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/" + str(StudentOfficeVisitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentOfficeVisit(EntityID = 1, setDocumentationIsComplete = None, setEntityID = None, setHasBeenReleased = None, setIsStudentOfficeVisitToday = None, setOfficeVisitCommentID = None, setSchoolID = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnStudentOfficeVisitID = True, returnCreatedTime = False, returnDisplayStatus = False, returnDocumentationIsComplete = False, returnEntityID = False, returnHasBeenReleased = False, returnIsStudentOfficeVisitToday = False, returnModifiedTime = False, returnOfficeVisitCommentID = False, returnSchoolID = False, returnSchoolYearID = False, returnStudentID = False, returnStudentOfficeVisitReasonsListDisplay = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentOfficeVisit(StudentOfficeVisitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentOfficeVisitNote(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1, returnStudentOfficeVisitNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(StudentOfficeVisitNoteID), verb = "get", return_params_list = return_params_list)

def modifyStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1, setNote = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/" + str(StudentOfficeVisitNoteID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentOfficeVisitNote(EntityID = 1, setNote = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitNoteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNote/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentOfficeVisitNote(StudentOfficeVisitNoteID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentOfficeVisitNotification(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitNotificationID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1, returnStudentOfficeVisitNotificationID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(StudentOfficeVisitNotificationID), verb = "get", return_params_list = return_params_list)

def modifyStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1, setNameID = None, setNote = None, setNotificationMethodID = None, setNotificationTime = None, setNotificationTimeDate = None, setNotificationTimeTime = None, setOfficeVisitGuardianResponseID = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitNotificationID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/" + str(StudentOfficeVisitNotificationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentOfficeVisitNotification(EntityID = 1, setNameID = None, setNote = None, setNotificationMethodID = None, setNotificationTime = None, setNotificationTimeDate = None, setNotificationTimeTime = None, setOfficeVisitGuardianResponseID = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitNotificationID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnNotificationMethodID = False, returnNotificationTime = False, returnNotificationTimeDate = False, returnNotificationTimeTime = False, returnOfficeVisitGuardianResponseID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitNotification/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentOfficeVisitNotification(StudentOfficeVisitNotificationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentOfficeVisitReason(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitReasonID = True, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1, returnStudentOfficeVisitReasonID = True, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(StudentOfficeVisitReasonID), verb = "get", return_params_list = return_params_list)

def modifyStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1, setOfficeVisitReasonID = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitReasonID = True, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/" + str(StudentOfficeVisitReasonID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentOfficeVisitReason(EntityID = 1, setOfficeVisitReasonID = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitReasonID = True, returnCreatedTime = False, returnModifiedTime = False, returnOfficeVisitReasonID = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitReason/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentOfficeVisitReason(StudentOfficeVisitReasonID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentOfficeVisitTimeTransaction(EntityID = 1, page = 1, pageSize = 100, returnStudentOfficeVisitTimeTransactionID = True, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1, returnStudentOfficeVisitTimeTransactionID = True, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(StudentOfficeVisitTimeTransactionID), verb = "get", return_params_list = return_params_list)

def modifyStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1, setDisplayOrder = None, setEndTime = None, setEndTimeDate = None, setEndTimeTime = None, setNote = None, setStartTime = None, setStartTimeDate = None, setStartTimeTime = None, setStatus = None, setStatusCode = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitTimeTransactionID = True, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/" + str(StudentOfficeVisitTimeTransactionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentOfficeVisitTimeTransaction(EntityID = 1, setDisplayOrder = None, setEndTime = None, setEndTimeDate = None, setEndTimeTime = None, setNote = None, setStartTime = None, setStartTimeDate = None, setStartTimeTime = None, setStatus = None, setStatusCode = None, setStudentOfficeVisitID = None, setRelationships = None, returnStudentOfficeVisitTimeTransactionID = True, returnCreatedTime = False, returnDisplayDuration = False, returnDisplayOrder = False, returnDuration = False, returnEndTime = False, returnEndTimeDate = False, returnEndTimeTime = False, returnModifiedTime = False, returnNote = False, returnStartTime = False, returnStartTimeDate = False, returnStartTimeTime = False, returnStatus = False, returnStatusCode = False, returnStudentOfficeVisitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Guidance/StudentOfficeVisitTimeTransaction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentOfficeVisitTimeTransaction(StudentOfficeVisitTimeTransactionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")